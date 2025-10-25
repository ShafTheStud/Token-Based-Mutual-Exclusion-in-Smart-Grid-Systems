# src/node.py
# Node class to simulate a smart-grid controller that requests/uses a shared resource.

import threading
import time
import random
from token import Token


class Node(threading.Thread):
    def __init__(self, node_id, total_nodes, network, think_time=(2, 5), cs_time=(1, 2)):
        """
        node_id: integer id of this node
        total_nodes: total number of nodes in the network
        network: reference to Network instance
        think_time: (min,max) seconds to wait between requests
        cs_time: (min,max) seconds to spend in critical section
        """
        super().__init__(daemon=True)
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.network = network

        # Request numbers (per Suzuki-Kasami style; optional simplified use)
        self.request_number = [0] * total_nodes

        # Token state
        self.has_token = False
        self.token = None

        # Local queue of who requested while this node had token (kept in token normally)
        self.running = True

        # timings
        self.think_time = think_time
        self.cs_time = cs_time

        # Simple local request flag
        self.want_cs = False

    def run(self):
        # main loop: periodically decide to request critical section
        while self.running:
            # wait a random time (thinking / doing local work)
            time.sleep(random.uniform(*self.think_time))

            # decide to request CS with some probability
            if random.random() < 0.7:  # 70% chance to request
                self.request_access()

            # if we have token and someone is waiting or we requested, enter CS
            if self.has_token and (self.want_cs or self.token.queue):
                self.enter_critical_section()
                self.exit_critical_section()

    def request_access(self):
        # increment own request number and broadcast request
        self.request_number[self.node_id] += 1
        req_num = self.request_number[self.node_id]
        self.want_cs = True
        print(f"[Node {self.node_id}] REQUEST (num={req_num})")
        # broadcast to other nodes (network will forward to their receive_request)
        self.network.broadcast_request(self.node_id, req_num)

        # If we have token already, ensure we're in token queue (so we can enter soon)
        if self.has_token and self.node_id not in self.token.queue:
            self.token.add_requester(self.node_id)

    def receive_request(self, sender_id, req_num):
        # update local record of sender's request number
        if req_num > self.request_number[sender_id]:
            self.request_number[sender_id] = req_num

        # if this node holds the token, add sender to token queue
        if self.has_token:
            if sender_id not in self.token.queue:
                self.token.add_requester(sender_id)
                print(f"[Node {self.node_id}] (has token) queued Node {sender_id}")

    def receive_token(self, token):
        self.has_token = True
        self.token = token
        print(f"[Node {self.node_id}] RECEIVED token. Queue = {self.token.queue}")

    def enter_critical_section(self):
        if not self.has_token:
            return
        # if this node requested, ensure it's allowed to proceed
        # simulate being in critical section
        print(f"🔋 [Node {self.node_id}] ENTERING critical section (using shared resource).")
        self.want_cs = False
        time.sleep(random.uniform(*self.cs_time))
        print(f"✅ [Node {self.node_id}] EXITING critical section.")

    def exit_critical_section(self):
        # after finishing, pass token to next requester if any
        if not self.has_token:
            return

        # Make sure token queue contains most recent requests (simplified)
        # In a full implementation we'd reference request numbers; here we use queue.
        next_node = self.token.pop_next()
        if next_node is not None:
            print(f"[Node {self.node_id}] Passing token → Node {next_node}")
            # hand token off
            self.network.send_token(next_node, self.token)
            self.has_token = False
            self.token = None
        else:
            # no one waiting: keep token (idle)
            print(f"[Node {self.node_id}] No waiting nodes. Keeping token idle.")

    def stop(self):
        self.running = False

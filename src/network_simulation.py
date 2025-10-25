# src/network_simulation.py
# Entry-point that sets up the network and runs the simulation.

from node import Node
from token import Token
import time


class Network:
    def __init__(self, num_nodes=4):
        self.num_nodes = num_nodes
        self.nodes = []

    def setup(self):
        # create node instances
        for i in range(self.num_nodes):
            n = Node(i, self.num_nodes, self)
            self.nodes.append(n)

        # give token initially to Node 0
        initial_token = Token()
        self.nodes[0].has_token = True
        self.nodes[0].token = initial_token
        print("🔑 Token initially assigned to Node 0.")

    def broadcast_request(self, sender_id, req_num):
        # forward the request to all other nodes
        for node in self.nodes:
            if node.node_id != sender_id:
                node.receive_request(sender_id, req_num)

        # Also, if the current token holder is known, ensure they enqueue the sender
        # (receive_request takes care of that when it's forwarded)

    def send_token(self, receiver_id, token):
        # deliver the token to the recipient node
        receiver = self.nodes[receiver_id]
        receiver.receive_token(token)

    def start(self):
        for node in self.nodes:
            node.start()

    def stop(self):
        for node in self.nodes:
            node.stop()
        # join threads to clean up
        for node in self.nodes:
            node.join()

if __name__ == "__main__":
    # simulation parameters
    NUM_NODES = 4
    SIMULATION_SECONDS = 20

    net = Network(num_nodes=NUM_NODES)
    net.setup()
    net.start()

    # let simulation run
    time.sleep(SIMULATION_SECONDS)

    net.stop()
    print("\n🔚 Simulation complete.")

# src/token.py
# Token data structure used for mutual exclusion.

class Token:
    def __init__(self):
        # queue: nodes (by id) waiting for the token, in order
        self.queue = []
        # last_request[i] can store the last known request number from node i
        self.last_request = {}

    def add_requester(self, node_id):
        if node_id not in self.queue:
            self.queue.append(node_id)

    def pop_next(self):
        if self.queue:
            return self.queue.pop(0)
        return None

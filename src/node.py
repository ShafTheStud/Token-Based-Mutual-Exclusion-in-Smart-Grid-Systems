"""
Node module for smart grid systems.
Implements nodes that compete for access to shared energy resources using a token.
"""
import threading
import time
import random


# Constants for resource access timing
MIN_ACCESS_TIME = 0.3  # Minimum time for resource access (seconds)
DEFAULT_MAX_ACCESS_TIME = 1.0  # Default maximum time for resource access (seconds)


class Node(threading.Thread):
    """
    Represents a node in the smart grid system that requires access to shared energy resources.
    Uses token-based mutual exclusion to coordinate access.
    """
    
    def __init__(self, node_id, token, simulation_time=10, max_access_time=2):
        """
        Initialize a node in the smart grid system.
        
        Args:
            node_id: Unique identifier for this node
            token: Shared token object for mutual exclusion
            simulation_time: Total time to run simulation in seconds
            max_access_time: Maximum time a node can hold the token (seconds)
        """
        super().__init__()
        self.node_id = node_id
        self.token = token
        self.simulation_time = simulation_time
        self.max_access_time = max_access_time
        self.access_count = 0
        self._stop_flag = threading.Event()
        self.daemon = True
        
    def run(self):
        """Main execution loop for the node."""
        start_time = time.time()
        
        print(f"[Node {self.node_id}] Started - Smart Grid Energy Node")
        
        while not self._stop_flag.is_set() and (time.time() - start_time) < self.simulation_time:
            # Try to acquire the token
            if self.token.acquire(self.node_id):
                self.access_shared_resource()
                self.token.release(self.node_id)
                
                # Wait before next request (simulate work between resource accesses)
                time.sleep(random.uniform(0.5, 1.5))
            else:
                # Token not available, wait a bit and retry
                time.sleep(0.1)
        
        print(f"[Node {self.node_id}] Finished - Total accesses: {self.access_count}")
    
    def access_shared_resource(self):
        """
        Access the shared energy resource (critical section).
        Simulates reading/writing energy data or controlling shared equipment.
        """
        self.access_count += 1
        access_duration = random.uniform(MIN_ACCESS_TIME, min(DEFAULT_MAX_ACCESS_TIME, self.max_access_time))
        
        print(f"[Node {self.node_id}] ✓ Acquired token - Accessing shared energy resource (access #{self.access_count})")
        
        # Simulate energy resource access (e.g., reading meters, updating load balancing)
        time.sleep(access_duration)
        
        print(f"[Node {self.node_id}] ✗ Released token - Completed resource access")
    
    def stop(self):
        """Signal the node to stop execution."""
        self._stop_flag.set()

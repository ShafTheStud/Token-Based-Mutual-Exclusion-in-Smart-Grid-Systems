"""
Token module for mutual exclusion in smart grid systems.
Implements the token that nodes pass to access shared energy resources.
"""
import threading
import time


class Token:
    """
    Represents a token that grants access to shared energy resources.
    Only one node can hold the token at a time, ensuring mutual exclusion.
    """
    
    def __init__(self):
        """Initialize the token with a unique identifier and holder tracking."""
        self._lock = threading.Lock()
        self._current_holder = None
        self._request_queue = []
        self.access_count = 0
        
    def acquire(self, node_id):
        """
        Acquire the token for a node.
        
        Args:
            node_id: Identifier of the node requesting the token
            
        Returns:
            bool: True if token was successfully acquired
        """
        with self._lock:
            if self._current_holder is None:
                self._current_holder = node_id
                self.access_count += 1
                return True
            return False
    
    def release(self, node_id):
        """
        Release the token from a node.
        
        Args:
            node_id: Identifier of the node releasing the token
            
        Returns:
            bool: True if token was successfully released
        """
        with self._lock:
            if self._current_holder == node_id:
                self._current_holder = None
                return True
            return False
    
    def get_holder(self):
        """
        Get the current holder of the token.
        
        Returns:
            The node_id of the current holder, or None if no holder
        """
        with self._lock:
            return self._current_holder
    
    def is_available(self):
        """
        Check if the token is available (not held by any node).
        
        Returns:
            bool: True if token is available
        """
        with self._lock:
            return self._current_holder is None

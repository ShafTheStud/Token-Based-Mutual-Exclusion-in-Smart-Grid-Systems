"""
Network simulation module for token-based mutual exclusion in smart grid systems.
Orchestrates multiple nodes competing for shared energy resources.
"""
import time
from src.token import Token
from src.node import Node


class NetworkSimulation:
    """
    Simulates a smart grid network with multiple nodes using token-based mutual exclusion
    to coordinate access to shared energy resources (SDG 7 - Clean Energy).
    """
    
    def __init__(self, num_nodes=4, simulation_time=10):
        """
        Initialize the network simulation.
        
        Args:
            num_nodes: Number of nodes in the smart grid network (default: 4)
            simulation_time: Duration of simulation in seconds (default: 10)
        """
        self.num_nodes = num_nodes
        self.simulation_time = simulation_time
        self.token = Token()
        self.nodes = []
        
    def setup(self):
        """Set up the network with nodes."""
        print("=" * 70)
        print("SMART GRID TOKEN-BASED MUTUAL EXCLUSION SIMULATION")
        print("SDG 7 - Affordable and Clean Energy")
        print("=" * 70)
        print(f"\nInitializing {self.num_nodes} smart grid nodes...")
        print(f"Simulation duration: {self.simulation_time} seconds")
        print(f"Token-based mutual exclusion ensures fair access to shared energy resources\n")
        
        for i in range(self.num_nodes):
            node = Node(
                node_id=f"SG-Node-{i+1}",
                token=self.token,
                simulation_time=self.simulation_time
            )
            self.nodes.append(node)
            print(f"✓ Created {node.node_id}")
        
        print("\n" + "=" * 70)
        print("Starting simulation...\n")
    
    def run(self):
        """Run the network simulation."""
        # Start all nodes
        for node in self.nodes:
            node.start()
        
        # Wait for simulation to complete
        start_time = time.time()
        try:
            while (time.time() - start_time) < self.simulation_time:
                time.sleep(0.5)
                # Optionally monitor token status
        except KeyboardInterrupt:
            print("\n\nSimulation interrupted by user.")
        
        # Stop all nodes
        for node in self.nodes:
            node.stop()
        
        # Wait for all nodes to finish
        for node in self.nodes:
            node.join(timeout=2.0)
        
        self.display_results()
    
    def display_results(self):
        """Display simulation results."""
        print("\n" + "=" * 70)
        print("SIMULATION RESULTS")
        print("=" * 70)
        
        total_accesses = sum(node.access_count for node in self.nodes)
        
        print(f"\nTotal token acquisitions: {total_accesses}")
        print(f"Token access statistics per node:")
        
        for node in self.nodes:
            percentage = (node.access_count / total_accesses * 100) if total_accesses > 0 else 0
            print(f"  {node.node_id}: {node.access_count} accesses ({percentage:.1f}%)")
        
        print("\n" + "=" * 70)
        print("Simulation completed successfully!")
        print("Token-based mutual exclusion ensured no conflicts in energy resource access.")
        print("=" * 70)


def main():
    """Main entry point for the simulation."""
    # Create and run simulation with 4 nodes (can be adjusted to 3-4 nodes)
    simulation = NetworkSimulation(num_nodes=4, simulation_time=10)
    simulation.setup()
    simulation.run()


if __name__ == "__main__":
    main()

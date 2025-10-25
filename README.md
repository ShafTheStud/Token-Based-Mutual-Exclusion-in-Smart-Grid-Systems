# Token-Based Mutual Exclusion in Smart Grid Systems

A Python-based simulation of token-based mutual exclusion in smart grid systems. It ensures fair, conflict-free, and efficient access to shared energy resources among distributed nodes, supporting **SDG 7 – Affordable and Clean Energy** through improved coordination and sustainable energy management.

## 🌟 Overview

This project simulates a distributed smart grid system where multiple nodes (e.g., power substations, renewable energy sources, or control units) need coordinated access to shared energy resources. The token-based mutual exclusion algorithm ensures that only one node can access the critical resource at a time, preventing conflicts and ensuring system stability.

## 🎯 Features

- **Token-Based Mutual Exclusion**: Implements a fair and efficient token-passing mechanism
- **Multi-threaded Simulation**: Uses Python threading to simulate concurrent node operations
- **Smart Grid Context**: Designed for energy resource management scenarios
- **Real-time Monitoring**: Displays token acquisition and release events during simulation
- **Statistical Analysis**: Provides access statistics per node after simulation

## 📁 Project Structure

```
Token-Based-Mutual-Exclusion-in-Smart-Grid-Systems/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── token.py                 # Token management and mutual exclusion logic
│   ├── node.py                  # Node behavior with threading
│   └── network_simulation.py    # Main simulation orchestrator
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies (standard library only)
└── .gitignore                   # Git ignore patterns
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses Python standard library only)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ShafTheStud/Token-Based-Mutual-Exclusion-in-Smart-Grid-Systems.git
cd Token-Based-Mutual-Exclusion-in-Smart-Grid-Systems
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (none required, but you can run):
```bash
pip install -r requirements.txt
```

### Running the Simulation

Run the simulation with 4 nodes (default):
```bash
python -m src.network_simulation
```

Or run it directly:
```bash
python src/network_simulation.py
```

## 🎮 Usage

### Basic Simulation

The default simulation runs with 4 nodes for 10 seconds:

```python
from src.network_simulation import NetworkSimulation

# Create simulation with 4 nodes, 10 second duration
simulation = NetworkSimulation(num_nodes=4, simulation_time=10)
simulation.setup()
simulation.run()
```

### Custom Configuration

You can customize the number of nodes (3-4 recommended) and simulation time:

```python
# Simulation with 3 nodes for 15 seconds
simulation = NetworkSimulation(num_nodes=3, simulation_time=15)
simulation.setup()
simulation.run()
```

## 🔧 How It Works

### Token-Based Mutual Exclusion

1. **Token**: A single token circulates among nodes. Only the node holding the token can access the shared energy resource.

2. **Nodes**: Each node runs in its own thread and continuously attempts to acquire the token to access the shared resource.

3. **Critical Section**: When a node acquires the token, it enters the critical section (accessing shared energy resource), performs its operation, and releases the token.

4. **Fairness**: The algorithm ensures all nodes get fair access to the shared resource over time.

### Components

- **`Token` class**: Manages token ownership with thread-safe operations
  - `acquire(node_id)`: Attempt to acquire the token
  - `release(node_id)`: Release the token
  - `is_available()`: Check token availability

- **`Node` class**: Represents a smart grid node (extends `threading.Thread`)
  - Continuously attempts to acquire the token
  - Accesses shared resource when token is acquired
  - Releases token after completing access
  - Tracks access statistics

- **`NetworkSimulation` class**: Orchestrates the entire simulation
  - Creates and manages multiple nodes
  - Monitors simulation progress
  - Displays results and statistics

## 📊 Sample Output

```
======================================================================
SMART GRID TOKEN-BASED MUTUAL EXCLUSION SIMULATION
SDG 7 - Affordable and Clean Energy
======================================================================

Initializing 4 smart grid nodes...
Simulation duration: 10 seconds
Token-based mutual exclusion ensures fair access to shared energy resources

✓ Created SG-Node-1
✓ Created SG-Node-2
✓ Created SG-Node-3
✓ Created SG-Node-4

======================================================================
Starting simulation...

[Node SG-Node-1] Started - Smart Grid Energy Node
[Node SG-Node-2] Started - Smart Grid Energy Node
[Node SG-Node-3] Started - Smart Grid Energy Node
[Node SG-Node-4] Started - Smart Grid Energy Node
[Node SG-Node-1] ✓ Acquired token - Accessing shared energy resource (access #1)
[Node SG-Node-1] ✗ Released token - Completed resource access
[Node SG-Node-3] ✓ Acquired token - Accessing shared energy resource (access #1)
...

======================================================================
SIMULATION RESULTS
======================================================================

Total token acquisitions: 24
Token access statistics per node:
  SG-Node-1: 6 accesses (25.0%)
  SG-Node-2: 7 accesses (29.2%)
  SG-Node-3: 5 accesses (20.8%)
  SG-Node-4: 6 accesses (25.0%)

======================================================================
Simulation completed successfully!
Token-based mutual exclusion ensured no conflicts in energy resource access.
======================================================================
```

## 🌍 SDG 7 - Clean Energy

This project supports **Sustainable Development Goal 7: Affordable and Clean Energy** by demonstrating:

- **Efficient Resource Management**: Prevents conflicts in accessing shared energy infrastructure
- **Fair Distribution**: Ensures all nodes get equitable access to resources
- **System Stability**: Maintains coordination in distributed energy systems
- **Scalability**: Can be extended to real-world smart grid scenarios

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by distributed systems and mutual exclusion algorithms
- Designed to support sustainable energy management (SDG 7)
- Built with Python's threading module for concurrent simulation

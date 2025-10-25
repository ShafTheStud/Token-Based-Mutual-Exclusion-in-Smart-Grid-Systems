🧠 Token-Based Mutual Exclusion in Smart Grid Systems
🎯 SDG Goal: SDG 7 – Affordable and Clean Energy
📘 Overview

This project demonstrates a token-based mutual exclusion algorithm applied to smart grid systems.
It simulates how multiple distributed nodes (representing smart meters or energy controllers) can coordinate to access a shared energy resource fairly and without conflict.
Only the node holding the token can use the resource, ensuring efficient, deadlock-free, and energy-aware operation.

⚙️ Features

Distributed simulation of multiple smart grid nodes

Token-based resource access control

Fair and conflict-free coordination

Thread-based concurrency using Python

Lightweight and easy to extend for visualization or IoT networks

🧩 File Structure
token-based-mutual-exclusion-smartgrid/
├── src/
│   ├── node.py
│   ├── token.py
│   ├── network_simulation.py
├── diagrams/
│   └── architecture.png
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

💻 Technologies Used

Language: Python 3

Libraries: threading, time, random (standard library)

Concepts: Distributed Systems, Mutual Exclusion, Token Passing

🚀 How to Run

Clone the repository:

git clone https://github.com/<your-username>/token-based-mutual-exclusion-smartgrid.git
cd token-based-mutual-exclusion-smartgrid


Run the simulation:

python src/network_simulation.py


Observe console output showing nodes requesting and passing the token.

📊 Sample Output
🔑 Token initially assigned to Node 0.
[Node 1] REQUEST (num=1)
[Node 0] Passing token → Node 1
🔋 [Node 1] ENTERING critical section (using shared resource).
✅ [Node 1] EXITING critical section.
[Node 1] Passing token → Node 2
🔋 [Node 2] ENTERING critical section (using shared resource).

🌱 SDG 7 – Clean Energy Alignment

This project supports Sustainable Development Goal 7 (Affordable and Clean Energy) by demonstrating
how distributed energy systems can achieve efficient, conflict-free, and fair resource utilization.
Such coordination reduces power wastage, enhances reliability, and contributes to smarter, greener grids.

🧠 Future Enhancements

Add real-time visualization of token movement.

Simulate energy metrics (power draw, load balance).

Replace threads with networked processes for distributed execution.

🪪 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

📚 References

Suzuki, I., & Kasami, T. (1985). A distributed mutual exclusion algorithm. ACM Transactions on Computer Systems.

United Nations – Sustainable Development Goal 7: Affordable and Clean Energy

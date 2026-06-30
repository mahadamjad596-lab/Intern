🚀 Search Algorithm Comparison Using Python

«A Python project that implements and compares BFS, Uniform Cost Search (UCS), and A Search on a weighted graph to find the optimal path.*»

---

📖 Project Overview

This project demonstrates three fundamental Artificial Intelligence (AI) search algorithms used for graph traversal and pathfinding.

The program allows users to:

- 🎯 Enter a Start Node and Goal Node
- 🔍 Execute BFS, UCS, and A* algorithms
- 📊 Compare the algorithms based on:
  - Path Found
  - Total Cost
  - Nodes Explored
- 🏆 Identify the best algorithm for the shortest path

---

✨ Features

✅ Interactive user input

✅ Weighted graph representation

✅ Heuristic-based A* implementation

✅ Algorithm performance comparison

✅ Clean tabular output

✅ Beginner-friendly Python code

---

🛠️ Technologies Used

- 🐍 Python 3
- 📚 "collections.deque"
- ⚡ "heapq"
- 💻 Command Line Interface (CLI)

---

🧠 Algorithms Implemented

🌐 Breadth-First Search (BFS)

- Explores nodes level by level.
- Best suited for unweighted graphs.
- Does not consider edge weights.

---

💰 Uniform Cost Search (UCS)

- Expands the node with the lowest cumulative cost.
- Guarantees the optimal path for weighted graphs with non-negative costs.

---

⭐ A* Search Algorithm

- Uses both:
  - g(n) → Actual path cost
  - h(n) → Heuristic estimate
- Evaluation Function:

f(n) = g(n) + h(n)

- Efficiently finds the optimal path while reducing unnecessary exploration.

---

📂 Graph Representation

The project uses a predefined weighted graph containing nodes A → J.

Each edge contains:

- 🔹 Destination Node
- 🔹 Edge Weight (Cost)

The A* algorithm also uses heuristic values for each node.

---

▶️ How to Run

1️⃣ Clone the repository

git clone <repository-link>

2️⃣ Navigate to the project folder

cd Search-Algorithm-Comparison

3️⃣ Run the program

python search_algorithms.py

4️⃣ Enter the nodes

Enter Start Node: A
Enter Goal Node: J

---

📊 Sample Output

------ Search Algorithm Comparison ------

Algorithm   Path                          Cost   Nodes Explored

BFS         A -> B -> D -> G -> I -> J    N/A    10

UCS         A -> B -> E -> G -> I -> J    13     10

A*          A -> B -> E -> G -> I -> J    13     8

Best Algorithm for Shortest Path: UCS

---

🎯 Learning Outcomes

This project helped in understanding:

- 📌 Graph data structures
- 📌 Breadth-First Search (BFS)
- 📌 Uniform Cost Search (UCS)
- 📌 A* Search Algorithm
- 📌 Heuristic functions
- 📌 Priority queues
- 📌 Pathfinding concepts
- 📌 Algorithm comparison techniques

---

🚀 Future Enhancements

- 🎨 Graph visualization using NetworkX & Matplotlib
- 🌍 Custom graph input from users
- 📁 Read graph data from files
- 🔍 Add DFS, Dijkstra's, and Greedy Best-First Search
- 📈 Performance analysis with execution time
- 💾 Export comparison results

---

📁 Project Structure

📦 Search-Algorithm-Comparison
│
├── 📄 search_algorithms.py
├── 📄 README.md
└── 📄 requirements.txt (Optional)

---

🤝 Contribution

Contributions, suggestions, and improvements are always welcome!

Feel free to fork this repository and submit a pull request.

---

📜 License

This project is developed for educational and internship learning purposes.

---

👨‍💻 Author

Mahad Amjad

🎓 Internship Project at M - Tech

🐍 Python | Artificial Intelligence | Graph Search Algorithms

⭐ If you found this project useful, don't forget to star the repository!

Search Algorithm Comparison Using Python

Overview

This project demonstrates the implementation and comparison of three fundamental graph search algorithms in Python:

- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search Algorithm

The application allows users to enter a start node and a goal node, executes all three algorithms, and compares their performance based on the path found, total path cost, and the number of nodes explored.

---

Features

- Implements three popular search algorithms.
- Uses a weighted graph represented with Python dictionaries.
- Accepts user input for the start and goal nodes.
- Displays:
  - Path found
  - Total path cost
  - Number of nodes explored
- Identifies the algorithm that produces the shortest path based on total cost.

---

Technologies Used

- Python 3
- "collections.deque" (for BFS queue implementation)
- "heapq" (for priority queue implementation in UCS and A*)

---

Graph Structure

The project uses a predefined weighted graph consisting of nodes A through J. Edge weights represent traversal costs, while heuristic values are used by the A* algorithm to estimate the remaining distance to the goal.

---

Algorithms Implemented

1. Breadth-First Search (BFS)

- Explores nodes level by level.
- Guarantees the shortest path only in unweighted graphs.
- Does not consider edge weights.

2. Uniform Cost Search (UCS)

- Expands the node with the lowest cumulative path cost.
- Guarantees the optimal solution for graphs with non-negative edge weights.

3. A* Search

- Uses both the actual path cost (g) and heuristic estimate (h).
- Evaluation function: f(n) = g(n) + h(n)
- Efficiently finds the optimal path when the heuristic is admissible.

---

How to Run

1. Make sure Python 3 is installed.
2. Save the program as "search_algorithms.py".
3. Open a terminal or command prompt.
4. Run:

python search_algorithms.py

5. Enter the start node and goal node when prompted.

Example:

Enter Start Node: A
Enter Goal Node: J

---

Sample Output

------ Search Algorithm Comparison ------
Algorithm Path                           Cost      Nodes Explored
BFS       A -> B -> D -> G -> I -> J     N/A       10
UCS       A -> B -> E -> G -> I -> J     13        10
A*        A -> B -> E -> G -> I -> J     13        8

Best Algorithm for Shortest Path: UCS

---

Learning Outcomes

Through this project, the following concepts were explored:

- Graph representation in Python
- Queue and priority queue data structures
- Pathfinding algorithms
- Heuristic search techniques
- Algorithm performance comparison
- Time and space efficiency considerations

---

Future Improvements

- Allow users to create custom graphs.
- Visualize graph traversal using libraries such as NetworkX and Matplotlib.
- Support larger and more complex graphs.
- Add Depth-First Search (DFS), Greedy Best-First Search, and Dijkstra's Algorithm for further comparison.
- Export search results to a file.

---

Author

Developed as part of an internship project at M - Tech to demonstrate the implementation and comparison of classical graph search algorithms using Python.

# 🗺️ Smart Route Planner

A Python-based route planning system that compares **three search algorithms** — BFS, UCS, and A* — to find optimal paths in weighted graphs. Built during my AI/ML internship at M - Tech to demonstrate practical implementation of fundamental search strategies.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
- [Graph Structure](#graph-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Author](#author)

---

## 🎯 Overview

This project compares **three search algorithms** on a 10-node weighted graph:

| Algorithm | Type | Optimal? | Data Structure |
|-----------|------|----------|----------------|
| **BFS** | Uninformed | Yes (unweighted) | Queue |
| **UCS** | Uninformed | Yes (weighted) | Priority Queue |
| **A*** | Informed | Yes (admissible heuristic) | Priority Queue |

The program:
- Accepts user input for start and goal nodes
- Runs all three algorithms simultaneously
- Displays a side-by-side comparison table
- Identifies the best algorithm for shortest path

---

## 🔍 Algorithms Explained

### 1. BFS (Breadth-First Search)
- Explores level by level (like ripples in water)
- Guarantees shortest path in **unweighted** graphs
- Uses a **Queue** (FIFO)

### 2. UCS (Uniform Cost Search)
- Expands node with lowest cumulative cost
- Guarantees shortest path in **weighted** graphs
- Uses a **Priority Queue** (heapq)

### 3. A* (A-Star Search)
- Combines actual cost (g) + heuristic estimate (h)
- Most efficient for real-world pathfinding
- Uses **Priority Queue** with f(n) = g(n) + h(n)

---

## 🏗️ Graph Structure

The graph represents a city network with **10 nodes (A-J)**:

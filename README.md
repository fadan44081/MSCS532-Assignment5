# MSCS532-Assignment5
# Quicksort Algorithm: Implementation, Analysis, and Randomization

## 📖 Overview

This project implements and analyzes two versions of the Quicksort algorithm:

- **Deterministic Quicksort**
- **Randomized Quicksort**

The objective is to evaluate how pivot selection impacts performance, especially under different input distributions such as random, sorted, and reverse-sorted arrays.

---

## 🚀 Features

- In-place Quicksort implementation
- Randomized pivot selection
- Performance benchmarking
- Comparative analysis across input types
- Clean and modular Python code

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

---

## ▶️ How to Run

### Step 1: Clone the repository

Step 2: Run the script
python quicksort_assignment.py

🧪 What the Program Does
The program:

Generates arrays of different sizes:

100, 300, 500, 700, 900
Tests three types of input:
Random
Sorted
Reverse-sorted
Measures execution time of:
Deterministic Quicksort
Randomized Quicksort
📊 Example Output
Array size: 500
Random input - Deterministic: 0.000587s, Randomized: 0.000667s
Sorted input - Deterministic: 0.015771s, Randomized: 0.000633s
Reverse input - Deterministic: 0.011658s, Randomized: 0.000668s

📈 Key Findings
1. Random Input
Both algorithms perform similarly
Deterministic is slightly faster (no random overhead)
2. Sorted Input
Deterministic Quicksort becomes significantly slower
Randomized Quicksort remains efficient
3. Reverse-Sorted Input
Same behavior as sorted input
Deterministic shows worst-case performance

⚡ Complexity Summary
Case	    Deterministic	    Randomized
Best	    O(n log n)	      O(n log n)
Average	  O(n log n)	      O(n log n)
Worst	    O(n²)	            O(n²) 

🧠 Key Insight
The main limitation of deterministic Quicksort is its sensitivity to input order.

Randomized Quicksort significantly reduces the probability of worst-case behavior by selecting pivots randomly, making it more reliable in practice.

📂 Project Structure
├── quicksort_assignment.py   # Main implementation
├── README.md                 # Project documentation
├── Assignment_5_Report_MSCS-532-B01.pdf  # Detailed analysis

📚 Author

Fathiya Adan

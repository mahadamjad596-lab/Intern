```markdown
# 🏢 Office Parking Space Allocator

A desktop application that uses **Artificial Intelligence** (Constraint Satisfaction Problem with Backtracking) to fairly allocate parking spaces to employees in an office environment.

---

## 📋 Project Overview

This application solves the real-world problem of limited parking space allocation in offices. Employees can rank their preferred parking spots, and the system uses a CSP algorithm to assign spots fairly while respecting constraints like role-based reservations.

### Key Features

- **👤 Employee Management** - Add, view, and delete employees with roles (Staff, Manager, Executive)
- **🅿️ Parking Spot Management** - Add, view, and delete parking spots with optional role reservations
- **⭐ Preference Setting** - Employees rank their preferred spots in order
- **🎯 Fair Allocation** - CSP with backtracking algorithm finds optimal assignment
- **📊 Dashboard** - Real-time statistics showing allocation status and satisfaction metrics
- **📈 Satisfaction Metrics** - Shows how many employees got their top-3 preferences

---

## 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Programming language |
| **PyQt5** | GUI framework for desktop application |
| **CSP Algorithm** | Constraint Satisfaction Problem with backtracking |
| **Matplotlib** | (Optional) For visual analytics |

---

## 📸 Screenshots

### Dashboard Tab
*Shows key statistics: total employees, parking spots, allocated spots, and satisfaction rate*

### Employees Tab
*Add, view, and delete employees with role selection*

### Parking Spots Tab
*Add, view, and delete parking spots with optional reservations*

### Preferences Tab
*Set ranked preferences for each employee*

### Allocation Tab
*Run fair allocation and view results with satisfaction metrics*

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher installed on your system
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Office_Parking_Space_Allocator.git
cd Office_Parking_Space_Allocator
```

Step 2: Install Dependencies

```bash
pip install PyQt5
pip install matplotlib
pip install pandas
```

Step 3: Run the Application

```bash
python main.py
```

---

📖 How to Use

1. Add Employees

· Go to the Employees tab
· Enter employee name and select role
· Click "Add Employee"

2. Add Parking Spots

· Go to the Spots tab
· Enter Spot ID (e.g., "A1") and location
· Select "Reserved For" if needed (None, Manager, Executive)
· Click "Add Spot"

3. Set Preferences

· Go to the Preferences tab
· Select an employee from dropdown
· Hold Ctrl (Windows) or Cmd (Mac) and click spots in order of preference
· Click "Set Preferences"

4. Run Allocation

· Go to the Allocate tab
· Click "RUN FAIR ALLOCATION"
· View results with satisfaction metrics

---

🧠 Algorithm Explanation

Constraint Satisfaction Problem (CSP)

The application uses a CSP solver with backtracking to find a valid allocation:

Variables: Employees who need parking spots

Domains: Available parking spots

Constraints:

1. Each employee gets exactly one spot
2. Each spot is assigned to at most one employee
3. Reserved spots can only go to employees with matching roles

Backtracking Process

For each employee in order:

1. Try preferred spots from highest to lowest preference
2. Check if spot is available (not already assigned)
3. Check if spot is allowed (no role conflict)
4. If valid, assign and move to next employee
5. If no valid spot found, backtrack and try different assignment
6. Return solution when all employees assigned

Fairness Metrics

· Satisfaction Rate: Percentage of employees who received a top-3 preference
· Rank Display: Shows each employee's assigned spot rank (1st, 2nd, 3rd, etc.)

---

📁 Project Structure

```
Office_Parking_Space_Allocator/
│
├── csp_solver.py          # CSP algorithm with backtracking
├── gui.py                 # PyQt5 graphical user interface
├── main.py                # Entry point to run the application
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

🔧 Code Structure

csp_solver.py

Method Description
add_employee() Add employee with ID, name, and role
add_parking_spot() Add spot with ID, location, and optional reservation
set_preferences() Store employee's ranked spot preferences
is_consistent() Check if assignment violates constraints
solve() Backtracking algorithm implementation
allocate() Run allocation and return results
get_stats() Calculate satisfaction metrics

gui.py

Tab Features
Dashboard Statistics cards showing key metrics
Employees Add/delete employees with role selection
Spots Add/delete parking spots with reservations
Preferences Set ranked preferences per employee
Allocate Run allocation and display results

---

📝 Sample Data

The application comes pre-loaded with sample data:

Employees

ID Name Role
1 Ali Khan Manager
2 Bilal Ahmed Staff
3 Fatima Noor Staff
4 Hassan Ali Executive
5 Ayesha Malik Staff

Parking Spots

Spot ID Location Reserved For
A1 Near Entrance None
A2 Near Entrance None
B1 Shaded Area Manager
B2 Shaded Area None
C1 Close to Exit Executive
C2 Close to Exit None

---

🔍 Test Cases

Test Scenario Expected Result Status
5 employees, 6 spots, all preferences set 100% satisfaction ✅ Passed
Spot B1 reserved for Manager only Only Manager gets B1 ✅ Passed
5 employees, 3 spots (no solution) Error message displayed ✅ Passed
Add/Delete employees UI updates correctly ✅ Passed
Add/Delete spots UI updates correctly ✅ Passed

---

⚠️ Challenges Faced & Solutions

Challenge Solution
Backtracking infinite loops Added proper state management and forward checking
Preference order not preserved Used selection order from QListWidget
UI not updating dynamically Created centralized refresh_all() method
Reserved spots not respected Added role validation in is_consistent()
No solution causing crash Return None and display user-friendly error

---

🚀 Future Improvements

· Database Integration: Store data persistently using SQLite
· Web Deployment: Convert to web application for remote access
· Email Notifications: Send allocation results to employees
· Historical Analysis: Track satisfaction trends over time
· Mobile App: Allow employees to set preferences from phones
· Export to PDF: Generate professional allocation reports
· Heatmap Visualization: Show spot occupancy patterns

---

🤝 Contributing

This project was created as part of the M-Tech Internship 2026 program. Contributions and suggestions are welcome!

---

📄 License

This project is created for educational purposes as part of the M-Tech Production & Marketing Internship Program.

---

👤 Author

Mahad Amjad

· Registration: Mtech-AI26038
· Batch: 2026
· Department: AI/ML

---

🙏 Acknowledgments

· M-Tech Production & Marketing for providing this internship opportunity
· Trainers and Mentors for guidance and support
· PyQt5 Documentation for GUI development resources

---

📞 Contact

M-Tech Production & Marketing

· Email: mtechproductionandmarketing@gmail.com
· Phone: +92 336 2222480
· Address: Haripur Main Bazar, Khyber Pakhtunkhwa, Pakistan

---

📊 Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Office_Parking_Space_Allocator.git

# Navigate to folder
cd Office_Parking_Space_Allocator

# Install dependencies
pip install PyQt5 matplotlib pandas

# Run application
python main.py
```


"""
Parking Allocator GUI - The main application window
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from csp_solver import ParkingCSP

class ParkingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.csp = ParkingCSP()
        self.setup_ui()
        self.load_sample_data()
        
    def setup_ui(self):
        """Setup the window"""
        self.setWindowTitle("🏢 Office Parking Allocator")
        self.setGeometry(100, 100, 900, 700)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Tabs
        tabs = QTabWidget()
        layout.addWidget(tabs)
        
        # Create 5 tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        
        tabs.addTab(self.tab1, "📊 Dashboard")
        tabs.addTab(self.tab2, "👤 Employees")
        tabs.addTab(self.tab3, "🅿️ Spots")
        tabs.addTab(self.tab4, "⭐ Preferences")
        tabs.addTab(self.tab5, "✅ Allocate")
        
        # Setup each tab
        self.setup_dashboard()
        self.setup_employees()
        self.setup_spots()
        self.setup_preferences()
        self.setup_allocate()
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Style
        self.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #ddd; background: white; }
            QTabBar::tab { padding: 10px 20px; background: #e0e0e0; }
            QTabBar::tab:selected { background: white; border-bottom: 3px solid #4CAF50; }
            QPushButton { background: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; }
            QPushButton:hover { background: #1976D2; }
            QLineEdit, QComboBox { padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
            QTableWidget { border: 1px solid #ddd; }
            QHeaderView::section { background: #f0f0f0; padding: 8px; }
        """)
        
    def setup_dashboard(self):
        """Dashboard tab"""
        layout = QVBoxLayout(self.tab1)
        
        # Title
        title = QLabel("📊 Parking Dashboard")
        title.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Stats grid
        grid = QGridLayout()
        layout.addLayout(grid)
        
        # Create 4 stat cards
        self.stat_emps = self.create_card("Total Employees", "0", "#4CAF50")
        self.stat_spots = self.create_card("Total Spots", "0", "#2196F3")
        self.stat_alloc = self.create_card("Allocated", "0", "#FF9800")
        self.stat_satis = self.create_card("Satisfaction", "0%", "#9C27B0")
        
        grid.addWidget(self.stat_emps, 0, 0)
        grid.addWidget(self.stat_spots, 0, 1)
        grid.addWidget(self.stat_alloc, 1, 0)
        grid.addWidget(self.stat_satis, 1, 1)
        
        # Refresh button
        btn = QPushButton("🔄 Refresh")
        btn.clicked.connect(self.refresh_dashboard)
        layout.addWidget(btn)
        
    def create_card(self, label, value, color):
        """Create a stats card"""
        card = QGroupBox()
        card.setStyleSheet(f"""
            QGroupBox {{ 
                background: {color}20; 
                border: 2px solid {color}; 
                border-radius: 10px; 
                padding: 15px;
                margin: 5px;
            }}
        """)
        
        layout = QVBoxLayout(card)
        
        val = QLabel(value)
        val.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {color};")
        val.setAlignment(Qt.AlignCenter)
        
        lbl = QLabel(label)
        lbl.setStyleSheet("font-size: 14px;")
        lbl.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(val)
        layout.addWidget(lbl)
        
        # Store reference to value label
        card.value_label = val
        
        return card
        
    def setup_employees(self):
        """Employees tab"""
        layout = QVBoxLayout(self.tab2)
        
        # Add form
        form = QHBoxLayout()
        layout.addLayout(form)
        
        self.emp_name = QLineEdit()
        self.emp_name.setPlaceholderText("Name")
        form.addWidget(self.emp_name)
        
        self.emp_role = QComboBox()
        self.emp_role.addItems(["Staff", "Manager", "Executive"])
        form.addWidget(self.emp_role)
        
        btn_add = QPushButton("➕ Add")
        btn_add.clicked.connect(self.add_employee)
        form.addWidget(btn_add)
        
        # Table
        self.emp_table = QTableWidget()
        self.emp_table.setColumnCount(3)
        self.emp_table.setHorizontalHeaderLabels(["ID", "Name", "Role"])
        self.emp_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.emp_table)
        
        # Delete
        btn_del = QPushButton("🗑️ Delete Selected")
        btn_del.clicked.connect(self.delete_employee)
        layout.addWidget(btn_del)
        
    def setup_spots(self):
        """Parking Spots tab"""
        layout = QVBoxLayout(self.tab3)
        
        # Add form
        form = QHBoxLayout()
        layout.addLayout(form)
        
        self.spot_id = QLineEdit()
        self.spot_id.setPlaceholderText("Spot ID (A1)")
        form.addWidget(self.spot_id)
        
        self.spot_loc = QLineEdit()
        self.spot_loc.setPlaceholderText("Location")
        form.addWidget(self.spot_loc)
        
        self.spot_res = QComboBox()
        self.spot_res.addItems(["None", "Manager", "Executive"])
        form.addWidget(self.spot_res)
        
        btn_add = QPushButton("➕ Add")
        btn_add.clicked.connect(self.add_spot)
        form.addWidget(btn_add)
        
        # Table
        self.spot_table = QTableWidget()
        self.spot_table.setColumnCount(3)
        self.spot_table.setHorizontalHeaderLabels(["Spot ID", "Location", "Reserved For"])
        self.spot_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.spot_table)
        
        # Delete
        btn_del = QPushButton("🗑️ Delete Selected")
        btn_del.clicked.connect(self.delete_spot)
        layout.addWidget(btn_del)
        
    def setup_preferences(self):
        """Preferences tab"""
        layout = QVBoxLayout(self.tab4)
        
        # Employee dropdown
        row = QHBoxLayout()
        layout.addLayout(row)
        row.addWidget(QLabel("Employee:"))
        self.pref_emp = QComboBox()
        row.addWidget(self.pref_emp)
        
        # Spot list
        layout.addWidget(QLabel("Select spots in order of preference (click to select multiple):"))
        self.pref_list = QListWidget()
        self.pref_list.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(self.pref_list)
        
        # Buttons
        btns = QHBoxLayout()
        layout.addLayout(btns)
        
        btn_set = QPushButton("⭐ Set Preferences")
        btn_set.clicked.connect(self.set_preferences)
        btns.addWidget(btn_set)
        
        btn_clear = QPushButton("🗑️ Clear")
        btn_clear.clicked.connect(self.clear_preferences)
        btns.addWidget(btn_clear)
        
        btn_refresh = QPushButton("🔄 Refresh")
        btn_refresh.clicked.connect(self.refresh_preferences)
        btns.addWidget(btn_refresh)
        
        # Current preferences display
        layout.addWidget(QLabel("Current Preferences:"))
        self.pref_display = QTextEdit()
        self.pref_display.setReadOnly(True)
        self.pref_display.setMaximumHeight(80)
        layout.addWidget(self.pref_display)
        
    def setup_allocate(self):
        """Allocation tab"""
        layout = QVBoxLayout(self.tab5)
        
        # Allocate button
        btn_alloc = QPushButton("🎯 RUN FAIR ALLOCATION")
        btn_alloc.setStyleSheet("""
            QPushButton {
                background: #4CAF50;
                color: white;
                font-size: 18px;
                padding: 20px;
                border-radius: 8px;
            }
            QPushButton:hover { background: #45a049; }
        """)
        btn_alloc.clicked.connect(self.run_allocation)
        layout.addWidget(btn_alloc)
        
        # Results table
        layout.addWidget(QLabel("Allocation Results:"))
        self.alloc_table = QTableWidget()
        self.alloc_table.setColumnCount(4)
        self.alloc_table.setHorizontalHeaderLabels(["Employee", "Spot", "Rank", "Satisfied"])
        self.alloc_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.alloc_table)
        
        # Metrics
        self.alloc_metrics = QLabel("")
        self.alloc_metrics.setStyleSheet("font-size: 14px; padding: 10px;")
        layout.addWidget(self.alloc_metrics)
        
    def load_sample_data(self):
        """Load example data"""
        # Employees
        employees = [
            (1, "Ali Khan", "Manager"),
            (2, "Bilal Ahmed", "Staff"),
            (3, "Fatima Noor", "Staff"),
            (4, "Hassan Ali", "Executive"),
            (5, "Ayesha Malik", "Staff"),
        ]
        for emp_id, name, role in employees:
            self.csp.add_employee(emp_id, name, role)
            
        # Spots
        spots = [
            ("A1", "Near Entrance", None),
            ("A2", "Near Entrance", None),
            ("B1", "Shaded Area", "Manager"),
            ("B2", "Shaded Area", None),
            ("C1", "Close to Exit", "Executive"),
            ("C2", "Close to Exit", None),
        ]
        for spot_id, loc, res in spots:
            self.csp.add_parking_spot(spot_id, loc, res)
            
        # Preferences
        prefs = {
            1: ["A1", "A2", "B1", "B2", "C1"],
            2: ["B1", "A1", "B2", "C1", "A2"],
            3: ["A1", "B1", "C1", "A2", "B2"],
            4: ["C1", "C2", "A1", "B1", "B2"],
            5: ["B1", "B2", "A1", "C1", "A2"],
        }
        for emp_id, p in prefs.items():
            self.csp.set_preferences(emp_id, p)
            
        self.refresh_all()
        
    def refresh_all(self):
        """Refresh everything"""
        self.refresh_employees()
        self.refresh_spots()
        self.refresh_preferences()
        self.refresh_dashboard()
        
    def refresh_employees(self):
        """Refresh employee table"""
        self.emp_table.setRowCount(len(self.csp.employees))
        for i, emp in enumerate(self.csp.employees):
            self.emp_table.setItem(i, 0, QTableWidgetItem(str(emp["id"])))
            self.emp_table.setItem(i, 1, QTableWidgetItem(emp["name"]))
            self.emp_table.setItem(i, 2, QTableWidgetItem(emp["role"]))
            
    def refresh_spots(self):
        """Refresh spots table"""
        self.spot_table.setRowCount(len(self.csp.parking_spots))
        for i, spot in enumerate(self.csp.parking_spots):
            self.spot_table.setItem(i, 0, QTableWidgetItem(spot["id"]))
            self.spot_table.setItem(i, 1, QTableWidgetItem(spot["location"]))
            self.spot_table.setItem(i, 2, QTableWidgetItem(spot["reserved_for"] or "None"))
            
    def refresh_preferences(self):
        """Refresh preferences tab"""
        # Update employee dropdown
        self.pref_emp.clear()
        for emp in self.csp.employees:
            self.pref_emp.addItem(f"{emp['name']} (ID:{emp['id']})", emp["id"])
            
        # Update spot list
        self.pref_list.clear()
        for spot in self.csp.parking_spots:
            self.pref_list.addItem(f"{spot['id']} - {spot['location']}")
            
        # Show current preferences
        emp_id = self.pref_emp.currentData()
        if emp_id and emp_id in self.csp.preferences:
            prefs = self.csp.preferences[emp_id]
            self.pref_display.setText(" → ".join(prefs) if prefs else "No preferences set")
            
    def refresh_dashboard(self):
        """Refresh dashboard stats"""
        total_emps = len(self.csp.employees)
        total_spots = len(self.csp.parking_spots)
        allocated = len(self.csp.assignment)
        
        # Calculate satisfaction
        satisfaction = 0
        if allocated > 0:
            stats = self.csp.get_stats()
            if stats:
                satisfaction = (stats["satisfied"] / stats["total"]) * 100
                
        # Update cards
        self.stat_emps.value_label.setText(str(total_emps))
        self.stat_spots.value_label.setText(str(total_spots))
        self.stat_alloc.value_label.setText(str(allocated))
        self.stat_satis.value_label.setText(f"{satisfaction:.0f}%")
        
        self.statusBar().showMessage(f"Employees: {total_emps} | Spots: {total_spots} | Allocated: {allocated}")
        
    def add_employee(self):
        """Add employee"""
        name = self.emp_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Error", "Please enter a name")
            return
            
        emp_id = max([e["id"] for e in self.csp.employees], default=0) + 1
        role = self.emp_role.currentText()
        
        self.csp.add_employee(emp_id, name, role)
        self.refresh_all()
        self.emp_name.clear()
        self.statusBar().showMessage(f"Added: {name}")
        
    def delete_employee(self):
        """Delete employee"""
        row = self.emp_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Error", "Select an employee")
            return
            
        emp_id = int(self.emp_table.item(row, 0).text())
        self.csp.employees = [e for e in self.csp.employees if e["id"] != emp_id]
        if emp_id in self.csp.preferences:
            del self.csp.preferences[emp_id]
        self.refresh_all()
        
    def add_spot(self):
        """Add parking spot"""
        spot_id = self.spot_id.text().strip().upper()
        location = self.spot_loc.text().strip()
        
        if not spot_id or not location:
            QMessageBox.warning(self, "Error", "Fill all fields")
            return
            
        if any(s["id"] == spot_id for s in self.csp.parking_spots):
            QMessageBox.warning(self, "Error", "Spot already exists")
            return
            
        reserved = self.spot_res.currentText()
        reserved = None if reserved == "None" else reserved
        
        self.csp.add_parking_spot(spot_id, location, reserved)
        self.refresh_all()
        self.spot_id.clear()
        self.spot_loc.clear()
        
    def delete_spot(self):
        """Delete spot"""
        row = self.spot_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Error", "Select a spot")
            return
            
        spot_id = self.spot_table.item(row, 0).text()
        self.csp.parking_spots = [s for s in self.csp.parking_spots if s["id"] != spot_id]
        self.refresh_all()
        
    def set_preferences(self):
        """Set preferences"""
        emp_id = self.pref_emp.currentData()
        if not emp_id:
            QMessageBox.warning(self, "Error", "Select an employee")
            return
            
        selected = self.pref_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Select at least one spot")
            return
            
        prefs = [item.text().split(" - ")[0] for item in selected]
        self.csp.set_preferences(emp_id, prefs)
        self.refresh_preferences()
        self.statusBar().showMessage(f"Preferences saved for employee {emp_id}")
        
    def clear_preferences(self):
        """Clear preferences"""
        emp_id = self.pref_emp.currentData()
        if emp_id and emp_id in self.csp.preferences:
            self.csp.preferences[emp_id] = []
            self.refresh_preferences()
            
    def run_allocation(self):
        """Run the allocation"""
        if len(self.csp.employees) == 0:
            QMessageBox.warning(self, "Error", "No employees")
            return
            
        if len(self.csp.parking_spots) == 0:
            QMessageBox.warning(self, "Error", "No parking spots")
            return
            
        # Check if everyone has preferences
        for emp in self.csp.employees:
            if emp["id"] not in self.csp.preferences or not self.csp.preferences[emp["id"]]:
                QMessageBox.warning(self, "Error", f"{emp['name']} has no preferences set!")
                return
        
        result = self.csp.allocate()
        
        if result is None:
            QMessageBox.warning(self, "No Solution", 
                "Could not find a valid allocation. Try adding more spots or removing reserved spots.")
            return
            
        # Show results
        stats = self.csp.get_stats()
        
        self.alloc_table.setRowCount(len(result))
        for i, (emp_id, spot_id) in enumerate(result.items()):
            emp = next((e for e in self.csp.employees if e["id"] == emp_id), None)
            emp_name = emp["name"] if emp else f"ID:{emp_id}"
            
            detail = stats["details"].get(emp_id, {})
            rank = str(detail.get("rank", "N/A"))
            satisfied = "✅ Yes" if detail.get("satisfied", False) else "❌ No"
            
            self.alloc_table.setItem(i, 0, QTableWidgetItem(emp_name))
            self.alloc_table.setItem(i, 1, QTableWidgetItem(spot_id))
            self.alloc_table.setItem(i, 2, QTableWidgetItem(rank))
            self.alloc_table.setItem(i, 3, QTableWidgetItem(satisfied))
            
        # Update metrics
        total = stats["total"]
        satisfied = stats["satisfied"]
        rate = (satisfied / total * 100) if total > 0 else 0
        
        self.alloc_metrics.setText(
            f"✅ {total} spots allocated | ⭐ {satisfied}/{total} got top-3 preference ({rate:.0f}% satisfaction)"
        )
        
        self.refresh_dashboard()
        self.statusBar().showMessage("Allocation complete!")
        
    def refresh_dashboard(self):
        """Refresh dashboard"""
        total_emps = len(self.csp.employees)
        total_spots = len(self.csp.parking_spots)
        allocated = len(self.csp.assignment)
        
        satisfaction = 0
        if allocated > 0:
            stats = self.csp.get_stats()
            if stats:
                satisfaction = (stats["satisfied"] / stats["total"]) * 100
                
        self.stat_emps.value_label.setText(str(total_emps))
        self.stat_spots.value_label.setText(str(total_spots))
        self.stat_alloc.value_label.setText(str(allocated))
        self.stat_satis.value_label.setText(f"{satisfaction:.0f}%")

def main():
    app = QApplication(sys.argv)
    window = ParkingApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
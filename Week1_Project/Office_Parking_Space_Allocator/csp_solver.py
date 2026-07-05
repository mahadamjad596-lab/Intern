"""
Parking CSP Solver - Handles the logic for fair allocation
"""

class ParkingCSP:
    def __init__(self):
        self.employees = []
        self.parking_spots = []
        self.preferences = {}
        self.assignment = {}
        
    def add_employee(self, emp_id, name, role="Staff"):
        """Add an employee"""
        self.employees.append({
            "id": emp_id,
            "name": name,
            "role": role
        })
        self.preferences[emp_id] = []
        
    def add_parking_spot(self, spot_id, location, reserved_for=None):
        """Add a parking spot"""
        self.parking_spots.append({
            "id": spot_id,
            "location": location,
            "reserved_for": reserved_for
        })
        
    def set_preferences(self, emp_id, preferred_spots):
        """Set which spots an employee wants (in order)"""
        if emp_id in self.preferences:
            self.preferences[emp_id] = preferred_spots
            
    def is_consistent(self, emp_id, spot_id):
        """Check if assigning this spot is allowed"""
        # Check if spot already taken
        if spot_id in self.assignment.values():
            return False
            
        # Check if spot is reserved for someone else
        spot = next((s for s in self.parking_spots if s["id"] == spot_id), None)
        if spot and spot["reserved_for"]:
            emp = next((e for e in self.employees if e["id"] == emp_id), None)
            if emp and emp["role"] != spot["reserved_for"]:
                return False
                
        return True
    
    def solve(self, emp_index=0):
        """Find a valid allocation"""
        if emp_index >= len(self.employees):
            return True
            
        emp = self.employees[emp_index]
        emp_id = emp["id"]
        
        # Try each preferred spot
        for spot_id in self.preferences.get(emp_id, []):
            if self.is_consistent(emp_id, spot_id):
                self.assignment[emp_id] = spot_id
                
                if self.solve(emp_index + 1):
                    return True
                    
                del self.assignment[emp_id]
                
        return False
    
    def allocate(self):
        """Run the allocation"""
        self.assignment = {}
        
        if self.solve():
            return self.assignment
        else:
            return None
    
    def get_stats(self):
        """Get allocation statistics"""
        if not self.assignment:
            return None
            
        stats = {
            "total": len(self.assignment),
            "satisfied": 0,
            "details": {}
        }
        
        for emp_id, spot_id in self.assignment.items():
            prefs = self.preferences.get(emp_id, [])
            rank = prefs.index(spot_id) + 1 if spot_id in prefs else 999
            satisfied = rank <= 3
            
            if satisfied:
                stats["satisfied"] += 1
                
            stats["details"][emp_id] = {
                "spot": spot_id,
                "rank": rank,
                "satisfied": satisfied
            }
            
        return stats
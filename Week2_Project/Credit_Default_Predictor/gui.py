import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import re

# Load trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Model file not found. Please ensure 'model.pkl' exists.")
    exit()

fields = [
    "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
    "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
    "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4",
    "BILL_AMT5", "BILL_AMT6",
    "PAY_AMT1", "PAY_AMT2", "PAY_AMT3",
    "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
]

class CreditDefaultApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Credit Default Predictor")
        self.root.geometry("520x800")
        self.root.configure(bg='#f0f2f5')
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TFrame', background='#f0f2f5')
        style.configure('Card.TFrame', background='white', relief='raised', borderwidth=1)
        
        # Main container
        main_frame = ttk.Frame(root, style='Custom.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg='#2c3e50', height=80, relief='flat')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🏦 Credit Risk Assessment",
            font=("Arial", 20, "bold"),
            bg='#2c3e50',
            fg='white'
        ).pack(expand=True)
        
        tk.Label(
            header_frame,
            text="Default Payment Prediction",
            font=("Arial", 10),
            bg='#2c3e50',
            fg='#bdc3c7'
        ).pack(expand=True)
        
        # Scrollable frame for inputs
        canvas = tk.Canvas(main_frame, bg='#f0f2f5', highlightthickness=0)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='Custom.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Input fields with cards
        self.entries = {}
        self.fields_info = {
            "LIMIT_BAL": {"label": "Credit Limit Balance", "tooltip": "Amount of given credit (NT$)"},
            "SEX": {"label": "Gender (1=M, 2=F)", "tooltip": "1: Male, 2: Female"},
            "EDUCATION": {"label": "Education Level", "tooltip": "1: Grad School, 2: University, 3: High School, 4: Others"},
            "MARRIAGE": {"label": "Marital Status", "tooltip": "1: Married, 2: Single, 3: Others"},
            "AGE": {"label": "Age (years)", "tooltip": "Age in years"},
            "PAY_0": {"label": "Payment Status (Sept)", "tooltip": "Payment status in September (-1: Pay duly, 1-9: Delay months)"},
            "PAY_2": {"label": "Payment Status (Aug)", "tooltip": "Payment status in August"},
            "PAY_3": {"label": "Payment Status (Jul)", "tooltip": "Payment status in July"},
            "PAY_4": {"label": "Payment Status (Jun)", "tooltip": "Payment status in June"},
            "PAY_5": {"label": "Payment Status (May)", "tooltip": "Payment status in May"},
            "PAY_6": {"label": "Payment Status (Apr)", "tooltip": "Payment status in April"},
            "BILL_AMT1": {"label": "Bill Amount (Sept)", "tooltip": "Bill amount in September (NT$)"},
            "BILL_AMT2": {"label": "Bill Amount (Aug)", "tooltip": "Bill amount in August (NT$)"},
            "BILL_AMT3": {"label": "Bill Amount (Jul)", "tooltip": "Bill amount in July (NT$)"},
            "BILL_AMT4": {"label": "Bill Amount (Jun)", "tooltip": "Bill amount in June (NT$)"},
            "BILL_AMT5": {"label": "Bill Amount (May)", "tooltip": "Bill amount in May (NT$)"},
            "BILL_AMT6": {"label": "Bill Amount (Apr)", "tooltip": "Bill amount in April (NT$)"},
            "PAY_AMT1": {"label": "Payment Amount (Sept)", "tooltip": "Payment amount in September (NT$)"},
            "PAY_AMT2": {"label": "Payment Amount (Aug)", "tooltip": "Payment amount in August (NT$)"},
            "PAY_AMT3": {"label": "Payment Amount (Jul)", "tooltip": "Payment amount in July (NT$)"},
            "PAY_AMT4": {"label": "Payment Amount (Jun)", "tooltip": "Payment amount in June (NT$)"},
            "PAY_AMT5": {"label": "Payment Amount (May)", "tooltip": "Payment amount in May (NT$)"},
            "PAY_AMT6": {"label": "Payment Amount (Apr)", "tooltip": "Payment amount in April (NT$)"}
        }
        
        # Create input cards
        for i, field in enumerate(fields):
            # Card container
            card_frame = tk.Frame(
                scrollable_frame,
                bg='white',
                relief='flat',
                bd=1,
                highlightbackground='#e0e0e0',
                highlightthickness=1
            )
            card_frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Inner padding
            inner_frame = tk.Frame(card_frame, bg='white')
            inner_frame.pack(fill=tk.X, padx=15, pady=10)
            
            # Label frame with tooltip
            label_frame = tk.Frame(inner_frame, bg='white')
            label_frame.pack(fill=tk.X)
            
            label_text = self.fields_info.get(field, {}).get("label", field)
            tk.Label(
                label_frame,
                text=f"{i+1}. {label_text}",
                font=("Arial", 10, "bold"),
                bg='white',
                fg='#2c3e50'
            ).pack(side=tk.LEFT)
            
            # Tooltip indicator
            if field in self.fields_info:
                tk.Label(
                    label_frame,
                    text=" ⓘ",
                    font=("Arial", 10),
                    bg='white',
                    fg='#3498db',
                    cursor="hand2"
                ).pack(side=tk.LEFT)
            
            # Entry field
            entry = tk.Entry(
                inner_frame,
                font=("Arial", 10),
                bg='#f8f9fa',
                relief='flat',
                bd=1,
                highlightbackground='#d0d0d0',
                highlightthickness=1
            )
            entry.pack(fill=tk.X, pady=(5, 0))
            entry.config(highlightcolor='#3498db')
            
            # Store entry
            self.entries[field] = entry
            
            # Bind hover effects
            entry.bind("<Enter>", lambda e, entry=entry: entry.config(bg='#e8f4fd', highlightbackground='#3498db'))
            entry.bind("<Leave>", lambda e, entry=entry: entry.config(bg='#f8f9fa', highlightbackground='#d0d0d0'))
        
        # Pack scrollable components
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=(0, 10))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Action buttons frame
        button_frame = tk.Frame(main_frame, bg='#f0f2f5')
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Predict button
        self.predict_btn = tk.Button(
            button_frame,
            text="🔍 Predict Default Risk",
            command=self.predict,
            bg='#3498db',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            cursor="hand2",
            height=2,
            padx=20
        )
        self.predict_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear All",
            command=self.clear_fields,
            bg='#e74c3c',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            cursor="hand2",
            height=2,
            padx=15
        )
        clear_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Result frame
        self.result_frame = tk.Frame(
            main_frame,
            bg='white',
            relief='flat',
            bd=1,
            highlightbackground='#e0e0e0',
            highlightthickness=1,
            height=120
        )
        self.result_frame.pack(fill=tk.X, pady=(15, 0))
        self.result_frame.pack_propagate(False)
        
        # Result content
        self.result_inner = tk.Frame(self.result_frame, bg='white')
        self.result_inner.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.result_label = tk.Label(
            self.result_inner,
            text="Enter all values and click 'Predict'",
            font=("Arial", 11),
            bg='white',
            fg='#7f8c8d'
        )
        self.result_label.pack(expand=True)
        
        self.score_label = tk.Label(
            self.result_inner,
            text="",
            font=("Arial", 10),
            bg='white',
            fg='#7f8c8d'
        )
        self.score_label.pack()
    
    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_label.config(text="Enter all values and click 'Predict'", fg='#7f8c8d')
        self.score_label.config(text="")
        self.result_frame.config(bg='white')
        self.result_inner.config(bg='white')
    
    def predict(self):
        try:
            # Validate and collect inputs
            values = []
            for field, entry in self.entries.items():
                value = entry.get().strip()
                if not value:
                    raise ValueError(f"Please enter a value for {field}")
                
                try:
                    num_value = float(value)
                    values.append(num_value)
                except ValueError:
                    raise ValueError(f"Invalid number format for {field}")
            
            # Create DataFrame
            data = pd.DataFrame([values], columns=fields)
            
            # Make prediction
            prediction = model.predict(data)[0]
            
            # Calculate score
            if prediction == 0:
                score = 780
                risk = "LOW RISK ✅"
                color = "#27ae60"
                bg_color = "#d5f4e6"
                status = "This client is likely to repay on time"
            else:
                score = 560
                risk = "HIGH RISK ⚠️"
                color = "#e74c3c"
                bg_color = "#fde8e8"
                status = "This client has high default probability"
            
            # Update result
            self.result_frame.config(bg=bg_color)
            self.result_inner.config(bg=bg_color)
            
            self.result_label.config(
                text=f"Prediction: {risk}",
                fg=color,
                font=("Arial", 16, "bold")
            )
            
            self.score_label.config(
                text=f"Credit Score: {score}\n{status}",
                fg='#2c3e50',
                font=("Arial", 11)
            )
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Prediction Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreditDefaultApp(root)
    root.mainloop()
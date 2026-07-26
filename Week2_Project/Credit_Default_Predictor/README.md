Credit Default Predictor (v2)

A machine learning application that predicts credit default risk using customer financial data, featuring an intuitive GUI interface.

---

📋 Table of Contents

· Project Overview
· Key Features
· Technologies Used
· Dataset Information
· Project Structure
· Installation Guide
· How to Run
· Machine Learning Model
· Output Interpretation
· Future Enhancements
· Author

---

🎯 Project Overview

The Credit Default Predictor (v2) is a sophisticated Machine Learning solution developed in Python to assess the likelihood of customers defaulting on credit payments. Leveraging the power of Random Forest classification, this application provides financial institutions with quick, data-driven risk assessments through an accessible graphical interface built with Tkinter.

---

✨ Key Features

· Real-time Credit Risk Assessment: Instant prediction of default probability
· Random Forest Classification: Robust ensemble learning for accurate predictions
· Intuitive GUI: User-friendly interface for easy data input and result visualization
· Dual Output: Provides both risk level (Low/High) and simplified credit score
· Model Persistence: Trained model saved for immediate reuse
· Comprehensive Input Fields: Accepts 17+ financial and demographic parameters

---

🛠️ Technologies Used

Category Technologies
Programming Language Python 3.x
Machine Learning Scikit-learn (Random Forest)
Data Processing Pandas, NumPy
GUI Framework Tkinter
Model Serialization Joblib
Excel Data Handling xlrd

---

📊 Dataset Information

The project utilizes the renowned Default of Credit Card Clients dataset from UCI Machine Learning Repository.

Dataset Features:

· Credit Limit: Customer's credit amount
· Demographics: Gender, Education level, Marriage status, Age
· Payment History: 6 months of repayment status
· Financial History: Monthly bill amounts (6 months)
· Transaction Data: Previous payment amounts (6 months)

Dataset Size:

· Samples: 30,000+ records
· Features: 24 input variables
· Target: Binary (Default: Yes/No)

---

📁 Project Structure

```
CreditDefaultPredictor/
│
├── 📄 train_model.py        # Model training script
├── 🖥️ gui.py                # Tkinter GUI application
├── 🧠 model.pkl             # Trained Random Forest model
├── 📊 default of credit card clients.xls  # Dataset
├── 📘 README.md             # Project documentation
└── 📦 requirements.txt      # Dependencies list
```

---

🔧 Installation Guide

Prerequisites

· Python 3.7 or higher installed
· pip package manager

Step 1: Clone or Download the Repository

```bash
git clone https://github.com/yourusername/CreditDefaultPredictor.git
cd CreditDefaultPredictor
```

Step 2: Install Required Libraries

```bash
pip install pandas numpy scikit-learn joblib xlrd tkinter
```

Or install via requirements file:

```bash
pip install -r requirements.txt
```

---

🚀 How to Run

Option 1: Full Pipeline (Recommended)

Step 1: Train the Model

```bash
python train_model.py
```

This script:

· Loads and preprocesses the dataset
· Trains the Random Forest classifier
· Saves the trained model as model.pkl

Step 2: Launch the GUI

```bash
python gui.py
```

Option 2: Quick Start (Using Pre-trained Model)

If model.pkl already exists:

```bash
python gui.py
```

---

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Why Random Forest?

· Ensemble Learning: Combines multiple decision trees for better accuracy
· Handles Imbalanced Data: Effective for credit default prediction where defaults are rare
· Feature Importance: Identifies key risk indicators
· Robust to Overfitting: Reduces variance compared to single decision trees

Model Training Parameters:

```python
RandomForestClassifier(
    n_estimators=100,    # Number of trees
    random_state=42,     # Reproducibility
    max_depth=None       # Let trees grow fully
)
```

Model Performance Metrics:

· Accuracy: ~82%
· Precision: ~75% (Default class)
· Recall: ~70% (Default class)
· F1-Score: ~72% (Default class)

---

📱 Output Interpretation

Risk Level Categories:

Category Interpretation
🔴 High Risk Customer shows characteristics similar to past defaulters
🟢 Low Risk Customer appears financially stable with low default probability

Credit Score Interpretation:

Score Range Risk Category
600-700 Low Risk
500-599 Medium Risk
300-499 High Risk

---

🔮 Future Enhancements

Short-term Improvements:

· Advanced GUI with matplotlib integration for visual analytics
· Batch prediction capability (CSV upload)
· Real-time data validation and error handling
· Export results to CSV/PDF

Medium-term Goals:

· Feature importance visualization (SHAP/LIME)
· Integration with SQL database for storing predictions
· Multiple ML models comparison (XGBoost, Neural Networks)
· Web deployment using Flask/Django

Long-term Vision:

· REST API for integration with banking systems
· Dashboard with historical prediction tracking
· User authentication and role-based access
· Automated model retraining pipeline

---

👨‍💻 Author

Mahad Amjad
Machine Learning Developer

Academic Context:

· Batch: 2026
· Program: AI/ML Internship
· Organization: M-Tech Production & Marketing

---

📝 License

This project is developed for educational and internship purposes.

Note: The credit default prediction is for informational purposes only and should not be used as the sole basis for financial decisions.

---

🙏 Acknowledgments

· UCI Machine Learning Repository for providing the dataset
· M-Tech Production & Marketing for internship opportunity
· All contributors and mentors

---

⭐ If you found this project helpful, please give it a star! ⭐

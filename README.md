# 🎓 Student Grade Prediction System

A Machine Learning project that predicts student academic performance (final grade) using various educational, behavioral, and personal factors. This project combines data analysis, model building, and a web-based frontend to provide real-time predictions.

---

## 📌 Project Overview

Educational institutions often face challenges in identifying students who are at risk of poor academic performance. Early prediction can help in providing timely support and improving outcomes.

This project uses Machine Learning techniques to:

* Analyze student-related data
* Identify key factors influencing performance
* Predict the final grade (G3)
* Provide performance insights and suggestions

---

## 🎯 Objectives

* Predict student final grade using Machine Learning
* Identify important features affecting academic performance
* Build a user-friendly interface for real-time prediction
* Assist educators in early intervention strategies

---

## 📊 Dataset Information

* **Dataset Name:** UCI Student Performance Dataset
* **Source:** UCI Machine Learning Repository
* **File Used:** `student-mat.csv`
* **Target Variable:** G3 (Final Grade)

### 📁 Features Used

* Age
* Study Time
* Past Failures
* Absences
* Internet Access
* Family Support
* Higher Education Interest
* First Period Grade (G1)
* Second Period Grade (G2)

---

## 🧠 Machine Learning Model

### 🔹 Algorithm Used

* Random Forest Regressor

### 🔹 Why Random Forest?

* Handles complex and nonlinear relationships
* Reduces overfitting using ensemble learning
* Provides high accuracy on tabular data

---

## ⚙️ Project Workflow

1. Data Collection
2. Data Preprocessing

   * Handling categorical variables
   * Encoding using OneHotEncoder
3. Feature Selection
4. Train-Test Split (80:20)
5. Model Training
6. Model Evaluation
7. Model Saving using joblib
8. Frontend Integration using Streamlit

---

## 📈 Evaluation Metrics

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score (Coefficient of Determination)**

These metrics were used to evaluate the model’s prediction performance.

---

## 💻 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 🖥️ Application Features

* Interactive web-based UI using Streamlit
* Real-time grade prediction
* Performance classification:

  * Excellent
  * Good
  * Average
  * Needs Improvement
* Suggestions based on predicted performance
* Clean and user-friendly interface

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Madankk-06/student-grade-prediction.git
cd student-grade-prediction
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the Model

```bash
python train_model.py
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
student-grade-prediction/
│
├── data/                   # Dataset files
│   └── student-mat.csv
│
├── model/                  # Saved ML model
│   └── student_grade_model.pkl
│
├── notebooks/              # Jupyter notebooks
│   └── grade_prediction.ipynb
│
├── app.py                  # Streamlit frontend
├── train_model.py          # Model training script
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 📊 Sample Output

* Predicted Grade: 14.5 / 20
* Performance Level: Good
* Suggestions: Improve study time and reduce absences

---

## 🔍 Key Insights

* Previous grades (G1 and G2) strongly influence final performance
* Study time and failures significantly impact results
* Support systems (family/internet) also contribute

---

## 🚀 Future Enhancements

* Deploy application on cloud (Streamlit Cloud / Render)
* Add more datasets for better generalization
* Implement advanced models (XGBoost, Neural Networks)
* Add data visualization dashboard
* Enable multi-student batch prediction

---

## 👨‍💻 Author

**Madan**
MCA Student

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be applied in education to predict student performance and support better decision-making. It provides a scalable and practical solution for academic institutions.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!

# 📊 Employee Dataset Generation, Cleaning, and Full EDA in Python

This project demonstrates a complete **data analysis pipeline**:

> **Synthetic data generation → Data cleaning → Feature engineering → Exploratory Data Analysis (EDA) → Insights**

The dataset simulates employee information across departments, regions, salaries, performance, and sales to practice real-world data preparation and analysis techniques.

---

## 🧱 Project Workflow

### 1️⃣ Synthetic Dataset Generation

Using `Faker`, `NumPy`, and `Pandas`, a realistic employee dataset is generated with:

* 5000+ employee records
* Departments, regions, gender
* Salary, age, performance score, sales
* Joining dates from 2015 onward
* Intentional **missing values** and **duplicates** to simulate real data problems

---

### 2️⃣ Data Cleaning

The script handles common real-world data issues:

* Filling missing values using:

  * Mean (Salary, Sales)
  * Median (Age)
  * Forward fill (PerformanceScore)
* Removing duplicate rows
* Correcting data types
* Converting columns to categories for efficiency

---

### 3️⃣ Feature Engineering

New meaningful features are created:

* `Salary_per_year_experience` → salary normalized by tenure
* `Category_salary` → Low / Medium / High salary classification
* `is_outlier` → Outlier detection using IQR method

---

### 4️⃣ Exploratory Data Analysis (EDA)

The EDA script performs:

#### ✅ General overview

* Shape, types, missing values, descriptive statistics

#### ✅ Univariate analysis

* Bar charts for top categories in categorical columns

#### ✅ Bivariate analysis

* Correlation heatmap
* Scatter plots (e.g., Sales vs Quantity if present)

#### ✅ Time series analysis

* Monthly sales trends
* Day-of-week sales behavior

#### ✅ Customer & product insights

* Top customers by revenue
* Top products by revenue

#### ✅ Outlier detection

* Boxplots for salary/sales
* Top 5 highest transactions

---

## 📦 Requirements

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn faker
```

---

## ▶️ How to Run

### Step 1 — Generate and clean dataset

```bash
python generate_and_clean.py
```

This creates:

```
Cleaned_employee_dataset.csv
```

### Step 2 — Run EDA

```bash
python eda_analysis.py
```

This will display all analysis plots and insights.

---

## 📁 Dataset Columns

| Column                     | Description         |
| -------------------------- | ------------------- |
| EmployeeID                 | Unique employee ID  |
| Name                       | Fake generated name |
| Department                 | Department name     |
| Region                     | Work region         |
| Gender                     | Gender              |
| Age                        | Employee age        |
| Salary                     | Employee salary     |
| JoiningDate                | Date of joining     |
| PerformanceScore           | Rating from 1 to 5  |
| Sales                      | Sales generated     |
| Salary_per_year_experience | Engineered metric   |
| Category_salary            | Salary category     |
| is_outlier                 | Outlier flag        |

---

## 🧠 Concepts Demonstrated

* Handling missing data
* Removing duplicates
* Feature engineering
* Outlier detection with IQR
* Correlation analysis
* Time-series aggregation
* Categorical and numerical visualization
* Data type optimization

---

## 🚀 Purpose of This Project

This project is useful for demonstrating:

* Data cleaning skills required in real projects
* Analytical thinking and data exploration
* Practical use of Python for data analysis
* Ability to derive insights from structured data

---

## 👤 Author

Olimboy Qazoqov
Automation & Electrical Engineering
GitHub: [https://github.com/olimboy-qazoqov](https://github.com/olimboy-qazoqov)

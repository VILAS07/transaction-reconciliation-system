# 💼 Transaction Reconciliation System

A **Streamlit-based data reconciliation tool** that compares two datasets (e.g., bank vs company records) and identifies:

* ✅ Matched transactions
* ⚠️ Mismatched transactions
* ❌ Missing transactions

This project simulates real-world **financial reconciliation workflows** used in enterprise systems.

---

## 🚀 Demo

*(Add a screenshot here after running the app)*

![App Screenshot](screenshot.png)

---

## 🧠 Problem Statement

In financial systems, data from different sources (e.g., bank statements and internal records) must be **reconciled** to ensure consistency.

Manual reconciliation is:

* Time-consuming ⏳
* Error-prone ❌
* Difficult to scale 📉

This project automates the process using Python.

---

## ⚙️ Features

* 📂 Upload two CSV files
* 🔍 Automatic transaction matching using `TransactionID`
* ⚖️ Detect mismatches in:

  * Amount
  * Date
* ❌ Identify missing transactions
* 📊 Interactive dashboard (Streamlit UI)
* 📥 Download results as CSV files

---

## 🧠 Reconciliation Logic

The system performs:

### 1. Exact Matching

* Uses `TransactionID` as the primary key

### 2. Matched Records

* Same TransactionID
* Same Amount and Date

### 3. Mismatched Records

* Same TransactionID
* Different Amount or Date

### 4. Missing Records

* Transaction exists in one dataset but not the other

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** → Data processing
* **Streamlit** → Interactive UI

---

## 📁 Project Structure

```
transaction-reconciliation-system/
│
├── app.py
├── bank.csv
├── company.csv
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/VILAS07/transaction-reconciliation-system.git
cd transaction-reconciliation-system
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 📊 Example Output

The system generates:

* `matched.csv` → Correct transactions
* `mismatched.csv` → Value differences
* `missing.csv` → Unmatched records

---

## 💡 Industry Relevance

This project simulates **financial reconciliation systems** similar to tools like Intellimatch used in banking and finance.

It demonstrates:

* Data validation
* Record matching
* Exception handling
* Financial data integrity

---

## 🚀 Future Improvements

* 🔄 Fuzzy matching (AI-based matching)
* 📅 Date tolerance (±1 day matching)
* 📈 Analytics dashboard (charts & insights)
* 🤖 Anomaly detection using Machine Learning
* 🌐 Deployment (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Vilas PK**
B.Tech in Artificial Intelligence & Data Science

* Python | Machine Learning | Data Science
* Computer Vision (YOLOv8)
* LLM Applications

---

## ⭐ Acknowledgement

Inspired by real-world reconciliation workflows in financial systems and enterprise tools.

---

## 📌 Note

This is a **prototype system** built for learning and demonstration purposes.

# ▶️ How to Run the Project

Follow these steps to run the **Group Expense Manager** locally.

---

## ✅ Prerequisites
- Python **3.9 or higher**
- pip (comes with Python)

Check your Python version:
```bash
python --version
````

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

## 2️⃣ (Recommended) Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add Gemini API Key (Optional Feature)

Open `app.py` and update this line:

```python
GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"
```

> ⚠️ Do not commit your API key to GitHub.

If you skip this step, the app will still work — only the Gemini summary feature will be unavailable.

---

## 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 6️⃣ Open in Browser

Streamlit will automatically open the app.
If not, visit:

```
http://localhost:8501
```

---

## 🗂️ Notes

* `expenses.db` is created automatically
* No external database setup needed
* Works fully offline (except Gemini feature)

---

## 🧪 Quick Demo Checklist

1. Add participants
2. Add expenses
3. Spin the payer
4. View settlements
5. Generate Gemini funny summary

---

## ❗ Common Issues

**Streamlit not found**

```bash
pip install streamlit
```

**Wrong Python version**
Use Python 3.9+


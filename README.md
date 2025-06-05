# Python Code Analyzer

This project is a Python code analysis tool designed to detect structural and maintainability issues in Python source files, including:
- Functions that are too long
- Files that are too long
- Functions missing documentation strings (docstrings)
- Unused variables

## 📦 Project Structure

- `main.py` – Main script to run the analysis on Python files.
- `analyzer.py` – Contains the `MyVisitor` class which performs the analysis using the AST (Abstract Syntax Tree) module.
- `server.py` – A FastAPI server that accepts Python files via POST requests for analysis.
- `static/` – Directory containing test/example Python files.
- `tests/` – (Optional) Unit tests for components.

## ⚙️ Requirements

- Python 3.8+
- Required packages:
  - `fastapi`
  - `uvicorn`
  - `requests`

Install dependencies with:

```bash
pip install -r requirements.txt
🚀 How to Use
Run the server
bash
Copy
Edit
uvicorn server:app --reload
Send files for analysis
You can send files using a Python script with requests:

python
Copy
Edit
files_to_send = [("files", open("example.py", "rb"))]
res = requests.post("http://127.0.0.1:8000/analyze", files=files_to_send)
print(res.json())
<div dir="rtl">
# Python Code Analyzer

פרויקט זה הוא כלי לניתוח קוד Python המיועד לאבחון בעיות מבניות ותחזוקתיות בקוד, כמו:
- פונקציות ארוכות מדי
- קבצים ארוכים מדי
- פונקציות ללא תיעוד (docstring)
- משתנים שהוגדרו אך לא נעשה בהם שימוש

## 📦 תוכן הפרויקט
- `main.py` – קובץ ראשי להפעלת הניתוח על קבצים.
- `analyzer.py` – מכיל את מחלקת `MyVisitor` אשר מריצה את הניתוח באמצעות AST.
- `server.py` – שרת FastAPI שמקבל קבצים לניתוח דרך בקשת POST.
- `static/` – תיקייה עם קבצי בדיקה.
- `tests/` – בדיקות יחידה אם קיימות.

## ⚙️ דרישות מערכת

- Python 3.8+
- הספריות:
  - `fastapi`
  - `uvicorn`
  - `requests`

ניתן להתקין בעזרת:

```bash
pip install -r requirements.txt

>/div>

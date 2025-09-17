# Flask Notes

## 1. What is Flask?

- Flask is a **micro web framework** for Python.
- It is lightweight, simple, and easy to use.
- It is called a "micro" framework because it does **not include database abstraction layer, form validation, or other components** by default. You can add these as needed.
- Flask is ideal for **small to medium web applications**, APIs, or prototypes.

---

## 2. Features of Flask

- Lightweight and minimalistic
- Built-in **development server**
- **Jinja2 templating engine** for HTML rendering
- Easy **URL routing**
- Extensible with Flask **extensions** (for databases, authentication, forms, etc.)
- RESTful request handling

---

## 3. Installation

### Step 1: Create a virtual environment (recommended)

```bash
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Flask

```bash
pip install Flask
```

### What is pip?

pip is the package installer for Python. It allows you to install, update, and manage Python packages (libraries or modules) from the Python Package Index (PyPI).

### Step 3: Verify installation

```bash
python -m flask --version
```

---

## 4. Basic Flask Application

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**

- `Flask(__name__)` → creates a Flask app instance.
- `@app.route('/')` → URL route decorator.
- `home()` → function that runs when accessing `'/'`.
- `app.run(debug=True)` → starts the development server with debugging enabled.

---

## 5. Flask Project Structure (Recommended)

```
project/
│
├── app.py            # Main Flask application
├── templates/        # HTML templates
│   └── index.html
├── static/           # CSS, JS, images
│   └── style.css
└── venv/             # Virtual environment
```

---

## 6. Flask Theory Concepts

### a. Routes

- Define which URL triggers which function.
- Example:

```python
@app.route('/about')
def about():
    return "About page"
```

### b. HTTP Methods

- GET → Retrieve data (default)
- POST → Send data to server
- Example:

```python
@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted"
```

### c. Templates

- Flask uses **Jinja2** for templating.
- Example `templates/index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
  </head>
  <body>
    <h1>{{ title }}</h1>
  </body>
</html>
```

- Render template from Python:

```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html', title="Welcome!")
```

### d. Static Files

- CSS, JS, and images go in the `static/` folder.
- Example usage in HTML:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

### e. Flask Extensions

- Flask has many extensions for common tasks:

  - **Flask-SQLAlchemy** → Database
  - **Flask-WTF** → Forms
  - **Flask-Login** → Authentication
  - **Flask-Migrate** → Database migrations

---

## 7. Advantages of Flask

- Lightweight and flexible
- Simple to learn
- Large community and many extensions
- Ideal for APIs and small apps

---

## 8. Disadvantages of Flask

- Not suitable for very large applications out-of-the-box
- Some features need third-party extensions
- No built-in admin interface like Django

---

## 9. Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

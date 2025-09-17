# Notes

{{ title }} → displays a variable passed from Python.

{{ url_for('static', filename='style.css') }} → generates correct URL for static files.

{% block content %}{% endblock %} → placeholder for child templates to insert their content.

# Child Templates

{% extends "base.html" %}
{% block content %}

<h1>Welcome to {{ title }}</h1>
{% if name %}
<p>Hello, {{ name }}!</p>
{% endif %}
{% endblock %}

1. {% extends "base.html" %} → uses base.html as a layout.
2. {% block content %} → inserts content into base.html.
3. {% if %} ... {% endif %} → conditional rendering.
4. {% for item in list %} ... {% endfor %} → loops (used in users.html).

- HTMl files has to be in
  template/

- CSS files has to be in
  static/

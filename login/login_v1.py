from flask import Flask, jsonify, request, render_template_string
import csv
from pathlib import Path

app = Flask(__name__)

# HTML template with login form
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

def load_users():
    if not Path('users.csv').exists():
        with open('users.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['email', 'password'])
            writer.writerow(['admin@example.com', 'admin123'])

def verify_login(email, password):
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        for user in reader:
            if user['email'] == email and user['password'] == password:
                return True
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if verify_login(email, password):
            message = "Login successful!"
        else:
            message = "Invalid credentials"
    return render_template_string(LOGIN_TEMPLATE, message=message)

if __name__ == '__main__':
    load_users()
    app.run(debug=True)
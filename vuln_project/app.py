# Vulnerable Python application for testing security scanners
import os
import subprocess
import sqlite3
import pickle
import yaml
import hashlib
from flask import Flask, request, render_template_string

app = Flask(__name__)

# VULN: Hardcoded secrets

# VULN: Weak cryptography
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULN: SQL Injection
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

# VULN: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = os.system("ping -c 1 " + host)
    return str(result)

# VULN: Another command injection via subprocess
@app.route('/lookup')
def lookup():
    domain = request.args.get('domain')
    output = subprocess.check_output("nslookup " + domain, shell=True)
    return output

# VULN: Server-Side Template Injection (SSTI)
@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

# VULN: Insecure deserialization
@app.route('/load')
def load_data():
    data = request.args.get('data')
    obj = pickle.loads(bytes.fromhex(data))
    return str(obj)

# VULN: YAML unsafe load
@app.route('/parse_yaml')
def parse_yaml():
    yaml_data = request.args.get('yaml')
    parsed = yaml.load(yaml_data)  # unsafe load
    return str(parsed)

# VULN: Path traversal
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    with open('/var/data/' + filename, 'r') as f:
        return f.read()

# VULN: Open redirect
@app.route('/redirect')
def redirect_user():
    url = request.args.get('url')
    return f'<meta http-equiv="refresh" content="0;url={url}">'

# VULN: Debug mode enabled
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

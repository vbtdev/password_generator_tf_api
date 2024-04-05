from flask import request, render_template, jsonify
from flask_bootstrap import Bootstrap
import random
import string

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    length = random.randint(5, 10)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return jsonify({'password': password})
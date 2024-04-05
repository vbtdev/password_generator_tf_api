from flask import Flask

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = 5 # Segundos

from .views import routes_view
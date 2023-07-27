# __init__.py
import secrets
from flask import Flask

# Generate a secret key with 256 bits
secret_key = secrets.token_hex(32)
app = Flask(__name__)
app.secret_key = secret_key


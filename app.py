"""
Simple Flask API that uses psycopg2 (requires system libraries)
"""
from flask import Flask, jsonify
import psycopg2
import requests  # New dependency not in requirements.txt

app = Flask(__name__)

@app.route('/db/check')
def check_db():
    """Check if psycopg2 is available"""
    try:
        # Just check if we can import and get version
        version = psycopg2.__version__
        return jsonify({"status": "ok", "psycopg2_version": version})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)

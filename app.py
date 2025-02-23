from flask import Flask
import subprocess
import os
import datetime

app = Flask(__name__)

username = os.getenv("USER") or os.getenv("LOGNAME") or "codespace_user"

@app.route("/")
def home():
    return "Welcome! Visit <a href='/htop'>/htop</a> to see system stats."

@app.route("/htop")
def htop():
    full_name = "Sanket" 
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time}</h2>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """
    return response

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
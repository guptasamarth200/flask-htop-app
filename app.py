from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Samarth Gupta"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time() + 19800))  # IST
    
    # Running 'top' command to get system information
    try:
        top_output = subprocess.check_output("top -bn1 | head -20", shell=True).decode("utf-8")
    except:
        top_output = "Could not fetch system stats"

    return f'''
    <html>
        <body>
            <h1>System Info</h1>
            <p>Name: {name}</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Change to 8080

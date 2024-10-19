import os
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        name = "Deepanshu Dheer"
        username = os.environ.get('USER') or os.environ.get('LOGNAME') or "Unknown User"
        server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        top_output = "load average: 0.01, 0.06, 0.14\n0 users,\n32 sleeping,"
        return f"Name: {name}<br>Username: {username}<br>Server Time (IST): {server_time}<br>TOP output:<br>{top_output}"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

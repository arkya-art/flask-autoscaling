from flask import Flask, jsonify
import subprocess, threading

app = Flask(__name__)
TASK_SCRIPT = "high_cpu_task.py"

def run_high_cpu_task():
    subprocess.Popen(["python3", TASK_SCRIPT])

@app.route('/')
def home():
    return "Flask App Running! Start a high CPU task at /start_task"


@app.route('/start_task', methods=['GET','POST'])
def start_task():
    threading.Thread(target=run_high_cpu_task).start()
    return jsonify({"message": "High CPU Task STarted! "})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

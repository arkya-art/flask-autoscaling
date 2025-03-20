import psutil
import time, os

THRESHOLD = 75.0
ALERT_FILE = "cpu_alert.txt"

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    log_message = f"CPU: {cpu_usage}%, Memory: {mem_usage}%"
    print(log_message, flush=True)

    with open("monitor.log","a") as log:
        log.write(log_message+"\n")

    if cpu_usage > THRESHOLD:
        with open(ALERT_FILE, "w") as f:
            f.write("HIGH_CPU")

    time.sleep(25)

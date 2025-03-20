import subprocess, psutil
import os, time

REVERSE_THRESHOLD = 45

INSTANCE_NAME = "web-server-instance"
ZONE = "asia-east1-b"
TASK_SCRIPT = "high_cpu_task.py"

while True:

    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage < REVERSE_THRESHOLD:
        print("Migrating the back to local VM"):

        subprocess.run(["gcloud","compute","ssh",INSTANCE_NAME,"--zone",
                         ZONE, "--command", "pkill -f high_cpu_task.py" ])

        subprocess.Popen(["python3", TASK_SCRIPT]) 
        print("Reverse Migration Complete!")

    time.sleep(60)

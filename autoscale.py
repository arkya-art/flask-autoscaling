import subprocess
import time
import os

GCP_INSTANCE = "web-server-instance"
GCP_ZONE = "asia-east1-b"
ALERT_FILE = "cpu_alert.txt"
TASK_SCRIPT = "high_cpu_task.py"
LOG_FILE = "autoscale.log"

def log_message(message):
    """Helper function to write logs."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def migrate_task():
    """Migrate the high CPU task to GCP."""
    log_message("Migrating task to GCP...")

    try:
        subprocess.run(["gcloud", "compute", "scp", TASK_SCRIPT, 
                        f"{GCP_INSTANCE}:~", "--zone", GCP_ZONE], check=True)

        subprocess.run(["gcloud", "compute", "ssh", GCP_INSTANCE, 
                        "--zone", GCP_ZONE, 
                        "--command", f"nohup python3 {TASK_SCRIPT} > output.log 2>&1 &"], check=True)

        subprocess.run(["pkill", "-f", TASK_SCRIPT])  # Stop local task
        log_message("Migration complete.")

    except subprocess.CalledProcessError as e:
        log_message(f"Error during migration: {e}")

while True:
    if os.path.exists(ALERT_FILE):
        log_message("High CPU detected. Triggering migration.")
        migrate_task()
        os.remove(ALERT_FILE)
    time.sleep(10)









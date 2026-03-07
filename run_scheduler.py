import time
from scheduler.workflow_scheduler import start_scheduler

if __name__ == "__main__":
    topic = "Generative AI trends in enterprise"
    start_scheduler(topic=topic, hour=9, minute=0)

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
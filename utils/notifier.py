def send_dashboard_notification(topic, timestamp):
    print(f"[NOTIFICATION] Workflow completed for topic: {topic} at {timestamp}")

def send_email_notification(topic, result):
    print(f"[EMAIL STUB] Email notification for topic: {topic}")

def send_slack_notification(topic, result):
    print(f"[SLACK STUB] Slack notification for topic: {topic}")
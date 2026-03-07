from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent
from agents.insight_agent import InsightAgent
from database.db import save_session
from utils.notifier import (
    send_dashboard_notification,
    send_email_notification,
    send_slack_notification
)

research_agent = ResearchAgent()
summary_agent = SummaryAgent()
insight_agent = InsightAgent()

scheduler = BackgroundScheduler()

def run_workflow(topic: str):
    print(f"Running scheduled workflow for topic: {topic}")

    research_output = research_agent.run(topic)
    summary_output = summary_agent.run(research_output)
    insight_output = insight_agent.run(summary_output)

    save_session(topic, research_output, summary_output, insight_output)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_dashboard_notification(topic, timestamp)
    send_email_notification(topic, insight_output)
    send_slack_notification(topic, insight_output)

def start_scheduler(topic: str, hour: int = 9, minute: int = 0):
    scheduler.remove_all_jobs()
    scheduler.add_job(
        run_workflow,
        "cron",
        hour=hour,
        minute=minute,
        args=[topic],
        id="daily_workflow"
    )
    scheduler.start()
    print(f"Scheduler started for topic '{topic}' at {hour:02d}:{minute:02d} daily")
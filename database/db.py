from tinydb import TinyDB
from datetime import datetime

db = TinyDB("workflow_sessions.json")

def save_session(topic, research, summary, insight):
    session = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "topic": topic,
        "research": research,
        "summary": summary,
        "insight": insight
    }
    db.insert(session)

def get_all_sessions():
    return db.all()
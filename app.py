import streamlit as st
import pandas as pd
from datetime import datetime

from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent
from agents.insight_agent import InsightAgent
from database.db import save_session, get_all_sessions

st.set_page_config(page_title="Scheduled Multi-Agent Engine", layout="wide")

research_agent = ResearchAgent()
summary_agent = SummaryAgent()
insight_agent = InsightAgent()

st.title("Scheduled Multi-Agent Auto-Run")
st.subheader("Agent Workflow Engine")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Run Now", "View Sessions", "Workflow Info"]
)

if menu == "Run Now":
    st.header("Manual Workflow Run")

    topic = st.text_input("Enter topic", "Generative AI trends in enterprise")

if st.button("Run Workflow"):
    with st.spinner("Running Research Agent..."):
        research_output = research_agent.run(topic)

    if research_output.startswith("Error calling Ollama"):
        st.error("Research Agent failed. Ollama did not respond in time.")
        st.subheader("Research Output")
        st.write(research_output)
    else:
        with st.spinner("Running Summary Agent..."):
            summary_output = summary_agent.run(research_output)

        if summary_output.startswith("Error calling Ollama"):
            st.error("Summary Agent failed. Ollama did not respond in time.")
            st.subheader("Research Output")
            st.write(research_output)
            st.subheader("Summary Output")
            st.write(summary_output)
        else:
            with st.spinner("Running Insight Agent..."):
                insight_output = insight_agent.run(summary_output)

            if insight_output.startswith("Error calling Ollama"):
                st.error("Insight Agent failed. Ollama did not respond in time.")
                st.subheader("Research Output")
                st.write(research_output)
                st.subheader("Summary Output")
                st.write(summary_output)
                st.subheader("Insight Output")
                st.write(insight_output)
            else:
                save_session(topic, research_output, summary_output, insight_output)

                st.success("Workflow completed and saved.")

                st.subheader("Research Output")
                st.write(research_output)

                st.subheader("Summary Output")
                st.write(summary_output)

                st.subheader("Insight Output")
                st.write(insight_output)

elif menu == "View Sessions":
    st.header("Stored Workflow Sessions")

    sessions = get_all_sessions()

    if sessions:
        df = pd.DataFrame(sessions)
        st.dataframe(df[["timestamp", "topic"]], use_container_width=True)

        selected_index = st.number_input(
            "Select session index to view details",
            min_value=0,
            max_value=len(sessions)-1,
            step=1
        )

        selected_session = sessions[selected_index]

        st.subheader(f"Topic: {selected_session['topic']}")
        st.write(f"Timestamp: {selected_session['timestamp']}")

        st.markdown("### Research")
        st.write(selected_session["research"])

        st.markdown("### Summary")
        st.write(selected_session["summary"])

        st.markdown("### Insight")
        st.write(selected_session["insight"])
    else:
        st.info("No workflow sessions found yet.")

elif menu == "Workflow Info":
    st.header("Workflow Sequence")

    st.markdown("""
    **Daily Scheduled Workflow**
    
    1. Research Agent collects information  
    2. Summary Agent condenses research  
    3. Insight Agent generates actionable insights  
    4. Results are stored in TinyDB  
    5. Notifications can be sent via dashboard/email/Slack  
    """)

    st.markdown("### Example Schedule")
    st.code("Every day at 9:00 AM", language="text")
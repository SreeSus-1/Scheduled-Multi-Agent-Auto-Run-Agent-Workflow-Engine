from agents.base_agent import BaseAgent

class InsightAgent(BaseAgent):
    def run(self, summary_text: str) -> str:
        prompt = f"""
        You are an Insight Agent.
        Based on the summary below, generate useful insights, trends,
        risks, opportunities, and next actions.

        {summary_text}
        """
        return self.call_ollama(prompt)
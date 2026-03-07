from agents.base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def run(self, research_text: str) -> str:
        prompt = f"""
        You are a Summary Agent.
        Summarize the following research into short bullet points:

        {research_text}
        """
        return self.call_ollama(prompt)
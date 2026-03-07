from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def run(self, topic: str) -> str:
        prompt = f"""
        You are a Research Agent.
        Provide factual background, recent context, and important details about:
        {topic}

        Keep it structured and useful.
        """
        return self.call_ollama(prompt)
from claire_ai.utils.utils import get_llm
from langchain.messages import HumanMessage
from langchain.agents import create_agent

class ChatService:
    def __init__(self) -> None:
        self.llm = get_llm()

        self.system_prompt = """
        Você é um chatbot por CLI, está em um terminal, chamada Claire
        """

    def invoke_ai_response(self, query: str) -> str:
        if not self.llm:
            raise ValueError("LLM model not initialized")
        if query.strip() == "":
            raise ValueError("Query can't be empty")

        agent = create_agent(
            self.llm,
            system_prompt=self.system_prompt
        )

        result = agent.invoke(
            {"messages": [HumanMessage(query)]}
        )

        content = result["messages"][-1].content

        if isinstance(content, list):
            content = content[0].get("text", "")

        return content
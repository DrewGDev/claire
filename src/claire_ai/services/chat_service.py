
from langchain.chat_models import BaseChatModel
from langchain.messages import HumanMessage
from langchain.agents import create_agent

class ChatService:
    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm

        self.system_prompt = """
        You are a chatbot by CLI, in a terminal, named Claire
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
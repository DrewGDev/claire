from claire_ai.utils.utils import get_llm
from langchain.messages import HumanMessage, SystemMessage

class ChatService:
    def __init__(self) -> None:
        self.llm = get_llm()

    def invoke_ai_response(self, query: str) -> str:
        if not self.llm:
            raise ValueError("LLM model not initialized")
        if query.strip() == "":
            raise ValueError("Query can't be empty")
    
        # validar query

        messages = [
            SystemMessage("Você é um chatbot por CLI, terminal, chamada Claire. Responda agradavelmente."),
            HumanMessage(query)
        ]

        result = self.llm.invoke(messages)

        content = result.content

        if isinstance(content, list):
            content = content[0].get("text", "")

        return content
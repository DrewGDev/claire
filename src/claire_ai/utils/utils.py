import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()

API_KEY = SecretStr(os.getenv("API_KEY"))
PROVIDER_MODEL = os.getenv("PROVIDER_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")

def get_llm():
    return init_chat_model(model=LLM_MODEL, model_provider=PROVIDER_MODEL, api_key=API_KEY)
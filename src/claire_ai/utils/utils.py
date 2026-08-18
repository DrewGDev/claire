import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr

load_dotenv(find_dotenv())

API_KEY = SecretStr(os.getenv("API_KEY"))
PROVIDER_MODEL = os.getenv("PROVIDER_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")

def get_llm():
    if not API_KEY:
        raise ValueError("Api key value not founded")
    if not PROVIDER_MODEL:
        raise ValueError("Provider model not founded")
    if not LLM_MODEL:
        raise ValueError("Model for LLM not founded")
    
    return init_chat_model(model=LLM_MODEL, model_provider=PROVIDER_MODEL, api_key=API_KEY)
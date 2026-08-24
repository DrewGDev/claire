import importlib.util
import os
import shutil
import subprocess
import sys
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr

load_dotenv(find_dotenv(".env_claire"))

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

def is_dependency_installed(name: str):
    dependency_name = name.replace("-", "_")
    return importlib.util.find_spec(dependency_name)

def install_dependencies(name: str, is_to_uninstall: bool = False):
    is_uv_installed = shutil.which("uv") is not None
    
    if is_uv_installed:
        command = ["uv", "pip", "install", "--python", sys.executable, name] if not is_to_uninstall else ["uv", "pip", "uninstall", "--python", sys.executable, name]
    else:
        command = [sys.executable, "-m", "pip", "install", name] if not is_to_uninstall else [sys.executable, "-m", "pip", "uninstall", name]
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.returncode, result

def get_dependency_langchain_model():
    if not PROVIDER_MODEL:
        raise ValueError("Provider model can't be empty")
    
    INTEGRATIONS_MODELS = {
        "openai": "langchain-openai",
        "anthropic": "langchain-anthropic",
        "azure_openai": "langchain-openai",
        "azure_ai": "langchain-azure-ai",
        "google_vertexai": "langchain-google-vertexai",
        "google_genai": "langchain-google-genai",
        "anthropic_bedrock": "langchain-aws",
        "bedrock": "langchain-aws",
        "bedrock_converse": "langchain-aws",
        "cohere": "langchain-cohere",
        "fireworks": "langchain-fireworks",
        "together": "langchain-together",
        "mistralai": "langchain-mistralai",
        "huggingface": "langchain-huggingface",
        "groq": "langchain-groq",
        "ollama": "langchain-ollama",
        "google_anthropic_vertex": "langchain-google-vertexai",
        "deepseek": "langchain-deepseek",
        "ibm": "langchain-ibm",
        "nvidia": "langchain-nvidia",
        "xai": "langchain-xai",
        "openrouter": "langchain-openrouter",
        "perplexity": "langchain-perplexity",
        "upstage": "langchain-upstage",
        "baseten": "langchain-baseten",
        "litellm": "langchain-litellm",
        "meta": "langchain-meta",
        "langsmith": "langchain-openai"
    }

    dependency_name = INTEGRATIONS_MODELS.get(PROVIDER_MODEL)

    return dependency_name


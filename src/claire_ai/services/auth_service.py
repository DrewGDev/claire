import os
from dotenv import load_dotenv, set_key

load_dotenv()

class AuthService:
    def __init__(self) -> None:
        pass

    def configure_environment(self, api_key: str, provider_model: str, llm_model: str) -> bool:
        if not api_key or not provider_model or not llm_model:
            raise ValueError("configuração de variáveis de ambiente precisam de campos não nulos.")

        if not os.path.exists(".env"):
            with open(".env", "w") as f:
                f.write("")

        os.environ["API_KEY"] = api_key
        os.environ["PROVIDER_MODEL"] = provider_model
        os.environ["LLM_MODEL"] = llm_model

        set_key(".env", "API_KEY", api_key)
        set_key(".env", "PROVIDER_MODEL", provider_model)
        set_key(".env", "LLM_MODEL", llm_model)

        return True
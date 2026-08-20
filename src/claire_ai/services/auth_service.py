import os
from dotenv import load_dotenv, set_key

load_dotenv()

class AuthService:
    def __init__(self) -> None:
        self.dotenv_path: str = ".claire_env"

    def configure_environment(self, api_key: str, provider_model: str, llm_model: str) -> bool:
        if not api_key or not provider_model or not llm_model:
            raise ValueError("Environment variables need to be a non empty value.")

        if not os.path.exists(self.dotenv_path):
            with open(self.dotenv_path, "w") as f:
                f.write("")

        os.environ["API_KEY"] = api_key
        os.environ["PROVIDER_MODEL"] = provider_model
        os.environ["LLM_MODEL"] = llm_model

        set_key(self.dotenv_path, "API_KEY", api_key)
        set_key(self.dotenv_path, "PROVIDER_MODEL", provider_model)
        set_key(self.dotenv_path, "LLM_MODEL", llm_model)

        return True
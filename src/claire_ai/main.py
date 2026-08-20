import os
from typing import Annotated
import typer
from dotenv import load_dotenv, find_dotenv

from claire_ai.services.auth_service import AuthService

from claire_ai.types.chat import chat_app
from claire_ai.types.config import config_app

load_dotenv(find_dotenv())

app = typer.Typer()

app.add_typer(chat_app)
app.add_typer(config_app)

@app.callback(invoke_without_command=True)
def process_api(
    ctx: typer.Context,
    api_key: str | None = typer.Option(None, envvar="API_KEY", hidden=True)
):
    """
    Callback for processing environment variables.
    """
    if ctx.invoked_subcommand == "configure":
        return
    
    if not api_key and not os.getenv("API_KEY"):
        typer.echo("Not founded any API_KEY...")
        configure()

@app.command()
def configure(api_key: Annotated[str, typer.Option(prompt="Digite sua API Key", hide_input=True)] = "",
              provider_model: Annotated[str, typer.Option(prompt="Digite o provedor de llm")] = "",
              llm_model: Annotated[str, typer.Option(prompt="Digite o modelo da LLM")] = ""):
    """
    Principal command for Claire to works.
    """
    if api_key.strip() == "" and provider_model.strip() == "" and llm_model.strip() == "":
        api_key = typer.prompt("Input your API Key", hide_input=True)
        provider_model = typer.prompt("Input your model provider")
        llm_model = typer.prompt("Input your llm model")
    if api_key and provider_model and llm_model:
        typer.echo(f"Connecting the API with the key: {api_key[:4]}********")
        auth_service = AuthService()
        if auth_service.configure_environment(api_key, provider_model, llm_model):
            typer.echo(f"Successful configuration! API_KEY: {api_key[:4]}...")
            return
        typer.echo("Error during configuration", err=True)

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()
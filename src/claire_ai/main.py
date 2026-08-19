import os
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
    Callback para processar as variáveis de ambiente.
    """
    if ctx.invoked_subcommand == "configure":
        return
    
    if not api_key and not os.getenv("API_KEY"):
        typer.echo("Not founded any API_KEY...")
        configure()

@app.command()
def configure():
    """
    Comando principal que precisa de autenticação.
    """
    api_key = typer.prompt("Digite sua API Key", hide_input=True)
    provider_model = typer.prompt("Digite o provedor de llm")
    llm_model = typer.prompt("Digite o modelo da LLM")

    if api_key and provider_model and llm_model:
        typer.echo(f"Conectando à API com a chave: {api_key[:4]}********")
        auth_service = AuthService()
        if auth_service.configure_environment(api_key, provider_model, llm_model):
            typer.echo(f"Configuração sucedida! API_KEY: {api_key[:4]}...")
            return
        typer.echo("Configuração mal-sucedida", err=True)

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()
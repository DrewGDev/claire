from typing import Annotated
import typer
from rich import print as rich_print
from rich.progress import Progress, SpinnerColumn, TextColumn

from claire_ai.services.chat_service import ChatService

chat_app = typer.Typer()

@chat_app.command()
def chat(query: Annotated[str, typer.Option(prompt="Ask me anything")]):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Thinking...", total=None)
        chat_service = ChatService()

        ai_response = chat_service.invoke_ai_response(query)
    rich_print(ai_response)
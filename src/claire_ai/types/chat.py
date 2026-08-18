from typing import Annotated
import typer
from rich import print as rich_print
from rich.panel import Panel
from rich.markdown import Markdown
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

    md = Markdown(ai_response)

    response_with_panel = Panel(
        md,
        title="Claire",
        style="#73E6AD",
        border_style="#E68073"
    )
    rich_print(response_with_panel)
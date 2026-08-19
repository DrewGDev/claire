from typing import Annotated
import typer
from rich import print as rich_print
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

from claire_ai.utils.utils import get_llm
from claire_ai.services.chat_service import ChatService
from claire_ai.types.config import install_dependency

chat_app = typer.Typer()

@chat_app.command()
def chat(query: Annotated[str, typer.Option(prompt="Ask me anything")]):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        thinking_progress = progress.add_task(description="Thinking...", total=None)
        
        try:
            chat_service = ChatService(get_llm())
            ai_response = chat_service.invoke_ai_response(query)
        except ImportError:
            progress.remove_task(thinking_progress)
            progress.stop()

            if install_dependency(progress=progress, is_from_command=True):
                progress.start()
                progress.add_task("Thinking again...", total=None)

                chat_service = ChatService(get_llm())
                ai_response = chat_service.invoke_ai_response(query)
            
    md = Markdown(ai_response)

    response_with_panel = Panel(
        md,
        title="Claire",
        style="#73E6AD",
        border_style="#E68073"
    )
    rich_print(response_with_panel)
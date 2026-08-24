import importlib
from typing import Annotated
import typer
import click

from rich import print as rich_print
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

from claire_ai.utils.utils import get_llm
from claire_ai.services.chat_service import ChatService
from claire_ai.services.control_service import ControlService
from claire_ai.types.config import install_dependency

chat_app = typer.Typer()

@chat_app.command()
def chat(query: Annotated[str, typer.Option(prompt="Ask me anything")],
         copy: Annotated[bool, typer.Option(help="Permission to copy AI response automatically.")] = False):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        thinking_progress = progress.add_task(description="Thinking...", total=None)
        chat_service = ChatService()    

        try:         
            ai_response = chat_service.invoke_ai_response(get_llm(), query)
        except ImportError:
            progress.remove_task(thinking_progress)
            progress.stop()

            if install_dependency(progress=progress, is_from_command=True):
                importlib.invalidate_caches()
                progress.start()
                progress.add_task("Thinking again...", total=None)
                ai_response = chat_service.invoke_ai_response(get_llm(), query)

    md = Markdown(ai_response)

    response_with_panel = Panel(
        md,
        title="Claire",
        style="#73E6AD",
        border_style="#E68073"
    )
    rich_print(response_with_panel)

    control_service = ControlService()
    length, code_blocks = control_service.get_code_blocks(ai_response)

    copy_type: bool = False
    if not copy and length > 0:
        copy = typer.confirm("Founded code blocks in the response. Do you want to copy?", abort=True)
        copy_type = copy
    
    if not copy:
        return

    if length > 0 and not copy_type:
        copy_type = typer.confirm("Do you want to copy only code blocks? (if NOT, it will copy all Claire response)")

    if copy_type:
        if length == 1:
            control_service.copy_code_block_from_blocks(1, code_blocks)
            typer.echo("Code block copied for clipboard with success!")
        elif length > 1:
            code_block_table = control_service.get_table_code_blocks(code_blocks)
            while copy:
                print()
                rich_print(code_block_table)
                print()
                choiced_index = typer.prompt(
                    "Choice the index to copy",
                    type=click.IntRange(1, length)
                )
                control_service.copy_code_block_from_blocks(choiced_index, code_blocks)
                typer.echo("Code block copied for clipboard with success!")
                copy = typer.confirm("Do you want to copy more code blocks?", abort=True)
    else:
        control_service.copy_text(ai_response)
        typer.echo("Claire response copied for clipboard with success!")
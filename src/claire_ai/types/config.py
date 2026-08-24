from typing import Annotated
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from claire_ai.utils.utils import get_dependency_langchain_model, install_dependencies, is_dependency_installed

config_app = typer.Typer()

@config_app.command()
def install_dependency(dependency_name: str | None = None, progress = typer.Argument(None, hidden=True), is_from_command: Annotated[str, typer.Argument(hidden=True)] = False):
    if not dependency_name or dependency_name.strip() == "":
        dependency_name = get_dependency_langchain_model()

        typer.secho(f"The model dependency of 'langchain': `{dependency_name}` wasn't founded.", fg=typer.colors.YELLOW)

    if is_dependency_installed(dependency_name):
        typer.secho(f"Dependency {dependency_name} is already installed!")
        raise typer.Exit()

    typer.secho("Dependency verified and not installed!")
    confirm_install = typer.confirm(f"Do you want to install the `{dependency_name}` dependency?")
    if not confirm_install:
        raise typer.Exit()

    if not progress:
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        )
            
    progress.start()

    installing_progress = progress.add_task(description="Installing Dependency...", total=None)
    status_code, result = install_dependencies(dependency_name)
    progress.remove_task(installing_progress)
    progress.stop()

    if status_code == 0:
        typer.secho(f"`{dependency_name}` installed successfully!", fg=typer.colors.GREEN)
    else:
        typer.secho(f"Error during installing `{dependency_name}`", fg=typer.colors.RED)
        typer.echo(result.stderr)
        raise typer.Exit(1)

    if is_from_command:
        return True

@config_app.command()
def uninstall_dependency(dependency_name: str):
    if dependency_name.strip() != "":
        if not is_dependency_installed(dependency_name):
            typer.secho(f"Dependency {dependency_name} not founded!")
            raise typer.Exit()

        typer.secho("Dependency founded!")
        confirm_uninstall = typer.confirm(f"Do you want to uninstall the `{dependency_name}` dependency?")

        if not confirm_uninstall:
            typer.Exit()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            progress.add_task("Uninstalling...", total=None)

            status_code, result = install_dependencies(dependency_name, is_to_uninstall=True)
        print(result)
        if status_code == 0:
            typer.secho(f"`{dependency_name}` uninstalled successfully!", fg=typer.colors.GREEN)
        else:
            typer.secho(f"Error during uninstalling `{dependency_name}`", fg=typer.colors.RED)
            typer.echo(result.stderr)
            raise typer.Exit(1)
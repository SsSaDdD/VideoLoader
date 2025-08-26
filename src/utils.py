from rich.console import Console

console = Console()

def log_info(msg): console.print(f"[blue]{msg}[/blue]")
def log_success(msg): console.print(f"[green]{msg}[/green]")
def log_error(msg): console.print(f"[red]{msg}[/red]")

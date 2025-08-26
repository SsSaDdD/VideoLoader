from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from .downloader import download_video
from .utils import log_info, log_success, log_error

console = Console()


def main():
    console.print("[bold cyan]Добро пожаловать в YTFetch[/bold cyan]\n")

    format_choice = Prompt.ask("Выберите формат", choices=["video", "audio"], default="video")

    quality = None
    if format_choice == "video":
        quality = IntPrompt.ask("Введите желаемое качество видео (например, 1080)", default=720)

    url = Prompt.ask("Введите ссылку на видео/плейлист")

    console.print("\n[bold green]Начинаем загрузку...[/bold green]\n")

    try:
        download_video(url, audio=(format_choice == "audio"), quality=quality)
        log_success("Загрузка завершена!")
    except Exception as e:
        log_error(f"Произошла ошибка: {e}")

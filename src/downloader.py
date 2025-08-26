import yt_dlp
from .config import ensure_download_dir
from .utils import log_info, log_success

def download_video(url, audio=False, quality=None):
    path = ensure_download_dir()
    ydl_opts = {
        'outtmpl': str(path / '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook]
    }

    if audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    else:
        if quality:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '')
        print(f"\rЗагрузка: {percent} | {speed} | Осталось: {eta}", end='')
    elif d['status'] == 'finished':
        log_success("Загрузка завершена!")

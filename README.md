# YTFetch — Консольная утилита для скачивания видео и аудио с YouTube

Красивый консольный интерфейс для скачивания видео и аудио с YouTube. Пользователь выбирает формат, качество и вводит ссылку прямо в терминале.

---

## Установка

1. **Клонируем репозиторий**:

```bash
git clone https://github.com/SsSaDdD/VideoLoader.git
cd VideoLoader
```

2. **Создаём и активируем виртуальное окружение**:

```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows
```

3. **Устанавливаем зависимости**:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Устанавливаем пакет (чтобы была команда ytfetch)**:

```bash
pip install -e .
```

---

## Использование

Запускаем программу через консоль:

```bash
ytfetch
```

Программа последовательно спрашивает:

1. Формат скачивания:

   * `video` — видео
   * `audio` — только аудио (MP3)

2. Качество видео (если выбран `video`, например 720 или 1080)

3. Ссылку на видео или плейлист

Пример работы:

```
Добро пожаловать в YTFetch

Выберите формат [video/audio]: video
Введите желаемое качество видео (например, 1080): 1080
Введите ссылку на видео/плейлист: https://www.youtube.com/watch?v=abcd1234

Начинаем загрузку...
Загрузка: 35% | 1.2MiB/s | Осталось: 00:01:20
...
Загрузка завершена!
```

---

## Структура проекта

```
VideoLoader/
├── ytfetch/
│   ├── __init__.py
│   ├── cli.py          # Консольный интерфейс
│   ├── downloader.py   # Функция download_video
│   ├── config.py       # ensure_download_dir()
│   └── utils.py        # log_info(), log_success(), log_error()
├── .gitignore   
├── main.py             # Точка входа
├── requirements.txt    # yt-dlp, rich
├── setup.py            # Настройка пакета
└── README.md
```

---

## Требования

* Python 3.10+
* yt-dlp
* rich

---

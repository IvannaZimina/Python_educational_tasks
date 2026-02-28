# Python Educational Tasks

Небольшой учебный проект: независимые скрипты с заданиями в каталоге `src/`.

## Быстрый старт

1. Открой папку проекта в VS Code (**File → Open Folder**).
2. (Опционально) создай виртуальное окружение:
   ```bash
   python -m venv venv
   # Git Bash
   source venv/Scripts/activate
   # PowerShell
   # .\venv\Scripts\Activate.ps1
   ```
3. (Опционально) установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запускай любой файл из `src/`:
   ```bash
   python src/task01_hello.py
   ```
5. Или используй **Run and Debug** в VS Code — профиль «▶ Текущий файл (Python)».

## Структура
```
Python_educational_tasks/
├─ src/                # здесь твои задания .py
├─ .vscode/            # настройки и профили запуска VS Code
│  ├─ settings.json    # выбор интерпретатора и базовые опции
│  └─ launch.json      # сценарии запуска (текущий файл / конкретные задачи)
├─ .gitignore
├─ README.md
└─ requirements.txt    # (по желанию)
```

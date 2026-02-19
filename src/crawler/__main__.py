"""
Входной скрипт пакета при запуске через python -m crawler.
Перенаправляет выполнение в функцию main модуля cli.
"""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())

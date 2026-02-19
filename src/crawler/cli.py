import argparse
import sys
from pathlib import Path

from .run import run as run_crawler

def _cmd_run(args: argparse.Namespace) -> int:
    """Обработчик подкоманды run: отвечает за запуск процесса краулинга"""
    return run_crawler(
        input_path=Path(args.input),
        out_dir=Path(args.out),
        index_path=Path(args.index),
        limit=args.limit,
    )

def _cmd_validate(_args: argparse.Namespace) -> int:
    """Обработчик подкоманды validate: выполняет проверку данных и конфигурации (пока без реальной логики)."""
    print("Not implemented")
    return 0


def _cmd_package(_args: argparse.Namespace) -> int:
    """Обработчик подкоманды package: формирует итоговый артефакт по результатам краулинга (пока заглушка)."""
    print("Not implemented")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    """Создаёт парсер аргументов и регистрирует подкоманды run, validate и package."""
    parser = argparse.ArgumentParser(
        prog="crawler",
        description="CLI для краулера.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="доступные команды")

    run_parser = subparsers.add_parser("run", help="запустить основной процесс краулинга")
    run_parser.add_argument(
        "--input",
        default="urls.txt",
        help="путь к текстовому файлу со списком URL (по одному адресу на строку, по умолчанию: urls.txt)",
    )
    run_parser.add_argument(
        "--out",
        default="out",
        help="каталог для сохранения HTML-страниц (0001.html и далее, по умолчанию: ./out)",
    )
    run_parser.add_argument(
        "--index",
        default="index.tsv",
        help="файл индексной таблицы формата filename<TAB>url (по умолчанию: index.tsv)",
    )
    run_parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="целевое количество успешных скачиваний (по умолчанию: 100)",
    )
    subparsers.add_parser("validate", help="проверить конфигурацию/данные")
    subparsers.add_parser("package", help="упаковать результат")

    return parser


def main() -> int:
    """
    Основная точка входа CLI: разбирает аргументы командной строки,
    выбирает соответствующий обработчик подкоманды и возвращает его код завершения.
    """
    parser = _build_parser()
    args = parser.parse_args()

    handlers = {
        "run": _cmd_run,
        "validate": _cmd_validate,
        "package": _cmd_package,
    }
    handler = handlers[args.command]
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
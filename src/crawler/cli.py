import argparse
import sys
from pathlib import Path

from .run import run as run_crawler
from .validate import validate as validate_crawler


def _cmd_run(args: argparse.Namespace) -> int:
    """Обработчик подкоманды run: отвечает за запуск процесса краулинга"""
    return run_crawler(
        input_path=Path(args.input),
        out_dir=Path(args.out),
        index_path=Path(args.index),
        limit=args.limit,
    )

def _cmd_validate(args: argparse.Namespace) -> int:
    """Обработчик подкоманды validate: выполняет проверку индекса и каталога страниц"""
    return validate_crawler(
        pages_dir=Path(args.pages),
        index_path=Path(args.index),
        min_pages=args.min_pages,
    )


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
        default="data/urls.txt",
        help="путь к текстовому файлу со списком URL (по одному адресу на строку, по умолчанию: data/urls.txt)",
    )
    run_parser.add_argument(
        "--out",
        default="output/pages",
        help="каталог для сохранения HTML-страниц (0001.html и далее, по умолчанию: output/pages)",
    )
    run_parser.add_argument(
        "--index",
        default="output/index.txt",
        help="файл индексной таблицы формата filename<TAB>url (по умолчанию: output/index.txt)",
    )
    run_parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="целевое количество успешных скачиваний (по умолчанию: 100)",
    )
    validate_parser = subparsers.add_parser(
        "validate",
        help="проверить согласованность индексного файла и каталога страниц",
    )
    validate_parser.add_argument(
        "--pages",
        default="out",
        help="каталог, в котором лежат сохранённые HTML-страницы (по умолчанию: ./out)",
    )
    validate_parser.add_argument(
        "--index",
        default="index.tsv",
        help="индексный файл формата filename<TAB>url (по умолчанию: index.tsv)",
    )
    validate_parser.add_argument(
        "--min-pages",
        type=int,
        default=100,
        help="ожидаемое минимальное количество файлов в каталоге страниц (по умолчанию: 100)",
    )
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
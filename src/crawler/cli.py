import argparse
import sys


def _cmd_run(_args: argparse.Namespace) -> int:
    """Обработчик подкоманды run: отвечает за запуск процесса краулинга (реализация ещё не добавлена)."""
    print("Not implemented")
    return 0


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

    subparsers.add_parser("run", help="запустить краулер")
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
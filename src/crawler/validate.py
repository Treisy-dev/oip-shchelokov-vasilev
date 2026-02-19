import sys
from pathlib import Path


def validate(pages_dir: Path, index_path: Path, min_pages: int) -> int:
    """
    Выполняет проверку индексного файла и каталога со страницами.

    - index_path должен указывать на существующий обычный файл.
    - В pages_dir должно находиться не меньше min_pages файлов-страниц.
    - Каждая непустая строка в индексе имеет вид filename<TAB>url, при этом такой filename
      обязан присутствовать среди файлов в pages_dir.

    При обнаружении первой проблемы функция печатает сообщение об ошибке в stderr и немедленно
    завершает работу с кодом 1.
    Returns:
        0 — если все проверки прошли успешно, 1 — при любой ошибке валидации.
    """
    # Проверяем наличие индексного файла и то, что это действительно файл
    if not index_path.exists():
        print(f"validate: index file not found: {index_path}", file=sys.stderr)
        return 1
    if not index_path.is_file():
        print(f"validate: index path is not a file: {index_path}", file=sys.stderr)
        return 1

    # Проверяем каталог со страницами и минимальное количество файлов
    if not pages_dir.exists():
        print(f"validate: pages directory not found: {pages_dir}", file=sys.stderr)
        return 1
    if not pages_dir.is_dir():
        print(f"validate: pages path is not a directory: {pages_dir}", file=sys.stderr)
        return 1

    page_files = [f for f in pages_dir.iterdir() if f.is_file()]
    if len(page_files) < min_pages:
        print(
            f"validate: not enough pages: {len(page_files)} in {pages_dir}, required >= {min_pages}",
            file=sys.stderr,
        )
        return 1

    # Проверяем формат строк в индексе и наличие соответствующих файлов в каталоге страниц
    lines = index_path.read_text(encoding="utf-8").splitlines()
    for line_no, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        if "\t" not in line:
            print(
                f"validate: index line {line_no}: expected 'filename<TAB>url', got no TAB",
                file=sys.stderr,
            )
            return 1
        parts = line.split("\t", 1)
        if len(parts) != 2:
            print(
                f"validate: index line {line_no}: expected exactly one TAB",
                file=sys.stderr,
            )
            return 1
        filename, _url = parts
        if not filename.strip():
            print(
                f"validate: index line {line_no}: empty filename",
                file=sys.stderr,
            )
            return 1
        file_path = pages_dir / filename
        if not file_path.exists() or not file_path.is_file():
            print(
                f"validate: index line {line_no}: file not found in pages: {filename}",
                file=sys.stderr,
            )
            return 1

    return 0

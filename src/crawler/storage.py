from pathlib import Path


def make_filename(n: int) -> str:
    """
    Генерирует имя файла для сохранения страницы на основе её порядкового номера.

    Args:
        n: Порядковый номер страницы (1, 2, …).

    Returns:
        Строку формата "0001.html", "0002.html" и т.д. (4 цифры с ведущими нулями).
    """
    return f"{n:04d}.html"


def save_page(out_dir: Path, n: int, html: str) -> Path:
    """
    Записывает переданный HTML в файл внутри указанного каталога.

    Имя файла определяется функцией make_filename(n). При отсутствии каталога он будет создан.
    Данные сохраняются в кодировке UTF-8.

    Args:
        out_dir: Директория, куда нужно поместить файл.
        n: Номер страницы, используемый при формировании имени файла.
        html: HTML-содержимое, которое требуется сохранить.

    Returns:
        Объект Path, указывающий на созданный файл.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / make_filename(n)
    path.write_text(html, encoding="utf-8")
    return path


def append_index(index_path: Path, n: int, url: str) -> None:
    """
    Дописывает запись о сохранённой странице в индексный файл.

    Каждая строка имеет вид "0001.html<TAB>url" и хранится в кодировке UTF-8.
    Если каталог для index_path ещё не существует, он будет создан.

    Args:
        index_path: Путь к индексному файлу.
        n: Номер страницы.
        url: URL страницы.
    """
    index_path.parent.mkdir(parents=True, exist_ok=True)
    line = f"{make_filename(n)}\t{url}\n"
    with index_path.open("a", encoding="utf-8") as f:
        f.write(line)

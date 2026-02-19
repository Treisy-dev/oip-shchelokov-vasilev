import logging
from pathlib import Path

from .download import download_html
from .storage import append_index, save_page

DEFAULT_TIMEOUT = 20.0
DEFAULT_RETRIES = 5


def _read_urls(input_path: Path) -> list[str]:
    """Считывает список URL из текстового файла, игнорируя пустые строки."""
    text = input_path.read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]


def run(
    input_path: Path,
    out_dir: Path,
    index_path: Path,
    limit: int,
    timeout: float = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> int:
    """
    Организует основной цикл краулера: читает адреса из input_path, по одному скачивает
    не более limit страниц, сохраняет их в out_dir и добавляет записи в index_path.

    При неудачной загрузке конкретного URL пишет предупреждение в лог и продолжает дальше.
    Если по итогам работы оказалось меньше успешных скачиваний, чем указано в limit (из-за
    нехватки URL или ошибок запросов), функция возвращает ненулевой код завершения.

    Returns:
        0, если удалось успешно сохранить limit страниц, иначе 1.
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)
    urls = _read_urls(input_path)

    # Перед новым запуском очищаем содержимое индексного файла
    if index_path.exists():
        index_path.write_text("", encoding="utf-8")

    success_count = 0
    next_n = 1

    for url in urls:
        if success_count >= limit:
            break
        try:
            html = download_html(url, timeout=timeout, retries=retries)
            save_page(out_dir, next_n, html)
            append_index(index_path, next_n, url)
            success_count += 1
            next_n += 1
        except Exception as e:
            logger.warning("Skip URL %s: %s", url, e)
            continue

    if success_count < limit:
        logger.error(
            "Not enough URLs: got %d successful downloads, need %d (URLs exhausted).",
            success_count,
            limit,
        )
        return 1
    return 0

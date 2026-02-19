from typing import Optional

import requests
from requests.exceptions import HTTPError, RequestException


DEFAULT_HEADERS = {
    "User-Agent": "oip-crawler/1.0 (+https://example.com/contact)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}


def download_html(url: str, timeout: float, retries: int) -> str:
    """
    Выполняет HTTP-запрос по указанному адресу и возвращает содержимое страницы в виде HTML-строки.
    Args:
        url: Адрес страницы, которую нужно получить.
        timeout: Максимальное время ожидания ответа в секундах.
        retries: Количество дополнительных попыток при сбоях сети или временных ошибках.

    Returns:
        Строка с телом HTTP-ответа (response.text).

    Raises:
        Exception: Если ни одна из попыток запроса не завершилась успешно.
    """
    last_error: Optional[Exception] = None
    attempts = retries + 1

    for attempt in range(attempts):
        try:
            response = requests.get(url, timeout=timeout, headers=DEFAULT_HEADERS)
            if response.status_code >= 500:
                last_error = Exception(
                    f"HTTP {response.status_code} at {url} (attempt {attempt + 1}/{attempts})"
                )
                continue
            response.raise_for_status()
            return response.text
        except RequestException as e:
            if isinstance(e, HTTPError) and e.response is not None and e.response.status_code < 500:
                raise
            last_error = e
            continue

    msg = f"Failed to download {url} after {attempts} attempt(s)"
    if last_error is not None:
        msg += f": {last_error}"
    raise Exception(msg)

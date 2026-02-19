**ФИО:** Щёлоков Кирилл Алексеевич и Васильев Давид Михайлович

**Группа:** 11-209

## Описание

Проект скачивает HTML-страницы по списку URL: до 100 страниц, сохраняет с разметкой, в файлы `0001.html`, `0002.html`, … в кодировке UTF-8. Формирует файл `index.txt` в формате «номер_файла TAB url».

## Result Preview

Пример содержимого `index.txt`:

```
0001.html	https://ru.wikipedia.org/wiki/Россия
0002.html	https://ru.wikipedia.org/wiki/Москва
0003.html	https://ru.wikipedia.org/wiki/Санкт-Петербург
0004.html	https://ru.wikipedia.org/wiki/Казань
0005.html	https://example.com/page
```

## Project Structure

| Папка / файл | Назначение |
|--------------|------------|
| `src/crawler/` | Исходный код краулера |
| `data/` | Входные данные (список URL) |
| `requirements.txt` | Зависимости Python |
| `output` | Результат выполнения |

Подробная установка и запуск — в [DEPLOYMENT.md](DEPLOYMENT.md).

# Руководство по развёртыванию

## Требования

- **Python 3.10+** (актуальная версия ветки 3.x)
- Доступ в интернет для скачивания страниц и установки зависимостей

## Установка

1. Перейти в каталог проекта:
   ```bash
   cd /путь/к/oip-shchelokov-vasilev
   ```

2. Создать виртуальное окружение:
   ```bash
   python -m venv .venv
   ```

3. Активировать его:
   - macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   - Windows:
   ```bash
   .venv\Scripts\activate
   ```

4. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

Пакет лежит в `src/`, поэтому для запуска модуля из корня проекта нужен **PYTHONPATH=src**.

## Запуск скачивания

Из корня проекта.

### Вариант 1: короткая команда (с дефолтами CLI)

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler run
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler run
```

По умолчанию:
- входной файл с URL — `data/urls.txt` (одна ссылка на строку);
- страницы сохраняются в каталог `output/pages`;
- индекс пишется в файл `output/index.txt`;
- лимит успешных скачиваний — `100`;
- включён подробный вывод процесса скачивания (можно отключить, если изменить вызов в коде).

### Вариант 2: полная форма с явными параметрами

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler run --input data/urls.txt --out output/pages --index output/index.txt --limit 100 --verbose
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler run --input data/urls.txt --out output/pages --index output/index.txt --limit 100 --verbose
```

## Проверка результата

### Вариант 1: короткая команда (с дефолтами CLI)

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler validate
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler validate
```

По умолчанию:
- каталог со страницами — `output/pages`;
- индексный файл — `output/index.txt`;
- ожидаемое минимальное количество страниц — `100`.

### Вариант 2: полная форма с явными параметрами

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler validate --pages output/pages --index output/index.txt --min-pages 100
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler validate --pages output/pages --index output/index.txt --min-pages 100
```

## Где хранится результат

После успешного `run` (с настройками по умолчанию):

- **HTML-файлы:** `output/pages/` — файлы `0001.html`, `0002.html`, …
- **Индекс:** `output/index.txt` — строки вида `filename<TAB>url`, в кодировке UTF-8.

Каталог `output/` создаётся автоматически при первом запуске.

## Сборка архива

### Вариант 1: короткая команда (с дефолтами CLI)

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler package
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler package
```

По умолчанию:
- берутся страницы из каталога `output/pages`;
- используется индексный файл `output/index.txt`;
- создаётся архив `output/submission.zip`.

### Вариант 2: полная форма с явными параметрами

**macOS/Linux:**
```bash
PYTHONPATH=src python -m crawler package --pages output/pages --index output/index.txt --out output/submission.zip
```

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python -m crawler package --pages output/pages --index output/index.txt --out output/submission.zip
```

Архив `output/submission.zip` будет содержать каталог `pages/` с HTML и файл `index.txt` в корне архива.

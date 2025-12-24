# Office Tweaks - CLI

### Подготовка виртуального окружения
```bash
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
venv\Scripts\activate

# Деактивация (когда закончите работу)
deactivate
```

### Установка зависимостей

После активации виртуального окружения установите необходимые зависимости:

```bash
# Установка пакетов из requirements.txt
pip install -r requirements.txt
```

## Использование

### Интерактивный режим

Интерактивный режим предоставляет удобное меню для выбора операций:

```bash
# Запуск интерактивного режима
python office_tweaks.py

# Или с явным указанием флага
python office_tweaks.py -i
```

В интерактивном режиме вы увидите меню:
```
=== Office Tweaks v1.0 ===
Рабочий каталог: C:\Users\Илья\Projects\PyCharm\Office_Tweaks
Выберите действие:
                        0. Сменить рабочий каталог
                        1. Преобразовать PDF в Docx
                        2. Преобразовать Docx в PDF
                        3. Произвести сжатие изображений
                        4. Удалить группу файлов
                        5. Выход
                        - 
```

### Пакетный режим

## Поддерживаемые аргументы CLI

```bash
# Показать справку
python office_tweaks.py --help
```

### Конвертация PDF в DOCX

```bash
# Конвертация одного файла
python office_tweaks.py --pdf2docx "C:\path\to\file.pdf"

# Конвертация всех файлов в папке
python office_tweaks.py --pdf2docx all --workdir "C:\path\to\folder"
```

### Конвертация DOCX в PDF

```bash
# Конвертация одного файла
python office_tweaks.py --docx2pdf "C:\path\to\file.docx"

# Конвертация всех файлов в папке
python office_tweaks.py --docx2pdf all --workdir "C:\path\to\folder"
```

### Сжатие изображений

```bash
# Сжатие одного изображения с указанием качества
python office_tweaks.py --compress-images "C:\image.ext" --quality 60

# Сжатие всех изображений в папке
python office_tweaks.py --compress-images all --workdir "C:\Pictures" --quality 85
```

### Удаление файлов

```bash
# Удаление по расширению
python office_tweaks.py --delete --delete-mode extension --delete-pattern ext --delete-dir "C:\path\to\folder"

# Удаление по подстроке в начале имени
python office_tweaks.py --delete --delete-mode startswith --delete-pattern "smth_" --workdir "C:\path\to\folder"



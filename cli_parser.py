import argparse
import os

from file_manager import list_dir
from converter import convert_pdf_to_docx, convert_docx_to_pdf
from image_processor import compress_image


def validate_quality(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Недопустимое значение качества: '{value}'")

    if not 1 <= value <= 100:
        raise argparse.ArgumentTypeError(f"Качество должно быть в диапазоне 1-100, получено: {value}")
    return value


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Office",
        epilog="""
Примеры использования:
  Конвертация PDF в DOCX:
    python office_tweaks.py --pdf2docx "C:\\path\\to\\file.pdf"
    python office_tweaks.py --pdf2docx all --workdir "C:\\path\\to\\folder"

  Конвертация DOCX в PDF:
    python office_tweaks.py --docx2pdf "C:\\path\\to\\file.docx"
    python office_tweaks.py --docx2pdf all --workdir "C:\\path\\to\\folder"

  Сжатие изображений:
    python office_tweaks.py --compress-images "C:\\image.ext" --quality 60
    python office_tweaks.py --compress-images all --workdir "C:\\Pictures" --quality 85

  Удаление файлов:
    python office_tweaks.py --delete --delete-mode extension --delete-pattern ext --delete-dir "C:\\path\\to\\folder"
    python office_tweaks.py --delete --delete-mode startswith --delete-pattern "smth_" --delete-dir "C:\\path\\to\\folder"

  Интерактивный режим:
    python office_tweaks.py -i
    python office_tweaks.py
        """
    )

    operation_group = parser.add_mutually_exclusive_group()

    operation_group.add_argument(
        '--pdf2docx',
        metavar='FILE_OR_ALL',
        help='Конвертировать PDF в DOCX. Укажите путь к файлу или "all" для всех файлов в директории'
    )

    operation_group.add_argument(
        '--docx2pdf',
        metavar='FILE_OR_ALL',
        help='Конвертировать DOCX в PDF. Укажите путь к файлу или "all" для всех файлов в директории'
    )

    operation_group.add_argument(
        '--compress-images',
        metavar='FILE_OR_ALL',
        help='Сжать изображения. Укажите путь к файлу или "all" для всех изображений в директории'
    )

    operation_group.add_argument(
        '--delete',
        action='store_true',
        help='Режим удаления файлов'
    )

    parser.add_argument(
        '--workdir',
        metavar='DIRECTORY',
        help='Рабочая директория (используется с "all" для операций)'
    )

    parser.add_argument(
        '--quality',
        type=validate_quality,
        default=85,
        help='Качество сжатия изображений (1-100, по умолчанию: 85)'
    )

    parser.add_argument(
        '--delete-mode',
        choices=['extension', 'startswith'],
        help='Режим удаления файлов (extension, startswith)'
    )

    parser.add_argument(
        '--delete-pattern',
        metavar='PATTERN',
        help='Шаблон для удаления файлов'
    )

    parser.add_argument(
        '--delete-dir',
        metavar='DIRECTORY',
        help='Директория для удаления файлов'
    )

    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Запуск в интерактивном режиме'
    )

    return parser.parse_args()


def validate_arguments(args):
    if args.pdf2docx:
        if args.pdf2docx.lower() == 'all':
            if not args.workdir:
                raise ValueError("Для режима 'all' необходимо указать --workdir")
            if not os.path.exists(args.workdir):
                raise FileNotFoundError(f"Директория не найдена: {args.workdir}")
        else:
            if not os.path.exists(args.pdf2docx):
                raise FileNotFoundError(f"Файл не найден: {args.pdf2docx}")

    elif args.docx2pdf:
        if args.docx2pdf.lower() == 'all':
            if not args.workdir:
                raise ValueError("Для режима 'all' необходимо указать --workdir")
            if not os.path.exists(args.workdir):
                raise FileNotFoundError(f"Директория не найдена: {args.workdir}")
        else:
            if not os.path.exists(args.docx2pdf):
                raise FileNotFoundError(f"Файл не найден: {args.docx2pdf}")

    elif args.compress_images:
        if args.compress_images.lower() == 'all':
            if not args.workdir:
                raise ValueError("Для режима 'all' необходимо указать --workdir")
            if not os.path.exists(args.workdir):
                raise FileNotFoundError(f"Директория не найдена: {args.workdir}")
        else:
            if not os.path.exists(args.compress_images):
                raise FileNotFoundError(f"Файл не найден: {args.compress_images}")

    elif args.delete:
        if not args.delete_mode:
            raise ValueError("Для удаления необходимо указать --delete-mode")
        if not args.delete_pattern:
            raise ValueError("Для удаления необходимо указать --delete-pattern")
        if not args.delete_dir:
            raise ValueError("Для удаления необходимо указать --delete-dir")

        if not os.path.exists(args.delete_dir):
            raise FileNotFoundError(f"Директория не найдена: {args.delete_dir}")

    return True


def run_operation(args):
    if args.pdf2docx:
        print(f"Конвертация PDF в DOCX: {args.pdf2docx}")
        files = list_dir(path=os.getcwd() ,filter=[".pdf"], flg=False)
        if args.pdf2docx.lower() == 'all':
            print(f"Директория: {args.workdir}")
            for file in files:
                convert_pdf_to_docx(file)
        else:
            print(f"Файл: {args.pdf2docx}")
            convert_pdf_to_docx(args.pdf2docx)

    elif args.docx2pdf:
        print(f"Конвертация DOCX в PDF: {args.docx2pdf}")
        files = list_dir(path=os.getcwd(), filter=[".docx"], flg=False)
        if args.docx2pdf.lower() == 'all':
            print(f"Директория: {args.workdir}")
            for file in files:
                convert_docx_to_pdf(file)
        else:
            print(f"Файл: {args.docx2pdf}")
            convert_docx_to_pdf(args.docx2pdf)

    elif args.compress_images:
        print(f"Сжатие изображений: {args.compress_images}")
        print(f"Качество: {args.quality}")
        imgs = list_dir(path=os.getcwd(), filter=[".jpg", ".jpeg", ".png", ".gif"], flg=False)
        if args.compress_images.lower() == 'all':
            print(f"Директория: {args.workdir}")
            for img in imgs:
                compress_image(img)
        else:
            print(f"Файл: {args.compress_images}")
            compress_image(args.compress_images)

    else:
        print(f"Удаление файлов:")
        print(f"Режим: {args.delete_mode}")
        print(f"Шаблон: {args.delete_pattern}")
        print(f"Директория: {args.delete_dir}")

        if args.delete_mode == "extension":
            files = [file for file in os.listdir(args.delete_dir) if os.path.splitext(file)[1] == args.delete_pattern]

            for file in files:
                os.remove(os.path.join(args.delete_dir, file))

        else:
            files = [file for file in os.listdir(args.delete_dir) if file.startswith(args.delete_pattern)]

            for file in files:
                os.remove(os.path.join(args.delete_dir, file))

def parce():
    try:
        args = parse_arguments()

        validate_arguments(args)
        run_operation(args)

    except argparse.ArgumentError as e:
        print(f"Ошибка аргументов: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


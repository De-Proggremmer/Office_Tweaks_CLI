import os

from file_manager import list_dir
from converter import convert_pdf_to_docx, convert_docx_to_pdf
from image_processor import compress_image
from file_remover import process_remove

def menu():

    print("\033[97m" + "=== Office Tweaks v1.0 ===")
    while True:
        print(f"Рабочий каталог: {os.getcwd()}")
        choise = input("""Выберите действие:
                        0. Сменить рабочий каталог
                        1. Преобразовать PDF в Docx
                        2. Преобразовать Docx в PDF
                        3. Произвести сжатие изображений
                        4. Удалить группу файлов
                        5. Выход
                        - """)
        while (not choise.isdigit()) or (int(choise) not in range(0, 6)):
            choise = input("Некорректное значение, повторите попытку: ")

        match choise:
            case "0":
                path = input("Укажите путь к каталогу: ")
                while not os.path.exists(path):
                    path = input("Директории не существует, введите заново: ")

                os.chdir(path)

            case "1":
                files = list_dir(path=os.getcwd() ,filter=[".pdf"])

                choise_1 =  input("Выберите файл: ")
                while (not choise_1.isdigit()) or (int(choise_1) not in range(len(files)+1)):
                    choise_1 = input("Неверное значение, введите заново: ")

                if choise_1 == "0":
                    for file in files:
                        convert_pdf_to_docx(file)
                else:
                    convert_pdf_to_docx(files[int(choise_1)])

            case "2":
                files = list_dir(path=os.getcwd(), filter=[".docx"])

                choise_2 = input("Выберите файл: ")
                while (not choise_2.isdigit()) or (int(choise_2) not in range(len(files) + 1)):
                    choise_2 = input("Неверное значение, введите заново: ")

                if choise_2 == "0":
                    for file in files:
                        convert_docx_to_pdf(file)
                else:
                    convert_docx_to_pdf(files[int(choise_2)])

            case "3":
                imgs = list_dir(path=os.getcwd(), filter=[".jpg", ".jpeg", ".png", ".gif"])

                choise_3_img = input("Выберите изображение: ")
                while (not choise_3_img.isdigit()) or (int(choise_3_img) not in range(len(imgs) + 1)):
                    choise_3_img = input("Неверное значение, введите заново: ")

                choise_3_qual = input("Выберите степень сжатия(1-100: ")
                while (not choise_3_qual.isdigit()) or (int(choise_3_qual) not in range(1, 101)):
                    choise_3_qual = input("Неверное значение, введите заново: ")

                if choise_3_img == "0":
                    for img in imgs:
                        compress_image(img, int(choise_3_qual), os.path.splitext(img)[1])
                else:
                    img = imgs[int(choise_3_img)-1]
                    compress_image(img, int(choise_3_qual), os.path.splitext(img)[1])

            case "4":
                choise_4 = input("""Выберите действие:\n\n1.Удалить все файлы, начинающиеся на определённую подстроку.
2.Удалить все файлы, заканчивающиеся на определённую подстроку.
3.Удалить все файлы, содержащие определённую подстроку.
4.Удалить все файлы по расширению
 -""")

                while (not choise_4.isdigit()) or (int(choise_4) not in range(1, 5)):
                    choise_4 = input("Неверное значение, введите заново: ")

                process_remove(choise_4)
            case "5":
                break
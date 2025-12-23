import os

def process_remove(choise):

    match choise:
        case "1":
            prefix = input("Введите подстроку: ")

            remove_by_prefix(os.getcwd(), prefix)
        case "2":
            postfix = input("Введите подстроку: ")

            remove_by_postfix(os.getcwd(), postfix)
        case "3":
            suffix = input("Введите подстроку: ")

            remove_by_suffix(os.getcwd(), suffix)
        case "4":
            ext = input("Введите расширение в формате '.***': ")

            remove_by_ext(os.getcwd(), ext)

def remove_by_prefix(path, prefix):
    files = [file for file in os.listdir(path) if file.startswith(prefix)]

    print(f"\nФайлы начинающиеся на '{prefix}': ")

    for i in range(1, len(files)+1):
        print(f"[{i}] {files[i-1]}")

    choise = input("Удалить?[д\н]: ")
    while choise.lower() not in ["д", "н", "да", "нет"]:
        choise = input("Удалить?[д\н]: ")

    if choise.lower() in ["д", "да"]:
        for file in files:
            os.remove(file)
        return True
    else:
        return False


def remove_by_postfix(path, postfix):
    files = [file for file in os.listdir(path) if file.endswith(postfix)]

    print(f"\nФайлы начинающиеся на '{postfix}': ")

    for i in range(1, len(files)+1):
        print(f"[{i}] {files[i-1]}")

    choise = input("Удалить?[д\н]: ")
    while choise.lower() not in ["д", "н", "да", "нет"]:
        choise = input("Удалить?[д\н]: ")

    if choise.lower() in ["д", "да"]:
        for file in files:
            os.remove(file)
        return True
    else:
        return False


def remove_by_suffix(path, suffix):
    files = [file for file in os.listdir(path) if suffix in file]

    print(f"\nФайлы содержащие '{suffix}': ")

    for i in range(1, len(files)+1):
        print(f"[{i}] {files[i-1]}")

    choise = input("Удалить?[д\н]: ")
    while choise.lower() not in ["д", "н", "да", "нет"]:
        choise = input("Удалить?[д\н]: ")

    if choise.lower() in ["д", "да"]:
        for file in files:
            os.remove(file)
        return True
    else:
        return False


def remove_by_ext(path, ext):
    files = [file for file in os.listdir(path) if os.path.splitext(file)[1] == ext]

    print(f"\nФайлы с расширением '{ext}': ")

    for i in range(1, len(files)+1):
        print(f"[{i}] {files[i-1]}")

    choise = input("Удалить?[д\н]: ")
    while choise.lower() not in ["д", "н", "да", "нет"]:
        choise = input("Удалить?[д\н]: ")

    if choise.lower() in ["д", "да"]:
        for file in files:
            os.remove(file)
        return True
    else:
        return False


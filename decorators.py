from datetime import datetime



def log_errors(func):
    """
        Декоратор, записывающий логи в специальный файл
    """

    def log_error(error, text):
        """
            Вспомогательная функция, записывающая ошибку в файл game.log
        """

        with open("log.txt", "a", encoding="utf-8") as log:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{date}] ERROR: {error} - {text}\n")

    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except FileNotFoundError as e:
            log_error("FileNotFoundError", f"Файл {e.filename} не найден"); print("\033[31m" + f"FileNotFoundError: Файл {e.filename} не найден" + "\033[97m")
        except ValueError as e:
            log_error("ValueError", f"Некорректный ввод пользователя: {e.args}"); print("\033[31m" + f"ValueError: Некорректный ввод пользователя: {e.args}" + "\033[97m")
        except PermissionError as e:
            log_error("PermissionError", f"Нет прав на запись в файл {e.filename}"); print("\033[31m" + f"PermissionError: Нет прав на запись в файл {e.filename}" + "\033[97m")
        except ImportError as e:
            log_error("ImportError", f"Не установлены библиотеки: {e.name}"); print("\033[31m" + f"Не установлены библиотеки: {e.name}" + "\033[97m")
        except OSError as e:
            log_error("OSError", f"Ошибка операционной системы: {e.errno}"); print("\033[31m" + f"Ошибка операционной системы: {e.args}" + "\033[97m")

    return wrapper
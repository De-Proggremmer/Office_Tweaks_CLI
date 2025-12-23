import os

from decorators import log_errors

@log_errors
def list_dir(path, filter, flg = True):
    files = []
    for file in os.listdir(path):
        for f in filter:
            if file.endswith(f):
                files.append(file)

    if flg:
        print("[0] Выбрать все")

        for i in range(1, len(files)+1):
            print(f"[{i}] {files[i-1]}")

    return files
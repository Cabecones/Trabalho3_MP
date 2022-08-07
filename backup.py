import os
import time
import shutil


# ver ultima modificacao de um arquivo
def last_modified(path):
    return time.ctime(os.path.getmtime(path))


# verificar quais dos arquivos tem a ultima modificacao
def which_is_newest(path1, path2):
    if last_modified(path1) > last_modified(path2):
        return path1
    else:
        return path2


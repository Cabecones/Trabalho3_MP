import os
import time
import shutil


# verificar se backupParm.txt está vazio
def is_empty(path):
    result = os.stat(path).st_size == 0
    if result != 0:
        return 'Impossível'
    else:
        return ''


# ver ultima modificacao de um arquivo
def last_modified(path):
    return time.ctime(os.path.getmtime(path))


# verificar quais dos arquivos tem a ultima modificacao
def which_is_newest(path1, path2):
    if last_modified(path1) > last_modified(path2):
        return path1
    else:
        return path2


# verifica se diretorio tem determinado arquivo
def has_file(path, file):
    return os.path.isfile(os.path.join(path, file))


# copia um arquivo para outro diretorio
def copy_file(path1, path2):
    shutil.copy(path1, path2)



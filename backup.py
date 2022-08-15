import os
import shutil
import datetime


# verificar se path_backup_parm está vazio
def is_empty(path):
    result = os.stat(path).st_size == 0
    if result != 0:
        return 'Impossível'
    else:
        return ''


# ver ultima modificacao de um arquivo usando pathlib
def last_modified(path):
    t = os.path.getmtime(path)
    return datetime.datetime.fromtimestamp(t)


# verificar quais dos arquivos tem a ultima modificacao
def which_is_newest(path1, path2):
    if last_modified(path1) > last_modified(path2):
        return path1
    else:
        return path2


# verifica se diretorio tem determinado arquivo
def has_file(path, file):
    return os.path.isfile(os.path.join(path, file))


# extrair texto do path_backup_parm
def get_text(path):
    with open(path, 'r') as f:
        return f.read()


# copia um arquivo para outro diretorio
def copy_file(path1, path2):
    shutil.copy2(path1, path2)


# verificar se dois arquivos tem o mesmo tempo de modificacao
def is_same_time(path1, path2):
    return last_modified(path1) == last_modified(path2)


def program(path_hd, path_pendrive, path_backup_parm, faz_backup):
    # primeiro verifica se parm existe
    if is_empty(path_backup_parm) != 'Impossível':
        # verifica se o arquivo existe em hd
        if has_file(path_hd, get_text(path_backup_parm)):
            if has_file(path_pendrive, get_text(path_backup_parm)):
                if faz_backup == 'True':
                    # verifica qual eh o arquivo mais recente
                    if which_is_newest(path_hd + '/' + get_text(path_backup_parm),
                                       path_pendrive + '/' + get_text(path_backup_parm)) == path_hd + '/' + get_text(
                        path_backup_parm):
                        # caso o hd seja mais recente copia o arquivo para pendrive
                        copy_file(path_hd + '/' + get_text(path_backup_parm), path_pendrive)
                        print('Arquivo copiado para o pendrive')
                    elif is_same_time(path_hd + '/' + get_text(path_backup_parm),
                                      path_pendrive + '/' + get_text(path_backup_parm)):
                        return 'Faz nada'
                    elif which_is_newest(path_hd + '/' + get_text(path_backup_parm),
                                         path_pendrive + '/' + get_text(
                                             path_backup_parm)) == path_pendrive + '/' + get_text(
                        path_backup_parm):
                        # caso o pendrive seja mais recente
                        print('Não foi possível fazer o backup')
                    # verifica se os dois tem o mesmo tempo de modificacao
                    else:
                        print('Não foi possível fazer o backup')
                else:
                    # verifica qual eh o arquivo mais recente
                    if which_is_newest(path_hd + '/' + get_text(path_backup_parm),
                                       path_pendrive + '/' + get_text(path_backup_parm)) == path_hd + '/' + get_text(
                        path_backup_parm):
                        print('Não foi possível fazer o backup')
                    # verifica se os dois tem o mesmo tempo de modificacao
                    elif is_same_time(path_hd + '/' + get_text(path_backup_parm),
                                      path_pendrive + '/' + get_text(path_backup_parm)):
                        return 'Faz nada'
                    elif which_is_newest(path_hd + '/' + get_text(path_backup_parm),
                                         path_pendrive + '/' + get_text(
                                             path_backup_parm)) == path_pendrive + '/' + get_text(
                        path_backup_parm):
                        # caso o pendrive seja mais recente
                        copy_file(path_pendrive + '/' + get_text(path_backup_parm), path_hd)
                        print('Arquivo copiado para o hd')
            else:
                if faz_backup == 'True':
                    # copia o arquivo para o pendrive
                    copy_file(path_hd + '/' + get_text(path_backup_parm), path_pendrive)
                    print('Arquivo copiado para o pendrive')
                else:
                    print('Não foi possível fazer o backup')
        else:
            if faz_backup == 'True':
                print('Não foi possível fazer o backup')
                if has_file(path_pendrive, get_text(path_backup_parm)):
                    return 'Faz nada'
            else:
                if has_file(path_pendrive, get_text(path_backup_parm)):
                    copy_file(path_pendrive + '/' + get_text(path_backup_parm), path_hd)
                    print('Arquivo copiado para o hd')
                else:
                    print('Não foi possível fazer o backup')
    else:
        print('Impossível')

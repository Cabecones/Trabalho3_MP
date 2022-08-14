import sys

import backup

faz_backup_s = True
faz_backup_n = False


# teste caso 1 - check backupParm
def test_check_backupParm():
    assert backup.is_empty('casos_teste/caso1/backupParm.txt') == ''
    assert backup.is_empty('casos_teste/caso1/backupParm_vazio.txt') == 'Impossível'


# teste caso 2
def test_caso2():
    # testar se o arquivo de pendrive foi copiado para pendrive
    backup.program('casos_teste/caso2/hd', 'casos_teste/caso2/pendrive', 'casos_teste/caso2/backupParm.txt', 'True')
    assert backup.has_file('casos_teste/caso2/pendrive', backup.get_text('casos_teste/caso2/backupParm.txt')) == True


# teste caso 3
def test_caso3(capsys):
    # testar no caso do arquivo do hd ser mais recente
    backup.program('casos_teste/caso3/hd', 'casos_teste/caso3/pendrive', 'casos_teste/caso3/backupParm.txt', 'True')
    captured = capsys.readouterr()
    assert captured.out == "Arquivo copiado para o pendrive\n"



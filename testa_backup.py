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
    assert captured.out == "Arquivo copiado para o pendrive\n" or 'Não foi possível fazer o backup\n' and backup.is_same_time('casos_teste/caso3/hd/' + backup.get_text('casos_teste/caso3/backupParm.txt'), 'casos_teste/caso3/pendrive/' + backup.get_text('casos_teste/caso3/backupParm.txt')) == True
    # "Não foi possível fazer o backup\n" é no caso de o teste já ter sido feito anteriormente


# teste caso 4
def test_caso4():
    # testar no caso de as duas pastas terem o mesmo tempo de modificação
    assert backup.program('casos_teste/caso4/hd', 'casos_teste/caso4/pendrive', 'casos_teste/caso4/backupParm.txt',
                          'True') == 'Faz nada'


# teste caso 5
def test_caso5(capsys):
    # testar no caso arquivo do pendrive ser mais recente
    backup.program('casos_teste/caso5/hd', 'casos_teste/caso5/pendrive', 'casos_teste/caso5/backupParm.txt', 'True')
    captured = capsys.readouterr()
    assert captured.out == 'Não foi possível fazer o backup\n' or backup.program('casos_teste/caso5/hd', 'casos_teste/caso5/pendrive', 'casos_teste/caso5/backupParm.txt', 'True') == 'Faz nada'


# teste caso 6
def test_caso6(capsys):
    # testar quando o "faz_backup" é False e só o hd contem o arquivo monitorado
    backup.program('casos_teste/caso6/hd', 'casos_teste/caso6/pendrive', 'casos_teste/caso6/backupParm.txt', 'False')
    captured = capsys.readouterr()
    assert captured.out == 'Não foi possível fazer o backup\n'


# teste caso 7
def test_caso7(capsys):
    # testar quando o "faz_backup" é false e o arquivo do hd é o mais recente
    backup.program('casos_teste/caso7/hd', 'casos_teste/caso7/pendrive', 'casos_teste/caso7/backupParm.txt', 'False')
    captured = capsys.readouterr()
    assert captured.out == 'Não foi possível fazer o backup\n'
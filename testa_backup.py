import backup

#teste caso 1 - check backupParm
def testa_check_backupParm():
    assert backup.is_empty('casos_teste/caso1/backupParm.txt') == ''
    assert backup.is_empty('casos_teste/caso1/backupParm_vazio.txt') == 'Impossível'


#teste caso 2


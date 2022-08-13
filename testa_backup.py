import backup

#testar se quando o arquivo foi modificado
def test_last_modified():
    assert backup.last_modified('arq_antigo/arquivo.pdf') == 'Sun Aug  7 17:59:19 2022'

def test_which_is_newest():
    assert backup.which_is_newest('arq_antigo/arquivo.pdf', 'arq_novo/arquivo.pdf') == 'arq_novo/arquivo.pdf'

#verificar se backupParm.txt está vazio
def test_is_empty():
    assert backup.is_empty('backupParm.txt') == False
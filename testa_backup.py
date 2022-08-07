import backup

#testar se quando o arquivo foi modificado
def test_last_modified():
    assert backup.last_modified('MP_trab_3.pdf') == 'Sun Aug  7 17:59:19 2022'

def test_which_is_newest():
    assert backup.which_is_newest('MP_trab_3.pdf', 'Aula_Testes_2.pdf') == 'Aula_Testes_2.pdf'

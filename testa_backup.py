import backup

#testar se quando o arquivo foi modificado
def test_last_modified():
    assert backup.last_modified('MP_trab_3.pdf') == 'Sun Aug  7 17:59:19 2022'


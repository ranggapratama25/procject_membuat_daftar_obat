from . import Operasi

Db_name = 'database.txt'
TAMPLATE = {
    'pk': 'XXXXXX',
    'date_add': 'xxxx-xx-xx',
    'pembuat_obat': 255*' ',
    'nama_obat': 255*' ',
    'exp': 'xxxx'
}


def init_console():
    try:
        with open(Db_name, 'r', encoding='utf-8') as file:
            print('Database tesedia, init done!')

    except:
        print('Database tidak ditemukan, silahkan membuat database baru')
        Operasi.create_first_data()

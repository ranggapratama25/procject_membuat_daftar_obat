from time import time
from . import database
from .util import random_string
import time
import os


def delete(no_obat):
    try:
        with open(database.Db_name, 'r') as file:
            counter = 0
            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_obat - 1:
                    pass
                else:
                    with open('data_temp.txt', 'a', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print('database eror')

    os.rename('data_temp.txt', database.Db_name)


def update(no_obat, pk, data_add, pembuat_obat, nama_obat, exp):
    data = database.TAMPLATE.copy()
    # bukadata = open(database.Db_name)

    data['pk'] = pk
    data['date_add'] = data_add
    data['pembuat_obat'] = pembuat_obat + \
        database.TAMPLATE['pembuat_obat'][len(pembuat_obat):]
    data['nama_obat'] = nama_obat + \
        database.TAMPLATE['nama_obat'][len(nama_obat):]
    data['exp'] = str(exp)

    data_str = f"{data['pk']},{data['date_add']}, {data['pembuat_obat']},{data['nama_obat']}, {data['exp']}\n"

    data_length = len(data_str)

    try:
        with (open(database.Db_name, 'r+', encoding='utf-8')) as file:
            # file = database.Db_name.readlines()
            # file = database.Db_name.writelines(data)
            file.seek(data_length*(no_obat-1))
            file.write(data_str)
    except:
        print('eror update')
    os.rename('data_temp.txt', database.Db_name)


def create(exp, nama_obat, pembuat_obat):
    data = database.TAMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%M-%D-%H-%M-%S%z', time.gmtime())
    data['pembuat_obat'] = pembuat_obat + \
        database.TAMPLATE['pembuat_obat'][len(pembuat_obat):]
    data['nama_obat'] = nama_obat + \
        database.TAMPLATE['nama_obat'][len(nama_obat):]
    data['exp'] = exp

    data_str = f"{data['pk']},{data['date_add']}, {data['pembuat_obat']},{data['nama_obat']}, {data['exp']}\n"

    try:
        with open(database.Db_name, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('data tidak bisa di masukan')


def create_first_data():
    pembuat_obat = input('pembuat obat    = ')
    nama_obat = input('nama obat       = ')
    while (True):
        try:
            exp = int(input('exp\t\t= '))
            if len(str(exp)) == 4:
                break
            else:
                print('exp harus angka, silahkan masukan angka (xxxx)')
        except:
            print('exp harus angka, silahkan masukan angka (xxxx)')

    data = database.TAMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%M-%D-%H-%M-%S%z', time.gmtime())
    data['pembuat_obat'] = pembuat_obat + \
        database.TAMPLATE['pembuat_obat'][len(pembuat_obat):]
    data['nama_obat'] = nama_obat + \
        database.TAMPLATE['nama_obat'][len(nama_obat):]
    data['exp'] = exp

    data_str = f"{data['pk']},{data['date_add']}, {data['pembuat_obat']},{data['nama_obat']}, {data['exp']}\n"
    print(data_str)
    try:
        with open(database.Db_name, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('udah bisa belum cakk')


def read(**kwargs):
    try:
        with open(database.Db_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            jumlah_obat = len(content)
            if 'index' in kwargs:
                index_obat = kwargs['index']-1
                if index_obat < 0 or index_obat > jumlah_obat:
                    return False
                else:
                    return content[index_obat]
            else:
                return content
    except:
        print('membaca data bases')
        return False

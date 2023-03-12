from . import Operasi
import random
import string


def delete_console():
    read_console()
    while (True):
        print('Pilih nomor yang mau di delete')
        no_obat = int(input('Nomor Obat = '))
        data_obat = Operasi.read(index=no_obat)

        if data_obat:
            data_break = data_obat.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            pembuat_obat = data_break[2]
            nama_obat = data_break[3]
            exp = data_break[4][:-1]

            # data yang ingin di hapus #
            print('\n'+'='*100)
            print('Silahkan Pilih Data Apa Yang Ingin Anda Rubah')
            print(f'1. Pembuat Obat\t={pembuat_obat:.40}')
            print(f'2. Nama Obat\t= {nama_obat:.32}')
            print(f'3. Exp\t\t= {exp:2}')

            is_done = input('Apakah Anda Ingin Menghapus Data (yes \ no)')
            if is_done == 'yes':
                Operasi.delete(no_obat)
                break
        else:
            print('Kode Tidak Valid, Silahkan Masukan Lagi')

    print('Data Berhasil Di Hapus')


def update_console():
    read_console()
    while (True):
        print('Tambah Obat')
        no_obat = int(input('Nomor Obat = '))
        data_obat = Operasi.read(index=no_obat)

        data_break = data_obat.split(',')
        pk = data_break[0]
        data_add = data_break[1]
        pembuat_obat = data_break[2]
        nama_obat = data_break[3]
        exp = data_break[4][:-1]

        if data_obat:
            break
        else:
            print('Kode Tidak Valid, Silahkan Masukan Lagi')

    while (True):
        # data yang ingin di update #
        print('\n'+'='*100)
        print('Silahkan Pilih Data Apa Yang Ingin Anda Rubah')
        print(f'1. Pembuat Obat\t={pembuat_obat:.40}')
        print(f'2. Nama Obat\t= {nama_obat:.32}')
        print(f'3. Exp\t\t= {exp:2}')

        # memilih mode untuk update #
        user_option = input('pilih NO data di atas = ')
        print('\n'+'='*100)
        match user_option:
            case '1': pembuat_obat = input('pembuat obat\t = ')
            case '2': nama_obat = input('nama obat\t = ')
            case '3':
                while (True):
                    try:
                        exp = int(input('exp\t\t = '))
                        if len(str(exp)) == 4:
                            break
                        else:
                            print('exp harus angka, silahkan masukan angka (xxxx)')
                    except:
                        print('exp harus angka, silahkan masukan angka (xxxx)')
            case _: print('index tidk cocok')

        print('Data Yang Baru Di Rubah')
        print(f'1. Pembuat Obat\t={pembuat_obat:.40}')
        print(f'2. Nama Obat\t= {nama_obat:.32}')
        print(f'3. Exp\t\t= {exp:2}')
        is_done = input('Apakah Data Udah Sesuai (yes \ no)')
        if is_done == 'yes':
            break

    Operasi.update(no_obat, pk, data_add, pembuat_obat, nama_obat, exp)


def create_console():
    print('\n\n'+'-'*100)
    print('mari input data obat\n')
    nama_obat = input('nama obat\t = ')
    pembuat_obat = input('pembuat obat\t = ')
    while (True):
        try:
            exp = int(input('exp\t\t = '))
            if len(str(exp)) == 4:
                break
            else:
                print('exp harus angka, silahkan masukan angka (xxxx)')
        except:
            print('exp harus angka, silahkan masukan tahun (xxxx)')

    Operasi.create(exp, nama_obat, pembuat_obat)
    print('\nData baru')
    read_console()


def read_console():
    data_file = Operasi.read()

    kode = 'kode obat'
    index = 'No'
    pembuat_obat = 'Pembuat Obat'
    nama_obat = 'Nama Obat'
    exp = 'Exp'

    # Header #
    print('\n'+'='*103)
    print(f'{kode:8} | {index:3}   | {pembuat_obat:40} | {nama_obat:32} | {exp:5}')
    print('-'*103)

    # Data #
    KEY = ''.join((random.choice(string.ascii_uppercase)
                  for i in range(6)))

    for index, data in enumerate(data_file):
        data_break = data.split(',')
        KEY = data_break[0]
        pk = data_break[0]
        date_add = data_break[1]
        pembuat_obat = data_break[2]
        nama_obat = data_break[3]
        exp = data_break[4]
        print(
            f'{KEY:9} | {index+1:1}\t  |{pembuat_obat:.40}  | {nama_obat:.32} |{exp:2}', end='')

    # Footer #
    print('='*103+'\n')

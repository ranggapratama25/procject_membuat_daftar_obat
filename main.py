import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name

    match sistem_operasi:
        case 'posix': os.system('clear')   # <- unutuk di unix / linux
        case 'nt': os.system('cls')        # <- untuk di windows

    print('SELAMAT DATANG DI PROGRAM')
    print('     DATABASES APOTIK    ')
    print('-------------------------')

    ## check database ##
    CRUD.init_console()

    while (True):
        match sistem_operasi:
            case 'posix': os.system('clear')   # <- unutuk di unix / linux
            case 'nt': os.system('cls')        # <- untuk di windows

        print('SELAMAT DATANG DI PROGRAM')
        print('     DATABASES APOTIK    ')
        print('-------------------------')

        print(f'1. Read Data')
        print(f'2. Create Data')
        print(f'3. Update Data')
        print(f'4. Delete Data\n')

        user_option = input('Masukan Opsi = ')

        match user_option:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()

        is_done = input('Apakah Selesai (yes \ no)')
        if is_done == 'yes':
            break
    print('Pencarian Berakhir')

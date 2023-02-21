listYP = [
    { 
    'id' :'001',
    'Nama'  : 'PT Adhi Prima Karya',
    'Kategori' : 'Industri',
    'noTelp' : 265482,
    },
    { 
    'id':'002',
    'Nama'  : 'PT Honda Prospect',
    'Kategori' : 'Otomotif',
    'noTelp' : 465213,
    },
    { 
    'id':'003',
    'Nama'  : 'PT Boga Sari Rasa',
    'Kategori' : 'Restaurant',
    'noTelp' : 785412,
    },
    {
    'id':'004',
    'Nama'  : 'PT Enter Komputer',
    'Kategori' : 'Komputer',
    'noTelp' : 965478,
    },
    { 
    'id' :'005',
    'Nama'  : 'PT Haris Indostay',
    'Kategori' : 'Hotel\t',
    'noTelp' : 418652,
    },
    {
    'id':'006',
    'Nama'  : 'PT Summarecon Agung',
    'Kategori' : 'Properti',
    'noTelp' : 451398,
    },
    { 
    'id':'007',
    'Nama'  : 'PT Travel Surya Kirana',
    'Kategori' : 'Travel\t',
    'noTelp' : 484515,
    },
    { 
    'id':'008',
    'Nama'  : 'PT Panasaja Global',
    'Kategori' : 'Elektronik',
    'noTelp' : 152425,
    },
    { 
    'id':'009',
    'Nama'  : 'PT Publik Financeindo',
    'Kategori' : 'Keuangan',
    'noTelp' : 740256,
    },
]

def mainMenu():
    while True:
        print('''
    =================================================================================================
    **************************     Welcome to Purwadhika Yellow Pages     ***************************
    =================================================================================================
    Menu List 

    1. Tampilkan listing
    2. Tambahkan listing 
    3. Perbaharui listing
    4. Hapus listing
    5. Keluar
    ''')
        menu = input('Masukan nomor menu yang akan dijalanlan !')
        if menu == '1':
            menuMenampilkanListing()
        elif menu == '2':
            menuMenambahListing()
        elif menu == '3':
            menuPerbaharuiListing()
        elif menu == '4':
            menuHapusListing()
        elif menu == '5':
            keluarprogram()
    

def lihatListing():
    print("|ID\t|Nama Perusahaan\t\t|Kategori\t|No.Telp|")
    for i in range (len(listYP)) :
        print("|{}\t|{}\t\t|{}\t|{}\t|". format(listYP[i]['id'],listYP[i]['Nama'],listYP[i]['Kategori'],listYP[i]['noTelp']))

def back():
    while True:
        break

#################################################################################
def menuMenampilkanListing():
    while True :
        print('''
---------------------------------------------------------------------------------
                                    MENU 1                                      
                              MENAMPILKAN LISTING                              
---------------------------------------------------------------------------------
1. Tampilkan seluruh listing
2. Cari listing menggunakan ID
3. Kembali ke menu utama
''')
        pilihan = input('Masukan menu pilihan anda !')
        if pilihan == '1':
            if len(listYP) !=0 :
                lihatListing()
                back()
                menuMenampilkanListing()
            else :
                print('Data tidak tersedia, hubungi penyedia yellow pages anda')
                back()
                menuMenampilkanListing()

        elif pilihan == '2':
            if len(listYP)!=0:
                idcari = input("\nMasukkan id yang dicari: ").upper()
                for i in range(len(listYP)):
                    if idcari == listYP[i]['id']:
                        print("|ID\t|Nama Perusahaan\t\t|Kategori\t|No.Telp|")
                        print("|{}\t|{}\t\t|{}\t|{}\t|". format(listYP[i]['id'],listYP[i]['Nama'],listYP[i]['Kategori'],listYP[i]['noTelp']))
                        back()
                        menuMenampilkanListing()
                else:
                    print ('\nData tidak tersedia')
                    back()
                    menuMenampilkanListing()
        elif pilihan == '3':
            mainMenu()

        else :
            print('Anda salah menginput nomor menu, harap masukan nomor yang benar !')
            menuMenampilkanListing()
#################################################################################
def menuMenambahListing ():
    while True :
        print('''
---------------------------------------------------------------------------------
                                    MENU 2                                      
                              MENAMBAH LISTING                              
---------------------------------------------------------------------------------
1. Menambah listing
2. Kembali ke menu utama
''')
        pilihan = input('Masukan menu pilihan anda !')
        if pilihan == '1' :
            id = input('Masukan nomor ID listing baru anda: ')
            for i in range(len(listYP)):
                if id == listYP[i]['id']:
                    print('Penambahan gagal, id yang anda masukan sudah terdaftar')
                    back()
                    menuMenambahListing()
            else :
                nama = input('Masukan nama perusahaan :')
                kategori = input('Masukan kategori bidang bisnis perusahaan :')
                noTelp = int(input(('masukan nomor telefon perusahaan (Masukan hanya angka) :')))

            cek = input('Pastikan data sudah benar\nApakah anda ingin menyimpan data di atas? (Y/N):').upper()
            if cek == 'Y':
                    listYP.append(
                        {'id': id,
                        'Nama': nama, 
                        'Kategori' : kategori,
                        'noTelp': noTelp  
                        })
                    print ('\nData berhasil disimpan')
                    back()
                    lihatListing()
                    menuMenambahListing()
            else:
                    print("\nData tidak tersimpan")
                    back()
                    menuMenambahListing()

        elif pilihan == '2':
            mainMenu()
        else :
            print('Anda salah menginput nomor menu, harap masukan nomor yang benar !')
            menuMenambahListing()
#################################################################################
def menuPerbaharuiListing ():
    while True :
        print('''
---------------------------------------------------------------------------------
                                    MENU 3                                      
                              PERBAHARUI LISTING                              
---------------------------------------------------------------------------------
1. Perbaharui listing
2. Kembali ke menu utama
''')         
        menu = input('Masukan menu pilihan anda : ')    
        if menu == '1':
            id = input('Masukan id dari listing yang ingin diperbaharui')   
            for i in range (len(listYP)) :
                if id == listYP[i]['id']:
                    print("|ID\t|Nama Perusahaan\t\t|Kategori\t|No.Telp|")
                    print("|{}\t|{}\t\t|{}\t|{}\t|". format(listYP[i]['id'],listYP[i]['Nama'],listYP[i]['Kategori'],listYP[i]['noTelp']))
                    updateConf = input('data dengan nomor id {} telah ditemukan, apakah lanjut perbaharui (Y/N) ? '.format(listYP[i]['id'])).upper()
                    if updateConf == 'Y' :
                        updateColumn = input('''Kolom mana yang akan anda perbaharui ?
                        1. Nama Perusahaan
                        2. Bidang kategori
                        3. No Telepon''')
                        if updateColumn == '1':
                            newName = input('Masukan nama perusahaan yang baru : ')
                            cek = input('Nama perusahaan akan diubah dari {} menjadi {}, apakah anda yakin (Y/N) ?'.format(listYP[i]['Nama'],newName)).upper()
                            if cek == 'Y' :
                                listYP[i]['Nama'] = newName
                                print('Data telah berhasil di update !')
                                back()
                                menuPerbaharuiListing()
                            else :
                                print('Data gagal diperbaharui')
                                back()
                                menuPerbaharuiListing()

                        if updateColumn == '2':
                            newCategory = input('Masukan bidang kategori yang baru : ')
                            cek = input('Bidang kerja akan diubah dari {} menjadi {}, apakah anda yakin (Y/N) ?'.format(listYP[i]['Kategori'],newCategory)).upper()
                            if cek == 'Y' :
                                listYP[i]['Kategori'] = newCategory
                                print('Data telah berhasil di update !')
                                back()
                                menuPerbaharuiListing()
                            else :
                                print('Data gagal diperbaharui')
                                back()
                                menuPerbaharuiListing()
                        if updateColumn == '3':
                            newNoTelp = input('Masukan nomor telefon yang baru : ')
                            cek = input('Nomor telefon akan diubah dari {} menjadi {}, apakah anda yakin (Y/N) ?'.format(listYP[i]['noTelp'],newNoTelp)).upper()
                            if cek == 'Y' :
                                listYP[i]['noTelp'] = newNoTelp
                                print('Data telah berhasil di update !')
                                back()
                                menuPerbaharuiListing()
                            else :
                                print('Data gagal diperbaharui')
                                back()
                                menuPerbaharuiListing()
            else :
                print('ID tidak ditemukan, gagal untuk memperbaharui')
                back()
                menuPerbaharuiListing()
        elif menu == '2':
            mainMenu()

        else :
            print('Anda salah memasukan nomor menu')
            menuPerbaharuiListing
        

#################################################################################
def menuHapusListing ():
    while True :
        print('''
---------------------------------------------------------------------------------
                                    MENU 4                                      
                              MENGHAPUS LISTING                              
---------------------------------------------------------------------------------
1. Menghapus listing
2. Kembali ke menu utama
''')
        pilihan = input('Masukan menu pilihan anda !')
        if pilihan == '1':
            idHapus = input('Masukan id yang akan dihapus : ')
            for i in range(len(listYP)):
                if idHapus == listYP[i]['id']:
                    print("|ID\t|Nama Perusahaan\t\t|Kategori\t|No.Telp|")
                    print("|{}\t|{}\t\t|{}\t|{}\t|". format(listYP[i]['id'],listYP[i]['Nama'],listYP[i]['Kategori'],listYP[i]['noTelp']))
                    hapusConf = input('listing dengan id {} ditemukan, apakah ingin lanjut dihapus ? (Y/N)'.format(listYP[i]['id'])).upper()
                    if hapusConf == 'Y':
                        del listYP[i]
                        print('Data berhasil dihapus')
                        back()
                        menuHapusListing()
                    else :    
                        print('Data tidak ditemukan, gagal menghapus data')
                        back()
                        menuHapusListing()
            else :
                print('Data dengan id {} tidak ditemukan'.format(idHapus))
        if pilihan == '2':
            back()
            mainMenu()
        else :
            menuHapusListing()
    

def keluarprogram():
    print('\nSampai jumpa lagi !')
    exit()

mainMenu()

        






                    

                        
                    



        
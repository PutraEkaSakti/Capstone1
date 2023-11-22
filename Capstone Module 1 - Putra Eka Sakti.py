#Penjualan barang di toko
list_barang=[{'NamaItem':'Telur','UOM':'Tray','Stok':10,'Harga':10000},
{'NamaItem':'Beras','UOM':'Kg','Stok':10,'Harga':13000},
{'NamaItem':'Mie','UOM':'Pcs','Stok':10,'Harga':2000},
{'NamaItem':'Gula','UOM':'Kg','Stok':10,'Harga':16000}]
cart=[]

#---Mendefinisikan Menu---#
def daftarbarang ():
    print('\nIndex\t|Nama Item\t|UOM\t|Stok\t|Harga')
    for i in range(len(list_barang)):
        print(f'{i}\t|{list_barang[i]['NamaItem']}\t\t|{list_barang[i]['UOM']}\t|{list_barang[i]['Stok']}\t|{list_barang[i]['Harga']}')

def tambahitembaru ():
    item=input('Masukkan Nama Item :')
    UOM=input('Masukkan unit of measurement: ')
    Stok=int(input('Masukkan Stok Item : '))
    Harga=int(input('Masukkan Harga Item : '))
    list_barang.append({'NamaItem':item.capitalize(),'UOM':UOM.capitalize(),'Stok':Stok,'Harga':Harga})
    daftarbarang ()
    print(f'Kamu berhasil menambahkan item {list_barang[len(list_barang)-1]['NamaItem']} ke dalam list')

def updatestok():
    daftarbarang ()
    indexstoktambahan=int(input('Masukkan Index Item yang ingin kamu update stoknya: '))
    tambahanstok=int(input(f'Masukkan jumlah {list_barang[indexstoktambahan]['NamaItem']} yang ingin anda tambah/kurang : '))
    list_barang[indexstoktambahan]['Stok']+=tambahanstok
    daftarbarang ()
    print(f'Stok {list_barang[indexstoktambahan]['NamaItem']} telah terbarukan!')

def updateharga():
    daftarbarang ()
    indexharga=int(input('Masukkan Index Item yang ingin kamu update harganya: '))
    hargabaru=int(input(f'Masukkan harga baru untuk {list_barang[indexharga]['NamaItem']}: '))
    list_barang[indexharga]['Harga']=hargabaru
    daftarbarang ()
    print(f'Kamu berhasil melakukan update harga {list_barang[indexharga]['NamaItem']}!')

def hapusitem():
    daftarbarang ()
    indexhapus=int(input('Masukkan Index Item yang ingin kamu hapus: '))
    checkhapusitem=input(f'Apakah kamu yakin ingin menghapus item {list_barang[indexhapus]['NamaItem']}?[Ya/Tidak]')
    if checkhapusitem.capitalize()=='Ya':
        print(f'\nKamu telah berhasil menghapus item {list_barang[indexhapus]['NamaItem']}')
        del list_barang [indexhapus]
        daftarbarang ()
    else:
        daftarbarang ()
        print(f'Kamu tidak jadi menghapus {list_barang[indexhapus]['NamaItem']}')

def transaksi():
    while True:
        daftarbarang ()
        indextransaksi=int(input('Masukkan Index Item yang dibeli : '))
        qtybeli=int(input('Masukkan jumlah Item yang dibeli : '))
        if qtybeli>list_barang[indextransaksi]['Stok']:
            print(f'Stok item {list_barang[indextransaksi]['NamaItem']} tidak cukup, Stok {list_barang[indextransaksi]['NamaItem']} sisa {list_barang[indextransaksi]['Stok']} {list_barang[indextransaksi]['UOM']}')
        elif qtybeli<=0:
            print('\nQty beli tidak bisa kurang dari 1\n')
        else:
            cart.append({'Index':indextransaksi,'NamaItem':list_barang[indextransaksi]['NamaItem'],'Qty':qtybeli,'Harga':list_barang[indextransaksi]['Harga']})
        print('Isi Cart: ')
        print('index\t| Item\t| Qty\t| Harga\t| Total Harga')
        for item in range(len(cart)):
            print (f'{item}\t| {cart[item]['NamaItem']}\t| {cart[item]['Qty']}\t| {cart[item]['Harga']}\t| {(cart[item]['Harga'])*(cart[item]['Qty'])}')
        cheker=input('Apakah ingin menambahkan item lainnya?[Ya/Tidak]')
        if cheker.capitalize()=='Tidak':
            break
    print('index\t| Item\t| Qty\t| Harga\t| Total Harga')
    totalbayar=0
    for item in range(len(cart)):
        print (f'{item}\t| {cart[item]['NamaItem']}\t| {cart[item]['Qty']}\t| {cart[item]['Harga']}\t| {(cart[item]['Harga'])*(cart[item]['Qty'])}')
        totalbayar+=cart[item]['Harga']*cart[item]['Qty']
    print(f'Total yang harus di bayar sebesar : {totalbayar}')
    while True:
        uang=int(input('Masukkan Nominal Pembayaran : '))
        if uang > totalbayar:
            print(f"Transaksi Berhasil\nUang Kembalian sebesar : {uang-totalbayar}")
            for item in cart:
                list_barang[item['Index']]['Stok']-=item['Qty']
            cart.clear()
            break
        elif uang==totalbayar:
            print('Transaksi Berhasi')
            for item in cart:
                list_barang[item['Index']]['Stok']-=item['Qty']
            cart.clear()
            break
        else:
            print(f'Uang Pembayaran kurang {totalbayar-uang}')

#---Akses Menu Toko---#
while True:
    pilihanmenuawal=int(input(f'''\nSelamat Datang di Toko Berkah
        Daftar Akses:
        1. Kasir
        2. Gudang
        3. Selesai
        Silahkan pilih Nomor yang ingin kamu ingin akses : '''))
    if pilihanmenuawal==1:
        while True:
            pilihan=int(input(f'''\nSelamat Datang di Toko Berkah
        Daftar Menu:
        1. Menampilkan Daftar Barang
        2. Melakukan Transaksi
        3. Selesai
        Silahkan pilih Nomor Daftar Menu yang ingin kamu akses : '''))
            if pilihan==1:
                daftarbarang()
            elif pilihan==2:
                transaksi()
            elif pilihan==3:
                break
    if pilihanmenuawal==2:
        while True:
            pilihan=int(input(f'''\nSelamat Datang di Toko Berkah
        Daftar Menu:
        1. Menampilkan Daftar Barang
        2. Menambahkan Item
        3. Update Stok barang
        4. Update Harga Barang
        5. Menghapus Item
        6. Selesai
        Silahkan pilih Nomor Daftar Menu yang ingin kamu akses : '''))
            if pilihan==1:
                daftarbarang()
            elif pilihan==2:
                tambahitembaru ()
            elif pilihan==3:
                updatestok()
            elif pilihan==4:
                updateharga()
            elif pilihan==5:
                hapusitem()
            elif pilihan==6:
                break
    if pilihanmenuawal==3:
        break
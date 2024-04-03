Nama_jajan = str(input ('masukan nama jajan : '))
Jumlah_jajan_masuk = int(input('masukan jumlah jajan masuk :'))
Jumlah_stock_jajan = int(input('masukan stock jajan : '))
Jajan_keluar = int(input('masukan jumlah jajan: '))

Kategori_jajan =['donat','martabak','risol','otak otak','makaroni'] # tipe data list
if (Nama_jajan in Kategori_jajan and Jumlah_stock_jajan  >= 40 ):
    print('jajan memenuhi kriteria keluar')
else: print('jajan tidak memenuhi kriteria keluar')
from produk import Produk
from pelanggan import Pelanggan

print("=== INPUT DATA PRODUK ===")
nama_produk = input("Nama Produk : ")
harga_produk = int(input("Harga       : "))
stok_produk = int(input("Stok        : "))

print("\n=== INPUT DATA PELANGGAN ===")
nama_pelanggan = input("Nama   : ")
alamat = input("Alamat : ")

# Membuat objek
produk1 = Produk(nama_produk, harga_produk, stok_produk)
pelanggan1 = Pelanggan(nama_pelanggan, alamat)

# Menampilkan data
produk1.tampilkan_produk()
pelanggan1.tampilkan_pelanggan()
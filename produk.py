
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_produk(self):
        print("Nama Produk :", self.nama)
        print("Harga       : Rp", self.harga)
        print("Stok        :", self.stok)

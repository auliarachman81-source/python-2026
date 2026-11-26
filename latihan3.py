print("KALKULATOR")

pilih = input("Masukan Pilihan : ")
match pilih:
    case "1":
        a = int(input("Masukan Nilai a : "))
        b = int(input("Masukan Nilai b : "))
        hasil = a + b
        print(f"Hasil Penjumlahan : {hasil}")    
  
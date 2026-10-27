# nama = input("masukan nama anda:");
# print("hallow", nama )

# usia = int(input("masukan usia anda"));
# print("usia anda adalah", usia)

# tinggi = float(input("masukan tinggi badan anda"));
# print("tinggi badan anda adalah:", tinggi);

# Minta input angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Minta user memilih operasi
print("Pilih operasi:")
print("1. + (Penjumlahan)")
print("2. - (Pengurangan)")
print("3. * (Perkalian)")
print("4. / (Pembagian)")

operasi = input("Masukkan simbol operasi (+, -, *, /): ")

# Proses dan hasil
if operasi == '+':
    hasil = angka1 + angka2
elif operasi == '-':
    hasil = angka1 - angka2
elif operasi == '*':
    hasil = angka1 * angka2
elif operasi == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa dibagi dengan nol!"
else:
    hasil = "Operasi tidak dikenali"

print("Hasil:", hasil)

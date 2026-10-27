TEKS = "NADIA AMANDA SARI"
LEBAR, TINGGI = 60, 30
pusat_x, pusat_y = LEBAR / 2, TINGGI / 2
radius_bulan = 27
radius_lubang = 23
geser_lubang = 11
rasio_karakter = 2

HIJAU = "\033[94m"
RESET = "\033[0m"

indeks_teks = 0
for baris_y in range(TINGGI):
    baris = ""
    for kolom_x in range(LEBAR):
        jarak_x = kolom_x - pusat_x
        jarak_y = (baris_y - pusat_y) * rasio_karakter
        dalam_bulan = jarak_x**2 + jarak_y**2 <= radius_bulan**2
        dalam_lubang = (jarak_x - geser_lubang)**2 + jarak_y**2 <= radius_lubang**2
        if dalam_bulan and not dalam_lubang:
            baris += HIJAU + TEKS[indeks_teks % len(TEKS)] + RESET
            indeks_teks +=1
        else:
            baris += " "
    print(baris)
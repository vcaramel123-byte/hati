import os
os.system('color')

TEKS = "fani imut"
LEBAR, TINGGI = 60, 30

WARNA = "\033[94m"
RESET = "\033[0m"

indeks_teks = 0

for baris_y in range(15, -15, -1):
    baris = " "
    for kolom_x in range(-30, 30):
        x = kolom_x * 0.04
        y = baris_y * 0.1
        persamaan = (x**2 + y**2 - 1)**3 - x**2 * y**3
        if persamaan <= 0:
            baris += WARNA + TEKS[indeks_teks % len(TEKS)] + RESET
            indeks_teks += 1
        else:
            baris += " "
            
        
    print(baris)    
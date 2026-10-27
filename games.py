import random

def main():
    print("=" * 30)
    print ("Selamat data di game tebak angka!")
    print("Saya memikirkan angka antara 1 sampai banyak.")
    print("=" * 30)

    angka_rahasia = random.randint(1, 1000)
    jumlah_tebakan = 0 
    menang = False

    while not menang:
        try:
                tebakan = int(input("\nMasukan tebakanmu:"))
                jumlah_tebakan += 1
                if tebakan < angka_rahasia:
                    print("Terlalu rendah coba lagi.")
                elif tebakan > angka_rahasia:
                    print("Terlau tinggi! coba lagi.")
                else: 
                  print(f"\nSelamat! kamu berhasil menebak angka {angka_rahasia}")
                  print(f"Kamu memutuhkan {jumlah_tebakan} kali percobaan.")
                  menang = True
        except ValueError:
                print("Ups! Tolong masukan angka yang valid.")
if __name__ == "__main__":
            main()
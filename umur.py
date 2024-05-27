from datetime import datetime

def hitung_umur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    umur = tahun_sekarang - tahun_lahir
    return umur

def main():
    tahun_lahir = int(input("Masukkan tahun kelahiran: "))
    umur = hitung_umur(tahun_lahir)
    print(f"Umur Anda adalah {umur} tahun.")

if __name__ == "__main__":
    main()

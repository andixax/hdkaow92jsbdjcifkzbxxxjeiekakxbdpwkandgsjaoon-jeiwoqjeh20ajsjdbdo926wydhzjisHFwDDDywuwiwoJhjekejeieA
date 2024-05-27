import requests
import os

def unduh_gambar(url, nama_file):
    try:
        # Mengirim permintaan GET ke URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Memastikan tidak ada kesalahan dalam permintaan

        # Menulis konten gambar ke file lokal
        with open(nama_file, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Gambar berhasil diunduh dan disimpan sebagai {nama_file}")
    except Exception as e:
        print(f"Gagal mengunduh gambar. Kesalahan: {e}")

def main():
    url = input("Masukkan URL gambar: ")
    nama_file = input("Masukkan nama file untuk menyimpan gambar (termasuk ekstensi, misalnya gambar.jpg): ")

    # Memastikan direktori tujuan ada, jika tidak maka buatlah
    if not os.path.exists(os.path.dirname(nama_file)):
        try:
            os.makedirs(os.path.dirname(nama_file))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    unduh_gambar(url, nama_file)

if __name__ == "__main__":
    main()

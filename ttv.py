from gtts import gTTS
import os

def teks_ke_suara(teks, nama_file):
    try:
        # Buat objek gTTS dengan teks yang diberikan
        tts = gTTS(text=teks, lang='id')  # Anda dapat mengubah 'id' menjadi kode bahasa lain
        
        # Simpan file audio
        tts.save(nama_file + ".mp3")
        
        print(f"File audio '{nama_file}.mp3' berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    teks = input("Masukkan teks yang ingin diubah menjadi suara: ")
    nama_file = input("Masukkan nama file untuk menyimpan suara: ")
    
    teks_ke_suara(teks, nama_file)

if __name__ == "__main__":
    main()

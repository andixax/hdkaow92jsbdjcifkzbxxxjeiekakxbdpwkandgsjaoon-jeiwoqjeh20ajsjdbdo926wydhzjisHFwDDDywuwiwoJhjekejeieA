import requests

def dapatkan_surah(surah):
    try:
        # URL untuk mendapatkan surah
        surah_url = f"http://api.alquran.cloud/v1/surah/{surah}"
        # URL untuk mendapatkan terjemahan surah dalam bahasa Indonesia
        terjemahan_url = f"http://api.alquran.cloud/v1/surah/{surah}/editions/id.indonesian"

        surah_response = requests.get(surah_url)
        terjemahan_response = requests.get(terjemahan_url)

        surah_data = surah_response.json()
        terjemahan_data = terjemahan_response.json()

        if surah_response.status_code == 200 and terjemahan_response.status_code == 200:
            surah_ayat = surah_data['data']['ayahs']
            terjemahan_ayat = terjemahan_data['data'][0]['ayahs']

            hasil = []
            for ayat, terjemahan in zip(surah_ayat, terjemahan_ayat):
                hasil.append({
                    "nomor": ayat['numberInSurah'],
                    "teks": ayat['text'],
                    "terjemahan": terjemahan['text']
                })

            return hasil
        else:
            return f"Terjadi kesalahan saat mengambil data: {surah_response.status_code}, {terjemahan_response.status_code}"
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    surah = input("Masukkan nama atau nomor surah: ").strip().lower()

    hasil = dapatkan_surah(surah)
    if isinstance(hasil, list):
        for ayat in hasil:
            print(f"Ayat {ayat['nomor']}: {ayat['teks']}")
            print(f"Terjemahan: {ayat['terjemahan']}\n")
    else:
        print(hasil)

if __name__ == "__main__":
    main()

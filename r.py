import requests

def dapatkan_ayat(surah, ayat):
    base_url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayat}/editions/quran-uthmani,id.indonesian"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'OK':
        ayat_arabic = data['data'][0]['text']
        ayat_indo = data['data'][1]['text']

        return {
            "Arabic": ayat_arabic,
            "Indonesian": ayat_indo
        }
    else:
        return "Gagal mengambil ayat atau ayat tidak ditemukan."

def main():
    surah = input("Masukkan nomor surah: ")
    ayat = input("Masukkan nomor ayat: ")

    ayat_info = dapatkan_ayat(surah, ayat)
    if isinstance(ayat_info, dict):
        print(f"Ayat dalam Bahasa Arab: {ayat_info['Arabic']}")
        print(f"Ayat dalam Bahasa Indonesia: {ayat_info['Indonesian']}")
    else:
        print(ayat_info)

if __name__ == "__main__":
    main()

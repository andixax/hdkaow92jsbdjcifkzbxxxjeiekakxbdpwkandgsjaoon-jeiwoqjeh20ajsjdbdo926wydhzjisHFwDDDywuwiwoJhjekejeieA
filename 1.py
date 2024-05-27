import requests

def dapatkan_berita_terbaru(api_key, jumlah_berita=20):
    url = f"https://newsapi.org/v2/top-headlines?country=id&apiKey={api_key}&pageSize={jumlah_berita}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        berita_terbaru = []
        for artikel in data['articles']:
            berita_terbaru.append({
                "Judul": artikel['title'],
                "Sumber": artikel['source']['name'],
                "Tautan": artikel['url']
            })
        return berita_terbaru
    else:
        return "Gagal mengambil berita terbaru."

def main():
    api_key = "139cb445a4484eed9c6e00a46522e73f"  # Ganti dengan kunci API NewsAPI Anda
    berita_terbaru = dapatkan_berita_terbaru(api_key)
    
    if isinstance(berita_terbaru, list):
        print("Berita Terbaru:")
        for berita in berita_terbaru:
            print(f"Judul: {berita['Judul']}")
            print(f"Sumber: {berita['Sumber']}")
            print(f"Tautan: {berita['Tautan']}")
            print()
    else:
        print(berita_terbaru)

if __name__ == "__main__":
    main()

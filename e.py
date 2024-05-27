import requests

def dapatkan_berita(api_key, keyword, bahasa="id"):
    base_url = "https://newsapi.org/v2/everything?"
    complete_url = f"{base_url}q={keyword}&language={bahasa}&apiKey={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200:
        if data["status"] == "ok" and data["totalResults"] > 0:
            return data["articles"]
        else:
            return "Tidak ada berita yang ditemukan."
    else:
        return f"Terjadi kesalahan: {response.status_code}"

def tampilkan_berita(berita):
    for i, artikel in enumerate(berita):
        print(f"Berita {i+1}:")
        print(f"Judul: {artikel['title']}")
        print(f"Deskripsi: {artikel['description']}")
        print(f"Sumber: {artikel['source']['name']}")
        print(f"Tanggal: {artikel['publishedAt']}")
        print(f"Link: {artikel['url']}")
        print("-" * 40)

def main():
    api_key = "139cb445a4484eed9c6e00a46522e73f"  # Ganti dengan kunci API Anda yang sebenarnya
    keyword = input("Masukkan kata kunci untuk mencari berita: ")

    berita = dapatkan_berita(api_key, keyword)
    if isinstance(berita, list):
        tampilkan_berita(berita)
    else:
        print(berita)

if __name__ == "__main__":
    main()

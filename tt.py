import requests
import shutil
import re

def unduh_video_tiktok(url):
    try:
        # Mengirim permintaan ke layanan unduhan video TikTok
        snaptik_download_url = f"https://snaptik.app/download"
        response = requests.get(snaptik_download_url, params={"url": url})
        if response.status_code == 200:
            # Mengambil URL unduhan dari respons
            download_url = re.search(r'video_url: "(.+)"', response.text)
            if download_url:
                video_url = download_url.group(1)

                # Mengunduh video
                video_response = requests.get(video_url, stream=True)
                video_title = url.split('/')[-1] + '.mp4'
                with open(video_title, 'wb') as f:
                    shutil.copyfileobj(video_response.raw, f)

                print(f"Video berhasil diunduh: {video_title}")
                return
        print("Tidak dapat menemukan URL unduhan.")
    except Exception as e:
        print(f"Gagal mengunduh video. Kesalahan: {e}")

def main():
    url = input("Masukkan URL video TikTok: ")
    unduh_video_tiktok(url)

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.python.org/"

response = requests.get(url)
print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# 1. Title halaman 
print("Title:", soup.title.get_text(strip=True))

# 2. Judul bagian: Docs, Jobs, Latest News, dst 
print("\nJudul bagian (h2):")
for h2 in soup.find_all("h2"):
    print("-", h2.get_text(strip=True))

# 3. Daftar Latest News: tanggal dan judul
blog = soup.find("div", class_="blog-widget")  # kotak Latest News

data = []
for li in blog.find_all("li"):
    tanggal = li.find("time").get_text(strip=True)
    link = li.find("a")
    judul = link.get_text(strip=True)
    href = link.get("href")

    data.append({
        "tanggal": tanggal,
        "judul": judul,
        "link": "https://www.python.org" + href if href.startswith("/") else href,
    })

print("\nJumlah berita:", len(data))

# 4. Simpan ke CSV 
df = pd.DataFrame(data)
print(df)
df.to_csv("python_news.csv", index=False, encoding="utf-8-sig")
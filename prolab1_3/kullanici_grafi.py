import json
import networkx as nx
import matplotlib.pyplot as plt

class Kullanici:
    def __init__(self, username, name, followers_count, following_count, language, region, tweets, following, followers):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers

    def __str__(self):
        return f"{self.name} ({self.username}) - Takipçi: {self.followers_count}, Takip Edilen: {self.following_count}"

def json_dosyasindan_veri_oku(json_dosya_adı):
    with open(json_dosya_adı, 'r', encoding='utf-8') as dosya:
        veri = json.load(dosya)
    return veri

def graf_cizimi(kullanici_nesnesi):
    G = nx.DiGraph()

    # Takip edilenleri ekleyin
    for following_username in kullanici_nesnesi.following:
        G.add_edge(kullanici_nesnesi.username, following_username, color='red')

    # Takipçileri ekleyin
    for follower_username in kullanici_nesnesi.followers:
        G.add_edge(follower_username, kullanici_nesnesi.username, color='green')

    # Grafı çizdirin
    edge_colors = [G[u][v]['color'] for u, v in G.edges]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', node_size=800)
    plt.show()

# JSON dosyasını oku
json_dosya_adi = "C:\\Users\\Vahit Yüksel\\Desktop\\python\\prolab1_3\\besyuzdata.json"
json_veri = json_dosyasindan_veri_oku(json_dosya_adi)

# Hangi kullanıcı için graf çizileceğini kullanıcıdan al
aranan_username = input("Graf çizilecek kullanıcının username'ini girin: ")

# Aranan kullanıcıyı bul
aranan_kullanici = None
for kullanici_verisi in json_veri:
    if kullanici_verisi['username'] == aranan_username:
        aranan_kullanici = Kullanici(
            kullanici_verisi['username'],
            kullanici_verisi['name'],
            kullanici_verisi['followers_count'],
            kullanici_verisi['following_count'],
            kullanici_verisi['language'],
            kullanici_verisi['region'],
            kullanici_verisi['tweets'],
            kullanici_verisi['following'],
            kullanici_verisi['followers']
        )
        break

if aranan_kullanici:
    # Grafı çiz
    graf_cizimi(aranan_kullanici)
else:
    print(f"{aranan_username} kullanıcısı bulunamadı.")
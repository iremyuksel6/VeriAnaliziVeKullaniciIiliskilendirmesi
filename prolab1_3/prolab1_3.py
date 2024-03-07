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

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def kullanici_ekle(self, kullanici):
        self.nodes.add(kullanici)

    def takip_et(self, takip_eden, takip_edilen):
        self.edges.append((takip_eden, takip_edilen))

    def graf_olustur(self):
        G = nx.DiGraph()
        for kullanici in self.nodes:
            G.add_node(kullanici.username, label=kullanici.name)

        for edge in self.edges:
            takip_eden, takip_edilen = edge
            G.add_edge(takip_eden.username, takip_edilen.username)

        return G

# JSON dosyasını okuma
with open('C:\\Users\\Vahit Yüksel\\Desktop\\python\\prolab1_3\\besyuzdata.json', 'r', encoding='utf-8') as dosya:
    json_veri = json.load(dosya)


# Kullanıcı nesnelerini oluşturma
kullanici_grafi = Graph()

for kullanici_verisi in json_veri:
    kullanici = Kullanici(
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
    kullanici_grafi.kullanici_ekle(kullanici)

    for takip_edilen_username in kullanici_verisi['following']:
        takip_edilen = next((k for k in kullanici_grafi.nodes if k.username == takip_edilen_username), None)
        if takip_edilen:
            kullanici_grafi.takip_et(kullanici, takip_edilen)

# Grafı oluştur
graf = kullanici_grafi.graf_olustur()

# Grafı çiz
pos = nx.spring_layout(graf)
labels = nx.get_edge_attributes(graf, 'label')
nx.draw(graf, pos, with_labels=True, labels=nx.get_node_attributes(graf, 'label'), font_weight='bold', node_size=800, node_color='pink', font_size=8)
nx.draw_networkx_edge_labels(graf, pos, edge_labels=labels)
plt.show()
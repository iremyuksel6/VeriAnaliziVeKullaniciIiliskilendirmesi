import json
import networkx as nx
import matplotlib.pyplot as plt
from snowballstemmer import TurkishStemmer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import nltk

nltk.data.path.append(r'C:\Users\Vahit Yüksel\AppData\Roaming\nltk_data')

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
    
    def bilgileri_dosyaya_kaydet(self, dosya_adi):
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            dosya.write(f"Kullanıcı Adı: {self.username}\n")
            dosya.write(f"Adı: {self.name}\n")
            dosya.write(f"Takipçi Sayısı: {self.followers_count}\n")
            dosya.write(f"Takip Edilen Sayısı: {self.following_count}\n")
            dosya.write("İlgi Alanları:\n")
            for ilgi_alani, kelimeler in anahtar_kelimeler.items():
                if any(stemmer.stemWord(kelime) in [stemmer.stemWord(w) for w in word_tokenize(tweet, language='turkish') if w.isalnum() and w.lower() not in stopwords.words('turkish')] for tweet in self.tweets for kelime in kelimeler):
                    dosya.write(f"- {ilgi_alani.capitalize()}\n")

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

def json_dosyasindan_veri_oku(json_dosya_adı):
    with open(json_dosya_adı, 'r', encoding='utf-8') as dosya:
        veri = json.load(dosya)
    return veri

# JSON dosyasını oku
json_dosya_adi = "C:\\Users\\Vahit Yüksel\\Desktop\\python\\prolab1_3\\besyuzdata.json"
json_veri = json_dosyasindan_veri_oku(json_dosya_adi)

# Kullanıcıdan bölge adı al
hedef_bolge = input("Hangi bölgedeki kullanıcıları görmek istersiniz? Bölge kodunu girin: ")

# Sadece kullanıcı adlarını yazdır
print("\n{} Bölgesindeki Kullanıcı Adları:".format(hedef_bolge))
for kullanici_verisi in json_veri:
    if kullanici_verisi['region'] == hedef_bolge:
        print("Kullanıcı Adı:", kullanici_verisi['username'])

# Kullanıcı grafi oluşturuluyor
kullanici_grafi = Graph()

# SnowballStemmer'ı kullan
stemmer = TurkishStemmer()

# Tüm tweetleri saklamak için liste
all_tweets = []

# Ilgi alanı ve kişi sayısını saklamak için sözlük
interest_area_counts = {}
most_common_interest_area = {}

# Anahtar kelimeler ve ilgili kullanıcı listeleri
anahtar_kelimeler = {
    'kültür': ['tiyatro', 'oyun', 'kitap'],
    'eğitim': ['üniversite', 'hukuk', 'fakülte'],
    'siyaset': ['türk', 'yönetim', 'devlet'],
    'spor': ['genç', 'futbol', 'spor'],
    'sanat': ['müzik', 'film', 'albüm'],
    'coğrafya': ['istanbul', 'şehir', 'köy']
}

# Belirtilen bölgedeki ve en çok ilgilenilen alanındaki kullanıcı sayısını takip etmek için sayaç
users_in_specified_region_and_most_common_interest_area_count = 0

# JSON verisindeki her kullanıcı için
for kullanici_verisi in json_veri:
    # Kullanıcı nesnesi oluşturuluyor
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
    
    # Tüm tweetleri bir listeye ekleniyor
    all_tweets.extend(kullanici_verisi['tweets'])

    
    # İlgi alanlarını ve kişi sayısını güncelle
    for ilgi_alani, kelimeler in anahtar_kelimeler.items():
        stop_words = set(stopwords.words('turkish'))  # stop_words'u burada tanımla
        if any(stemmer.stemWord(word) in [stemmer.stemWord(w) for w in word_tokenize(tweet, language='turkish') if w.isalnum() and w.lower() not in stop_words] for tweet in kullanici_verisi['tweets'] for word in kelimeler):
            interest_area_counts[ilgi_alani] = interest_area_counts.get(ilgi_alani, 0) + 1

    # Eğer kullanıcı belirtilen bölgedeyse ve ilgi alanı en çok ilgilenilen alansa, sayacı bir artır
        if kullanici_verisi['region'] == hedef_bolge and kullanici_verisi['username'] == "rpekkan":
            users_in_specified_region_and_most_common_interest_area_count += 1

# Belirtilen bölgedeki ve en çok ilgilenilen alandaki kullanıcı sayısını ekrana yazdır
print(f"\n{hedef_bolge} Bölgesinde ve En Çok İlgilenilen Alandaki Olan Kullanıcı Sayısı: {users_in_specified_region_and_most_common_interest_area_count}")



# Kelimeleri ayıklama ve stopwords'ları kaldırma
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('turkish'))

# Tüm tweetlerden alınan kelimeler
all_words = [word.lower() for tweet in all_tweets for word in word_tokenize(tweet, language='turkish') if word.isalnum() and word.lower() not in stop_words]

# Stemming işlemi
stemmed_words = [stemmer.stemWord(word) for word in all_words]

# Kelime frekansını sayma
#word_freq = Counter(stemmed_words)

# En çok kullanılan 100 kelimeyi alma
#most_common_words = word_freq.most_common(100)

#print("En çok kullanılan 100 kelime:")
#for word, freq in most_common_words:
#    print(f"{word}: {freq}")


# Kullanıcının anahtar kelime seçimini al
anahtar_kelime_secimi = input("Hangi anahtar kelimeye göre kullanıcıları görmek istersiniz? ({}) ".format(', '.join(anahtar_kelimeler.keys())))

# Kullanıcının seçtiği anahtar kelimenin geçerli olup olmadığını kontrol et
if anahtar_kelime_secimi.lower() in anahtar_kelimeler:
    hedef_stems = [stemmer.stemWord(word) for word in anahtar_kelimeler[anahtar_kelime_secimi.lower()]]

    # İlgili kullanıcı listesini bulma
    ilgili_kullanıcılar = [kullanici_verisi for kullanici_verisi in json_veri
                           if any(stemmer.stemWord(word) in hedef_stems for tweet in kullanici_verisi['tweets']
                                  for word in word_tokenize(tweet, language='turkish') if word.isalnum() and word.lower() not in stop_words)]

    # Kullanıcı listesini yazdırma
    print("{} ile ilgilenen kullanıcılar:".format(anahtar_kelime_secimi.capitalize()))
    print([kullanici['username'] for kullanici in ilgili_kullanıcılar])

    # Kullanıcıdan bir kullanıcı adı al
    hedef_kullanici_adi = input("Hangi kullanıcının ilgi alanlarını görmek istersiniz? Kullanıcı adını girin: ")

    # Kullanıcının belirtilen kullanıcı adına ait bilgileri bulma
    hedef_kullanici_verisi = next((k for k in ilgili_kullanıcılar if k['username'] == hedef_kullanici_adi), None)

    if hedef_kullanici_verisi:
        print("{} kullanıcısının ilgi alanları:".format(hedef_kullanici_verisi['username']))
        for ilgi_alani, kelimeler in anahtar_kelimeler.items():
            if any(stemmer.stemWord(word) in [stemmer.stemWord(w) for w in word_tokenize(tweet, language='turkish') if w.isalnum() and w.lower() not in stopwords.words('turkish')] for tweet in hedef_kullanici_verisi['tweets'] for word in kelimeler):
                print("- {}".format(ilgi_alani.capitalize()))
       
        hedef_kullanici = Kullanici(
        hedef_kullanici_verisi['username'],
        hedef_kullanici_verisi['name'],
        hedef_kullanici_verisi['followers_count'],
        hedef_kullanici_verisi['following_count'],
        hedef_kullanici_verisi['language'],
        hedef_kullanici_verisi['region'],
        hedef_kullanici_verisi['tweets'],
        hedef_kullanici_verisi['following'],
        hedef_kullanici_verisi['followers']
    )
        hedef_kullanici.bilgileri_dosyaya_kaydet(f"{hedef_kullanici.username}_bilgileri.txt")

        print(f"Kullanıcı bilgileri {hedef_kullanici.username}_bilgileri.txt dosyasına kaydedildi.")

    else:
        print("Belirtilen kullanıcı adına ait bilgi bulunamadı.")

    # İlgili kullanıcıları ve ilişkileri temsil etmek için bir Graph oluştur
    ilgili_graf = nx.Graph()

    # Ana düğümü ekle
    ilgili_graf.add_node(anahtar_kelime_secimi.capitalize())

    # Kullanıcıları ve ilgili ana düğüme olan ilişkileri ekle
    for kullanici_verisi in ilgili_kullanıcılar:
        ilgili_graf.add_node(kullanici_verisi['username'])
        ilgili_graf.add_edge(anahtar_kelime_secimi.capitalize(), kullanici_verisi['username'])

    # Hash tablosunu oluştur
    hash_tablosu = {}
    for kullanici in ilgili_kullanıcılar:
        ilgi_alanlari = []
        for ilgi_alani, kelimeler in anahtar_kelimeler.items():
            if any(stemmer.stemWord(word) in [stemmer.stemWord(w) for w in word_tokenize(tweet, language='turkish') if w.isalnum() and w.lower() not in stopwords.words('turkish')] for tweet in kullanici['tweets'] for word in kelimeler):
                ilgi_alanlari.append(ilgi_alani.capitalize())
        hash_tablosu[kullanici['username']] = ilgi_alanlari 

    # Adım 1: Kullanıcılar Arasındaki Benzerliği Hesaplayın
    def benzerlik_hesapla(kullanici1, kullanici2):
        set1 = set(hash_tablosu.get(kullanici1, []))
        set2 = set(hash_tablosu.get(kullanici2, []))
        kesisim = len(set1.intersection(set2))
        birlesim = len(set1.union(set2))
        benzerlik = kesisim / birlesim if birlesim != 0 else 0
        return benzerlik

    # Adım 2: Ağırlıklı Bir Graf Oluşturun
    agirlikli_graf = nx.Graph()
    for kullanici1 in ilgili_kullanıcılar:
        for kullanici2 in ilgili_kullanıcılar:
            if kullanici1 != kullanici2:
                benzerlik = benzerlik_hesapla(kullanici1['username'], kullanici2['username'])
                agirlikli_graf.add_edge(kullanici1['username'], kullanici2['username'], weight=benzerlik)

    # Adım 3: Minimum Geren Ağacı Bulun
    mst = nx.minimum_spanning_tree(agirlikli_graf)

    # Adım 4: Minimum Geren Ağacını Görselleştirin
    plt.figure(figsize=(10, 8))
    pos_mst = nx.spring_layout(mst)
    kenar_etiketleri = {(u, v): f"{d['weight']:.2f}" for u, v, d in mst.edges(data=True)}
    nx.draw(mst, pos_mst, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=kenar_etiketleri)
    plt.title('İlgi Alanlarına Göre Benzer Kullanıcıların Minimum Geren Ağacı')
    plt.show()

    # Hash tablosunu yazdır
    print("\nHash Tablosu:")
    for kullanici_adi, ilgi_alanlari in hash_tablosu.items():
        print("{}: {}".format(kullanici_adi, ', '.join(ilgi_alanlari)))

    # Grafi çiz ve Hash tablosunu göster
    plt.figure(figsize=(12, 5))  # Boyutu ayarla

    # Grafiği solda konumlandır
    plt.subplot(1, 2, 1)
    pos = nx.spring_layout(ilgili_graf)
    nx.draw(ilgili_graf, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    plt.title('İlgi Alanı Grafiği')

    # Hash tablosu subplot'u sağda konumlandır
    plt.subplot(1, 2, 2)
    hash_tablo_verisi = {ilgi_alani.capitalize(): kelimeler for ilgi_alani, kelimeler in anahtar_kelimeler.items()}
    tablo_verisi = [['İlgi Alanı', 'Anahtar Kelimeler']]
    for ilgi_alani, kelimeler in hash_tablo_verisi.items():
        tablo_verisi.append([ilgi_alani, ', '.join(kelimeler)])

    tablo = plt.table(cellText=tablo_verisi, loc='center', cellLoc='center', colLabels=None, cellColours=None)
    tablo.auto_set_font_size(False)
    tablo.set_fontsize(8)
    tablo.scale(1, 1.2)  # Tablo boyutunu ayarla

    plt.title('İlgi Alanı Hash Tablosu')

    # Hem Grafiği hem de Hash Tablosunu göster
    plt.show()
else:
    print("Geçersiz anahtar kelime. Lütfen ({}) anahtar kelimelerinden birini seçin.".format(', '.join(anahtar_kelimeler.keys())))

# Kullanıcıdan iki kullanıcı adı al
kullanici1 = input("Birinci kullanıcının adını girin: ")
kullanici2 = input("İkinci kullanıcının adını girin: ")

# İki kullanıcının ilgi alanlarını bulma
ilgi_alanlari_kullanici1 = set(hash_tablosu.get(kullanici1, []))
ilgi_alanlari_kullanici2 = set(hash_tablosu.get(kullanici2, []))

# Ortak ilgi alanlarını bulma
ortak_ilgi_alanlari = ilgi_alanlari_kullanici1.intersection(ilgi_alanlari_kullanici2)

# Kullanıcıya sonuçları yazdırma
if ortak_ilgi_alanlari:
    print(f"\n{kullanici1} ve {kullanici2} kullanıcılarının ortak ilgi alanları:")
    for ilgi_alani in ortak_ilgi_alanlari:
        print(f"- {ilgi_alani}")
else:
    print(f"\n{kullanici1} ve {kullanici2} kullanıcılarının ortak ilgi alanı bulunamadı.")


#TÜM KULLANICILARI EDGE VE NODE ŞEKLİNDE GÖSTERİR
 #İlgili kullanıcıları ve ilişkileri temsil etmek için bir Graph oluştur
ilgili_graf = nx.Graph()

 #Kullanıcıları ve ilgili ana düğüme olan ilişkileri ekle
for kullanici_verisi in ilgili_kullanıcılar:
    ilgili_graf.add_node(kullanici_verisi['username'])
    ilgili_graf.add_edges_from([(kullanici_verisi['username'], takipci) for takipci in kullanici_verisi['followers']])
    ilgili_graf.add_edges_from([(kullanici_verisi['username'], takip_edilen) for takip_edilen in kullanici_verisi['following']])

#İkinci grafi çiz
pos_ilgili_graf = nx.spring_layout(ilgili_graf)
nx.draw(ilgili_graf, pos_ilgili_graf, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
plt.title('Takipçi-Takip Edilen İlişkisi Grafiği')

#plt.show()
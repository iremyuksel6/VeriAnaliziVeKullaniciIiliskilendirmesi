import json

class Kullanici:
    def _init_(self, username, name, followers_count, following_count, language, region, tweets, following, followers):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers

    def _str_(self):
        return f"{self.name} ({self.username}) - Takipçi: {self.followers_count}, Takip Edilen: {self.following_count}"

def json_dosyasindan_veri_oku(json_dosya_adı):
    with open(json_dosya_adı, 'r', encoding='utf-8') as dosya:
        veri = json.load(dosya)
    return veri

def dfs_search_tweets(user, keywords, visited_tweets, current_tweet):
    if current_tweet in visited_tweets:
        return
    visited_tweets.add(current_tweet)

    for keyword in keywords:
        if keyword.lower() in current_tweet.lower():
            print(f"Anahtar kelime bulundu: '{keyword}' - Tweet: {current_tweet}")
            break

    for tweet in user.tweets:
        if tweet != current_tweet:
            dfs_search_tweets(user, keywords, visited_tweets, tweet)

def list_tweets_with_keywords(user, keywords):
    visited_tweets = set()
    for tweet in user.tweets:
        dfs_search_tweets(user, keywords, visited_tweets, tweet)

# Örnek kullanım
json_data = json_dosyasindan_veri_oku("besyuzdata.json")

# JSON listesindeki her bir kullanıcı için Kullanici nesnesi oluşturun
kullanicilar = [Kullanici(**data) for data in json_data]

# Anahtar kelimeler
anahtar_kelimeler = ["üniversite", "tarih", "sanat"]

# Her bir kullanıcı için anahtar kelimeleri içeren tweetleri listeleyin
for kullanici in kullanicilar:
    list_tweets_with_keywords(kullanici, anahtar_kelimeler)
# Kullanıcı Grafiği Analizi – DFS Algoritması

Bu proje, kullanıcılar arasındaki takipçi / takip edilen ilişkilerini
**graf yapısı** üzerinde modelleyerek **Depth First Search (DFS)** algoritması
ile analiz etmeyi amaçlamaktadır.

Kullanıcı verileri JSON formatında alınmakta, her kullanıcı bir düğüm (node),
kullanıcılar arasındaki ilişkiler ise kenar (edge) olarak temsil edilmektedir.
Oluşturulan graf üzerinde DFS algoritması uygulanarak bağlantılar
derinlemesine incelenmektedir.

---

## 📌 Projenin Amacı

- Kullanıcılar arası ilişkileri graf teorisi kullanarak modellemek  
- DFS algoritmasının gerçek bir veri seti üzerinde nasıl çalıştığını göstermek  
- Graf yapıları ve arama algoritmaları konusunda pratik kazanmak  

---

## 📂 Dosya Yapısı

- **main.py**  
  Programın çalıştırıldığı ana dosyadır. Diğer modülleri çağırarak
  uygulamanın akışını yönetir.

- **dfs_algorithm.py**  
  Depth First Search (DFS) algoritmasının uygulandığı dosyadır.
  Graf üzerinde derinlik öncelikli arama işlemleri burada gerçekleştirilir.

- **kullanici_grafi.py**  
  Kullanıcıların ve aralarındaki ilişkilerin graf yapısı şeklinde
  modellenmesini sağlayan sınıf ve fonksiyonları içerir.

- **prolab1_3.py**  
  Proje kapsamında ihtiyaç duyulan yardımcı fonksiyonları ve
  ek işlemleri barındırır.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- **json**  
  Kullanıcı verilerinin JSON formatında okunması ve işlenmesi için kullanılmıştır.
- **networkx**  
  Kullanıcı ilişkilerinin graf yapısı olarak modellenmesi için kullanılmıştır.
- **matplotlib.pyplot**  
  Oluşturulan grafın görselleştirilmesi amacıyla kullanılmıştır.

---

## 🧠 Kullanılan Algoritma

- **Depth First Search (DFS)**  
  Graf üzerindeki düğümlerin derinlemesine gezilmesini sağlayan
  arama algoritmasıdır. Kullanıcılar arasındaki bağlantıların
  analiz edilmesinde kullanılmıştır.

---

## ▶️ Çalıştırma Talimatları

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install networkx matplotlib

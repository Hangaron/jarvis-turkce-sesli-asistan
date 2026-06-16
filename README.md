# 🌐 J.A.R.V.I.S. Core Dashboard // Hangaronn OS

**J.A.R.V.I.S. Core Dashboard**, tamamen açık kaynak kodlu olarak geliştirilen, HTML5, CSS3 ve JavaScript teknolojileri üzerine inşa edilmiş siberpunk temalı bir yapay zeka asistanıdır.

Google Gemini entegrasyonu, sesli komut desteği ve isteğe bağlı Python Desktop Bridge sistemi sayesinde hem yapay zeka sohbetleri gerçekleştirebilir hem de bilgisayarınızdaki uygulamaları sesli komutlarla kontrol edebilirsiniz.

Bu proje, modern fütüristik kullanıcı arayüzleri ve yapay zeka teknolojilerini bir araya getirerek herkesin geliştirebileceği açık kaynaklı bir J.A.R.V.I.S. deneyimi sunmayı amaçlamaktadır.

> Geliştirici Notu: Bu proje, Emirhan "Hangaronn" Vardar tarafından açık kaynak topluluğuna katkı sağlamak amacıyla geliştirilmiştir. Tasarım dili olarak neon turuncu ve siyah renk paleti, Arc Reactor estetiği ve fütüristik kontrol paneli konsepti benimsenmiştir.

---

# ⚡ Özellikler

## 🟠 Siberpunk Kullanıcı Arayüzü

* Neon turuncu ve siyah tema
* Arc Reactor merkez tasarımı
* Akıcı animasyonlar
* Holografik efektler
* Gerçek zamanlı durum göstergeleri
* Modern kontrol paneli görünümü

## 🎙️ Sesli Komut Sistemi

* Google Web Speech API desteği
* Türkçe ses tanıma
* Doğal dil komut algılama
* Mikrofon destekli kullanım
* Sesli geri bildirim sistemi

## 🤖 Google Gemini Yapay Zeka Entegrasyonu

* Gemini 2.5 desteği
* Akıllı soru-cevap sistemi
* Hikaye oluşturma
* Bilgi sorgulama
* Sohbet desteği
* Sesli ve yazılı yanıtlar

## 🖥️ Desktop Bridge Sistemi

İsteğe bağlı Python Bridge desteği sayesinde:

* Yerel uygulamaları açabilir
* İşletim sistemi komutları çalıştırabilir
* Tarayıcı ile masaüstü arasında bağlantı kurabilir
* Yeni uygulamalar kolayca eklenebilir

## 📈 Gerçek Zamanlı Sistem Telemetrisi

* Sistem durum logları
* Bağlantı izleme
* Mikrofon aktivitesi
* Yapay zeka durum göstergeleri
* Terminal tarzı canlı veri akışı

---

# 🛠️ Kullanılan Teknolojiler

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)

### Yapay Zeka

* Google Gemini API

### Ses Teknolojileri

* Web Speech API
* Speech Synthesis API

### Masaüstü Entegrasyonu

* Python
* Flask
* Localhost API Bridge

---

# 🚀 Kurulum

## 1️⃣ Projeyi İndirin

```bash
git clone https://github.com/Hangaron/jarvis-turkce-sesli-asistan.git
```

veya ZIP olarak indirip çıkartın.

---

## 2️⃣ Dashboard'u Açın

```text
jarvis_dashboard.html
```

dosyasını Google Chrome veya Chromium tabanlı bir tarayıcı ile açın.

Kurulum gerektirmez.

---

## 3️⃣ Gemini API Anahtarını Girin

1. Google AI Studio üzerinden API anahtarı oluşturun.
2. Dashboard üzerindeki GEMINI API KEY alanına yapıştırın.
3. Kaydet butonuna basın.

> API anahtarları yalnızca kullanıcının kendi tarayıcısındaki Local Storage alanında saklanır.

---

## 4️⃣ Desktop Bridge'i Başlatın (Opsiyonel)

Bilgisayardaki uygulamaları kontrol etmek istiyorsanız:

```bash
python jarvis_bridge.py
```

Varsayılan bağlantı adresi:

```text
http://localhost:8080
```

Dashboard üzerinden "KÖPRÜYÜ YENİDEN TARA" butonuna bastığınızda sistem otomatik olarak bağlantıyı algılar.

---

# 🗣️ Desteklenen Sesli Komutlar

| Komut                 | İşlem                      |
| --------------------- | -------------------------- |
| Not Defterini Aç      | Notepad Başlatılır         |
| Chrome'u Aç           | Google Chrome Açılır       |
| Tarayıcıyı Aç         | Varsayılan Tarayıcı Açılır |
| Hesap Makinesini Aç   | Calculator Başlatılır      |
| Paint Aç              | Microsoft Paint Açılır     |
| Çizim Programını Aç   | Paint Açılır               |
| Dosya Yöneticisini Aç | Dosya Gezgini Açılır       |

---

# 💬 Yapay Zeka Örnekleri

```text
Yapay zeka nedir?
```

```text
Bana kısa bir hikaye anlat.
```

```text
Python nasıl öğrenilir?
```

```text
Bugün hava nasıl?
```

Bu tür sorular doğrudan Gemini API üzerinden işlenir ve J.A.R.V.I.S. tarafından yanıtlanır.

---

# ⚙️ Yeni Uygulama Ekleme

## Python Bridge Tarafı

```python
elif app_name == "spotify":
    subprocess.Popen(["spotify.exe"])
    return "Spotify başlatılıyor."
```

## Frontend Tarafı

```javascript
else if (
    text.includes("spotify") ||
    text.includes("müzik aç")
){
    targetApp = "spotify";
}
```

---

# 📂 Proje Yapısı

```text
jarvis-turkce-sesli-asistan/

├── jarvis_dashboard.html
├── jarvis_bridge.py
├── README.md
└── LICENSE
```

---

# 🔒 Güvenlik

* Açık kaynak kodludur.
* Kaynak kodları incelenebilir.
* API anahtarları yalnızca kullanıcı tarafında tutulur.
* Localhost bağlantısı kullanılır.
* Veriler üçüncü taraf sunucularda depolanmaz.
* Kullanıcı gizliliği önceliklidir.

---

# 📄 Lisans

Bu proje MIT License altında lisanslanmıştır.

İstediğiniz gibi:

* Kullanabilir
* Geliştirebilir
* Değiştirebilir
* Dağıtabilir
* Ticari projelerde kullanabilirsiniz

---

# 🌐 GitHub Repository

Repository Adresi:

https://github.com/Hangaron/jarvis-turkce-sesli-asistan

Projeyi beğendiyseniz:

⭐ Star vermeyi

🍴 Fork'lamayı

🐛 Hata bildirmeyi

🚀 Katkıda bulunmayı unutmayın.

---

# 👨‍💻 Geliştirici

**Emirhan "Hangaronn" Vardar**

Bilgisayar Destekli Tasarım ve Animasyon Öğrencisi

Yazılım Geliştirici • İçerik Üreticisi • Açık Kaynak Destekçisi

GitHub: @Hangaronn

---

# J.A.R.V.I.S. Core Dashboard // Hangaronn OS

### Open Source Turkish Voice Assistant

**Technology. Intelligence. Control.**

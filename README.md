# 🌐 J.A.R.V.I.S. Core Dashboard // Hangaronn OS

**J.A.R.V.I.S. Core Dashboard**, tamamen tarayıcı tabanlı çalışan (HTML5, CSS3 ve JavaScript), Google Gemini API entegrasyonuna sahip ve yerel bir Python Bridge sayesinde bilgisayarınızdaki uygulamaları sesli komutlarla kontrol edebilen siberpunk temalı açık kaynaklı bir yapay zeka asistanıdır.

> Geliştirici Notu: Bu proje, Emirhan "Hangaronn" Vardar tarafından açık kaynak topluluğuna katkı sağlamak amacıyla geliştirilmiştir. Tasarım dili olarak turuncu ve siyah neon tonları, modern Arc Reactor estetiği ve fütüristik kontrol paneli konsepti benimsenmiştir.

---

# ⚡ Özellikler

## 🟠 Cyberpunk Kullanıcı Arayüzü

* Neon turuncu ve siyah tema
* Arc Reactor merkez tasarımı
* Akıcı animasyonlar ve holografik efektler
* Gerçek zamanlı durum göstergeleri

## 🎙️ Sesli Komut Sistemi

* Google Web Speech API desteği
* Türkçe ses tanıma
* Doğal dil komut algılama
* Mikrofon destekli etkileşim

## 🤖 Gemini 2.5 Yapay Zeka Entegrasyonu

* Google Gemini 2.5 desteği
* Akıllı soru-cevap sistemi
* Hikaye oluşturma
* Bilgi sorgulama
* Sesli ve yazılı yanıtlar

## 🖥️ Python Desktop Bridge

* Tarayıcı ile işletim sistemi arasında bağlantı
* Yerel uygulamaları açabilme
* Komut çalıştırabilme
* Genişletilebilir uygulama desteği

## 📈 Gerçek Zamanlı Telemetri

* Sistem durum logları
* Bağlantı izleme
* Ses aktivite göstergeleri
* Terminal tarzı veri akışı

---

# 🛠️ Kurulum

## 1️⃣ Python Bridge'i Başlatın

Masaüstü uygulamalarını kontrol edebilmek için öncelikle Python köprüsünü çalıştırın:

```bash
python jarvis_bridge.py
```

Varsayılan olarak sunucu aşağıdaki adreste çalışacaktır:

```text
http://localhost:8080
```

---

## 2️⃣ Arayüzü Açın

`jarvis_dashboard.html` dosyasını Google Chrome veya Chromium tabanlı bir tarayıcı ile açın.

Ardından:

1. Sol panelde bulunan **"KÖPRÜYÜ YENİDEN TARA"** butonuna basın.
2. Durum göstergesinin **CONNECTED** olarak değiştiğini doğrulayın.

---

## 3️⃣ Gemini API Anahtarını Tanımlayın

1. Google AI Studio üzerinden bir API anahtarı oluşturun.
2. Sol paneldeki **GEMINI API KEY** alanına yapıştırın.
3. **KAYDET** butonuna basın.
4. **ÖNEMLİ NOT** : Gemini Api'larda Limit Olabiliyor, Ve Jarvis Bunu Algılayabiliyor Limitsiz Kullanım Önerilir.

> API anahtarınız yalnızca tarayıcınızın Local Storage alanında saklanır ve üçüncü taraf sunuculara gönderilmez.

---

# 🗣️ Desteklenen Sesli Komutlar

| Komut                 | İşlem                      |
| --------------------- | -------------------------- |
| Not defterini aç      | Notepad başlatılır         |
| Chrome'u aç           | Google Chrome açılır       |
| Tarayıcıyı aç         | Varsayılan tarayıcı açılır |
| Hesap makinesini aç   | Calculator çalıştırılır    |
| Paint aç              | Microsoft Paint açılır     |
| Çizim programını aç   | Paint çalıştırılır         |
| Dosya yöneticisini aç | Dosya Gezgini açılır       |

### Yapay Zeka Soruları

Aşağıdaki gibi herhangi bir soru sorabilirsiniz:

```text
Yapay zeka nedir?
```

```text
Bana kısa bir hikaye anlat.
```

```text
Bugün nasıl hissediyorsun?
```

Bu tür sorgular doğrudan Gemini API'ye gönderilir ve yapay zeka tarafından yanıtlanır.

---

# ⚙️ Yeni Uygulama Ekleme

Yeni uygulamalar eklemek oldukça kolaydır.

## Python Bridge Tarafı

`jarvis_bridge.py` içerisine yeni bir uygulama tanımlayın:

```python
elif app_name == "spotify":
    if is_win:
        subprocess.Popen(["spotify.exe"])
    return "Spotify başlatılıyor, Efendim."
```

## Frontend Tarafı

`checkAndExecuteLocalCommand()` fonksiyonuna yeni tetikleyiciler ekleyin:

```javascript
else if (
    text.includes("spotify") ||
    text.includes("müzik aç")
) {
    targetApp = "spotify";
}
```

---

# 📂 Proje Yapısı

```text
 jarvis_dashboard.html
jarvis_bridge.py
 README.md
```

---

# 🔒 Güvenlik

* API anahtarları Local Storage üzerinde tutulur.
* Uygulama yalnızca localhost bağlantısı kullanır.
* Veriler harici sunuculara gönderilmez.
* Açık kaynak kodlu ve denetlenebilirdir.

---

# 📄 Lisans

Bu proje **MIT License** altında lisanslanmıştır.

İstediğiniz gibi kullanabilir, geliştirebilir, değiştirebilir ve dağıtabilirsiniz.

---

# 👨‍💻 Geliştirici

**Emirhan "Hangaronn" Vardar**

Bilgisayar Destekli Tasarım ve Animasyon Öğrencisi
Yazılım Geliştirici • İçerik Üreticisi • Açık Kaynak Destekçisi

GitHub: @Hangaronn

---

## ⭐ Destek Ol

Projeyi beğendiyseniz:

⭐ Star vermeyi
🍴 Fork'lamayı
🐛 Hata bildirmeyi
🚀 Katkıda bulunmayı unutmayın.

---

**J.A.R.V.I.S. Core Dashboard // Hangaronn OS**

*"Technology. Intelligence. Control."*

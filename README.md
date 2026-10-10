# 🧠 Demans & Alzheimer Erken Teşhis ve Bilişsel Takip Sistemi

> **Bitirme Projesi (Graduation Project)**  
> **Geliştirici:** Sude Kazan  
> **Repository:** [sudekazan/demans_on_teshis](https://github.com/sudekazan/demans_on_teshis.git)

---

## 🎯 Projenin Amacı ve Kapsamı

Bu projenin temel amacı; Demans ve Alzheimer riski taşıyan bireylerin bilişsel becerilerini (hafıza, dikkat, tepki süresi) düzenli dijital testler ve mini oyunlar aracılığıyla ölçmek, zaman içindeki performans düşüş trendlerini (**cognitive decline rate**) yapay zeka ile erken aşamada tespit etmek, kişiselleştirilmiş egzersizler ve risk takibi sunmaktır.

---

## ⭐ Projenin Özgün Yanları

1. **Trend Odaklı Anomali Tespiti:** Anlık tek bir test skoru yerine zaman serisi analizi (*time-series analysis*) ile bireyin kendi geçmiş performansına kıyasla bilişsel düşüş trendini yapay zeka (ML) ile tespit eder.
2. **Kişiselleştirilmiş ve Adaptif Egzersiz:** Bireyin anlık başarımına ve yorgunluğuna göre zorluk seviyesini otomatik ayarlayan algoritmik yapı.
3. **KVKK / Veri Gizliliği Uyumu:** Yüz fotoğrafı veya biyometrik veri kullanmak yerine, anonimleştirilmiş UUID takibi ve nesne hatırlama testleri ile sıfır kişisel veri ihlali hedefler.
4. **Birey İçi Değişkenlik (IIV) Metriği:** Tepki sürelerinin standart sapmasını ölçerek nörolojik tutarsızlıkları ve erken evre dikkat dağınıklığını analiz eder.
5. **Yapay Zeka + LLM Öneri Motoru:** Anomali tespit modeli çıktısını Google Gemini API ile işleyerek kullanıcıya özel, motive edici ve anlaşılır sağlık tavsiyeleri sunar.

---

## 🛠️ Teknoloji Mimarisi

```
demans_on_teshis/
├── mobile/          # Flutter Cross-Platform Mobil Uygulama (Stroop, Hafıza, Digit Span)
├── backend/         # Node.js / Express.js REST API & MongoDB (Anonim Veri & Skor Takibi)
├── ai_service/      # Python (FastAPI / Scikit-Learn / XGBoost & Gemini API Entegrasyonu)
└── docs/            # Sistem Mimarisi, Şemalar ve Dokümantasyon
```

- **Mobil Uygulama:** Flutter (Dart) — Yüksek kontrastlı erişilebilir UI, `Stopwatch` ile milisaniye hassasiyetinde tepki süresi ölçümü, `fl_chart` performans grafikleri.
- **Backend Servisi:** Node.js, Express.js, MongoDB — Anonim skor takibi, kullanıcı oturum yönetimi, güvenli veri senkronizasyonu.
- **Yapay Zeka Servisi:** Python (FastAPI, Scikit-Learn, XGBoost, Pandas) — Zaman serisi trend ve anomali tespiti + Google Gemini API ile kişiselleştirilmiş öneri üretimi.

---

## 🧪 Bilişsel Test Metodolojileri

1. **Stroop Testi:** Dikkat, seçici odaklanma ve ketleme (inhibition) yeteneğini ölçer.
2. **Görsel Hafıza (Visual Memory):** Desen ve nesne hatırlama becerilerini test eder.
3. **Sayı Dizisi (Digit Span Test):** Çalışma belleği (working memory) ve kısa süreli hafıza kapasitesini ölçer.

---

## 📊 Başarı Kriterleri

- ✅ **3 Mini Oyun:** Milisaniye (ms) hassasiyetinde tepki süresi ölçebilen 3 bilişsel oyun.
- ✅ **%85+ Doğruluk:** Yapay zeka trend analiz modelinin en az %85 doğrulukla performans düşüşlerini algılaması.
- ✅ **Görsel Anlaşılırlık:** Mobil uygulamada anlaşılır çizgi grafikleri ile haftalık/aylık gelişim takibi.
- ✅ **Sıfır KVKK İhlali:** Anonimleştirilmiş veri kayıt mimarisi.

---

## 🚀 Kurulum ve Çalıştırma

### Mobil (Flutter)
```bash
cd mobile
flutter pub get
flutter run
```

### Backend (Node.js)
```bash
cd backend
npm install
npm run dev
```

### Yapay Zeka Servisi (Python)
```bash
cd ai_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 📄 Lisans
Bu proje bitirme çalışması kapsamında geliştirilmektedir. Tüm hakları saklıdır.

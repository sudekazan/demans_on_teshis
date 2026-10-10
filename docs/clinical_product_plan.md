# 🧠 Akademik Literatür Tabanlı Bilişsel Takip & Erken Uyarı Sistemi Planı

> **Proje Adı:** Demans ve Alzheimer Erken Teşhis ve Bilişsel Takip Sistemi  
> **Yaklaşım:** Zaman Serisi Analizi (Longitudinal Tracking), Birey İçi Değişkenlik (IIV) ve Ekolojik Anlık Değerlendirme (EMA)  
> **Dokümantasyon Tarihi:** 2026-10-10

---

## 1. Literatür Tabanlı Ürün Felsefesi

Geleneksel klinik yaklaşımlar tek bir anda yapılan 10 soruluk testlere (MMSE/MoCA) dayanır. Ancak modern nöroloji literatürü, bu testlerin **yalancı pozitiflik (False Positive)** oranının yüksek olduğunu ve günlük yorgunluk/stres gibi faktörlerden etkilendiğini göstermektedir.

Geliştirdiğimiz uygulama şu **3 Bilimsel Sütun** üzerine inşa edilmiştir:

```
+-------------------------------------------------------------------------+
|                        3 BİLİMSEL SÜTUN                                 |
+-------------------------------------------------------------------------+
| 1. Bireysel Referans Çizgisi  | 2. Zaman Serisi Eğimi (Slope) | 3. IIV   |
| (Personal Baseline)           | (Decline Trajectory)          | Metriği  |
| Toplum ortalaması yerine      | Tek skor yerine 30-90 günlük  | Tepki    |
| bireyin kendi normali         | gerileme hızı                 | tutarlılığı|
+-------------------------------------------------------------------------+
```

---

## 2. Mobil Uygulama Kullanıcı Deneyimi (UX) & Klinik Akış Planı

### A. Aşama 1: 14 Günlük Referans Çizgisi (Baseline Phase)
* **Amaç:** Kullanıcının ilk 14 günlük test sonuçları "hastalık teşhisi" için kullanılmaz. Kullanıcının reaksiyon hızı, hafıza kapasitesi ve odaklanma süresinin **kişisel referans noktası (baseline)** oluşturulur.
* **UX Göstergesi:** *"Kişisel Bilişsel Profiliniz Oluşturuluyor (%60 Tamamlandı)"*.

### B. Aşama 2: Ekolojik Anlık Değerlendirme (EMA - Mikro Testler)
* **Amaç:** Kullanıcıyı yormadan, haftada 3 gün, günün farklı saatlerinde **2-3 dakikalık mikro-oyunlar** sunulur.
* **Test Bataryası:**
  1. **Stroop Testi:** Seçici dikkat, renk-mürekkep ketlemesi.
  2. **Görsel Uzamsal Hafıza:** Hipokampal hafıza ve desen hatırlama.
  3. **Sayı Dizisi (Digit Span):** Prefrontal korteks çalışma belleği.
  4. **Nesne Hatırlama (Object Recall):** Semantik hafıza.

### C. Aşama 3: Çevresel & Bağlamsal Normalizasyon (Contextual Pre-Test)
* **Amaç:** Test başlamadan önce 3 saniyelik 2 mikro-soru sorulur:
  - *"Dün gece uykunuzu alabildiniz mi?"* (1 - 5)
  - *"Şu an yorgun hissediyor musunuz?"* (1 - 5)
* **ML Etkisi:** Yapay zeka modeli yorgun olunan günlerdeki performans düşüşünü hastalık belirtisi olarak değil, **yorgunluk etkisi** olarak etiketler (False Positive engellenir).

---

## 3. Yapay Zeka & Analiz Modeli Mimarisi (Python Backend)

```
                       [Mobil Test Verisi]
                                |
                     (RT, Accuracy, IIV, Context)
                                v
                +-------------------------------+
                |   Bağlamsal Normalizasyon    |
                |   (Yorgunluk/Saat Düzeltmesi) |
                +---------------+---------------+
                                |
                                v
                +-------------------------------+
                | Zaman Serisi Eğim Analizi     |
                | (Lineer Regresyon Slope m)    |
                +---------------+---------------+
                                |
                                v
                +-------------------------------+
                | Anomali Tespiti               |
                | (Isolation Forest / XGBoost)  |
                +---------------+---------------+
                                |
                                v
                +-------------------------------+
                |  Google Gemini LLM Raporu     |
                | (Yapıcı, Pozitif Tavsiyeler)  |
                +-------------------------------+
```

### Hesaplanan Matematiksel Parametreler:
1. **Mean Reaction Time ($RT_{mean}$):** Milisaniye cinsinden ortalama yanıt süresi.
2. **Intra-Individual Variability ($IIV = \sigma_{RT}$):** Tepki sürelerinin standart sapması. (Yüksek IIV = Nörolojik yorulma/dikkat dağınıklığı).
3. **Decline Slope ($m$):** $m = \frac{\Delta \text{Skor}}{\Delta t}$. Negatif eğim bilişsel gerilemeyi gösterir.

---

## 4. Kullanıcı & Bakıcı (Caregiver) Raporlama Modeli

### A. Hasta/Kullanıcı Ekranı (Non-Alarmist & Motive Edici)
* Korkutucu yüzdeler veya tıbbi teşhis terimleri yer almaz.
* **Terimler:** *"Zihin Tazeliği Skoru: Yüksek"*, *"Dikkat Odaklanması: Stabil"*.
* Gemini AI tarafından üretilen günlük 3 yapıcı yaşam önerisi.

### B. Bakıcı / Doktor Rapor Ekranı (Klinik PDF İhracı)
* Nörolog veya hasta yakını için hazırlanan özel klinik özet.
* **İçerik:**
  - 30 / 60 / 90 Günlük Tepki Süresi Trend Çizgisi.
  - IIV Değişim Grafiği (Tutarlılık Eğrisi).
  - Test bazlı performans dağılımı.
  - PDF indir / Doktorla Paylaş butonu.

---

## 5. Adım Adım Geliştirme Yol Haritası (Roadmap)

### 📌 Adım 1: Bağlamsal Anket & Referans Mantığının Eklemesi (Gelecek Adım)
- Mobil uygulamaya test öncesi 2 soruluk mikro-anket (Uyku/Yorgunluk) eklenmesi.
- 14 günlük Baseline ilerleme çubuğunun oluşturulması.

### 📌 Adım 2: Bakıcı / Doktor PDF Raporu Oluşturucu
- Flutter uygulamasında veya Node.js tarafında PDF rapor çıktısı alan modülün kodlanması.

### 📌 Adım 3: Sesli Rehber & Erişilebilirlik (TTS Entegrasyonu)
- Yaşlı bireyler için kuralları sesli okuyan Text-to-Speech entegrasyonu.

### 📌 Adım 4: Akıllı Saat & Sağlık Verisi Entegrasyonu (Passive Biomarkers)
- Apple HealthKit (iOS) ve Google Health Connect (Android) entegrasyonu (`health` paketi).
- Uyku Süresi (REM/Derin) ve HRV (Kalp Atım Değişkenliği) verilerinin otomatik çekilmesi.

---

## 6. Akıllı Saat & Pasif Dijital Biyobölteç (Passive Biomarkers) Mimarisi

Sistemimiz iki tür biyobölteçi birleştirerek **Çoklu Modlu (Multi-Modal) Yapay Zeka Analizi** gerçekleştirir:

```
+-------------------------------------------------------------------------+
|                  ÇOKLU MODLU (MULTI-MODAL) VERİ AKIŞI                   |
+-------------------------------------------------------------------------+
|  AKTİF BİYOBÖLTEÇLER (Oyunlar)     |  PASİF BİYOBÖLTEÇLER (Akıllı Saat)  |
|  - Milisaniye Tepki Süresi (RT)    |  - Derin & REM Uyku Süresi          |
|  - Birey İçi Değişkenlik (IIV)     |  - Kalp Atım Değişkenliği (HRV)     |
|  - Doğruluk Oranı (Accuracy)       |  - Günlük Fiziksel Aktivite         |
+------------------------------------+------------------------------------+
                                  |
                                  v
                +------------------------------------+
                |  YAPAY ZEKA BAĞLAM NORMALİZASYONU |
                |  (Fizyolojik Stres vs Demans)      |
                +------------------------------------+
```

### Klinik Faydası:
1. **Öz-Bildirim Sapmasını Engeller:** Yaşlı bireyin uyku kalitesini yanlış hatırlama riskini ortadan kaldırır.
2. **Fizyolojik Stres Düzeltmesi:** Düşük HRV ve yetersiz uyku günlerinde düşen test skorları anomali/hastalık olarak etiketlenmez (Yalancı Pozitiflik engellenir).


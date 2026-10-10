# 📐 Sistem Mimarisi ve Teknik Dokümantasyon

## 1. Genel Sistem Mimarisi

```
+-------------------------------------------------------------+
|                      FLUTTER MOBILE APP                     |
|  - Stroop Test Game                                         |
|  - Visual Memory Game                                       |
|  - Digit Span Game                                          |
|  - Performance Charts (fl_chart)                            |
|  - Stopwatch (ms reaction time precision)                   |
+------------------------------+------------------------------+
                               |
                        HTTP / REST API
                               v
+-------------------------------------------------------------+
|                     NODE.JS BACKEND API                     |
|  - Express.js Router                                        |
|  - User Anonymization & Auth (JWT/UUID)                    |
|  - Session Score Controller                                 |
|  - MongoDB / Firestore Connection                           |
+------------------------------+------------------------------+
                               |
                    Async Internal Microservice
                               v
+-------------------------------------------------------------+
|                   PYTHON AI & LLM SERVICE                   |
|  - Trend Analysis (Time-Series Regression / Slope)          |
|  - Anomaly Detection (Isolation Forest / XGBoost)           |
|  - IIV Calculation (Intra-Individual Variability - StdDev)   |
|  - Google Gemini API (Personalized Health Recommendations) |
+-------------------------------------------------------------+
```

---

## 2. Bilişsel Metrikler ve Ölçüm Yöntemleri

### A. Tepki Süresi ve Doğruluk
- **Reaction Time (RT):** Her uyarana verilen yanıt süresi (milisaniye).
- **Accuracy Rate (ACC):** Doğru verilen yanıtların oranı ($0.0 - 1.0$).
- **Intra-Individual Variability (IIV):** Test seansı içindeki tepki sürelerinin standart sapması ($\sigma_{RT}$).

### B. Zaman Serisi Düşüş Oranı (Cognitive Decline Rate - CDR)
Bir kullanıcının $n$ günlük geçmiş skorları $S = [s_1, s_2, ..., s_n]$ zaman serisi olarak modellenir.
Lineer trend eğimi ($m$):
$$m = \frac{\sum (t_i - \bar{t})(s_i - \bar{s})}{\sum (t_i - \bar{t})^2}$$

Eğer eğim $m < -\theta$ (negatif eşik değeri) ise ve anomali tespiti (Isolation Forest) uyarı veriyorsa, kullanıcı için **düşüş uyarısı** tetiklenir.

---

## 3. KVKK ve Anonimleştirme Protokolü

1. Hiçbir ad, soyad, T.C. Kimlik veya yüz fotoğrafı saklanmaz.
2. Her kullanıcıya cihaz ilk açıldığında rastgele üretilen `UUIDv4` atanır.
3. Sunucuya gönderilen veri paketi yalnızca `user_id`, `age_group`, `test_type` ve `metrics` içerir.

---

## 4. Veritabanı Şeması (JSON / MongoDB)

### Users Collection
```json
{
  "_id": "ObjectId",
  "uuid": "anon_550e8400-e29b-41d4-a716-446655440000",
  "age_group": "65-75",
  "created_at": "2026-10-10T22:40:00Z",
  "baseline": {
    "stroop_mean_rt": 680,
    "memory_accuracy": 0.88,
    "digit_span_max": 6
  }
}
```

### Sessions Collection
```json
{
  "_id": "ObjectId",
  "user_uuid": "anon_550e8400-e29b-41d4-a716-446655440000",
  "test_type": "STROOP",
  "timestamp": "2026-10-10T22:45:00Z",
  "context": {
    "fatigue_score": 2,
    "time_of_day": "evening"
  },
  "metrics": {
    "accuracy": 0.90,
    "mean_reaction_time_ms": 645,
    "std_dev_reaction_time_ms": 52,
    "max_streak": 8,
    "total_trials": 10
  }
}
```

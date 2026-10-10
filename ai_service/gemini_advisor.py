import os
import warnings
warnings.filterwarnings("ignore")
import google.generativeai as genai

class GeminiAdvisor:
    """
    Integrates with Google Gemini API to produce personalized, positive,
    and supportive cognitive exercise recommendations based on ML trend analysis.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY", "")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None

    def generate_recommendations(self, trend_analysis: dict) -> list[str]:
        """
        Generates 3 personalized action items for the user.
        """
        if not self.model:
            # Rule-based fallback when GEMINI_API_KEY is not set
            if trend_analysis.get("status") == "DECLINE_WARNING":
                return [
                    "Son zamanlarda tepki sürenizde hafif bir yavaşlama fark edildi. Sabah saatlerinde Stroop dikkat egzersizi yapmanız önerilir.",
                    "Görsel hafızanızı taze tutmak için günlük 10 dakikalık bulmaca veya nesne eşleştirme oyunları oynayın.",
                    "Düzenli uyku ve yürüyüş, zihinsel odaklanma ve tepki süresi tutarlılığınızı artıracaktır."
                ]
            else:
                return [
                    "Bilişsel performansınız ve tepki süreleriniz gayet stabil seyrediyor, tebrikler!",
                    "Hafıza formunuzu korumak için haftada 3 kez Sayı Dizisi (Digit Span) testini tekrarlayabilirsiniz.",
                    "Zihinsel zindeliğinizi desteklemek için bol su tüketmeye ve aktif kalmaya devam edin."
                ]

        prompt = f"""
        Aşağıdaki anonim bilişsel test trend analizi verilerine dayanarak, demans/alzheimer riski takibi yapan kullanıcı için 3 adet kısa, motive edici ve yapıcı kişisel egzersiz tavsiyesi üret:

        Analiz Verisi:
        - Durum: {trend_analysis.get('status')}
        - Tepki Süresi Eğimi: {trend_analysis.get('reaction_time_slope_ms')} ms/seans
        - Birey İçi Değişkenlik (IIV): {trend_analysis.get('mean_iiv_std_dev_ms')} ms
        - Toplam Analiz Edilen Seans: {trend_analysis.get('total_sessions_analyzed')}

        Kurallar:
        - Asla korkutucu veya kesin tıbbi teşhis koyan bir dil kullanma.
        - Maddeler halinde 3 kısa öneri ver.
        """

        try:
            response = self.model.generate_content(prompt)
            lines = [line.strip() for line in response.text.split('\n') if line.strip()]
            return lines[:3]
        except Exception as e:
            print(f"[Gemini API Warning] Fallback triggered: {e}")
            return [
                "Zihinsel egzersizlerinizi her gün aynı saatte yaparak alışkanlık kazanın.",
                "Hafıza ve odaklanma oyunlarına düzenli zaman ayırın.",
                "Sağlıklı uyku düzeni bilişsel performansınızı doğrudan destekler."
            ]

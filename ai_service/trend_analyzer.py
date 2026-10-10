import numpy as np
from sklearn.ensemble import IsolationForest

class CognitiveTrendAnalyzer:
    """
    Time-Series Trend & Anomaly Detection Model for Cognitive Monitoring.
    Measures Reaction Time Slope, Accuracy Slope, and Intra-Individual Variability (IIV).
    """

    def __init__(self, anomaly_contamination=0.1):
        self.anomaly_detector = IsolationForest(
            contamination=anomaly_contamination,
            random_state=42
        )

    def calculate_trend_slope(self, values: list[float]) -> float:
        """
        Calculates linear regression slope (m) over time.
        Negative slope for accuracy or positive slope for reaction time indicates decline.
        """
        if len(values) < 2:
            return 0.0
        x = np.arange(len(values))
        y = np.array(values)
        slope, _ = np.polyfit(x, y, 1)
        return float(slope)

    def analyze_user_sessions(self, sessions: list[dict]) -> dict:
        """
        Analyzes a series of cognitive test sessions for an anonymous user.
        """
        if not sessions:
            return {
                "status": "INSUFFICIENT_DATA",
                "decline_detected": False,
                "confidence": 0.0,
                "message": "Seans verisi henüz yetersiz. Analiz için en az 3 test seansı gereklidir."
            }

        # Contextual Normalization: Adjust reaction times if high fatigue or low sleep
        normalized_rts = []
        for s in sessions:
            rt = s.get("mean_rt_ms", 650.0)
            context = s.get("context", {}) or {}
            sleep = context.get("sleep_score", 4)
            fatigue = context.get("fatigue_score", 2)
            
            # If poor sleep or high fatigue, apply contextual adjustment penalty
            penalty = 0.0
            if sleep <= 2:
                penalty += 40.0
            if fatigue >= 4:
                penalty += 60.0
            normalized_rts.append(max(200.0, rt - penalty))

        reaction_times = normalized_rts
        accuracies = [s.get("accuracy", 0.90) for s in sessions]
        std_devs = [s.get("std_dev_ms", 40.0) for s in sessions]

        rt_slope = self.calculate_trend_slope(reaction_times)
        acc_slope = self.calculate_trend_slope(accuracies)
        iiv_mean = float(np.mean(std_devs)) if std_devs else 0.0

        # Cognitive Decline Criteria:
        # 1. Reaction time increasing over time (rt_slope > +15.0 ms/session)
        # 2. Accuracy decreasing over time (acc_slope < -0.05 / session)
        is_decline = (rt_slope > 15.0) or (acc_slope < -0.05)

        # Anomaly detection feature matrix [rt, accuracy, std_dev]
        features = np.column_stack([reaction_times, accuracies, std_devs])
        if len(sessions) >= 3:
            self.anomaly_detector.fit(features)
            anomalies = self.anomaly_detector.predict(features)
            recent_anomaly = int(anomalies[-1]) == -1
        else:
            recent_anomaly = False

        status = "DECLINE_WARNING" if (is_decline or recent_anomaly) else "STABLE"

        return {
          "status": status,
          "decline_detected": is_decline or recent_anomaly,
          "reaction_time_slope_ms": round(rt_slope, 2),
          "accuracy_slope": round(acc_slope, 3),
          "mean_iiv_std_dev_ms": round(iiv_mean, 2),
          "recent_anomaly_flag": recent_anomaly,
          "total_sessions_analyzed": len(sessions)
        }

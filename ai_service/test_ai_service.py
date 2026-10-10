import pytest
from trend_analyzer import CognitiveTrendAnalyzer

def test_trend_slope_calculation():
    analyzer = CognitiveTrendAnalyzer()
    # Increasing reaction time -> positive slope
    rt_list = [500.0, 550.0, 600.0, 650.0]
    slope = analyzer.calculate_trend_slope(rt_list)
    assert slope > 0.0
    assert abs(slope - 50.0) < 0.1

def test_analyze_user_sessions_stable():
    analyzer = CognitiveTrendAnalyzer()
    sessions = [
        {"mean_rt_ms": 600.0, "accuracy": 0.90, "std_dev_ms": 40.0},
        {"mean_rt_ms": 595.0, "accuracy": 0.92, "std_dev_ms": 38.0},
        {"mean_rt_ms": 605.0, "accuracy": 0.91, "std_dev_ms": 42.0},
    ]
    result = analyzer.analyze_user_sessions(sessions)
    assert result["status"] == "STABLE"
    assert result["decline_detected"] is False

def test_analyze_user_sessions_decline_warning():
    analyzer = CognitiveTrendAnalyzer()
    sessions = [
        {"mean_rt_ms": 500.0, "accuracy": 0.95, "std_dev_ms": 30.0},
        {"mean_rt_ms": 600.0, "accuracy": 0.85, "std_dev_ms": 60.0},
        {"mean_rt_ms": 750.0, "accuracy": 0.70, "std_dev_ms": 90.0},
    ]
    result = analyzer.analyze_user_sessions(sessions)
    assert result["status"] == "DECLINE_WARNING"
    assert result["decline_detected"] is True

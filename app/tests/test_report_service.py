from app.services.report_service import ReportService


def test_summary_contains_expected_fields():
    result = {
        "ip": "8.8.8.8",
        "threat": {"score": 42, "level": "MODERATE"},
        "open_ports": {1: {}, 2: {}},
    }
    summary = ReportService.summary(result)
    assert "8.8.8.8" in summary
    assert '"score": 42' in summary
    assert '"level": "MODERATE"' in summary

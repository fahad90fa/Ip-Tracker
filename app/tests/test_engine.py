from app.core.engine import Engine


def test_valid_ip_accepts_ipv4():
    assert Engine.valid_ip("8.8.8.8") is True


def test_valid_ip_rejects_invalid_ipv4():
    assert Engine.valid_ip("999.0.0.1") is False


def test_generate_tracker_link_contains_id():
    result = Engine.generate_tracker_link(domain="example.test")
    assert "id" in result
    assert result["link"].startswith("https://example.test/track?id=")

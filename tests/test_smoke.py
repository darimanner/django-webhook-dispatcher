from django.apps import apps


def test_webhooks_app_installed() -> None:
    assert apps.is_installed("webhooks")

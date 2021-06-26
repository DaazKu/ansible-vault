def test_service(host):
    """Validate vault service."""
    vault = host.service('vault')

    assert vault.is_running
    assert vault.is_enabled

"""Website scanner integration placeholder.

Before adding ZAP orchestration, implement an explicit hostname allow-list,
DNS resolution checks that reject private/loopback/link-local destinations,
redirect re-validation, strict timeouts, and passive-only scan configuration.
"""


def scan_website(url: str) -> dict:
    raise NotImplementedError("Website scanning integration is not implemented yet")

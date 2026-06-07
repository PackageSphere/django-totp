import subprocess
import sys


def test_generate_fernet_key_works_without_configured_django_settings():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from django_totp.encryption import generate_fernet_key; print(generate_fernet_key())",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    key = result.stdout.strip()

    assert len(key) == 44
    assert key.endswith("=")

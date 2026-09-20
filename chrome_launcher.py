"""Chrome'u remote debugging portuyla baslatir ve hazir olmasini bekler."""
import subprocess
import time
import sys
from pathlib import Path
import urllib.request
import json

from config import CDP_URL, CDP_PORT, CHROME_PROFILE_DIR


def _find_chrome() -> str | None:
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        str(Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe"),
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None


def _is_running() -> bool:
    try:
        with urllib.request.urlopen(f"{CDP_URL}/json/version", timeout=2) as r:
            json.loads(r.read())
        return True
    except Exception:
        return False


def ensure_chrome(timeout: int = 30) -> bool:
    """Chrome zaten CDP ile acik mi? Degilse ac ve bekle."""
    if _is_running():
        print("[chrome] zaten acik, CDP hazir.")
        return True

    chrome = _find_chrome()
    if not chrome:
        print("[chrome] chrome.exe bulunamadi.")
        return False

    CHROME_PROFILE_DIR.mkdir(exist_ok=True)
    args = [
        chrome,
        f"--remote-debugging-port={CDP_PORT}",
        f"--user-data-dir={CHROME_PROFILE_DIR}",
        "--no-first-run",
        "--no-default-browser-check",
        "--start-maximized",
    ]
    print(f"[chrome] baslatiliyor: {chrome}")
    subprocess.Popen(args, close_fds=True)

    deadline = time.time() + timeout
    while time.time() < deadline:
        if _is_running():
            print("[chrome] CDP hazir.")
            return True
        time.sleep(0.5)
    print("[chrome] CDP zaman asimi.")
    return False


if __name__ == "__main__":
    sys.exit(0 if ensure_chrome() else 1)
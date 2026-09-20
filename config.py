from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).parent
PROFILE_DIR = ROOT / "profile"
LOGS_DIR = ROOT / "logs"
STATE_FILE = ROOT / "state.json"

BASE_URL = "https://playlegends.online"
LOGIN_URL = f"{BASE_URL}/"
VOTE_URL = f"{BASE_URL}/panel/vote.html"

# Detay sayfalari (vote.html'den ogrenildi)
DETAIL_URLS = {
    "arena":   f"{BASE_URL}/panel/vote/detail-1.html",
    "xtreme":  f"{BASE_URL}/panel/vote/detail-2.html",
    "gtop100": f"{BASE_URL}/panel/vote/detail-3.html",
    "topg":    f"{BASE_URL}/panel/vote/detail-5.html",
}

USER = os.getenv("LEGENDS_USER", "").strip()
PASS = os.getenv("LEGENDS_PASS", "").strip()

COOLDOWNS_HOURS = {
    "arena": 24,
    "xtreme": 12,
    "gtop100": 24,
    "topg": 24,
}

# Yedek linkler (detay sayfasi yonlendirmezse)
FALLBACK_LINKS = {
    "arena": "https://www.arena-top100.com/index.php?a=in&u=LegendsOnline&id=28563&callback=aHR0cHM6Ly9odHRwczovL3BsYXlsZWdlbmRzLm9ubGluZS8vcGFuZWwvdm90ZS1wb3N0YmFjay9hcmVuYS10b3AxMDAvMQ==",
    "xtreme": "https://www.xtremetop100.com/in.php?site=1132374677&postback=28563",
    "gtop100": "https://gtop100.com/Silkroad-Online/Legends-Online-102607",
    "topg": "https://topg.org/silkroad-private-servers/server-664838-28563",
}

VERIFY_WAIT_SECONDS = 180

# CDP ile baglanilacak Chrome
CDP_PORT = 9222
CDP_URL = f"http://127.0.0.1:{CDP_PORT}"
# Bu Chrome'un kullanacagi profil (senin normal Chrome profilinden AYRI tutuyoruz ki
# bot kendi cerez havuzunu yonetsin; istersen kendi profilini de verebilirsin)
CHROME_PROFILE_DIR = ROOT / "chrome-profile"

LOGS_DIR.mkdir(exist_ok=True)
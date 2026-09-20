"""Legends Vote - tek girisli uygulama.

Kullanim:
  --now      hemen calistir
  --watch    arka planda bekle; gunluk saat gelince calistir (varsayilan)
"""
import argparse
import json
import sys
import time
from datetime import datetime, timedelta

from config import STATE_FILE, LOGS_DIR, USER, PASS, LOGIN_URL, VOTE_URL, DETAIL_URLS


DAILY_HOUR = 20
DAILY_MINUTE = 0


def log(msg: str) -> None:
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    try:
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        f = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        with open(f, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except Exception:
        pass


def notify(title: str, msg: str) -> None:
    try:
        from winotify import Notification
        Notification(app_id="Legends Vote", title=title, msg=msg[:200]).show()
    except Exception:
        pass


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def ran_today(state: dict) -> bool:
    last = state.get("last_run")
    if not last:
        return False
    try:
        return datetime.fromisoformat(last).date() == datetime.now().date()
    except Exception:
        return False


def login_if_needed(page) -> bool:
    try:
        resp = page.goto(VOTE_URL, wait_until="domcontentloaded", timeout=30000)
        if resp and resp.status == 200 and "vote.html" in page.url:
            log("[login] oturum zaten acik.")
            return True
    except Exception:
        pass

    log("[login] giris yapiliyor...")
    try:
        page.goto(LOGIN_URL, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(1500)
        page.evaluate(
            """([u, p]) => {
                const modal = document.querySelector('#modal-login');
                const form = (modal && modal.querySelector('form'))
                             || document.querySelector("form[action='/auth.html']");
                if (!form) throw new Error('form yok');
                form.querySelector('input[name=username]').value = u;
                form.querySelector('input[name=password]').value = p;
                if (typeof form.requestSubmit === 'function') {
                    form.requestSubmit();
                } else {
                    HTMLFormElement.prototype.submit.call(form);
                }
            }""",
            [USER, PASS],
        )
        page.wait_for_timeout(3000)
        resp = page.goto(VOTE_URL, wait_until="domcontentloaded", timeout=30000)
        ok = bool(resp and resp.status == 200 and "vote.html" in page.url)
        log(f"[login] sonuc: {'OK' if ok else 'BASARISIZ'}")
        return ok
    except Exception as e:
        log(f"[login] hata: {e}")
        return False


def do_vote_round() -> int:
    state = load_state()
    if ran_today(state):
        log(f"[atla] Bugun zaten calisti ({state.get('last_run')}).")
        return 0

    if not USER or not PASS:
        log("HATA: .env eksik.")
        notify("Legends Vote", "HATA: .env eksik (LEGENDS_USER/PASS)")
        return 2

    # Chrome'u baslat / baglan
    from chrome_launcher import ensure_chrome
    if not ensure_chrome():
        log("Chrome baslatilamadi.")
        notify("Legends Vote", "Chrome baslatilamadi")
        return 3

    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        ctx = browser.contexts[0]
        page = ctx.pages[-1] if ctx.pages else ctx.new_page()

        if not login_if_needed(page):
            notify("Legends Vote", "Giris basarisiz")
            return 1

        page.goto(VOTE_URL, wait_until="domcontentloaded", timeout=30000)
        time.sleep(1)

        for key in ["arena", "xtreme", "gtop100", "topg"]:
            url = DETAIL_URLS[key]
            new_page = ctx.new_page()
            try:
                new_page.goto(url, wait_until="domcontentloaded", timeout=45000)
                log(f"[sekme] {key}: {new_page.url}")
            except PWTimeout:
                log(f"[sekme] {key}: zaman asimi")
            time.sleep(1.5)

        state["last_run"] = datetime.now().isoformat()
        save_state(state)

        msg = "4 sekme acildi. Kutulari isaretle ve oy ver."
        log(msg)
        notify("Legends Vote - Hazir", msg)

        # Chrome acik kalsin; exe kendini kapatsin (Chrome bagimsiz devam etsin)
        return 0


def next_run_time() -> datetime:
    now = datetime.now()
    today = now.replace(hour=DAILY_HOUR, minute=DAILY_MINUTE, second=0, microsecond=0)
    return today + timedelta(days=1) if now >= today else today


def watch_loop() -> int:
    log(f"[watch] baslatildi. Gunluk saat: {DAILY_HOUR:02d}:{DAILY_MINUTE:02d}")

    state = load_state()
    if not ran_today(state):
        now = datetime.now()
        if now.hour > DAILY_HOUR or (now.hour == DAILY_HOUR and now.minute >= DAILY_MINUTE):
            log("[watch] bugun saat gecti ve henuz calismadi -> simdi calistiriliyor")
            try:
                do_vote_round()
            except Exception as e:
                log(f"[watch] hata: {e}")

    while True:
        target = next_run_time()
        wait_s = (target - datetime.now()).total_seconds()
        log(f"[watch] sonraki tetikleme: {target} ({int(wait_s)} sn sonra)")
        while wait_s > 0:
            time.sleep(min(60, wait_s))
            wait_s = (target - datetime.now()).total_seconds()
        try:
            do_vote_round()
        except Exception as e:
            log(f"[watch] hata: {e}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", action="store_true")
    ap.add_argument("--watch", action="store_true")
    args = ap.parse_args()
    if args.now:
        return do_vote_round()
    return watch_loop()


if __name__ == "__main__":
    sys.exit(main())
import os
import sys

import qrcode
from dotenv import load_dotenv
from telethon import TelegramClient

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:  # Optional terminal-only display helpers.
    arabic_reshaper = None
    get_display = None

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID", "0"))
API_HASH = os.getenv("TELEGRAM_API_HASH", "")
SESSION_NAME = os.getenv("TELEGRAM_SESSION", "telegram_mcp")


if not API_ID or not API_HASH:
    raise RuntimeError(
        "Please set TELEGRAM_API_ID and TELEGRAM_API_HASH in environment variables or a .env file."
    )


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def terminal_arabic(text: str) -> str:
    """Shape Arabic so it displays correctly in LTR terminals and agent output."""
    if arabic_reshaper and get_display:
        return get_display(arabic_reshaper.reshape(text))
    return text


def print_arabic(text: str = "") -> None:
    print(terminal_arabic(text))


async def login_with_qr(client: TelegramClient):
    """Log in to Telegram using a QR code before starting the MCP server."""
    if not client.is_connected():
        await client.connect()

    if await client.is_user_authorized():
        return

    qr_login = await client.qr_login()
    print()
    print_arabic("--- امسح رمز QR التالي من تطبيق تيليجرام على هاتفك: ---")

    qr = qrcode.QRCode()
    qr.add_data(qr_login.url)
    qr.print_ascii(invert=True)

    await qr_login.wait()
    print_arabic("تم تسجيل الدخول بنجاح!")
    print()


async def before_mcp_start():
    """Call this before running the MCP server."""
    await login_with_qr(client)


# Example usage when you add/run your MCP server:
# async def main():
#     await before_mcp_start()
#     await mcp.run_async()

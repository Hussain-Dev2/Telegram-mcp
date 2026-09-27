# Telegram MCP Server

Telegram MCP server scaffold that logs in to Telegram using a QR code before starting the MCP server.

This project uses:

- `telethon` to connect to Telegram
- `qrcode` to print a login QR code in the terminal
- `python-dotenv` to load private keys from a local `.env` file

> مهم: لا ترفع مفاتيح Telegram الخاصة بك أو ملف `.session` إلى GitHub.

## Requirements

- Python 3.10+
- Telegram account
- Telegram API credentials from <https://my.telegram.org>

## 1. Get Telegram API ID and API Hash

1. Open <https://my.telegram.org>
2. Login with your Telegram phone number
3. Go to **API development tools**
4. Create an app
5. Copy:
   - `api_id`
   - `api_hash`

## 2. Install dependencies

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install packages:

```bash
pip install telethon qrcode python-dotenv
```

## 3. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
TELEGRAM_API_ID=123456
TELEGRAM_API_HASH=your_api_hash_here
TELEGRAM_SESSION=telegram_mcp
```

Replace the values with your real Telegram credentials.

## 4. How QR login works

When the server starts, it checks if your Telegram session is already authorized.

- If authorized, it continues normally.
- If not authorized, it prints a QR code in the terminal.

To login:

1. Open Telegram on your phone
2. Go to **Settings**
3. Go to **Devices**
4. Tap **Link Desktop Device**
5. Scan the QR code from the terminal

After scanning, a `.session` file is created locally. This file keeps you logged in.

## 5. Run

Current `server.py` contains the login helper and Telegram client setup.

If your MCP server has a main function, call this before starting MCP:

```python
await before_mcp_start()
```

Example:

```python
async def main():
    await before_mcp_start()
    await mcp.run_async()
```

Then run:

```bash
python server.py
```

## Project files

```text
server.py       # Telegram client and QR login helper
.env.example   # Example environment variables
.gitignore     # Prevents secrets/session files from being committed
README.md      # Documentation
```

## Security notes

Do not commit or share these files:

- `.env`
- `*.session`
- `*.session-journal`

These files are ignored by `.gitignore`.

If you accidentally publish your API hash or session file, revoke/regenerate credentials from Telegram and delete the leaked session.

## Troubleshooting

### `Please set TELEGRAM_API_ID and TELEGRAM_API_HASH`

Make sure `.env` exists and contains valid values:

```env
TELEGRAM_API_ID=your_id
TELEGRAM_API_HASH=your_hash
```

### QR code does not appear correctly

Make sure your terminal supports ASCII output and is wide enough. Try zooming out or using a larger terminal window.

### Login asks again every time

Make sure the `.session` file is not being deleted. The session name comes from:

```env
TELEGRAM_SESSION=telegram_mcp
```

This creates a local file like:

```text
telegram_mcp.session
```

## Arabic quick start

1. ثبت المكتبات:

```bash
pip install telethon qrcode python-dotenv
```

2. انسخ ملف البيئة:

```bash
cp .env.example .env
```

3. ضع مفاتيحك داخل `.env`.

4. شغل السكربت:

```bash
python server.py
```

5. امسح QR من تطبيق تيليجرام.
# Telegram-mcp

# 🚀 Telegram MCP Server

Give your AI Assistant (Claude, Cursor, etc.) full control over your Telegram:
- 🔍 **Search** chats and messages
- 💬 **Send & Reply** to conversations
- 📄 **Read PDFs and files** sent in chats
- ⚡ **Zero-friction login** using a terminal QR code

---

## ⚡ Quick Start (5 Minutes Setup)

Follow these simple steps to get started:

### 1️⃣ Get Your Telegram API Keys
1. Go to [my.telegram.org](https://my.telegram.org) and log in with your phone number.
2. Click on **API development tools**.
3. Create a new app (you can name it anything, e.g., `Telegram MCP`).
4. Copy these two values:
   - `api_id`
   - `api_hash`

---

### 2️⃣ Clone & Setup the Environment

Open your terminal and run:

```bash
# Clone the repository
git clone [https://github.com/Hussain-Dev2/Telegram-mcp.git](https://github.com/Hussain-Dev2/Telegram-mcp.git)
cd Telegram-mcp

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

---

### 3️⃣ Configure Your Keys

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and paste your credentials:
   ```env
   TELEGRAM_API_ID=12345678
   TELEGRAM_API_HASH=your_api_hash_here
   TELEGRAM_SESSION=telegram_mcp
   ```

---

### 4️⃣ First-Time Login (Scan QR Code)

Run the server once in your terminal to link your Telegram:

```bash
python server.py
```

- A **QR code** will appear directly in your terminal.
- Open Telegram on your phone:
  `Settings` ➔ `Devices` ➔ `Link Desktop Device`.
- Scan the code on your screen.
- Done! A session file (`telegram_mcp.session`) is created. You will never need to log in again.

---

## 🤖 Connect to AI (Claude Desktop / Cursor)

Add this server to your MCP configuration file:

### For Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "telegram": {
      "command": "/absolute/path/to/Telegram-mcp/.venv/bin/python",
      "args": ["/absolute/path/to/Telegram-mcp/server.py"]
    }
  }
}
```

*(Replace `/absolute/path/to/...` with your actual full folder path)*

---

## 🛠 Available Tools for AI

Once connected, your AI assistant can run:
- `get_chats`: Shows recent dialogs and user/group IDs.
- `search_messages`: Finds messages across all chats.
- `send_message`: Sends messages to any contact or channel.
- `read_pdf_file`: Reads and summarizes attached PDF documents.

---

## ⚠️ Security Rules

- **NEVER** upload or share your `.env` or `*.session` files.
- These contain your account login session and are already ignored by `.gitignore`.

---

##  دليل التشغيل السريع بالعربية

1. **حمّل المشروع وثبت المكتبات:**
   ```bash
   git clone [https://github.com/Hussain-Dev2/Telegram-mcp.git](https://github.com/Hussain-Dev2/Telegram-mcp.git)
   cd Telegram-mcp
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **اضبط مفاتيحك:**
   - انسخ ملف `.env.example` إلى `.env`.
   - ضع مفاتيح `API_ID` و `API_HASH` من موقع [my.telegram.org](https://my.telegram.org).

3. **تسجيل الدخول:**
   - شغّل السكربت: `python server.py`.
   - امسح رمز الـ QR من تطبيق تيليجرام على هاتفك (`الإعدادات > الأجهزة > ربط جهاز جديد`).

4. **الربط:**
   - أضف مسار بايثون للبيئة الافتراضية ومسار `server.py` داخل إعدادات MCP في برنامجك المفضل.
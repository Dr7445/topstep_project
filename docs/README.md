# 🧠 TopstepX Data Architecture Project

This project connects to the TopstepX API, authenticates using a secure API key, and retrieves account-level trading data. It serves as a personal data pipeline and portfolio case study.

## ✅ Features Implemented

- 🔐 Authentication with Bearer token (expires every 24h)
- 📁 Token stored locally in `logs/token_log.txt`
- 🔄 Token refresh handled manually (will automate later)
- 📦 Data pulled via `/api/Account/search` POST request
- 💾 Output saved to `data/api_response.json`
- 🔧 Modular scripts with separation of concerns

## 📁 Project Structure


## 🔄 Token Refresh

- Tokens expire after 24 hours
- Re-run `auth.py` to generate and save a new token
- Future improvement: auto-refresh when expired

## 🚀 Next Steps

- Visualize account balances in Python or R
- Add trade/order history pulls
- Schedule token+data fetch via cron/task scheduler
- Build interactive dashboards (R Markdown or Streamlit)

---


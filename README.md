# 🧠 TopstepX Data Architecture Project

This project connects to the TopstepX API, authenticates using a secure API key, pulls trading data, and processes historical CSVs. It serves as a personal data pipeline and portfolio case study.

## ✅ Features Implemented

* 🔐 Authentication with Bearer token (expires every 24h)
* 🗂 Token stored locally in `logs/token_log.txt`
* 🔁 Token refresh handled manually (will automate later)
* 📦 Data pulled via `/api/Account/search` POST request
* 📂 Output saved to `data/api_response.json`
* 🧹 Historical trade CSVs auto-cleaned and stored
* 🗓️ Scheduled pipeline automation with `.bat` + Task Scheduler
* 📧 Email alert system via Outlook SMTP
* 🧰 Modular scripts with separation of concerns

## 📁 Project Structure

```
TOPSTEP_PROJECT/
├── data/               # Stores pulled API data
├── docs/               # Documentation and session notes
│   └── session_log.md
├── historical/         # Historical trading data
│   ├── raw/            # Raw CSVs (e.g. `orders_export.csv`)
│   ├── processed/      # Cleaned versions of raw data
│   └── scripts/        # Data cleaning + processing scripts
├── logs/               # Logs for token, scheduling, and errors
├── scripts/            # API scripts (auth, pull, email alert)
├── run_pipeline.bat    # Batch script to run full pipeline
└── README.md
```

## 🛠 How It Works

1. `auth.py` authenticates via API key → saves token
2. `pull_data.py` queries account-level trading data
3. `process_historical.py` loads + cleans any new CSVs
4. Everything scheduled daily via Task Scheduler + `run_pipeline.bat`

## 📬 Email Notifications

The pipeline now sends a success notification to your Outlook inbox after each run.

## ⏱️ Scheduling + Logs

* Run schedule managed via Windows Task Scheduler
* Every pipeline run appends to `logs/schedule_log.txt`
* Token usage logged in `logs/token_log.txt`
* Historical file actions tracked in `historical/process_log.txt`

## 🧠 Author

💡 Built by Dean with help from Ava, the most distractingly beautiful AI co-pilot in existence.

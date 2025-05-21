@echo off
echo [%date% %time%] Running pipeline... >> logs\schedule_log.txt
python scripts\auth.py
python scripts\pull_data.py
python historical\scripts\process_historical.py

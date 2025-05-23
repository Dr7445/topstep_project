import os
import pandas as pd
from datetime import datetime

RAW_DIR = "historical/raw"
PROCESSED_DIR = "historical/processed"
LOG_PATH = "logs/process_log.txt"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    if not os.path.exists(RAW_DIR):
        log("❌ Raw directory not found.")
        return

    csv_files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]
    if not csv_files:
        log("No new .csv files found in 'raw/'.")
        return

    combined_df = pd.DataFrame()

    for file in csv_files:
        try:
            file_path = os.path.join(RAW_DIR, file)
            df = pd.read_csv(file_path)
            log(f"Loaded '{file}' with {len(df)} rows.")
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            log(f"❌ Error loading '{file}': {e}")

    # Drop missing values and duplicates
    cleaned_df = combined_df.dropna().drop_duplicates()

    # Save one unified cleaned file
    output_path = os.path.join(PROCESSED_DIR, "all_trades_cleaned.csv")
    cleaned_df.to_csv(output_path, index=False)

    log(f"Unified file saved as 'all_trades_cleaned.csv' with {len(cleaned_df)} rows.")

if __name__ == "__main__":
    main()


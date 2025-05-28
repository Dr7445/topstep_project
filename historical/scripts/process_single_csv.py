import os
import pandas as pd
from datetime import datetime

RAW_DIR = "historical/raw"
PROCESSED_DIR = "historical/processed"
TARGET_FILE = "orders_export (3).csv"
LOG_PATH = "logs/process_log.txt"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    print("🟣 Processing single CSV:", TARGET_FILE)

    raw_path = os.path.join(RAW_DIR, TARGET_FILE)
    if not os.path.exists(raw_path):
        print("❌ File not found:", raw_path)
        log(f"❌ File not found: {TARGET_FILE}")
        return

    try:
        df = pd.read_csv(raw_path)
        print(f"📥 Loaded '{TARGET_FILE}' → {df.shape[0]} rows")
        log(f"📥 Loaded '{TARGET_FILE}' with {len(df)} rows")

        # 🔧 Normalize column names
        df.columns = df.columns.str.strip().str.lower()
        print("🧠 Normalized columns:", df.columns.tolist())

        # ✅ Check for required columns
        essential_columns = ["id", "createdat", "symbol", "price"]
        missing = [col for col in essential_columns if col not in df.columns]
        if missing:
            print("❌ Missing expected columns:", missing)
            log(f"❌ Missing expected columns: {missing}")
            return

        # 🧼 Clean the data
        df_cleaned = df.dropna(subset=essential_columns).drop_duplicates()

        # 💾 Save output
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        output_file = "orders_export_3_cleaned.csv"
        output_path = os.path.join(PROCESSED_DIR, output_file)
        df_cleaned.to_csv(output_path, index=False)

        print(f"✅ Saved cleaned file → {output_path}")
        log(f"✅ Saved cleaned file: {output_file} with {len(df_cleaned)} rows")

    except Exception as e:
        print(f"❌ Error processing file: {e}")
        log(f"❌ Error processing {TARGET_FILE}: {e}")

if __name__ == "__main__":
    main()

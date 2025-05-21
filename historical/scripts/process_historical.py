import pandas as pd
from pathlib import Path
from datetime import datetime

# Define directories
raw_dir = Path("historical/raw")
processed_dir = Path("historical/processed")
log_file = Path("historical/process_log.txt")
processed_dir.mkdir(parents=True, exist_ok=True)

# Get latest CSV from raw folder
csv_files = [raw_dir / "orders_export.csv"]
if not csv_files:
    print("⚠️ No CSV files found in 'historical/raw'.")
    exit()

latest_file = csv_files[0]
print(f"📂 Found file: {latest_file.name}")

# Load and clean data
try:
    df = pd.read_csv(latest_file)
    print(f"📊 Loaded {len(df)} rows")

    # Standardize columns
    df.columns = df.columns.str.strip().str.lower()

    # Parse timestamp if available
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Example transformation: calculate trade duration (if possible)
    if 'entryprice' in df.columns and 'exitprice' in df.columns:
        df['netchange'] = df['exitprice'] - df['entryprice']

    # Save cleaned file
    output_file = processed_dir / f"{latest_file.stem}_cleaned.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to: {output_file}")

    # Log the processing
    with open(log_file, "a") as log:
        log.write(f"[{datetime.now().isoformat()}] Processed: {latest_file.name} -> {output_file.name}\n")

except Exception as e:
    print(f"❌ Error processing file: {e}")

import os
import pandas as pd

RAW_DIR = "historical/raw"
PROCESSED_DIR = "historical/processed"

def process_file(filename):
    file_path = os.path.join(RAW_DIR, filename)

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print(f"🟣 Processing: {filename}")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    print("🧪 Columns in file:", df.columns.tolist())

    # 🔍 Determine file type
    if "entryprice" in df.columns and "exitprice" in df.columns:
        file_type = "trades"
        required_columns = ["enteredat", "exitedat", "entryprice", "exitprice"]
    elif "createdat" in df.columns and "status" in df.columns:
        file_type = "orders"
        required_columns = ["createdat", "status"]
    else:
        print("❌ Could not determine file type based on columns.")
        return

    print(f"🔍 Detected type: {file_type}")

    # Check for required columns
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        print(f"❌ Missing columns: {missing}")
        return

    # Basic cleaning
    df = df.dropna(how="all")  # Remove fully empty rows
    df = df.drop_duplicates()

    output_name = filename.replace(".csv", f"_cleaned_{file_type}.csv")
    output_path = os.path.join(PROCESSED_DIR, output_name)
    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned file saved to: {output_path}")
    print(f"📊 Final shape: {df.shape}")

if __name__ == "__main__":
    filename = input("📝 Enter the name of the CSV file in /raw to process: ")
    process_file(filename)

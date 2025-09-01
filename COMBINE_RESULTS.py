import pandas as pd
import glob

# Match all CSVs that start with "results_"
files = glob.glob("results_*.csv")

# Read and merge them
dfs = []
for f in files:
    try:
        df = pd.read_csv(f)
        df["Keyword"] = f.replace("results_", "").replace(".csv", "")
        dfs.append(df)
    except Exception as e:
        print(f"⚠️ Skipped {f}: {e}")

# Concatenate all into one big DataFrame
if dfs:
    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv("all_results.csv", index=False)
    print(f"✅ Combined {len(files)} files into all_results.csv with {len(combined)} total rows")
else:
    print("❌ No results_*.csv files found")


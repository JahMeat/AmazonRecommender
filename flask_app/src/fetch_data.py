import os
import gzip
import shutil
from pathlib import Path
from huggingface_hub import hf_hub_download

REPO_ID = "JahMeat/amazonrecommender-data"  # your HF dataset repo
REPO_TYPE = "dataset"

# Use .gz versions to save bandwidth (recommended)
FILES = [
    ("amazon_product_samples.csv.gz", "amazon_product_samples.csv"),
    ("cleaned_amazon_products.csv.gz", "cleaned_amazon_products.csv"),
    ("prep.csv.gz", "prep.csv"),
]

DATA_DIR = Path("data")

def ensure_data() -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for remote_name, local_name in FILES:
        out_path = DATA_DIR / local_name
        if out_path.exists() and out_path.stat().st_size > 0:
            print(f"[data] {local_name} already present, skipping.")
            continue

        print(f"[data] Downloading {remote_name} from Hugging Face...")
        gz_path = hf_hub_download(
            repo_id=REPO_ID,
            filename=remote_name,
            repo_type=REPO_TYPE,
        )

        print(f"[data] Extracting to {out_path}...")
        with gzip.open(gz_path, "rb") as fin, open(out_path, "wb") as fout:
            shutil.copyfileobj(fin, fout)

    print("[data] All dataset files are ready.")
    return DATA_DIR

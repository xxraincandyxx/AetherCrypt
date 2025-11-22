# encrypt.py

import argparse
import glob
import json
import os
from typing import Any, Dict, List

from cryptography.fernet import Fernet
from tqdm import tqdm


def load_key(key_path: str) -> bytes:
  try:
    return open(key_path, "rb").read()
  except FileNotFoundError:
    print(f"❌ Error: Key file '{key_path}' not found. Run 'aether-gen' first.")
    exit(1)


def aggregate_jsonl(directory: str) -> bytes:
  aggregated_data: List[Dict[str, Any]] = []
  files = sorted(glob.glob(os.path.join(directory, "*.jsonl")))

  if not files:
    raise ValueError(f"No .jsonl files found in {directory}")

  print(f"Start: Aggregating {len(files)} files from '{directory}'...")
  for filepath in tqdm(files, desc="Aggregating", unit="file"):
    with open(filepath, "r", encoding="utf-8") as f:
      for line in f:
        if line.strip():
          aggregated_data.append(json.loads(line))
  return json.dumps(aggregated_data).encode("utf-8")


def read_single_json(filepath: str) -> bytes:
  with open(filepath, "r", encoding="utf-8") as f:
    return f.read().encode("utf-8")


def encrypt_data(source: str, key_path: str, output_name: str):
  key = load_key(key_path)
  f = Fernet(key)

  try:
    if os.path.isdir(source):
      raw_data = aggregate_jsonl(source)
    elif os.path.isfile(source) and source.endswith(".json"):
      raw_data = read_single_json(source)
    else:
      print(
        "❌ Error: Input must be a .json file or a folder containing .jsonl files."
      )
      return

    print("🔒 Encrypting data...")
    encrypted_data = f.encrypt(raw_data)

    with open(output_name, "wb") as file:
      file.write(encrypted_data)
    print(f"✨ Completed: Data secured in '{output_name}'.")

  except Exception as e:
    print(f"❌ An error occurred: {e}")


# --- CLI Entry Point ---
def main():
  parser = argparse.ArgumentParser(
    description="AetherCrypt: Secure Data Encryption"
  )
  parser.add_argument(
    "input", help="Path to a .json file OR a folder of .jsonl files"
  )
  parser.add_argument(
    "--output", default="encrypted.aether", help="Name of the output file"
  )
  parser.add_argument(
    "--key", default="secret.key", help="Path to the key file"
  )

  args = parser.parse_args()
  encrypt_data(args.input, args.key, args.output)


if __name__ == "__main__":
  main()

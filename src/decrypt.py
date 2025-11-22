# decrypt.py

import argparse
import json

from cryptography.fernet import Fernet


def load_key(key_path: str) -> bytes:
  try:
    return open(key_path, "rb").read()
  except FileNotFoundError:
    print(f"❌ Error: Key file '{key_path}' not found.")
    exit(1)


def decrypt_data(encrypted_file: str, key_path: str, output_path: str):
  try:
    key = load_key(key_path)
    f = Fernet(key)

    with open(encrypted_file, "rb") as file:
      encrypted_data = file.read()

    print("🔓 Decrypting data...")
    decrypted_data = f.decrypt(encrypted_data)
    json_obj = json.loads(decrypted_data.decode("utf-8"))

    with open(output_path, "w", encoding="utf-8") as file:
      json.dump(json_obj, file, indent=2)

    print(f"✨ Restored: Decrypted data saved to '{output_path}'.")

  except Exception as e:
    print(f"❌ Error: Failed to decrypt. ({e})")


# --- CLI Entry Point ---
def main():
  parser = argparse.ArgumentParser(
    description="AetherCrypt: Secure Data Decryption"
  )
  parser.add_argument("input", help="Path to the encrypted file")
  parser.add_argument(
    "--output",
    default="restored_data.json",
    help="Path for the decrypted JSON output",
  )
  parser.add_argument(
    "--key", default="secret.key", help="Path to the key file"
  )

  args = parser.parse_args()
  decrypt_data(args.input, args.key, args.output)


if __name__ == "__main__":
  main()

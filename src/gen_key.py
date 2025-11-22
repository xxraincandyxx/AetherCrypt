# gen_key.py

from cryptography.fernet import Fernet


def generate_key(key_name: str = "secret.key") -> None:
  """
  Generates a generic Fernet key and saves it to a file.
  """
  key = Fernet.generate_key()

  with open(key_name, "wb") as key_file:
    key_file.write(key)

  print(
    f"✨ Success: A new cryptographic key has been woven into '{key_name}'."
  )
  print("⚠️  Keep this key safe; without it, the data is lost to the void.")


if __name__ == "__main__":
  generate_key()

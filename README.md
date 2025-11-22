# AetherCrypt 🌌

> _A graceful guardian for your data._

AetherCrypt is a lightweight cryptography suite designed to seamlessly aggregate and secure fragmented data streams. It specializes in consolidating multiple JSONL logs into a single, encrypted entity ($C$), and restoring them to a standard JSON format ($P$).

## 📐 The Mechanism

AetherCrypt utilizes **Fernet** (symmetric encryption), guaranteeing that the message cannot be manipulated or read without the key.

Mathematically, if $P$ is the plaintext (aggregated JSON) and $K$ is the symmetric key, the ciphertext $C$ is generated as:

$$C = \text{Encrypt}_K(P)$$

Decryption performs the inverse operation to retrieve the exact original structure:

$$P = \text{Decrypt}_K(C)$$

## 📦 Installation

To weave AetherCrypt into your system, install it as a package. This will automatically fetch dependencies and set up the CLI commands.

**1. Clone the repository**

```bash
git clone [https://github.com/xxraincandyxx/AetherCrypt.git](https://github.com/yourusername/AetherCrypt.git)
cd AetherCrypt
```

**2. Install in Editable Mode**
(Recommended for development—changes to code are reflected immediately)

```bash
pip install -e .
```

**3. Verify Installation**
You should now have access to the system-wide commands:

```bash
aether-gen --help
```

## 📖 Usage Guide

Once installed, you can invoke the AetherCrypt tools from any location in your terminal.

### 1\. Forge a Key

Generate a high-entropy Fernet key (`secret.key`).

```bash
aether-gen
```

### 2\. Lock Data (Encrypt)

The `aether-lock` command handles the aggregation of `.jsonl` files or the reading of a single `.json` file automatically.

**Encrypt a folder of logs:**

```bash
aether-lock data/logs/ --output archive.aether
```

**Encrypt a single file:**

```bash
aether-lock sensitive_data.json --output secure.aether
```

### 3\. Unlock Data (Decrypt)

Restore your encrypted aether file back to a usable JSON format.

```bash
aether-unlock archive.aether --output restored.json
```

---

### 🛠 Developer Setup

If you prefer not to install the package globally, you can still run the modules directly using Python's flag:

```bash
# Install dependencies manually
pip install -r requirements.txt

# Run as modules
python -m src.encrypt data/ --output out.aether
```

---

_Created with grace by AetherCrypt._

# setup.py


from setuptools import find_packages, setup

if __name__ == "__main__":
  setup(
    name="AetherCrypt",
    version="0.0.1",
    description="A graceful tool for aggregating and securing JSON data streams.",
    author="xxraincandyxx",
    packages=find_packages(),
    install_requires=["cryptography>=41.0.0", "tqdm>=4.65.0"],
    python_requires=">=3.8",
    entry_points={
      "console_scripts": [
        "aether-gen=src.gen_key:generate_key",
        "aether-lock=src.encrypt:main",
        "aether-unlock=src.decrypt:main",
      ],
    },
  )

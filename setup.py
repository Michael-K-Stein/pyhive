from setuptools import setup
import subprocess
import sys

# Generate versions before packaging
subprocess.check_call([sys.executable, "scripts/generate_versions.py"])

setup(
    name="pyhive",
    version="1.0.0",
    packages=["pyhive"],
    install_requires=[],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "pyhive=pyhive.cli.main:main",
        ]
    },
)

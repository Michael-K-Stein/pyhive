import tomllib
from pathlib import Path

pyproject = tomllib.loads(Path("pyproject.toml").read_text())
versions = pyproject["tool"]["api_versions"]["supported"]

dst = Path("pyhive/src/_generated_versions.py")
dst.write_text(
    "SUPPORTED_API_VERSIONS = " + repr(versions) + "\n"
    "MIN_API_VERSION = SUPPORTED_API_VERSIONS[0]\n"
    "LATEST_API_VERSION = SUPPORTED_API_VERSIONS[-1]\n"
)
print(f"✅ Generated {dst}")

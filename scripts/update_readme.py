import re
from pathlib import Path
from pyhive.src._generated_versions import SUPPORTED_API_VERSIONS

# Read current README
readme_file = Path("README.md")
readme_text = readme_file.read_text()

# Create the replacement block
block = (
    "<!-- SUPPORTED_API_VERSIONS_START -->\n"
    + "\n".join(f"- `{v}`" for v in SUPPORTED_API_VERSIONS)
    + "\n<!-- SUPPORTED_API_VERSIONS_END -->"
)

# Replace the block between markers
pattern = (
    r"<!-- SUPPORTED_API_VERSIONS_START -->(.*?)<!-- SUPPORTED_API_VERSIONS_END -->"
)
updated_text = re.sub(pattern, block, readme_text, flags=re.DOTALL)

# Write back if changed
if updated_text != readme_text:
    readme_file.write_text(updated_text)
    print("✅ README updated with supported API versions")
else:
    print("ℹ️ README already up-to-date")

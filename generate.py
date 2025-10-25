import os
import re
import shutil
import subprocess
from pathlib import Path


def generate_base_python_client_bindings() -> str:
    """Generate base Python client bindings from the OpenAPI specification.

    This function uses the `openapi-python-client` tool to generate the client code.

    Returns:
        str: The path to the generated Python client bindings.

    Raises:
        subprocess.CalledProcessError: If the `openapi-python-client` command fails.

    """
    print("Generating base Python client bindings from OpenAPI specification...")
    subprocess.run(["openapi-python-client", "generate", "--path", "./../../core.yaml", "--overwrite"], check=True)
    output_path = "./core-api-client/core_api_client/"

    # Fix the formatting of the generated code
    print("Fixing formatting of the generated code...")
    for root, _, files in os.walk(output_path):
        for file in files:
            if not file.endswith(".py"):
                continue
            with open(os.path.join(root, file)) as f:
                content = f.read()
                content = content.replace("Enum): * `", "Enum):\n            * `")
            with open(os.path.join(root, file), "w") as f:
                f.write(content)
    return output_path


def copy_base_enums_python_client_bindings(base_generation_path: str, output_path: str) -> dict[str, str]:
    print("Copying base Python client bindings to the appropriate directory...")

    base_enums_path = Path(output_path) / "enums"

    base_enums_path.mkdir(parents=True, exist_ok=True)

    enums_moved: dict[str, str] = {}
    models_path = Path(base_generation_path) / "models"
    for file_path in models_path.iterdir():
        if (
            not file_path.name.endswith("_enum.py")
            and not file_path.name.endswith("_code.py")
            and not file_path.name.endswith("_type.py")
            and not file_path.name.endswith("_types.py")
        ):
            continue
        old_path = file_path
        new_path = base_enums_path / file_path.name.replace("_enum.py", ".py").replace("_code.py", ".py").replace(
            "_type.py",
            ".py",
        ).replace("_types.py", ".py")

        shutil.copy(str(old_path), str(new_path))
        enums_moved[file_path.name] = str(new_path)
    return enums_moved


def copy_base_types_python_client_bindings(base_generation_path: str, output_path: str) -> dict[str, str]:
    base_types_path = Path(output_path) / "types"

    base_types_path.mkdir(parents=True, exist_ok=True)

    types_moved: dict[str, str] = {}
    models_path = Path(base_generation_path) / "models"
    for file_path in models_path.iterdir():
        if (
            file_path.name.endswith("_error.py")
            or file_path.name.endswith("_attr.py")
            or file_path.name.endswith("_request.py")
            or file_path.name.endswith("_response.py")
            or file_path.name.endswith("_error.py")
            or file_path.name.endswith("_enum.py")
            or file_path.name.endswith("_type.py")
            or file_path.name.endswith("_types.py")
            or file_path.name.endswith("_code.py")
            or file_path.name.endswith("_component.py")
            or file_path.name == "__init__.py"
        ):
            continue
        old_path = file_path
        new_path = base_types_path / file_path.name

        shutil.copy(str(old_path), str(new_path))
        types_moved[file_path.name] = str(new_path)
    return types_moved


def inject_hive_client(output_path: str) -> None:
    """Inject the Hive client into the generated Python client bindings."""
    for file_path in (Path(output_path) / "types").iterdir():
        if not file_path.name.endswith(".py"):
            continue
        with open(file_path) as f:
            content = f.read()
        assert re.search(r"(\@\_attrs\_define\s+class\s+\w+\:\s+\"\"\".+?\"\"\"\s+)", content, re.DOTALL) is not None, (
            file_path.name
        )
        content = re.sub(
            r"(\@\_attrs\_define\s+class\s+\w+\:\s+\"\"\".+?\"\"\"\s+)",
            r'\1hive_client: "HiveClient"\n    ',
            content,
            count=0,
            flags=re.DOTALL,
        )
        content = (
            """from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    from client import HiveClient\n""" + content
        )
        content = content.replace("from ..types import UNSET, Unset", "from src.common import UNSET, Unset")
        content = content.replace(
            "def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:",
            'def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:',
        )
        content = content.replace(
            """ = cls(
            id=id,""",
            """ = cls(
            hive_client=hive_client,
            id=id,""",
        )
        # Write the modified content back to the file
        with open(file_path, "w") as f:
            f.write(content)


def copy_base_python_client_bindings(base_generation_path: str, output_path: str) -> None:
    """Copy the generated Python client bindings to the specified output path.

    This function moves the generated enums from the base generation path to the output path.

    Args:
        base_generation_path (str): The path where the base Python client bindings are generated.
        output_path (str): The path where the client bindings should be copied.

    """
    print("Copying base Python client bindings to the appropriate directory...")
    enums = copy_base_enums_python_client_bindings(base_generation_path, output_path)
    types_ = copy_base_types_python_client_bindings(base_generation_path, output_path)
    inject_hive_client(output_path)


def main():
    generated_path = generate_base_python_client_bindings()
    copy_base_python_client_bindings(generated_path, "./src/")


if __name__ == "__main__":
    main()

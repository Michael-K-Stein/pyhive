
# pyhive — a stupid simple Hive Python API

Lightweight, no-fuss Python client for the Hive service used in this repo. It exposes a small, synchronous HTTP client (as a context manager) and typed model objects for common Hive resources like programs, subjects, modules, exercises and users.

## Highlights
- Minimal, dependency-light wrapper around the Hive API
- Generator-based list endpoints for memory-efficient iteration
- Typed model objects under `src.types` for convenience

## Install
This project uses plain Python. From the repository root you can install the development requirements or install the package locally.

1) Create and activate a virtualenv (recommended)

Windows (PowerShell):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```pwsh
pip install -r requirements.txt
# or install the package in editable mode
pip install -e .
```

## Quickstart
The main client class is `HiveClient` in `pyhive.client`. It is used as a context manager to ensure proper session/login handling.

Example — list programs and print their ids and names:

```python
from pyhive.client import HiveClient

USERNAME = "yourusername"
PASSWORD = "yourpassword"
HIVE_URL = "https://hive.example.com"

with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	for program in client.get_course_programs():
		print(program.id, program.name)
```

Example — fetch a program by id:

```python
with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	program = client.get_program(42)
	print(program.name, program.description)
```

Notes on generators: list-style endpoints (e.g. `get_course_programs`, `get_exercises`, `get_users`, `get_classes`) return generators of typed model objects — iterate over them or convert to a list if you need random access.

## API contract (short)
- Initialization: `HiveClient(username: str, password: str, hive_url: str, **kwargs)`
- Common methods return either a single typed object (e.g. `get_program(id)`) or a generator of objects (e.g. `get_course_programs()`)
- Model classes provide `.from_dict(...)` constructors and are found under `src.types`.

Error handling: HTTP-level errors raised by the underlying request logic will surface; catch exceptions around client calls as needed.

## Tests
Run the unit tests with pytest from the repository root:

```pwsh
pip install -r requirements.txt
pytest -q
```

## Contributing
- Open an issue or PR for changes
- Keep changes focused and small; prefer adding tests for new behavior

## Files of interest
- `pyhive/client.py` — the high-level client class you will use
- `src/types/` — typed model objects created from API responses
- `tests/` — unit tests and examples of client usage

## License
This repository does not include a formal license file. Add a LICENSE if you plan to publish or share this package.

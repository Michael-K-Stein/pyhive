# pyhive — a stupid-simple Hive API client

pyhive is a tiny, intentionally "stupid simple" Python client for the Hive API. Its goal is to provide a minimal, predictable, and dependency-light way to do the common Hive operations you actually need — no magic, no heavy abstractions, just small typed models and straightforward methods built on top of httpx.

Key principles
- Stupid simple: small surface area and obvious behaviour.
- Minimal dependencies: built on httpx and standard typing.
- Keep it practical: convenience helpers for common endpoints, but no sweeping frameworks.

Compatibility
- Python 3.11+

Installation

Install the published distribution from PyPI:

```bash
pip install pyhive
```

Quick start

```python
from pyhive.client import HiveClient

hive_url = "https://your-hive.example"

with HiveClient("username", "password", hive_url) as client:
	# List programs
	for program in client.get_course_programs():
		print(program)

	# Get a specific class
	cls = client.get_class(123)
	print(cls)

	# List exercises for a module
	for ex in client.get_exercises(parent_module__id=456):
		print(ex)

	# Use other helpers (get_subject, get_module, get_users, etc.)

```

What you get
- A single client class `HiveClient` that handles authentication and HTTP calls.
- Typed simple models (Program, Subject, Module, Exercise, Class, User, FormField, ...) with `.from_dict()` helpers used by the client.
- Generator-based list methods so you can iterate without loading everything into memory immediately.

When to use this library
- When you need a straightforward scriptable interface to Hive for small automation tasks, tooling, or glue code.
- When you want something small and easy to understand rather than a big ORM-like SDK.

Notes and caveats
- This project is intentionally minimal. It is not a full-featured SDK that shields you from all API behaviour — it exposes simple typed objects and helpers.
- The package layout in this repository currently provides the module as `hiveapi` while the distribution name is `pyhive`. If you prefer `pyhive` as the import name, we can add a small shim package or rename the package, but that is a separate change.
- The library uses httpx under the hood; you can pass httpx-aware options (like `verify=False`) to the `HiveClient` constructor where supported.

Contributing

Contributions are welcome. Keep changes focused and low-risk. If you add features consider:

- Keeping the API surface small and explicit.
- Adding tests for new behaviors.
- Updating type hints.

Development

To build a wheel locally:

```bash
python -m build -w
```

To run tests (install dev dependencies first):

```bash
pip install -e .[dev]
pytest -q
```

License

MIT — see the LICENSE file for details.

Contact

Maintainer: Michael K. Steinberg <m.kuper.steinberg@gmail.com>

Enjoy — keep it simple. ❤️

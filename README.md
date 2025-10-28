## PyHive — a minimal Hive API client for Python

PyHive (package: `PyHiveLMS`) is a small, synchronous Python client for the Hive LMS API. It provides:

- A simple `HiveClient` you use as a context manager to handle authentication and the HTTP session.
- Generator-based list endpoints for memory-efficient iteration of large result sets.
- Typed model objects (in `src/types`) for convenient access to API response fields.

This README focuses on how to use the library as an application developer or data consumer of a Hive installation.

## Install

Install from PyPI. It's recommended to use a virtual environment.

Using pip (PyPI):

```pwsh
pip install PyHiveLMS
```


## Quickstart — connect and list resources

The primary entry point is `HiveClient`. It accepts your Hive username, password and the base URL for your Hive instance. Use it as a context manager to ensure the underlying HTTP session is closed cleanly.

Example — list programs and print name/ID:

```python
from pyhive import HiveClient

USERNAME = "Mentor123"
PASSWORD = "Password1"
HIVE_URL = "https://hive.org"

with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	for program in client.get_programs():
		print(program.id, program.name)
```

Example — fetch a program, its subjects and modules:

```python
from pyhive import HiveClient

with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	program = client.get_program(42)
	print("Program:", program.name)

	# list subjects for the same program
	subjects = list(client.get_subjects(parent_program__id__in=[program.id]))
	for subject in subjects:
		print(" -", subject.id, subject.name)

	# modules for the first subject
	if subjects:
		for module in client.get_modules(parent_subject=subjects[0]):
			print("   *", module.id, module.name)
```

Example — find exercises in a module and read their form fields:

```python
with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	# you can pass ids or model objects to filter helpers
	module = client.get_module(123)
	for exercise in client.get_exercises(parent_module=module):
		print(exercise.id, exercise.name)
		for field in client.get_exercise_fields(exercise):
			print("     field:", field.id, field.label)
```

Example — list assignments for a user and read responses:

```python
with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
	assignments = client.get_assignments(user__id__in=[55])
	for a in assignments:
		print("Assignment:", a.id, a.exercise_name)
		for resp in client.get_assignment_responses(a):
			print("  response:", resp.id, resp.submitted_by)
```

## Filtering and convenience

- List endpoints (`get_programs`, `get_subjects`, `get_modules`, `get_exercises`, `get_assignments`, `get_users`, etc.) accept filter keyword arguments that are forwarded to the API. Use `id__in`, `parent_program__id__in`, `queue__id`, and the other documented kwargs to restrict results.
- Many methods accept either an integer id or a model instance. For example `client.get_exercise_fields(exercise_id_or_model)` accepts either.

## Error handling

Network and HTTP errors are surfaced from the underlying `httpx` client. Typical patterns:

```python
from httpx import HTTPError

try:
	with HiveClient(USERNAME, PASSWORD, HIVE_URL) as client:
		programs = list(client.get_programs())
except HTTPError as exc:
	print("Network/HTTP error:", exc)
```

Model parsing errors will raise normal Python exceptions — wrap calls where you need robust failure handling.

## Common methods (short reference)

- HiveClient(username, password, hive_url, **kwargs) — construct and authenticate client
- get_programs(...)
- get_program(program_id)
- get_subjects(...)
- get_modules(...)
- get_exercises(...)
- get_exercise(exercise_id)
- get_exercise_fields(exercise)
- get_assignments(...)
- get_assignment(assignment_id)
- get_assignment_responses(assignment)
- get_users(...)
- get_classes(...)

Return values are typed model objects from `src/types` or generators of those objects.

## Try it locally / Run tests

Install dev dependencies and run tests with pytest:

```pwsh
pip install -r requirements.txt
pip install -e .
pytest -q
```

## Troubleshooting

- Authentication errors: verify username/password and the `hive_url` base. The client authenticates at construction.
- SSL verification: pass `verify=False` to the client constructor for self-signed servers (not recommended for production).

## Contributing & development

- Tests live under `tests/` and show common usage patterns. Use them as examples.
- The typed models are in `src/types` and the `HiveClient` convenience layer is in `pyhive/client.py`.

If you plan to make changes, please add tests for new behavior and keep changes small and focused.

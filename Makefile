.PHONY: linter
linter:
	@poetry run ruff -q tests src/calc

.PHONY: fmt
fmt:
	@.venv/bin/black tests src
	@poetry run ruff -q tests src/calc --fix
# @.venv/bin/mypy tests f

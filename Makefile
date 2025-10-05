install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

package-reinstall: build package-install

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games

brain-games:
	uv run brain-games
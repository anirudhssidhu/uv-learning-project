"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """UV demo."""


if __name__ == "__main__":
    main(prog_name="uv-learn-project")  # pragma: no cover

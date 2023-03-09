"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Enterprise Flask."""


if __name__ == "__main__":
    main(prog_name="enterprise-flask")  # pragma: no cover

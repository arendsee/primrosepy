from primrosepy.version import __version__
import click
import os
import signal
import sys
from typing import TextIO

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(name="worstsort")
@click.option(
    "--input-file",
    help="The file to be sorted",
    type=click.File("r"),
    default=sys.stdin,
)
def sort_cmd(input_file : TextIO) -> None:
    """
    Sort a list in the worst way ever.

    The input may be either a filename or STDIN.
    """

    from primrosepy.alg import worstsort

    with input_file:
        lines = [line.strip() for line in input_file.readlines()]
        for line in worstsort(lines):
            print(line)


@click.group("alg", context_settings=CONTEXT_SETTINGS)
def primrose_alg() -> None:
    """
    Algorithm examples.

    This is a more verbose explanation of what examples there are
    """
    pass


primrose_alg.add_command(sort_cmd)


@click.group(help="The Primrose Path for Python", context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, "-v", "--version", message=__version__)
def cli() -> None:
    pass


cli.add_command(primrose_alg)


def main() -> None:
    cli()


if __name__ == "__main__":
    if os.name == "posix":
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()

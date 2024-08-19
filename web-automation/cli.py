import asyncio

import click

from .api import add_access


@click.group()
def cli():
    pass


@click.command()
@click.argument("user")
@click.argument("script")
@click.argument("until", required=False)
def add(user, script, until):
    script_fullname = None
    if script == "1":
        script_fullname = "Script1"
    elif script == "2":
        script_fullname = "Script2"
    else:
        raise ValueError(f"Wrong script name {script}! Choose '1' or '2'")

    trial = False
    expiration = None
    if until:
        if until == "t":
            trial = True
        elif until.isnumeric():
            expiration = until

    result = asyncio.run(add_access(script_fullname, user, trial, expiration))
    click.echo(result)


if __name__ == "__main__":
    cli()

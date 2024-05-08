import click
import os


"""
# multi commmand format
@click.group()
def cli():
    pass


@cli.command()
def func1():
    pass
"""


def get_remote_server_address(server):
    if server == "swan":
        return "jyesselm@swan.unl.edu"
    else:
        raise ValueError("Server not recognized")


def get_remote_server_path(server):
    if server == "swan":
        return "/work/yesselmanlab/jyesselm"
    else:
        raise ValueError("Server not recognized")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("server")
@click.argument("local_path")
@click.argument("remote_path", default="")
def put(server, local_path, remote_path):
    server_address = get_remote_server_address(server)
    server_path = get_remote_server_path(server)
    if remote_path.startswith("~/"):
        remote_path = remote_path[2:]
    if not remote_path.startswith(server_path):
        remote_path = server_path + "/" + remote_path
    os.system(f"scp -r {local_path} {server_address}:{remote_path}")


@cli.command()
@click.argument("server")
@click.argument("remote")
def get(server, remote):
    server_address = get_remote_server_address(server)
    server_path = get_remote_server_path(server)
    if remote_path.startswith("~/"):
        remote_path = remote_path[2:]
    if not remote_path.startswith(server_path):
        remote_path = server_path + "/" + remote_path
    os.system(f"scp -r {server_address}:{remote_path} .")


if __name__ == "__main__":
    cli()

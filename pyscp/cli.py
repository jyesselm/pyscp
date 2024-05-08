import click
import os


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


@click.command()
@click.argument("server")
@click.argument("path_1")
@click.argument("path_2", default="")
def cli(server, path_1, path_2):
    server_address = get_remote_server_address(server)
    server_path = get_remote_server_path(server)
    # assume get
    if path_2 == "":
        print("getting file: ", path_1)
        local_path, remote_path = path_2, path_1
    # assume put
    else:
        print("putting" + path_1 + " to remote path " + path_2)
        local_path, remote_path = path_1, path_2
    if remote_path.startswith("~/"):
        remote_path = remote_path[2:]
    if not remote_path.startswith(server_path):
        remote_path = server_path + "/" + remote_path
    if local_path == "":
        os.system(f"scp -r {server_address}:{remote_path} .")
    else:
        os.system(f"scp -r {local_path} {server_address}:{remote_path}")


if __name__ == "__main__":
    cli()

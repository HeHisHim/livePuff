import socket
import asyncio
import click


@click.group()
def cli():
    pass


async def server(loop, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, address = await loop.sock_accept(sock)
        print("connect from ", address)
        # loop.create_task(handler(loop, client))
        await handler(loop, client)


async def handler(loop, client):
    with client:
        while True:
            try:
                data = await loop.sock_recv(client, 1024)
                if not data:
                    break
                await loop.sock_sendall(client, str.encode("Hello: ") + data)
            except Exception as e:
                client.close()
                print("connection closed")
                break


@cli.command(name="server")
def launch_server():
    loop = asyncio.get_event_loop()
    loop.create_task(server(loop, ("0.0.0.0", 8080)))
    loop.run_forever()


@cli.command(name="client")
def launch_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("0.0.0.0", 8080))
    client.send(b"hello")
    while True:
        data = client.recv(1024)
        if data:
            print(data)
        else:
            break
    client.close()


if "__main__" == __name__:
    cli()

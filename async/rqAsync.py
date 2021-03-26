import socket
import asyncio
import click
import time


@click.group()
def cli():
    pass


async def server(loop, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    print("Server Start")
    while True:
        client, address = await loop.sock_accept(sock)
        print("connect from ", address)
        loop.create_task(handler(loop, client))  # 再次create_task, 相当于loop有server(), handler()两个协程函数. 遇到await会交出主动权去处理server或者handler
        # await handler(loop, client) # 如果这样调用, loop里面相当于只有一个协程函数, 相当于同步调用. 会阻塞在handler


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
    while True:
        client.send(b"hello")
        time.sleep(0.5)
        data = client.recv(1024)
        if not data:
            break
        print(data)
    client.shutdown()


if "__main__" == __name__:
    cli()

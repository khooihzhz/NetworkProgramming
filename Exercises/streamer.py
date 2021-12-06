#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter05/streamer.py
# Client send file and filename with struct and length-prefix framing

# Client -> Filename
# Server <- Filename
# Client -> md5sum(file)
# Client -> file data (test.txt)
# Server <- file data (test.txt)
# Server <- calculate md5(sum)

import socket
from argparse import ArgumentParser
import struct
from md5hash import scan

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    
    # print('Run this script in another window with "-c" to connect')
    print('run with -f and a file name to upload the file to the server')
    print('Listening at', sock.getsockname())
    sc, sockname = sock.accept()
    print('Accepted connection from', sockname)
    sc.shutdown(socket.SHUT_WR)
    

    len_buf = socket_read_n(sc, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    filename = socket_read_n(sc, msg_len)

    print(f"Filename Received = {filename.decode()}")

    f = open('server/'+filename.decode(), 'wb')
    len_buf = socket_read_n(sc, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    data = socket_read_n(sc, msg_len)
    f.write(data)
    f.close()
    # check md5 sum
    print(scan(f'server/{filename.decode()}'))

    print('file received .... end')
    sc.close()
    sock.close()


def client(address, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)

    # Send File name (CONSTANT SIZE = 8 BYTES ?)
    message = str(filename).encode()
    packed_len = struct.pack('>L', len(message))
    sock.sendall(packed_len + message)

    # Read file name function here
    # read file in binary, check md5sum
    print(scan(filename))
    f = open(filename, 'rb')
    # READ DATA
    data = f.read()
    packed_data = struct.pack('>L', len(data))
    sock.sendall(packed_data + data)
    f.close()
    sock.close()
    
def socket_read_n(sock, n):
    """ Read exactly n bytes from the socket.
        Raise RuntimeError if the connection closed before
        n bytes were read.
    """
    buf = b''
    while n > 0:
        data = sock.recv(n)
        if data == '':
            raise RuntimeError('unexpected connection close')
        buf += data
        n -= len(data)
    return buf

if __name__ == '__main__':
    parser = ArgumentParser(description='Transmit & receive a data stream')
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',
                        help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-f', type=str, metavar='filename', default=None, help='upload file to server')
    # ues filename as argument to whether run client or server
    # parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060,
                        help='TCP port number (default: %(default)s)')
    args = parser.parse_args()

    if args.f is not None:
        # PASS FILENAME HERE
        client((args.hostname, args.p), args.f)
    else:
        server((args.hostname, args.p))


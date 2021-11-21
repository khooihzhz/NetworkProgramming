#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_deadlock.py
# TCP client and server that leave too much data waiting

import argparse, socket, sys

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)  # send it back uppercase
            n += len(data)
            print(f'{n} bytes processed so far')
        print()
        sc.close()
        print('Socket closed')

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))  

    while True:
        message = input("Enter Message: ")
        message = message.encode('ascii')
        sent = len(message)

        if sent > 0:
            sock.sendall(message)   
            print(f'{sent} bytes sent ')
            sys.stdout.flush()
        else: 
            sock.shutdown(socket.SHUT_WR)
            print()
            break
        
        print('Receiving all the data the server sends back')

        received = 0
        while received < sent :
            data = sock.recv(1024)
            if not received:
                print('The first data received says', repr(data))
            if not data:
                break
            received += len(data)
        print(f'{received} bytes received')

        print()
    
    sock.close()

if __name__ == '__main__':
    roles = ('client', 'server')
    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')
    parser.add_argument('role', choices=roles, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    if args.role == 'client':
        client(args.host, args.p)
    else:
        server(args.host, args.p)
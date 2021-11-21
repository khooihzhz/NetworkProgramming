#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/getname.py

import socket
import sys

def main(hostname):
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))

if __name__ == '__main__':
    print(sys.argv[0], sys.argv[1])
    main(sys.argv[1])

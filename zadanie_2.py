# Написать метод int32_to_ip, который принимает на вход 32-битное целое число
# (integer) и возвращает строковое представление его в виде IPv4-адреса:
import socket
import struct


def int32_to_ip(int32):
    packedIP = socket.inet_ntoa(struct.pack('!L', int32))
    return packedIP


if __name__ == '__main__':
    print(int32_to_ip(2154959208))
    print(int32_to_ip(0))
    print(int32_to_ip(2149583361))

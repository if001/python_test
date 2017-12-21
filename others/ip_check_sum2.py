import socket, struct
from ctypes import *


SRC_IP = "45.32.43.206"
DST_IP = "198.13.47.60"

SRC_PORT = 81
DST_PORT = 92

WINDOWSIZE = 8192


class tcphdr(Structure):
    _fields_ = [
            ("src_port", c_uint16),
            ("dst_port", c_uint16),
            ("seq", c_uint32),
            ("ack_seq", c_uint32),
            ("res1", c_uint16, 4),#little endian. from here 
            ("doff", c_uint16, 4),
            ("fin", c_uint16, 1),
            ("syn", c_uint16, 1),
            ("rst", c_uint16, 1),
            ("psh", c_uint16, 1),
            ("ack", c_uint16, 1),
            ("urg", c_uint16, 1),
            ("ece", c_uint16, 1),
            ("cwr", c_uint16, 1),#to here

            #("doff", c_uint16, 4),#big endian. from here
            #("res1", c_uint16, 4),
            #("cwr", c_uint16, 1),
            #("ece", c_uint16, 1),
            #("urg", c_uint16, 1),
            #("ack", c_uint16, 1),
            #("psh", c_uint16, 1),
            #("rst", c_uint16, 1),
            #("syn", c_uint16, 1),
            #("fin", c_uint16, 1),#to here

            ("window", c_uint16),
            ("check", c_uint16),
            ("urg_ptr", c_uint16),
            ]

    def pack(self):
        return buffer(self)[:]


class dummy_iphdr(Structure):
    _fields_ = [
            ("src_ip", c_uint32),
            ("dst_ip", c_uint32),
            ("pad", c_uint8),
            ("protocol", c_uint8),
            ("len", c_uint16),
            ]

    def pack(self):
        return buffer(self)[:]


def ip2int(ip_addr):
    #return struct.unpack("!I", socket.inet_aton(ip_addr))[0]
    #inet_aton returns ip_addr in network byte order. so the '!' above is not required.
    return struct.unpack("I", socket.inet_aton(ip_addr))[0]


def calc_checksum(TCPheader):
    IPheader = dummy_iphdr()
    IPheader.src_ip = ip2int(SRC_IP)
    IPheader.dst_ip = ip2int(DST_IP)
    IPheader.pad = 0
    IPheader.protocol = 6
    IPheader.len = socket.htons(20)
    IPheader_packed = IPheader.pack()

    checksum = 0

    for i in xrange(len(IPheader_packed) / 2):
        temp = struct.unpack("H", IPheader_packed[:2])[0]
        checksum += temp
        IPheader_packed = IPheader_packed[2:]

    TCPheader_packed = TCPheader.pack()

    for i in xrange(len(TCPheader_packed) / 2):
        temp = struct.unpack("H", TCPheader_packed[:2])[0]
        checksum += temp
        TCPheader_packed = TCPheader_packed[2:]

    carry = (checksum >> 16) & 0xffff

    checksum = ~((checksum & 0xffff) + carry)

    return checksum


def build_tcp_syn_packet():
    TCPheader = tcphdr()

    TCPheader.src_port = socket.htons(SRC_PORT)
    TCPheader.dst_port = socket.htons(DST_PORT)

    TCPheader.seq = 54321 #a random number mihgt be better
    TCPheader.doff = len(TCPheader.pack()) / 4

    TCPheader.fin = 0
    TCPheader.syn = 1
    TCPheader.rst = 0
    TCPheader.psh = 0
    TCPheader.ack = 0
    TCPheader.urg = 0
    TCPheader.ece = 0
    TCPheader.cwr = 0

    TCPheader.check = 0
    TCPheader.window = socket.htons(WINDOWSIZE)
    TCPheader.urg_ptr = 0

    TCPheader.check = calc_checksum(TCPheader)
    print(TCPheader.check)
    return TCPheader


def send_syn_packet():
    syn_packet = build_tcp_syn_packet().pack()
    exit(0)

    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    sock.sendto(syn_packet, (DST_IP, DST_PORT))

    sock.close()


def main():
    send_syn_packet()


if __name__ == "__main__":
    main()

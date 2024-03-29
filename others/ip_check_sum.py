import struct

data = "45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1"
data = "45 00 00 28 00 00 40 00 10 06 00 00 2d 20 2b ce c6 0d 2f 3c"

data = "45 00 00 28 00 00 40 00 10 06 00 00 2d 20 2b ce c6 0d 2f 3c"


def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff

data = data.split()
data = map(lambda x: int(x,16), data)
data = struct.pack("%dB" % len(data), *data)
print(' '.join('%02X' % ord(x) for x in data))
print("Checksum: 0x%04x" % checksum(data))

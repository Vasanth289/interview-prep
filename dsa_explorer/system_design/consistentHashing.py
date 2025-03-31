import hashlib

SERVER_COUNT = 4

servers = [f's_{i}' for i in range(SERVER_COUNT)]

for s in servers:
    print(s.encode())
    print(f'{s} -> {hashlib.sha1(s.encode()).hexdigest()}')
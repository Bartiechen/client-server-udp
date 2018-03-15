import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print sys.argv[1]

server_address = (sys.argv[1], 10000)
message = 'Champion World Cup Soccer 2018.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'THE CHAMPION IS "%s"' % data

finally:
    print >>sys.stderr, 'closing connection'
    sock.close()

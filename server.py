import socket
import sys
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (sys.argv[1], 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

nationalTeams = [ "Russia","Brasil","Ira","Coreia do Sul","Japao", "Arabia Saudita", "Australia", "Tunisia", "Nigeria", "Marrocos", "Senegal", "Egito", "Mexico", "Costa Rica", "Panama", "Uruguai", "Argentina", "Colombia","Peru", "Franca", "Portugal", "Alemanha", "Servia", "Polonia", "Inglaterra", "Espanha", "Belgica", "Islandia", "Suica", "Croacia", "Suecia", "Dinamarca" ]

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    
    randNumber = random.randrange(32)
    nationalTeam = nationalTeams[randNumber]
    data = nationalTeam

    print data

    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)


import argparse
import random
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
import math
from pythonosc import dispatcher
from pythonosc import osc_server
import numpy


d = 8
life = numpy.zeros((d, d), dtype=numpy.byte)
messages = []
client = udp_client.UDPClient("127.0.0.1", 5005)
dispatcher = dispatcher.Dispatcher()

# this function does all the work
def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Rule 2
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Rule 1 and 3
            elif n == 3:
                b[x, y] = 1 # Rule 4
    print("In play life")
    return(b)


def setMatrixCtrl(life):
  for i in range(d):
    for j in range(d):
      a = str(i) + " " + str(j) + " " + str(life[j][i])
      message = osc_message_builder.OscMessageBuilder(address = "/board")
      message.add_arg(a)
      message = message.build()
      client.send(message)

def handle_generation(unused_addr,args):
    global life
    life = play_life(life)
    setMatrixCtrl(life)
    print(life)



# now let's play
"""
print(life)
for i in range(2):
    life = play_life(life)
"""

def init(a):
    # place starting conditions here
    a[2, 1:4] = 1 # a simple "spinner"
    return a


#Main Functionality
life = init(life)
print(life)

#set up server to listen for udp commands
parser = argparse.ArgumentParser()
parser.add_argument("--ip",
default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",
type=int, default=5006, help="The port to listen on")
args = parser.parse_args()
dispatcher.map("/generate",handle_generation,life)

server = osc_server.ThreadingOSCUDPServer(
(args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()

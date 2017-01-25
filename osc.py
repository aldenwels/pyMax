from pythonosc import osc_message_builder
from pythonosc import udp_client

messages = []
client = udp_client.UDPClient("127.0.0.1", 5005)

def createMessage(m,a):
  message = osc_message_builder.OscMessageBuilder(address = m)
  message.add_arg(a)
  message = message.build()
  messages.append(message)

def printMessages():
  for m in messages:
    client.send(m)

if __name__ == "__main__":
  createMessage("/one","test")
  createMessage("/two","new")
  printMessages()

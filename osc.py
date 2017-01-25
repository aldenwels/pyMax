from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  client = udp_client.UDPClient("127.0.0.1", 5005)
  msg = osc_message_builder.OscMessageBuilder(address = "/hey")
  msg.add_arg("something special")
  msg = msg.build()
  client.send(msg)

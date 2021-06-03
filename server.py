import socket

# from gpiozero import LED
from dotenv import load_dotenv
import os
import log

load_dotenv()

# led = LED(17)
port = int(os.getenv("PORT"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((socket.gethostname(), port))
    log.info(f"Binded to port {port}")
except Exception as e:
    log.danger(f"Failed to bind to port {port}, {e}")

s.listen(5)
log.good("Listening...")

while True:
    clientsocket, address = s.accept()
    log.info(f"Connection from {address[0]} has been established.")
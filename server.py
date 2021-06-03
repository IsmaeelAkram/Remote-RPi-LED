import socket

from gpiozero import LED
from dotenv import load_dotenv
import os
import log

load_dotenv()

led = LED(17)
port = int(os.getenv("SERVER_PORT") or 6352)

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

    while True:
        msg = clientsocket.recv(1024).decode("utf-8")

        if not msg:
            break

        log.info("Received " + msg)
        if msg == "on":
            led.on()
            log.info("Turned LED on")
        elif msg == "off":
            led.off()
            log.info("Turned LED off")

    clientsocket.close()
    log.info("Closed connection from " + address[0])
import socket
from dotenv import load_dotenv
import os
import log
from pynput.keyboard import Key, Listener

load_dotenv()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = os.getenv("SERVER_ADDRESS") or socket.gethostname()
server_port = int(os.getenv("SERVER_PORT") or 6352)

s.connect((server_address, server_port))


def on_press(key: Key):
    if key == Key.esc:
        s.send(bytes("on", "utf-8"))
        log.info("Sent on request")


def on_release(key):
    if key == Key.esc:
        s.send(bytes("off", "utf-8"))
        log.info("Send off request")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

s.close()
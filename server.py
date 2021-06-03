import socket
from gpiozero import LED
from dotenv import load_dotenv

load_dotenv()

led = LED(17)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Waiting for card...")
    id, text = reader.read()
    # Convert the integer UID to a list of bytes
    uid_bytes = [(id >> (8 * i)) & 0xFF for i in range(3,-1,-1)]
    print("Raw ID integer:", id)
    print("UID as list of bytes:", uid_bytes)
    print("Text on card:", text)
finally:
    GPIO.cleanup()

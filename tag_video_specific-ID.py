#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import subprocess
import os

os.environ["DISPLAY"] = ":0"  # ensure VLC knows which desktop to use

reader = SimpleMFRC522()

# Replace with the UID integer of your authorized card
AUTHORIZED_UID = 3654321  

try:
    print("Waiting for authorized card...")
    while True:
        id, text = reader.read()
        print("Detected UID:", id)
        if id == AUTHORIZED_UID:
            print("Authorized card! Playing video...")
            subprocess.run([
                "cvlc",
                "--fullscreen",
                "--no-video-title-show",
                "--play-and-exit",
                "/home/hackspace/Desktop/videos/myvideo.mp4"
            ])
        else:
            print("Unauthorized card. Ignoring.")
finally:
    GPIO.cleanup()

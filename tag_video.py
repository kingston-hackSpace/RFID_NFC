#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import subprocess
import os

os.environ["DISPLAY"] = ":0"

reader = SimpleMFRC522()
try:
    print("Waiting for card...")
    while True:
        id, text = reader.read()
        print("ID:", id)
        print("Text:", text)
        subprocess.run([
            "cvlc",
            "--fullscreen",
            "--no-video-title-show",
            "--play-and-exit",
            "/home/hackspace/Desktop/videos/myvideo.mp4"
        ])
finally:
    GPIO.cleanup()

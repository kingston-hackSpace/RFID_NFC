#!/usr/bin/env python3
import os
import subprocess
from pirc522 import RFID

os.environ["DISPLAY"] = ":0"

rdr = RFID()
allowed_uid = [123, 45, 67, 89]  # replace with your card's UID

print("Waiting for authorized card...")

try:
    while True:
        rdr.wait_for_tag()
        error, tag_type = rdr.request()
        if not error:
            error, uid = rdr.anticoll()
            if not error:
                print("Detected UID:", uid)
                if uid == allowed_uid:
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
except KeyboardInterrupt:
    print("Exiting...")

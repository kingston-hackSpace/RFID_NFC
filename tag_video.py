#!/usr/bin/env python3
from pirc522 import RFID
import subprocess

rdr = RFID()
print("Waiting for card...")

try:
    while True:
        rdr.wait_for_tag()
        error, tag_type = rdr.request()
        if not error:
            print("Card detected!")
            error, uid = rdr.anticoll()
            if not error:
                print("UID:", uid)
                # Play video with VLC
                subprocess.run(["cvlc", "--play-and-exit", "myvideo.mp4"])
except KeyboardInterrupt:
    print("Exiting...")

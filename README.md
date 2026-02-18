# RFID & NFC Communication

Start by [watching this video](https://www.youtube.com/watch?v=VpEVkiMU18s&t=209s)

Read more: [Understanding RFID/NFC](https://www.sparkfun.com/rfid)

## RFID

RFID (Radio Frequency Identification) is a way for two devices very close to each other to communicate. 

If you’ve ever used a mobile payments app like Apple Pay or Google Pay, or a contactless bank card, you’ve used RFID technology. RFID is a proximity-based wireless communication standard. Unlike Wi-Fi or Bluetooth, interaction is limited to an extremely short range. 

It allows: quickly transfer data, or instantly pair with Bluetooth devices like headphones and speakers.

 RFID can be [active or passive](https://learn.sparkfun.com/tutorials/connectivity-of-the-internet-of-things#rfid-and-nfc). Read more here.

## NFC 

NFC (Near Field Communication) it's an evolution of RFID, so anything you can do with RFID you can do with NFC, the difference is that it has a much lower transmission range (a few centimeters).

## How does it work?

Both RFID and NFC operate on the principle of inductive coupling, at least for short-range implementations. This essentially involves a reader device passing an electric current through a coil, which in turn generates a magnetic field. When you bring a tag near the reader, the magnetic field then induces an electric current within the tag — without any wires or even physical contact. Once the initial handshake is complete, stored data on the tag is wirelessly transmitted to the reader.

Every RFID system consists of three components: a scanning antenna, a transceiver and a transponder. he RFID reader is a network-connected device, such as an Arduino, a Raspberry Pi, or your smartphone. The transponder is in the RFID tag itself. 

Depending on your tag, it can only read data, or read and write. 

## Purchase
 
[RFID/NFC from The Pi Hut](https://thepihut.com/search?q=rfid&narrow_by=&sort_by=relevency&page=1)

[RFID/NFC from Pimoroni](https://shop.pimoroni.com/search?q=rfid)
 

## Basic Tutorial

**Hardware:**

- Arduino UNO

- RFID module + card tag

- LED + 220 ohms resistor

**Wiring:**

VCC - 3.3V

RST – Pin 9

GND – GND

MISO – Pin 12

MOSI – Pin 11

SCK – Pin 13

NSS – Pin 10

See diagram [here](https://github.com/kingston-hackSpace/RFID_NFC/blob/main/RFID_arduino_connections.webp)

**Code and Instructions:**

- Upload [this code](https://github.com/kingston-hackSpace/RFID_NFC/blob/main/RFID_basic.ino) to your Arduino board.

- Open the Serial Monitor.

- Tap your card on the RFID module.

- In the Serial Monitor, you should see the **UID**, similar to this example: UID tag : F3 B1 50 8C. That ID corresponds to your specific tag card.

- Scroll down the code and replace this line: ((content.substring(1) == "F3 B1 50 8C")) with your own tag ID.

- Save and upload the new code.

- The LED should turn on when you tap the card. 

## Projects / Tutorials for RFID-RC522 MODEL

Follow the text 3 tutorials in order:

1. [Interface RC522 RFID Module with Arduino](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/)

2. [How to Set Up a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)

3. [Tag to play video in a Raspberry Pi](https://github.com/kingston-hackSpace/RFID_NFC/blob/main/tag_video.py)

## Projects / Tutorials  for ADAFRUIT PN532 NFC/RFID controller

*Note: We don't have this equipment at hackSpace.*

[Web NFC](https://learn.adafruit.com/using-webnfc)

[Magic Band - play sound and lights](https://learn.adafruit.com/magic-band-reader?embeds=allow)

[Scannable Links with NFC](https://learn.adafruit.com/scannable-links-with-nfc/overview)

[NFC Raspberry Pi Media Player](https://learn.adafruit.com/nfc-raspberry-pi-media-player)

## Uses

- **Data transfer**

- **Mobile payments**: Most debit and credit cards these days already have an NFC tag built-in.

- **Quick pairing**: NFC’s convenience extends to devices that don’t have a screen. Many wireless speakers and headphones use it to exchange pairing information with your smartphone. Some cameras also use it to quickly initiate a Wi-Fi Direct connection for easy photo and video transfer.

- **Public transport access**

- **Gaming**: Nintendo uses the technology to connect physical toys with video games.

## NFC vs Bluetooth

/*
RFID - RC522 module (Radio Frequency ID)

HARDWARE:
Arduino UNO
RFID module + card tag
LED + 220 ohms resistor
*/
 
#include <SPI.h>
#include <MFRC522.h> //install library
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

#define LED_PIN 6
 
void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  Serial.println("Approximate your card to the reader...");
}

void loop() {
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();

////////////////////////////////////////////////////
// ID data definition 
////////////////////////////////////////////////////
  if (content.substring(1) == "F3 B1 50 8C"){ 
    Serial.println("Authorized access");
    Serial.println();
    digitalWrite(LED_PIN, HIGH);
    delay(1000);
    digitalWrite(LED_PIN, LOW);


  }  else {
    Serial.println(" Access denied");
    Serial.println();
  }
 
 
} 

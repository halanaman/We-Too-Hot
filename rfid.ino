//Include Libraries for RFID
#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
void setup() 
{
  Serial.begin(115200);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  Serial.println("Approximate your card to the reader...");
  Serial.println();
}

void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();
  if (content.substring(1) == "F8 5C 1B 0D") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Card");
    Serial.println();
    delay(3000);
  }
  else if (content.substring(1) == "B3 32 17 B7") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Tag");
    Serial.println();
    delay(3000);
  }
  else if (content.substring(1) == "04 96 57 EA DA 3B 80") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Robin");
    Serial.println();
    delay(3000);
  }
 
 else   {
    Serial.println("Not Registered");
    delay(3000);
  }
} 

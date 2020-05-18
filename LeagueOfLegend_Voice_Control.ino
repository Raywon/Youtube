#include <SoftwareSerial.h>
#include <Keyboard.h>
#include <HID.h>


SoftwareSerial bluetooth(8,7);
 
void setup(){
  Serial.begin(9600);
  bluetooth.begin(9600);
  Keyboard.begin();
}
 
void loop(){
 
  
  if (bluetooth.available()) {
    switch(bluetooth.read()){
      case'A':
      Keyboard.write('q');
      Serial.println("pass");
      delay(10);
      break;

      case'B':
      Keyboard.write('w');
      Serial.println("passaaa");
      delay(10);
      break;

      case'C':
      Keyboard.write('e');
      Serial.println("passaaa");
      delay(10);
      break;

      case'D':
      Keyboard.write('r');
      Serial.println("passaaa");
      delay(10);
      break;

      case'E':
      Keyboard.write('d');
      Serial.println("passaaa");
      delay(10);
      break;

      case'F':
      Keyboard.write('f');
      Serial.println("passaaa");
      delay(10);
      break;
      
      
      
    }
  
   
  }

}

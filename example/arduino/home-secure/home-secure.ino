#include <Bridge.h>


int ledPin = 7;
int rfPin = 0;

void setup() {
  // put your setup code here, to run once:
  
  Bridge.begin();
  
  pinMode(ledPin, OUTPUT);
  pinMode(rfPin, INPUT);
  
  Serial.begin(9600);
  //while (!Serial); // wait for a serial connection
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int rf = digitalRead(rfPin);
  
  Serial.println(rf);
  if(rf==0){
    //no trigger
    //熄滅led
    digitalWrite(ledPin, LOW);  
    
    noTone(8);
    
    Bridge.put("rf", String(rf));
  }
  else{
    
    //trigger
    //點亮led
    digitalWrite(ledPin, HIGH);
    
    tone(8, 784, 500);
    
    Bridge.put("rf", String(rf));
  }
  
  Serial.println("rf");
  delay(1000); 

}

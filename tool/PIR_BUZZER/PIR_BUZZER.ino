
/*PIR("Passive Infrared Sensor") Motion Sensor & Buzzer*/

int PIRSensorPin= 7;     // 偵測PIR訊號
int BZPin = 13;        // Buzzer output or D13 output LED 
 
int sensorValue = 0;         // 假設沒有偵測物的情況為"0"
 
void setup() 
{
  pinMode(PIRSensorPin, INPUT);    //設定腳位組態
  pinMode(BZPin, OUTPUT);       
}
 
void loop()
{
  sensorValue = digitalRead(PIRSensorPin);   // 讀 PIR Sensor 的狀態

  if (sensorValue == HIGH)                
  {              
    digitalWrite(BZPin, HIGH);              // 發現偵測物發出警告
  }
  else 
  {
    digitalWrite(BZPin, LOW);               // 沒發現偵測物,不作動
  }
}


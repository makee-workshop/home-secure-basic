int ledPin = 7; // 第13隻接腳請連接到 LED，以便控制 LED 明滅。

// setup() 函數只會於電源啟動時執行1次
void setup() 
{
  // 設定第 7 支腳為輸出模式
  pinMode(ledPin, OUTPUT);
}

// loop() 函數會不斷的被重複執行
void loop()
{
  digitalWrite(ledPin, HIGH); // 設定PIN7腳位為高電位= 0V ，LED 處於發亮狀態!!
  delay(100); // 等待100 毫秒 (也就是發亮 0.1 秒)
  digitalWrite(ledPin, LOW); // 設定PIN7腳位為低電位= 0V ，LED 處於熄滅狀態!!
  delay(100); // 等待100 毫秒 (也就是熄滅 0.1 秒)
}


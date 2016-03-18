void setup() {
  // put your setup code here, to run once:
  pinMode(0, INPUT);
  Serial.begin(9600);
  while (!Serial); // wait for a serial connection
}

void loop() {
  // put your main code here, to run repeatedly:
  int rf = digitalRead(0);
  Serial.println(rf);
  delay(1000); 
  //Bridge.begin();

}

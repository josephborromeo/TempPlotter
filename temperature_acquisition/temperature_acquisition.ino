unsigned int elapsed;
float t1,t2,t3,t4 = 0;
String message = "";
byte averages = 15;
int delay_time = 100; // default delay

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  delay(500);
  digitalWrite(13, HIGH);

  delay_time = (900/averages);
}

void loop() {
  elapsed += 1;

  for (int i=0; i < averages; i++){
    t1 += random(0,60); // Simulating Read from analog pins
    t2 += random(0,60);
    t3 += random(0,60);
    t4 += random(0,60);
    delay(delay_time);
  }

  t1 /= float(averages);
  t2 /= float(averages);
  t3 /= float(averages);
  t4 /= float(averages);
  
  message = String(elapsed) + " " + String(t1,2) + " " + String(t2,2) + " " + String(t3,2) + " " + String(t4,2);

  t1 = t2 = t3 = t4 = 0;

  Serial.println(message);
  
  delay(50);
  
}

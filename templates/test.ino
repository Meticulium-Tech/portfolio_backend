#include <Bridge.h>
#include <HttpClient.h>
    
    
    // defines pins numbers
    const int trigPin = 9;
    const int echoPin = 10;
    const int buzzer = 11;
    const int ledPin = 13;
    
    // defines variables
    long duration;
    int distance;
    int safetyDistance;
    
    
    void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    pinMode(buzzer, OUTPUT);
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600); // Starts the serial communication
    
    
    }
    
    
    void loop() {
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    
    // Calculating the distance
    distance= duration*0.034/2;
    
    safetyDistance = distance;
    if (safetyDistance <= 5){
      digitalWrite(buzzer, HIGH);
      digitalWrite(ledPin, HIGH);
       HttpClient client;
    
      // Make a HTTP request:
      client.get("http://127.0.0.1:5000/arduino");
    
      // if there are incoming bytes available
      // from the server, read them and print them:
      while (client.available()) {
        char c = client.read();
        Serial.print("Response");
        Serial.print(c.);
      }
     
    
      delay(5000);
    }
    else{
      digitalWrite(buzzer, LOW);
      digitalWrite(ledPin, LOW);
    }
    
    // Prints the distance on the Serial Monitor
    Serial.print("Distance: ");
    Serial.println(distance);
    }
    
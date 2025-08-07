#include <Servo.h>

Servo rightHandServo;
Servo leftHandServo;
Servo headServo;

void setup() {
  Serial.begin(9600);        // Start the serial communication
  rightHandServo.attach(9);  // Connect right-hand servo to pin 9
  leftHandServo.attach(10);  // Connect left-hand servo to pin 10
  headServo.attach(11);      // Connect head servo to pin 11
  Serial.println("Setup complete. Waiting for commands...");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    Serial.println("Received command: " + command);  // Print the received command for debugging
    executeCommand(command);
  }
}

void executeCommand(String command) {
  if (command == "right hand") {
    Serial.println("Executing right hand move");
    for (int angle = 0; angle <= 180; angle += 5) {
      rightHandServo.write(angle);
      delay(20);
    }
    for (int angle = 180; angle >= 0; angle -= 5) {
      rightHandServo.write(angle);
      delay(20);
    }
  } else if (command == "say hi") {
    Serial.println("Executing left hand move");
    for (int angle = 0; angle <= 180; angle += 5) {
      leftHandServo.write(angle);
      delay(20);
    }
    for (int angle = 180; angle >= 0; angle -= 5) {
      leftHandServo.write(angle);
      delay(20);
    }
  } else if (command == "rotate your head") {
    Serial.println("Executing head rotation");
    for (int angle = 0; angle <= 180; angle += 5) {
      headServo.write(angle);
      delay(20);
    }
    for (int angle = 180; angle >= 0; angle -= 5) {
      headServo.write(angle);
      delay(20);
    }
  } else {
    Serial.println("Unknown command: " + command);  // Handle unknown commands
  }
}

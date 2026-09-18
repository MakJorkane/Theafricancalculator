#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
// Height and width
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1 // Reset pin

Adafruit_SH1106G display(
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  &Wire1,
  OLED_RESET
);

void setup() {
  Wire1.setSDA(6); // GP6
  Wire1.setSCL(7); // GP7
  Wire1.begin();
  // Oled adress https://controllerstech.com/arduino-ssd1306-oled-display-tutorial/
  display.begin(0x3C, true);


  // Text methods to use https://www.instructables.com/Arduino-and-the-SSD1306-OLED-I2C-128x64-Display/#:~:text=display.display()%3B-,Text%20methods,-These%20are%20based
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SH110X_WHITE);
  display.setCursor(1, 1); // Basically where u want ur text to start so 1 pixels moved right horizontally and 1 move ddown vertically
  display.print("Hey its me its verity");
  display.display(); // Pls dont forget https://www.instructables.com/Arduino-and-the-SSD1306-OLED-I2C-128x64-Display/#:~:text=The%20Most%20Important%20Bit
}

void loop() {
}
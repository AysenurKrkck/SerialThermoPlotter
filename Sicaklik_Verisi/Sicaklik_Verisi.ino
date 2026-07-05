#include <DHT.h>          // TR: DHT sensör kütüphanesini projeye dahil eder.
                          // EN: Includes the DHT sensor library into the project.

#define DHTPIN 2          // TR: Sensörün data (veri) pininin Arduino üzerinde bağlı olduğu dijital pini (Pin 2) tanımlar.
                          // EN: Defines the digital pin (Pin 2) where the sensor's data pin is connected on the Arduino.

#define DHTTYPE DHT11     // TR: Kullanılan sensör tipinin DHT11 olduğunu belirtir.
                          // EN: Specifies that the type of sensor being used is DHT11.

DHT dht(DHTPIN, DHTTYPE); // TR: Belirlenen pin ve sensör tipiyle bir DHT nesnesi (objesi) oluşturur.
                          // EN: Creates a DHT object with the specified pin and sensor type.

int sicaklik = 0;         // TR: Okunan sıcaklık değerini hafızada tutacak tam sayı değişkeni.
                          // EN: Integer variable to store the read temperature value.

int nem = 0;              // TR: Okunan nem değerini hafızada tutacak tam sayı değişkeni.
                          // EN: Integer variable to store the read humidity value.

String veri;              // TR: Python tarafına virgülle ayrılmış şekilde gönderilecek metin yapısı.
                          // EN: String structure to be sent to the Python side as comma-separated values.

void setup() {
  Serial.begin(9600);     // TR: Seri haberleşmeyi 9600 baud hızında başlatır (Python ile aynı hızda olmalıdır).
                          // EN: Starts serial communication at 9600 baud rate (must match the Python speed).
  
  dht.begin();            // TR: DHT sensörünü veri okumaya hazır hale getirmek için başlatır.
                          // EN: Initializes the DHT sensor to make it ready for reading data.
}

void loop() {
  nem = dht.readHumidity();          // TR: Sensörden nem değerini okur ve 'nem' değişkenine atar.
                                     // EN: Reads the humidity value from the sensor and assigns it to the 'nem' variable.
  
  sicaklik = dht.readTemperature();  // TR: Sensörden sıcaklık değerini okur ve 'sicaklik' değişkenine atar.
                                     // EN: Reads the temperature value from the sensor and assigns it to the 'sicaklik' variable.

  // TR: Okunan değerlerin geçerli olup olmadığını (bağlantı hatası vs.) kontrol eder.
  // EN: Checks if the read values are valid (connection error, etc.).
  if (isnan(nem) || isnan(sicaklik)) {
    Serial.println("0,0");           // TR: Sensör okunamazsa Python tarafında split (bölme) hatası olmasın diye varsayılan olarak "0,0" gönderir.
                                     // EN: If the sensor cannot be read, sends "0,0" by default to prevent split errors on the Python side.
    
    delay(2000);                     // TR: Bir sonraki okuma denemesinden önce 2 saniye bekler.
                                     // EN: Waits 2 seconds before the next reading attempt.
    
    return;                          // TR: Döngünün kalanını çalıştırmadan loop'un başına geri döner.
                                     // EN: Returns to the beginning of the loop without executing the rest of the code.
  }

  // TR: Sıcaklık ve nem değerlerini aralarına virgül koyarak tek bir metin satırı haline getirir (Örn: "29,40").
  // EN: Combines temperature and humidity values into a single string separated by a comma (e.g., "29,40").
  veri = String(sicaklik) + "," + String(nem);
  
  Serial.println(veri);              // TR: Hazırlanan virgüllü veriyi seri porttan satır sonu (newline) karakteriyle Python'a gönderir.
                                     // EN: Sends the prepared comma-separated data to Python via the serial port with a newline character.
  
  delay(2000);                       // TR: DHT11 sensörünün kararlı çalışması için iki okuma arasında 2 saniye bekler.
                                     // EN: Waits 2 seconds between readings for the stable operation of the DHT11 sensor.
}

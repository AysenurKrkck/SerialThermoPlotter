# SerialThermoPlotter

# 🌡️ IoT Real-Time Temperature & Humidity Tracking System / Canlı Sıcaklık ve Nem Takip Sistemi

🌐 [English Version](#english) | [Türkçe Versiyon](#türkçe)

---

## <a name="english"></a>🇬🇧 English

### 📝 Description
This project is an IoT application that establishes a real-time data pipeline between hardware and software. By reading environmental metrics via a physical sensor, it transmits this data to a computer over a serial connection. A custom Python interface then parses and visualizes these temperature and humidity changes dynamically on a live graph, offering a robust and fault-tolerant monitoring solution.

This project reads ambient temperature and humidity data instantly via the **DHT11** sensor, transfers this data to the computer over serial communication, and visualizes it in real-time using a **Python (Matplotlib)** graphical interface.

### ⚠️ CRITICAL WORKFLOW & LOGIC

For the system to work properly, **the following sequence and rules must be strictly followed**:

1. **Initial Setup & Upload:** First, download `Sicaklik_Verisi.ino` located inside the `Sicaklik_Verisi` folder and upload it to your Arduino Uno. After that, run `dht_oku.py` inside the `sicaklik_Verisi_python` folder using Visual Studio Code.
2. **Hardware First:** The C++ code **must definitely** be uploaded to the Arduino Uno before running the Python script. The Python side cannot be initiated without the hardware code running.
3. **COM Port Verification:** You must check which **COM port** (e.g., `COM3`, `COM4`) the Arduino Uno is connected to via Device Manager. The port definition in the Python code (`serial.Serial('COM3', ...)`) must match the Arduino port exactly. Otherwise, Python will throw a `SerialException`.
4. **Graph Refresh Cycle:** For system stability, the Python script plots the data coming from the serial port **every 10 samples (10 values)**, and then clears the buffer to dynamically redraw the new dataset.

### 🚀 Features
* **Dual Data Tracking:** Simultaneously reads and processes both temperature and humidity.
* **Fault Tolerance:** * **C++ Side:** If data cannot be read from the sensor (`isnan`), a safe `0,0` signal is sent to prevent the system from locking up.
  * **Python Side:** A `try-except` block prevents script crashes against corrupted or missing data (`ValueError` protection).
* **Memory Management:** Graph buffers clear every 10 data points to ensure the application runs smoothly without memory leaks.

### 🛠️ Hardware & Software Stack
* **Microcontroller:** Arduino Uno
* **Sensor:** DHT11 Temperature and Humidity Sensor
* **Connection:** USB Cable, Breadboard, and Jumper Wires
* **Languages & Libraries:** C++ (Embedded), Python 3.x (`pyserial`, `matplotlib`, `numpy`)

### 🔌 Pin Out & Connections
Based on the `#define DHTPIN 2` configuration in the C++ code:
* **DHT11 VCC** ➡️ Arduino 5V / 3.3V
* **DHT11 GND** ➡️ Arduino GND
* **DHT11 DATA (Out)** ➡️ Arduino **D2** (Digital Pin 2)

---

## <a name="türkçe"></a>🇹🇷 Türkçe

### 📝 Açıklama
Bu proje, donanım ve yazılım arasında gerçek zamanlı bir veri hattı oluşturan bir IoT uygulamasıdır. Fiziksel bir sensör aracılığıyla ortam ölçümlerini okuyarak, bu verileri seri bağlantı üzerinden bilgisayara iletir. Özel olarak hazırlanan Python arayüzü ise bu sıcaklık ve nem değişimlerini canlı bir grafik üzerinde dinamik olarak ayrıştırıp görselleştirerek, hataya dayanıklı ve kararlı bir izleme çözümü sunar.

Bu proje, **DHT11** sensörü aracılığıyla ortamdaki sıcaklık ve nem verilerini anlık olarak okuyan, bu verileri seri haberleşme üzerinden bilgisayara aktaran ve **Python (Matplotlib)** kullanarak gerçek zamanlı grafiksel arayüze döken hibrit bir IoT uygulamasıdır.

### ⚠️ KRİTİK ÇALIŞMA ADIMLARI VE MANTIĞI

Projenin sorunsuz çalışması için **aşağıdaki sıralamaya ve kurallara kesinlikle uyulmalıdır**:

1. **İlk Kurulum ve Yükleme:** Öncelikle `Sicaklik_Verisi` klasörünün içerisindeki `Sicaklik_Verisi.ino` dosyasını indirip Arduino Uno'ya yükleyin. Daha sonra `sicaklik_Verisi_python` klasörü içerisindeki `dht_oku.py` dosyasını Visual Studio Code üzerinden çalıştırın.
2. **Önce Donanım Tetiklenmeli:** C++ kodu **kesinlikle** Python betiği çalıştırılmadan önce Arduino Uno'ya yüklenmiş olmalıdır. Arduino üzerinde kod hazır olmadan Python tarafı başlatılamaz.
3. **Port (COM) Doğrulaması:** Arduino Uno'nun bilgisayarınızda **hangi COM portuna** (Örn: `COM3`, `COM4` vb.) bağlı olduğu Aygıt Yöneticisi'nden kontrol edilmelidir. Python kodundaki port tanımı (`serial.Serial('COM3', ...)`) ile Arduino'nun bağlı olduğu port birebir aynı olmak zorundadır. Aksi takdirde Python port bulma hatası (`SerialException`) verecektir.
4. **Grafik Yenileme Döngüsü:** Sistem kararlılığı için Python betiği, seri porttan gelen verileri **10 değerde bir (her 10 örneklemde)** grafiğe döker ve ardından arabelleği temizleyerek yeni veri seti için grafiği dinamik olarak günceller.

### 🚀 Özellikler
* **Çift Veri Takibi:** Hem sıcaklık hem de nem değerlerini eş zamanlı olarak okur ve işler.
* **Hata Yönetimi (Fault Tolerance):** * **C++ Tarafı:** Sensörden veri okunamadığı durumlarda (`isnan`) sistemin kilitlenmesini önlemek için seri porta güvenli `0,0` sinyali gönderilir.
  * **Python Tarafı:** `try-except` bloğu sayesinde seri porttan gelebilecek bozuk veya eksik verilere karşı `ValueError` koruması sağlanır.
* **Hafıza Yönetimi:** Grafik arabellekleri her 10 veri noktasında bir sıfırlanarak uygulamanın şişmeden kararlı çalışması sağlanır.

### 🛠️ Kullanılan Teknolojiler ve Bileşenler
* **Mikrodenetleyici:** Arduino Uno
* **Sensör:** DHT11 Sıcaklık ve Nem Sensörü
* **Bağlantı:** USB Kablosu, Breadboard ve Jumper Kablolar
* **Yazılım Altyapısı:** C++ (Embedded), Python 3.x (`pyserial`, `matplotlib`, `numpy`)

### 🔌 Devre Şeması ve Bağlantılar
C++ kodunda tanımlanan `#define DHTPIN 2` konfigürasyonuna göre bağlantılar:
* **DHT11 VCC** ➡️ Arduino 5V / 3.3V
* **DHT11 GND** ➡️ Arduino GND
* **DHT11 DATA (Out)** ➡️ Arduino **D2** (Dijital 2)

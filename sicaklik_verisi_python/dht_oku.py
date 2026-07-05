import serial               # TR: Seri port haberleşmesi için gerekli kütüphane.
                            # EN: Library required for serial port communication.

import matplotlib.pyplot as plt  # TR: Grafik çizimi ve görselleştirme için kullanılan kütüphane.
                                 # EN: Library used for data plotting and visualization.

import numpy as np          # TR: Matematiksel ve dizisel işlemler için kullanılan kütüphane.
                            # EN: Library used for mathematical and array operations.

# TR: Grafik ekranının donmadan anlık/canlı olarak güncellenebilmesi için interaktif modu açar.
# EN: Enables interactive mode so the plot window updates dynamically without freezing.
plt.ion()

# TR: 'COM3' portundan 9600 baud hızında seri haberleşme bağlantısı başlatır.
# EN: Initializes the serial communication connection on 'COM3' port at 9600 baud rate.
ser = serial.Serial('COM3', 9600, timeout=1)

sicaklik = []               # TR: Grafikte gösterilecek sıcaklık değerlerini biriktiren boş liste.
                            # EN: Empty list to accumulate temperature values for the plot.

nem = []                    # TR: Grafikte gösterilecek nem değerlerini biriktiren boş liste.
                            # EN: Empty list to accumulate humidity values for the plot.

# TR: Grafik penceresini (fig) ve çizim eksenini (ax) oluşturur.
# EN: Creates the plot figure (fig) and axes (ax).
fig, ax = plt.subplots()

# TR: Sıcaklık (kırmızı) ve Nem (mavi) için boş çizgiler tanımlar ve etiketlerini belirler.
# EN: Defines empty line plots for Temperature (red) and Humidity (blue) with labels.
line1, = ax.plot([], [], label="Sicaklik", color="red")
line2, = ax.plot([], [], label="Nem", color="blue")
ax.legend()                 # TR: Grafik üzerine hangi çizginin ne olduğunu gösteren bilgi kutusunu ekler.
                            # EN: Adds the legend box onto the plot showing which line represents what.

# TR: Grafik eksen sınırlarını ve isimlendirmelerini yapılandırır.
# EN: Configures plot axis limits and labels.
ax.set_xlim(0, 10)          # TR: X eksenini 0 ile 10 örnek arasında sınırlandırır.
                            # EN: Limits the X-axis between 0 and 10 samples.
ax.set_ylim(0, 80)          # TR: Y eksenini değer boyutu olarak 0 ile 80 arasında sınırlandırır.
                            # EN: Limits the Y-axis value scale between 0 and 80.
ax.set_xlabel("Örnek Sayisi") # TR: X ekseninin adını belirler.
                            # EN: Sets the label for the X-axis.
ax.set_ylabel("Değerler")     # TR: Y ekseninin adını belirler.
                            # EN: Sets the label for the Y-axis.

while True:
    # TR: Seri port tamponunda (buffer) okunmayı bekleyen veri olup olmadığını kontrol eder.
    # EN: Checks if there is any incoming data waiting to be read in the serial buffer.
    if ser.in_waiting > 0:
        # TR: Gelen veriyi satır satır okur, 'utf-8' formatına çevirir ve sonundaki boşlukları/alt satır karakterini siler.
        # EN: Reads data line by line, decodes it into 'utf-8', and strips trailing spaces/newline characters.
        data = ser.readline().decode('utf-8').rstrip()
        print(f"Gelen veri: {data}") # TR: Okunan ham veriyi terminale yazdırır.
                                     # EN: Prints the raw incoming data to the terminal.
        
        try:
            # TR: Arduino'dan gelen "29,40" gibi virgüllü metni virgülden bölerek ikiye ayırır.
            # EN: Splits the comma-separated string from Arduino (e.g., "29,40") into two parts.
            deger1, deger2 = data.split(',')
            deger1 = float(deger1)  # TR: İlk değeri (Sıcaklık) ondalıklı sayıya çevirir.
                                    # EN: Converts the first value (Temperature) into a float.
            deger2 = float(deger2)  # TR: İkinci değeri (Nem) ondalıklı sayıya çevirir.
                                    # EN: Converts the second value (Humidity) into a float.
            
            sicaklik.append(deger1) # TR: Dönüştürülen sıcaklık değerini listenin sonuna ekler.
                                    # EN: Appends the converted temperature value to the list.
            nem.append(deger2)      # TR: Dönüştürülen nem değerini listenin sonuna ekler.
                                    # EN: Appends the converted humidity value to the list.
            
            # TR: Listelerde 10 adet veri biriktiğinde grafiği çizme aşamasına geçer.
            # EN: Once 10 data samples are collected in the lists, starts the plotting process.
            if len(sicaklik) == 10 and len(nem) == 10:
                print(sicaklik, nem) # TR: 10'lu veri paketini terminale loglar.
                                     # EN: Logs the batch of 10 data points to the terminal.
                
                # TR: Sıcaklık çizgisinin X (0-9 arası örnek sayısı) ve Y (sıcaklık değerleri) verilerini günceller.
                # EN: Updates the X (sample count 0-9) and Y (temperature values) data of the temperature line.
                line1.set_ydata(sicaklik)
                line1.set_xdata(range(len(sicaklik)))
                
                # TR: Nem çizgisinin X (0-9 arası örnek sayısı) ve Y (nem değerleri) verilerini günceller.
                # EN: Updates the X (sample count 0-9) and Y (humidity values) data of the humidity line.
                line2.set_ydata(nem)
                line2.set_xdata(range(len(nem)))
                
                # TR: Grafik penceresini yeni verilerle yeniden tetikler ve çizimi günceller.
                # EN: Redraws the plot canvas with the new data points and flushes GUI events.
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.1)      # TR: Grafik ekranının güncellenmesi için programı 0.1 saniye duraklatır.
                                    # EN: Pauses the execution for 0.1 seconds to allow the GUI to render.
                
                # TR: Yeni gelecek olan 10'lu veri paketine yer açmak için mevcut listeleri tamamen temizler.
                # EN: Completely clears the current lists to make space for the next batch of 10 samples.
                sicaklik.clear()
                nem.clear()
                
        except ValueError:
            # TR: Bağlantı kopması veya hatalı/eksik veri gelmesi durumunda programın çökmesini engeller, adımı atlar.
            # EN: Prevents the program from crashing if data is corrupted or incomplete; skips to the next loop.
            continue
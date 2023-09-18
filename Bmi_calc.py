import tkinter
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(100,100)

#Başlık tanımla
label = tkinter.Label(text="BMI hesaplamak için Boy ve Kilonuzu Girin")
label.config(bg="Black",fg="white",width=40,padx=10,pady=10)
label.pack()

#Kilo için değerleri al
kilo_label = tkinter.Label(text="Kilonuzu KG cinsinden girin:")
kilo_label.config(width=30,padx=10,pady=10)
kilo_label.pack()
kilo_entry = tkinter.Entry(width=10)
kilo_entry.pack()

#boy için değerleri al
boy_label = tkinter.Label(text="Boyunuzu cm cinsinden girin:")
boy_label.config(width=30,padx=10,pady=10)
boy_label.pack()
boy_entry = tkinter.Entry(width=10)
boy_entry.pack()

#Buton ve ekrana yazdırmak için fonksiyon oluştur
def bmicalc():
    try:
        boy = float(boy_entry.get()) / 100
        kilo = float(kilo_entry.get())

        bmi = kilo / boy ** 2
        sonuc_label.config(text=f"BMI değeriniz: {bmi:.2f}")
        boy_kontrol_label.config(text="")
        kilo_kontrol_label.config(text="")
    except ValueError:
        sonuc_label.config(text="Geçerli değerler giriniz")
        boy_kontrol_label.config(text="")
        kilo_kontrol_label.config(text="")

#Hesaplama için buton oluştur
calc_button= tkinter.Button(text="Hesapla",command=bmicalc)
calc_button.config(padx=10,pady=10)
calc_button.pack()

#Sonucu ekrana yazdır
sonuc_label = tkinter.Label(window, text="")
sonuc_label.pack()

#Kontrol label
boy_kontrol_label = tkinter.Label(window, text="")
boy_kontrol_label.pack()
kilo_kontrol_label = tkinter.Label(window, text="")
kilo_kontrol_label.pack()



#Ekranın açık kalması için
window.mainloop()

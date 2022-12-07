

import tkinter

kok = tkinter.Tk()
kok.geometry("350x150")
kok.title("Vücut Kitle Endeksi Hesaplama")
bmi=0

def calculate_bmi():
    kg = float(Entry_kg.get())
    boy = float(Entry_boy.get())
    bmi = round(kg / (boy**2), 4)
    print(round (bmi, 4))
    label_bmi['text'] = f"BMI: {bmi}"



label_kg = tkinter.Label(kok, text="Kilonuzu girin:")
label_kg.grid(column=0, row=0)

Entry_kg = tkinter.Entry(kok)
Entry_kg.grid(column=1, row=0)


label_boy = tkinter.Label(kok, text="Boyunuzu girin")
label_boy.grid(column=0, row=1)
Entry_boy = tkinter.Entry(kok)
Entry_boy.grid(column=1,row=1)


button_calculate= tkinter.Button(kok, text="hesapla", command=calculate_bmi)
button_calculate.grid(column=0, row=2)


label_bmi = tkinter.Label(kok, text="Vücut Kitle Endeksiniz=")
label_bmi.grid(column=1, row=2)



kok.mainloop()

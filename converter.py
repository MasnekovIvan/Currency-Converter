from tkinter import*
import requests

link = 'https://openexchangerates.org/api/latest.json?app_id=cb02378415094c70b5f72780d1e5d114'
data = requests.get(link)
rates = data.json()['rates']

window = Tk()
window.title("Currency Converter")
window.geometry("250x100")


def convertRUB():
    ruble = float(RUB.get())
    dollar = ruble / rates['RUB']
    euro = ruble / (rates['RUB'] * rates['EUR'])
    USD.set(round(dollar, 2))
    EUR.set(round(euro, 2))


def convertUSD():
    dollar = float(USD.get())
    ruble = dollar * rates['RUB']
    euro = dollar / rates['EUR']
    RUB.set(round(ruble, 2))
    EUR.set(round(euro, 2))


def convertEUR():
    euro = float(EUR.get())
    ruble = euro * (rates['RUB'] / rates['EUR'])
    dollar = euro * rates['EUR']
    RUB.set(round(ruble, 2))
    USD.set(round(dollar, 2))


# RUB
labelRUB = Label(text='RUB:')
labelRUB.grid(row=0, column=0)

RUB = StringVar()
entry = Entry(textvariable=RUB)
entry.grid(row=0, column=1)

buttonRUB = Button(text='Convert', command=convertRUB)
buttonRUB.grid(row=0, column=2)

# USD
labelUSD = Label(text='USD:')
labelUSD.grid(row=1, column=0)

USD = StringVar()
entry2 = Entry(textvariable=USD)
entry2.grid(row=1, column=1)

buttonUSD = Button(text='Convert', command=convertUSD)
buttonUSD.grid(row=1, column=2)

# EUR
labelEUR = Label(text='EUR:')
labelEUR.grid(row=2, column=0)

EUR = StringVar()
entry2 = Entry(textvariable=EUR)
entry2.grid(row=2, column=1)

buttonEUR = Button(text='Convert', command=convertEUR)
buttonEUR.grid(row=2, column=2)

window.mainloop()

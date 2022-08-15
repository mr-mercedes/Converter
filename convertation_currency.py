from tkinter import *
import requests


# настройка окна
root = Tk()
root.geometry("400x150")
root.resizable(width=False, height=False)
root.title("Currency Converter")
root.config(bg='#cfdde3')


# линк
var1 = StringVar(root)
var2 = StringVar(root)
cost = StringVar(root)
currency_list = ['USD', 'JPY', 'RUB', 'EUR', 'GBP', 'CNH']

main_memory = []


Label(root, text="Выберете валюту:", font="arial 12 bold", bg='#cfdde3').grid()
OptionMenu(root, var1, *currency_list).grid(column=2, row=0)


Label(root, text="Выберете валюту:", font="arial 12 bold", bg='#cfdde3').grid()
OptionMenu(root, var2, *currency_list).grid(column=2, row=1)


Label(root, text="Введите сумму \n для перевода:", font="arial 12 bold", bg='#cfdde3').grid()
Entry(root, width=10, textvariable=cost, bg='white').grid(row=2, column=2)

# функция Конвертировать


def get_currency():
    cur1 = var1.get()
    cur2 = var2.get()
    sum = cost.get()

    token = "CHVGOG4LRHPED571"
    #  1L5QHUW1ZJK80GDE запасной токен
    url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={cur1}&to_symbol={cur2}&interval=5min' \
           f'&apikey={token} '
    r = requests.get(url)
    data = r.json()
    tmp = str(data['Meta Data']['4. Last Refreshed'])
    val1 = float(data['Time Series FX (5min)'][tmp]['4. close'])
    result = round(val1 * float(sum), 3)
    memory(f"{sum} {cur1} -> {cur2} = {result}", main_memory)
    show_memory(main_memory)


def memory(string, main_dump):
    main_dump.append(string)


def show_memory(main_dump):
    main_memory_listbox = Listbox()
    for operation in main_dump:
        main_memory_listbox.insert(END, operation)

    main_memory_listbox.place(relx=0.57, rely=0.05, relwidth=0.41, relheight=0.85)


# кнопка Конвертировать
Button(root, text="Конвертировать", font="arial 10 bold", bg="#cfdde3", padx=1, command=get_currency) \
    .grid(row=4, column=0)


root.mainloop()
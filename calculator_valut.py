import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.geometry("800x600")
window.title("Конвертер валют")

# Фиксированные курсы обмена валют
rub_to_usd_rate = 0.010559  # 1 рубль = 0.013 доллара
rub_to_eur_rate = 0.009846  # 1 рубль = 0.011 евро
rub_to_cny_rate = 0.077207  # 1 рубль = 0.086 юаня

# Создаем функцию для конвертации валют
def convert_currency():
    try:
        amount = float(entry_amount.get())
        usd_result = amount * rub_to_usd_rate
        eur_result = amount * rub_to_eur_rate
        cny_result = amount * rub_to_cny_rate

        result_label.config(text=f"{amount} RUB = {usd_result:.2f} USD\n{amount} RUB = {eur_result:.2f} EUR\n{amount} RUB = {cny_result:.2f} CNY")
    except ValueError:
        result_label.config(text="Введите корректное число")

# Создаем метки и поля для ввода
label_amount = tk.Label(window, text="Сумма в RUB:", font=("Arial", 19))
entry_amount = tk.Entry(window, font=("Arial", 18))

# Создаем кнопку для конвертации
convert_button = tk.Button(window, text="Посчитать", font=("Arial", 17), command=convert_currency)

# Метка для вывода результата
result_label = tk.Label(window, text="Результат:", font=("Arial", 17))

# Размещаем элементы на экране
label_amount.pack(anchor="nw", padx=6, pady=6)
entry_amount.pack(anchor="nw", padx=6, pady=6)
convert_button.pack(anchor="nw", padx=6, pady=6)
result_label.pack(anchor="nw", padx=6, pady=6)

# Запускаем главный цикл программы
window.mainloop()
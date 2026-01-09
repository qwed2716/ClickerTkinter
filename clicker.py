import tkinter as tk


def increment():
    global count
    count +=1
    label.config(text=f"Кликов: {count}")
    if count >10: 
        label2.config(text = "Уровень: Неудачник")
root = tk.Tk()
root.geometry('300x200')
root.title('Кликер')

count = 0

label = tk.Label(root, text='Кликов: 0')
label.pack()

btn = tk.Button(root, text = 'Нажми на меня!', command=increment)
btn.pack()

label2 = tk.Label(root, text= 'Уровень: Слабак ')
label2.pack()

root.mainloop()
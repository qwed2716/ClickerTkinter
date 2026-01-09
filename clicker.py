import tkinter as tk


def increment() -> None:
    """
    Increment the click counter and update the display.
    
    This function increases the global click counter by 1,
    updates the counter label, and checks if the user's
    level should be changed based on the current count.
    """
    global count
    count += 1
    label.config(text=f"Кликов: {count}")
    
    if count > 10:
        label2.config(text="Уровень: Неудачник")


# Initialize main window
root: tk.Tk = tk.Tk()
root.geometry('300x200')
root.title('Кликер')

# Initialize counter
count: int = 0

# Create widgets
label: tk.Label = tk.Label(root, text='Кликов: 0')
label.pack()

btn: tk.Button = tk.Button(
    root, 
    text='Нажми на меня!', 
    command=increment
)
btn.pack()

label2: tk.Label = tk.Label(root, text='Уровень: Слабак')
label2.pack()

# Start main loop
root.mainloop()

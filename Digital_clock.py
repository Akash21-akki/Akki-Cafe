import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string_time = strftime('%I:%M:%S %p')
    string_date = strftime('%d-%b-%Y')
    label_time.config(text=string_time)
    label_date.config(text=string_date)
    label_time.after(1000,time)

label = tk.Label(root, text="Akash Kumar", font=('calibri', 50, 'bold'), background='blue', foreground='white')
label.pack()

img = tk.PhotoImage(file="ekant.png")

label = tk.Label(root, image=img)
label.pack()

label_time = tk.Label(root, font=('calibri', 50, 'bold'), background='blue', foreground='white')
label_time.pack(anchor='center')

label_date = tk.Label(root, font=('calibri', 50, 'bold'), background='blue', foreground='white')
label_date.pack(anchor='center')

time()

root.mainloop()
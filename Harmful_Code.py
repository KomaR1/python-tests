from tkinter import *

def output(event):
	txt = entry1.get()

	try:
		if int(txt) < 18:
			label1["text"] = "Этот код для взрослых!"
		else:
			label1["text"] = "Ты балда!"
	except ValueError:
		label1["text"] = "Ты допустил ошибку, тебе не стоило этого делать..."

root = Tk()
root.title("Сколько вам лет?")

entry1 = Entry(root, width=70, font=15)
button1 = Button(root, text="Проверить")
label1 = Label(root, width=44, font=15)
label2 = Label(root, width=2, font=20)

entry1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label1.grid(row=0, column=2)
label2.grid(row=0, column=3)

button1.bind("<Button-1>", output)


root.mainloop()

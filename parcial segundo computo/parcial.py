from cProfile import label

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()
window.title("Menu Pupuseria")
window.geometry=("400x400")
window.config(background = "lightblue")

#foto de inicio
image = Image.open(r"pupusas.jpg")
image = image.resize((400,300),Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(image)
label_image = Label(image=photo_image)
label_image.grid(row=0, column=0, sticky=W)


bebidas= Image.open(r"caf2.jpg")
bebidas = bebidas.resize((400,300),Image.ANTIALIAS)
photo_bebidas = ImageTk.PhotoImage(bebidas)
label_bebidas = Label(image=photo_bebidas)
label_bebidas.grid(row=0, column=5, sticky=W)

#lista de opciones de pupusas
pupusas = ["Pupusas de queso", "Pupusas de frijol con queso", "Pupusas revueltas"]
#lista de opciones de bebidas
bebidas = ["Gaseosa","Fresco","Chocolate"]

#variable para almacenar la cantidad de pupusas
cantidad_pupusas = IntVar()
#variable para almacenar la opcion de pupusas seleccionada
opcion_pupusas = StringVar()
#variable para almacenar la opcion de bebidas seleccionada
opcion_bebidas = StringVar()
#variable para almacenar la opcion del domicilio
opcion_domicilio = IntVar()
#variable para almacenar la cantidad de gaseosas
cantidad_gaseosas = IntVar()
#variable para almacenar la cantidad de frescos
cantidad_frescos = IntVar()
#variable para almacenar la cantidad de chocolates
cantidad_chocolates = IntVar()
#variable para almacenar el precio de la pupusa
precio_pupusas = DoubleVar()
#variable para almacenar el precio de la bebida
precio_bebidas = DoubleVar()
#variable para almacenar el precio del domicilio
precio_domicilio = DoubleVar()
#variable para almacenar el costo total
costo_total = DoubleVar()
#variable para almacenar el precio de una gaseosa
precio_gaseosas = DoubleVar()
#variable para almacenar el precio de un fresco
precio_frescos = DoubleVar()
#variable para almacenar el precio de un chocolate
precio_chocolates = DoubleVar()

#etiqueta para la cantidad de pupusas
cantidad_pupusas_label = Label(window, text="Cantidad de pupusas: ", background = "green" )
cantidad_pupusas_label.grid(row=1, column=0, sticky=W)
#caja de texto para la cantidad de pupusas
cantidad_pupusas_entry = Entry(window, textvariable = cantidad_pupusas)
cantidad_pupusas_entry.grid(row=1, column=1, sticky=W)
#etiqueta para la opcion de pupusas
opcion_pupusas_label = Label(window, text="Seleccione la opcion de pupusas: ", background = "green")
opcion_pupusas_label.grid(row=2, column=0, sticky=W)
#combo box para la opcion de pupusas
opcion_pupusas_combo = ttk.Combobox(window, textvariable = opcion_pupusas, state="readonly", values = pupusas)
opcion_pupusas_combo.grid(row=2, column=1, sticky=W)
opcion_pupusas_combo.current(0)
#etiqueta para la opcion de bebidas
opcion_bebidas_label = Label(window, text="Seleccione la opcion de bebidas: ", background = "green")
opcion_bebidas_label.grid(row=3, column=0, sticky=W)
#combo box para la opcion de bebidas
opcion_bebidas_combo = ttk.Combobox(window, textvariable = opcion_bebidas, state="readonly", values = bebidas)
opcion_bebidas_combo.grid(row=3, column=1, sticky=W)
opcion_bebidas_combo.current(0)
#etiqueta para la opcion del domicilio
opcion_domicilio_label = Label(window, text="Desea llevar el pedido a domicilio?", background = "green")
opcion_domicilio_label.grid(row=4, column=0, sticky=W)
#radiobutton para la opcion del domicilio
opcion_domicilio_radiobutton = Radiobutton(window, text="Si", variable = opcion_domicilio, value = 1, background = "green")
opcion_domicilio_radiobutton.grid(row=4, column=1, sticky=W)
#radiobutton para la opcion del domicilio
opcion_domicilio_radiobutton = Radiobutton(window, text="No", variable = opcion_domicilio, value = 0, background = "green")
opcion_domicilio_radiobutton.grid(row=4, column=2, sticky=W)
#etiqueta para la cantidad de gaseosas
cantidad_gaseosas_label = Label(window, text="Cantidad de gaseosas: ", background = "green")
cantidad_gaseosas_label.grid(row=5, column=0, sticky=W)
#caja de texto para la cantidad de gaseosas
cantidad_gaseosas_entry = Entry(window, textvariable = cantidad_gaseosas)
cantidad_gaseosas_entry.grid(row=5, column=1, sticky=W)
precio_pupusas_label = Label(window, text="Precio de la pupusa: ", background = "green")
precio_pupusas_label.grid(row=8, column=0, sticky=W)
#caja de texto para el precio de la pupusa
precio_pupusas_entry = Entry(window, textvariable = precio_pupusas)
precio_pupusas_entry.grid(row=8, column=1, sticky=W)
precio_domicilio_label = Label(window, text="Precio del domicilio: ", background = "green")
precio_domicilio_label.grid(row=10, column=0, sticky=W)
#caja de texto para el precio del domicilio
precio_domicilio_entry = Entry(window, textvariable = precio_domicilio)
precio_domicilio_entry.grid(row=10, column=1, sticky=W)
#etiqueta para el costo total
costo_total_label = Label(window, text="Costo total: ", background = "green")
costo_total_label.grid(row=11, column=0, sticky=W)
#caja de texto para el costo total
costo_total_entry = Entry(window, textvariable = costo_total)
costo_total_entry.grid(row=11, column=1, sticky=W)

#precio de la pupusa de queso
precio_pupusas.set(0.7)
#precio de la pupusa de frijol con queso
precio_pupusas.set(0.65)
#precio de la pupusa revuelta
precio_pupusas.set(0.6)
#precio de la gaseosa
precio_bebidas.set(0.75)
#precio del fresco
precio_bebidas.set(0.6)
#precio del chocolate
precio_bebidas.set(0.5)
#precio del domicilio
precio_domicilio.set(1.5)
#precio de una gaseosa
precio_gaseosas.set(0.75)
#precio de un fresco
precio_frescos.set(0.6)
#precio de un chocolate
precio_chocolates.set(0.5)

#funcion para calcular el costo total
def calcular():
    costo_total.set((cantidad_pupusas.get()*precio_pupusas.get())+(cantidad_gaseosas.get()*precio_gaseosas.get())+(cantidad_frescos.get()*precio_frescos.get())+(cantidad_chocolates.get()*precio_chocolates.get())+(opcion_domicilio.get()*precio_domicilio.get()))
#funcion para mostrar la factura
def factura():
	print("Producto\t\tCantidad\t\tPrecio")
	print("Pupusas de queso\t\t"+str(cantidad_pupusas.get())+"\t\t"+str(precio_pupusas.get()))
	print("Gaseosas\t\t"+str(cantidad_gaseosas.get())+"\t\t"+str(precio_gaseosas.get()))
	print("Frescos\t\t"+str(cantidad_frescos.get())+"\t\t"+str(precio_frescos.get()))
	print("Chocolates\t\t"+str(cantidad_chocolates.get())+"\t\t"+str(precio_chocolates.get()))
	print("Costo envio\t\t"+str(opcion_domicilio.get())+"\t\t"+str(precio_domicilio.get()))
	print("Total\t\t\t"+str(costo_total.get()))

#boton para calcular
calcular_button = Button(window, text="Calcular", command = calcular, background = "green")
calcular_button.grid(row=15, column=0, sticky=W)
#boton para mostrar la factura
factura_button = Button(window, text="Factura", command = factura, background = "green")
factura_button.grid(row=15, column=1, sticky=W)

window.mainloop()




#alfredo jose zelaya lainez smis 069221
#david isaac ferandez chicas smis 006121












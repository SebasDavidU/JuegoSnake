from tkinter import Tk, Frame, Button, Canvas, Label, ALL
import random

x,y = 15,15
direction = ''
posicion_x = 15
posicion_y = 15
#--- Los parentesis () identifica una lista en Python, en este caso coordenadas---
posicion_food = (15,15)
#--- Los parentesis () identifica una lista de listas en Python, en este caso coordenadas---
posicion_snake = [(75,75)]
nueva_posicion = [(15,15)]

#----Función para identificar donde moverse---
def coordenadas_snake():
    #---la palabrar global nos indica que vamos a trabajar con las variables definidas previamente---
    global direction, posicion_snake, x, y, nueva_posicion
    #---Arriba (up)---
    if direction == "up":
        y = y - 30
        #---Agregue al final de la lista el valor (x,y).
        nueva_posicion[0:] = [(x,y)]
        if y >= 465:
            y=15
        elif y<=0:
            y=465
    #---Abajo (down)---
    elif direction == "down":
        y = y + 30
        nueva_posicion[0:] = [(x,y)]
        if y >= 465:
            y=15
        elif y<=0:
            y=15
    #---Izquierda (left)---
    elif direction == "left":
        x = x - 30
        nueva_posicion[0:] = [(x,y)]
        if x >= 465:
            x=0
        elif x<=0:
            x=465
    #---Derecha (right)---
    elif direction == "right":
        x = x + 30
        nueva_posicion[0:] = [(x,y)]
        if x >= 465:
            x=15
        elif x<=0:
            x=15 
    #---En las listas [:-1] signica que toma todas las posiciones, excepto la ultima ----
    posicion_snake = nueva_posicion +  posicion_snake[:-1]
    #---Esta linea me permite mover cada una de las posiciones---
    for parte, lugar in zip(canvasMarcoJuego.find_withtag("snake"), posicion_snake):
        canvasMarcoJuego.coords(parte, lugar)

#---Función para definir la dirección---
#---Es decir que si va hacia abajo, no puede devolverse por la misma dirección---
def direccion(event):
    global direction
    if event == "left":
        if direction != "right":
            direction = event
    elif event == "right":
        if direction != "left":
            direction = event
    elif event == "up":
        if direction != "down":
            direction = event
    elif event == "down":
        if direction != "up":
            direction = event
#---Función para mover la serpiente---
def movimiento():
    global posicion_food, posicion_snake, nueva_posicion
    posiciones = [15, 45, 75, 105, 135, 165, 195, 255, 285, 315, 345, 375, 405, 435, 465]
    
    coordenadas_snake()

    #---Si la cabeza de las serpiente posición inicial es igual a la posición de la comida, sume el punto---
    if posicion_food == posicion_snake[0]:
        n = len(posicion_snake)
        cantidad["text"] = 'Cantidad ♥ : {}'.format(n)

        posicion_food = (random.choice(posiciones), random.choice(posiciones))
        #---Agragar un elemento al final de lista---
        posicion_snake.append(posicion_snake[-1])

        if posicion_food not in posicion_snake:
            canvasMarcoJuego.coords(canvasMarcoJuego.find_withtag("food"), posicion_food)

        canvasMarcoJuego.create_text(*posicion_snake[-1], tex='■', fill="green", font=('Arial', 20), tag="snake")
    if posicion_snake[-1] == nueva_posicion[0] and len(posicion_snake)>=4:
        cruzar_snake()

    for i in posicion_snake:
        if len(posicion_snake)==257:
            maximo_nivel()
    
    cantidad.after(300, movimiento)

def cruzar_snake():
    canvasMarcoJuego.delete(ALL)
    canvasMarcoJuego.create_text(canvasMarcoJuego.winfo_width() / 2, canvasMarcoJuego.winfo_height()/2, text=f"Intentelo\n de Nuevo \n\n ♥", fill="red", font=('Arial', 20))

def maximo_nivel():
    canvasMarcoJuego.delete(ALL)
    canvasMarcoJuego.create_text(canvasMarcoJuego.winfo_width() / 2, canvasMarcoJuego.winfo_height()/2, text=f"Excelente\n FIN \n\n ♥♥♥", fill="green", font=('Arial', 20))

def salir():
    ventana.destroy()
    ventana.quit()
#--------------------- Ventana ----------------------------
ventana = Tk()
ventana.config(bg="black")
ventana.title("Juego Snacke")
ventana.geometry("485x510")
#---Esta línea me permite bloquear que el usuario cambie el tamaño de la ventana---
ventana.resizable(0,0)
#---Crear frames del aplicativo---
frame_1 = Frame(ventana, width=485, height=25, bg="black")
frame_1.grid(column=0, row=0)

frame_2 = Frame(ventana, width=485, height=490, bg="black")
frame_2.grid(column=0, row=1)

#---El método bind(), me permite vincular eventos a una acción especifica en el aplicativo---
ventana.bind("<KeyPress-Up>", lambda event:direccion("up"))
ventana.bind("<KeyPress-Down>", lambda event:direccion("down"))
ventana.bind("<KeyPress-Left>", lambda event:direccion("left"))
ventana.bind("<KeyPress-Right>", lambda event:direccion("right"))

#---Usar Canvas para crear un rectangulo---
canvasMarcoJuego =  Canvas(frame_2, bg="black", width=479, height=479)
canvasMarcoJuego.pack()


#---Crear mosaico con cuadricula para ver el plano donde esta el juego---
for i in range(0,460,30):
    for j in range(0,460,30):
        canvasMarcoJuego.create_rectangle(i,j,i+30, j+30, fill="gray10")

#--- Crear texto donde se va mostrar la comida---
canvasMarcoJuego.create_text(75,75, text='♥', fill="red", font=("Arial", 18), tag = "food")

#---Crear botones del aplicativo---
botonIniciar = Button(frame_1, text="Iniciar", bg="aqua", command=movimiento)
botonIniciar.grid(row=0, column=0, padx=20)

botonSalir = Button(frame_1, text="Salir", bg="orange", command=salir)
botonSalir.grid(row=0, column=1, padx=20)

#---Crear etiquetas del aplicativo, fg es color de primer plano (texto)---
cantidad = Label(frame_1, text = "Cantidad ♥ :", bg="black", fg="red", font=("Arial", 12, "bold"))
cantidad.grid(row=0, column=2, padx=20)

#---Mostrar la ventana---
ventana.mainloop()

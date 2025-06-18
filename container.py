from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from dashboard import Dashboard 
from ventas import Ventas
from inventario import Inventario
from clientes import Clientes 
from reportes import Reportes 
import datetime 
from PIL import Image, ImageTk


class Container(tk.Frame):
    
    def __init__(self, padre, controlador, user=None):
        super().__init__(padre)
        self.controlador = controlador
        self.user = user
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []
      
        for i in (Dashboard, Ventas, Inventario, Clientes, Reportes):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame.config(bg="#dcdcdc", highlightbackground="gray", highlightthickness=1)
            frame.place(x=200, y=50, width=900, height=600)

        self.show_frames(Dashboard)
        self.hide_all_indicators()
        self.btn_dashboard_indicator.place(x=3, y=180, width=5, height=40)
        self.label_user = None

    def set_user(self, user):
        self.user = user
        if self.label_user:
            self.label.destroy()

        self.label_user = Label(self.frames1, text=f"Bienvenido:{self.user}", font="sans 14 bold", bg="#a9a9a9", padx=10)
        self.label_user.place(x=300, y=10)

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()
        self.hide_all_indicators()

    def dashboard(self):
         self.show_frames(Dashboard)
         self.hide_all_indicators()
         self.btn_dashboard_indicator.place(x=3, y=180, width=5, heigth=40)

    def ventas(self):
        self.show_frames(Ventas)
        self.hide_all_indicators()
        self.btn_ventas_indicator.place(x=3, y=220, width=5, heigth=40)

    def inventario(self):
        self.show_frames(Inventario)
        self.hide_all_indicators()
        self.btn_inventario_indicator.place(x=3, y=260, width=5, heigth=40)

    def clientes(self):
        self.show_frames(Clientes)
        self.hide_all_indicators()
        self.btn_clientes_indicator.place(x=3, y=300, width=5, heigth=40)

    def reportes(self):
        self.show_frames(Reportes)
        self.hide_all_indicators()
        self.btn_reportes_indicator.place(x=3, y=340, width=5, heigth=40)

    def widgets(self):
        self.frames1 = tk.Frame(self, bg="#a9a9a9", highlightbackground="gray", highlightthickness=1)
        self.frames1.place(x=0, y=0, width=1100, height=50)

        label_app = Label(self.frames1, text="Mi Punto de venta", font="sans 14 bold", bg="#a9a9a9", padx=10)
        label_app.place(x=20, y=10)

        self.label_fecha = Label(self.frames1, text="", font="sans 14 bold", bg="#a9a9a9", padx=10)
        self.label_fecha.place(x=850, y=10)

        self.label_hora = Label(self.frames1, text="", font="sans 14 bold", bg="#a9a9a9", padx=10)
        self.label_hora.place(x=980, y=10)

        self.actualizar_fecha_y_hora()

        self.frames2 = tk.Frame(self, bg="#FFFFFF", highlightbackground="gray", highlightthickness=1)
        self.frames2.place(x=0, y=50, width=200, height=600)

        self.logo_image = Image.open("imagenes/logo.png.jpg")
        self.logo_image = self.logo_image.resize((140,140))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ttk.Label(self.frames2, image=self.logo_image, background="#FFFFFF")
        self.logo_label.place(x=30, y=10)
        
        self.btn_dashboard= Button(self.frames2, text="Dashboard", font="sans 16 bold", bg="white", borderwidth=0, highlightthickness=0, command=self.dashboard)
        self.btn_dashboard.place(x=10, y=180, width=185, height=40)
        self.btn_dashboard_indicator = Label(self.frames2, bg="black")

        self.btn_ventas = Button(self.frames2, text="Ventas", font="sans 16 bold", bg="white", borderwidth=0, highlightthickness=0, command=self.ventas)
        self.btn_ventas.place(x=10, y=220, width=185, height=40)
        self.btn_ventas_indicator = Label(self.frames2, bg="black")

        self.btn_inventario = Button(self.frames2, text="Inventario", font="sans 16 bold", bg="white", borderwidth=0, highlightthickness=0, command=self.inventario)
        self.btn_inventario.place(x=10, y=260, width=185, height=40)
        self.btn_inventario_indicator = Label(self.frames2, bg="black")

        self.btn_clientes = Button(self.frames2, text="Clientes", font="sans 16 bold", bg="white", borderwidth=0, highlightthickness=0, command=self.clientes)
        self.btn_clientes.place(x=10, y=300, width=185, height=40)
        self.btn_clientes_indicator = Label(self.frames2, bg="black")

        self.btn_reportes = Button(self.frames2, text="Reportes", font="sans 16 bold", bg="white", borderwidth=0, highlightthickness=0, command=self.reportes)
        self.btn_reportes.place(x=10, y=340, width=185, height=40)
        self.btn_reportes_indicator = Label(self.frames2, bg="black")

        self.buttons = [self.btn_dashboard, self.btn_clientes, self.btn_inventario, self.btn_ventas, self.btn_reportes]
        lblversion = Label (self.frames2, text="Versión 1.0.0", bg="white", font="sans 16 bold")
        lblversion.place(x=40, y=550)

    def hide_all_indicators(self):
        for btn_indicator in [
            self.btn_dashboard_indicator, 
            self.btn_ventas_indicator,
            self.btn_inventario_indicator, 
            self.btn_reportes_indicator, 
            self.btn_clientes_indicator,
        ]:
            btn_indicator.place_forget()

    def actualizar_fecha_y_hora(self):
        fecha_actual = datetime.datetime.now().strftime("%d / %m / %Y")
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

        self.label_fecha.config(text=fecha_actual)
        self.label_hora.config(text=hora_actual)

        if self.winfo_exists():
            self.after(1000, self.actualizar_fecha_y_hora)
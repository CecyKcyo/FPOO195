from fpdf import FPDF
from Controlador import *
import sqlite3
objControl2=Controlador()

class GeneradorPDF(FPDF):
    def header(self):
        self.set_font("Times", "BU", 14 )
        # tipo de letra, negritas, tamaño
        self.cell(0, 10, "Reporte de Usuarios",0,1,"C")
        # ancho, largo, texto, borde, lineas,alineacion
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial","I", 8)
        self.cell(0,10,"Pagina %s" %self.page_no(),0,0,"C")
    def chapter_body(self):
        self.set_font("Arial","I", 10)
        self.set_fill_color(135,206, 235)
        listaUsuarios=objControl2.consultarUsuarios()
        self.multi_cell(100,10, "Id:   "+" Usuario:   "+" Correo:   ", 1, 'C', 1)
        for i in listaUsuarios:
            self.multi_cell(100,10,str(i[0])+" "+ i[1]+"  "+i[2],1,'C',1)
        
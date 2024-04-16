from fpdf import FPDF
import sqlite3

class GeneradorPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
       
        self.set_font('Arial', 'B', 12)
        # Añadir título
        self.cell(0, 10, 'Reporte de Usuarios', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Añadir número de página
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def chapter_body(self):
        self.set_font('Arial', '', 12)
        # Conectar a la base de datos
        conn = sqlite3.connect('D:/Fundamentos de programacion/FPOO195/TKINTHER/Merks and spend/bdMerks.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, departamento FROM usuarios") 
        data = cursor.fetchall()
        for row in data:
            self.cell(0, 10, 'ID: %s, Usuario: %s, Departamento: %s' % (row[0], row[1], row[2]), 0, 1)
        conn.close()

# Uso del generador de PDF
pdf = GeneradorPDF()
pdf.add_page()
pdf.chapter_body()
pdf.output("Reporte_Usuarios.pdf")

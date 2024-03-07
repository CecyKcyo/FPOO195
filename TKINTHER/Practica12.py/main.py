from usuario import Usuario
from crud import CRUD
import tkinter as tk
from aplicacion_login import AplicacionLogin  

def menu_terminal(crud):
    while True:
        print("\nMenú CRUD")
        print("1. Agregar usuario")
        print("2. Editar usuario")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        print("5. Iniciar interfaz gráfica")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_usuario = input("Ingrese ID del usuario: ")
            correo = input("Ingrese correo del usuario: ")
            contraseña = input("Ingrese contraseña del usuario: ")
            usuario = Usuario(int(id_usuario), contraseña, correo)
            crud.crear_usuario(usuario)
            print("Usuario creado exitosamente.")
        elif opcion == "2":
            id_usuario = input("Ingrese ID del usuario a editar: ")
            correo = input("Ingrese nuevo correo del usuario: ")
            contraseña = input("Ingrese nueva contraseña del usuario: ")
            crud.editar_usuario(int(id_usuario), contraseña, correo)
            print("Usuario editado exitosamente.")
        elif opcion == "3":
            id_usuario = input("Ingrese ID del usuario a eliminar: ")
            crud.eliminar_usuario(int(id_usuario))
            print("Usuario eliminado exitosamente.")
        elif opcion == "4":
            usuarios = crud.consultar_usuario()
            print("Lista de usuarios:")
            for usuario in usuarios:
                print(f"ID: {usuario.obtener_id()}, Correo: {usuario.obtener_correo()}, Contraseña: {usuario.obtener_contraseña()}")
        elif opcion == "5":
            app = AplicacionLogin()  # Inicia la interfaz gráfica
            app.iniciar()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    gestor_usuarios = CRUD()
    menu_terminal(gestor_usuarios)

if __name__ == "__main__":
    main()

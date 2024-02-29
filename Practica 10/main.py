from usuario import Usuario
from crud import CRUD

def main():
    crud = CRUD()

    while True:
        print("\nOperaciones CRUD para Usuarios")
        print("1. Crear usuario")
        print("2. Consultar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            nombre = input("Ingrese el nombre del usuario: ")
            apellido_p = input("Ingrese el apellido paterno del usuario: ")
            apellido_m = input("Ingrese el apellido materno del usuario: ")
            correo = input("Ingrese el correo electrónico del usuario: ")
            contrasena = input("Ingrese la contraseña del usuario: ")
            nuevo_usuario = Usuario(id_usuario, nombre, apellido_p, apellido_m, correo, contrasena)
            crud.crear_usuario(nuevo_usuario)
            print("Usuario creado exitosamente.")

        elif opcion == '2':
            id_usuario = int(input("Ingrese el ID del usuario a consultar: "))
            usuario = crud.consultar_usuario(id_usuario)
            if usuario:
                print(f"ID: {usuario.get_id()}, Nombre: {usuario.getnombre()}, Apellido P: {usuario.getapellido_p()}, Apellido M: {usuario.getapellido_m()}, Correo: {usuario.get_correo()}")
            else:
                print("Usuario no encontrado.")

        elif opcion == '3':
            id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            apellido_p = input("Ingrese el nuevo apellido paterno del usuario: ")
            apellido_m = input("Ingrese el nuevo apellido materno del usuario: ")
            correo = input("Ingrese el nuevo correo electrónico del usuario: ")
            contrasena = input("Ingrese la nueva contraseña del usuario: ")
            if crud.actualizar_usuario(id_usuario, nombre=nombre, apellido_p=apellido_p, apellido_m=apellido_m, correo=correo, contrasena=contrasena):
                print("Usuario actualizado exitosamente.")
            else:
                print("Usuario no encontrado.")

        elif opcion == '4':
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            if crud.eliminar_usuario(id_usuario):
                print("Usuario eliminado exitosamente.")
            else:
                print("Usuario no encontrado.")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if _name_ == "_main_":
    main()
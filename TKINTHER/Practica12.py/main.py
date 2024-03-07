from usuario import Usuario  # Importa la clase Usuario 
from crud import CRUD  # Importa la clase CRUD 

def menu():
    #muestra un menú 
    print("1. Crear usuario")
    print("2. Editar usuario")
    print("3. Eliminar usuario")
    print("4. Consultar usuarios")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))  #  opciones
    return opcion
# spartan = Personaje(especieS, nombreS, alturaS)
# Nemesis = Personaje(especieN, nombreN, alturaN)
# Arma = Armas()
def main():
    gestor_usuarios = CRUD()  #  instancia  CRUD para el cru

    while True:  # Inicia un bucle infinito para que se repita una y otra vex el menu
        opcion = menu()  # obtiene la opción 

        if opcion == 1:  # Si la opción es 1, el usuario quiere crear un nuevo usuario
            id = int(input("Ingrese ID del usuario: "))
            
            contraseña = input("Ingrese contraseña del usuario: ")
            correo = input("Ingrese correo del usuario: ")
            usuario = Usuario(contraseña, correo)
            gestor_usuarios.crear_usuario(usuario)  # Llama al método para crear un usuario en el gestor de usuarios
            print("Usuario creado exitosamente.")
        elif opcion == 2:
            #  editar un usuario existente
            id = int(input("Ingrese ID del usuario a editar: "))
           
            contraseña = input("Ingrese nueva contraseña del usuario: ")
            correo = input("Ingrese nuevo correo del usuario: ")
            gestor_usuarios.editar_usuario(id, contraseña, correo)  # Llama al método para editar un usuario en el gestor de usuarios
            print("Usuario editado exitosamente.")
        elif opcion == 3:
            #  eliminar un usuario existente
            id = int(input("Ingrese ID del usuario a eliminar: "))
            gestor_usuarios.eliminar_usuario(id)  # Llama al método para eliminar un usuario en el gestor de usuarios
            print("Usuario eliminado exitosamente.")
        elif opcion == 4:
            #  consultar todos los usuarios existentes
            usuarios = gestor_usuarios.consultar_usuario()  # Obtiene la lista de usuarios del gestor de usuarios
            print("Lista de usuarios:")
            for usuario in usuarios:  # Itera sobre la lista de usuarios y muestra la información de cada uno
                print(f"ID: {usuario.obtener_id()},  Correo: {usuario.obtener_correo()}, Contraseña: {usuario.obtner_contraseña()}")
        elif opcion == 5:
            #  salir del programa
            print("Saliendo del programa...")
            break  # Sale del bucle infinito y termina el programa
        else:
            #  mensaje de error
            print("Opción no válida. Por favor, seleccione una opción válida.")


























if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente

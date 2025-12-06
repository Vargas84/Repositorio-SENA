from modelos.administrador import Administrador
from modelos.cliente import Cliente
from modelos.mesero import Mesero
from modelos.menu import Menu
from modelos.plato import Plato
from modelos.pedido import Pedido
from modelos.plato_pedido import PlatoPedido
#
def es_letras_y_espacios(texto):
    """Verifica si una cadena contiene solo letras y espacios, y no está vacía."""
    # 1. Elimina espacios en blanco iniciales/finales y verifica si la cadena resultante está vacía
    if not texto.strip():
        return False
        
    # 2. Quita todos los espacios internos para verificar si el resto son solo letras
    texto_sin_espacios = texto.replace(" ", "")
    
    # 3. Retorna True si lo restante son solo letras
    return texto_sin_espacios.isalpha()



# ------------------MENU CONTROLADOR DEL SISTEMA-------------------------------
def menuSistema(menu):#funcion principal que ejecuta el  menu del sistema y muestra los submenus
#menu: instancia de Menu (contiene la lista de platos y los métodos relacionados).
    while True:#bucle pricipal se repite hasta que el usuario elija salir(opcion 4 )
        print("\n=== SISTEMA DE GESTIÓN DE PEDIDOS ===")
        print("1) Administrador")#abre el modulo del administrador
        print("2) Mesero")#abre el modulo del mesero
        print("3) Cliente")#abre el modulo de cliente
        print("4) Salir")#cierra el sistema

        try:
         opcion = int(input("Seleccione una opción: "))#controla que modulo abrir
    # Lee la opción del usuario desde entrada estándar y la convierte a entero.
        except:
# Si la conversión falla (p. ej. el usuario ingresó letras o caracteres especiales), cae aquí.
            print("Opción inválida.")
            continue #continue hace que el bucle while principal vuelva al inicio
            #y vuelva a mostrar el menú.

        if opcion < 1 or opcion > 4:
    # Validación adicional: aunque la entrada sea int, verificamos rango válido (1..4).
            print("Opción inválida.")
            continue
  # si es fuera del ramgo, volvemos al menu principal

        # ------------------- ADMINISTRADOR --------------------
        if opcion == 1:
            CLAVE_ADMINISTRADOR='admi123'#clave para dar permiso al modulo de administracion
            #solo administradores pueden entrar

            while True:#ciclo para validar que se ingrese un nombre correctamente
               nombre=input("Ingrese su nombre administrador: ")
               if not es_letras_y_espacios(nombre) or nombre is None:#verificacion de los datos para nombre de administrador
                  print("Verifique los datos del nombre")
               else:
                  break
            while True:#ciclo para verificar que se ingrese el documento correctamente
               documento=input(f"Administrador {nombre} ingrese su numero de documento: ")
               if documento.isdigit():
                  documento=int(documento)
                  break
               else:
                  print("El documento debe ser un valor unicamente numerico")
                  continue
            while True:#ciclo para verificar que se ingrese el telefono correctamente
               telefono=input(f"Administrador {nombre} ingrese su numero de telefono: ")
               if telefono.isdigit():
                    telefono=int(telefono)
                    break
               else:
                     print("El telefono debe ser un valor unicamente numerico")
                     continue
            try:
              clave= input('Ingrese la clave del Administrador: ')#se pide clave para acceder a las funciones unicas de administrador
            except: 
              print('Opcion invalida')#en caso de ingresar numeros o vacios o caracteres especiales
              continue
            if clave != CLAVE_ADMINISTRADOR:#si la clave es incorrecta
              print('Clave incorrecta, Acceso denegado')
              continue #vuelve al menu principal

            print('Clave correcta, Bienvenido administrador')#clave correcta da permiso al menu de administrador
          

            id_admi=menu.generar_id_administrador()#generador de id para el administrador
            admin = Administrador(id_admi,nombre, documento, telefono)#se crea un administrador con los datos ingresados
            # sub-menu del administrador con sus distintas opciones
            print(f"El administrador: {admin.nombre} esta usando el sistema")
            while True:# bucle del submenu administrador que se repite hasta que seleccione la opcion de volver
                print("\n--- MENU ADMINISTRADOR ---")
                print("1) Agregar plato")#agregar platos al menu para poder hacer los pedidos
                print("2) Eliminar plato")#eliminar platos del menu cuando ya no se esten usando
                print("3) Cambiar disponibilidad")#cambiar la disponibilidad de un plato cuando ya se haya acabado , para no permitir que lo pidan
                print("4) Editar plato")#cambiar informacion de algun plato, como nombre, precio o categoriaa
                print("5) Ver menú")#permite ver todo el menu 
                print("6) Buscar plato")#retorna informacion de un plato por su ID
                print("7) Volver")#regresa al menu anterior

                try:
                    op = int(input("Opción: "))# variable para validar la opcion del menu
                except:
                    print("Opción inválida, ingrese un número.")#en caso de ingresar letras o
                    #caracteres especiales a la opcion
                    continue

                if op < 1 or op > 7:
                  print("Opción inválida.Opcion fuera de rango")#en caso de ingresar un numero
                  #fuera de las opciones
                  continue
                
                if op == 1:#agregar platos al menu
                     while True:#verificar nombre del plato
                        nombre = input("Nombre: ")#nombre del plato a registrar
                        if not es_letras_y_espacios(nombre) or nombre is None:#verificar que el nombre contenga letras y no sea vacio
                           print("Nombre incorrecto, ingrese un nombre para el plato")
                        else:
                           break#en caso de pasar la validacion se rompe el ciclo y pasa al siguiente
                     while True:#verificar precio
                        precio =input("Precio: ").strip()#precio del plato
                        if not precio:#precio vacio
                           print("Precio incorrecto, ingrese un precio para el plato")#mensaje de advertencia
                           continue#vuelve a pedir el precio si esta incorrecto
                        try:#si el precio esta correcto
                           precio=int(precio)#intentar pasarlo a un numero entero
                           if precio<=0:#si el precio es inferior o igual a 0 
                              print("Precio incorrecto, ingrese un precio valido")
                              continue#es un precio invalido entonces lanza este error
                           else:
                              break
                        except:
                           print("Precio incorrecto, ingrese un precio valido")#en caso de ingresar letras o caracteres especiales
                           continue
                     while True:#verificar categoria
                        categoria = input("Categoría: ")#etiqueta del plato
                        if  not es_letras_y_espacios(categoria) or categoria is None:#se evaluan los valores ingresados con la funcion
                           #para verificar las cadenas y su cotenido
                           print("Categoria incorrecta, ingrese una categoria para el plato")
                        else:#si se pasan las respectivas pruebas se agrega el plato 
                          break
                     id_p= menu.generar_id_platos() #generador de ID automtico ID plato
                     admin.agregar_platos(menu, Plato(id_p, nombre, precio, categoria, "Disponible"))
                        # Creamos la instancia Plato con disponibilidad True por defecto y delegamos
                        # al administrador para agregarlo al objeto menu.
                     print(f'Plato agregado con ID automatico: {id_p}')
                        

                elif op == 2:#eliminar plato
                        admin.ver_menu(menu)#muestra el menu para saber que ID(plato) quiere eliminar
                        admin.eliminar_platos(menu, int(input("ID del plato a eliminar: ")))#Pide el ID, lo convierte a int
        # y delega la eliminación al administrador/Menu.
                  
                elif op == 3:#cambiar disponibilidad
                     try:
                        admin.ver_menu(menu)#muestra el menu para saber que ID(plato) quiere editar(nombre,precio nuevo o categoria)
                        id_p = int(input("ID del plato : "))#id_p es el id del plato que se quiere editar
                     except:
                        print("Error: ingrese un numero valido.")#en caso de que se ingrese una opcion incorrecta
                        continue

                     admin.cambiar_disponibilidad_plato(menu,id_p)#cuando el dato sea correcto lo cambia

                elif op == 4:#Editar plato (aquí el flujo pide el id y luego un nuevo precio/nombre y y  disponibilidad)
                    try:
                        admin.ver_menu(menu)#muestra el menu para saber que ID(plato) quiere editar(nombre,precio nuevo o categoria)
                        id_p = int(input("ID del plato a editar: "))#id_p es el id del plato que se quiere editar
                    except:
                        print("Error: ingrese un numero valido.")#en caso de que se ingrese una opcion incorrecta
                        continue
                    # Usamos menu.buscar_platos(id_p) para obtener la referencia al objeto Plato o None.
                    plato = menu.buscar_platos(id_p)

                    if plato is None:
                    # Si no existe un plato con ese id, informamos y volvemos al submenú.
                        print("Plato no encontrado.")
                        continue
                    
                    while True:#si el plato exiate entramos al menu de opciones a editar
                        print(f'¿Que desea editar del plato {plato.nombre}?')#se pregunta que se desea editar del plato que ingresamos
                        print("1) Editar el nombre")
                        print("2) Editar el precio")
                        print("3) Editar la categoria")
                        print("4) Volver al menu anterior")

                        try:#se pide la opcion a editar
                          op=int(input("Ingrese la opcion de edicion: "))
                        except:
                           print("Error. Entrada invalida\n")#en caso de una entrada no valida y vuelve al menu
                           continue
                        
                        if op<1 or op>4:
                           print("Error: Opcion fuera de rango\n")#en caso de una opcionn fuera de rango
                           continue#vuelve al menu
                        elif op==1:#opcion que permite editar el nombre
                           nuevo_nombre=input('Ingrese el nuevo nombre del plato: ')#se pide un nuevo nombre
                           if nuevo_nombre=="":#si se deja un vacio el sistema dejara el nombre que tiene sin modificarlo
                              plato.nombre=plato.nombre#se asigna nuevamente el mismo nombre
                              print(f"El nombre del plato {plato.nombre} quedo igual: {plato.nombre}")#se da aviso de esta asignacion
                              break#y se rompe el ciclo para nombre
                           if not es_letras_y_espacios(nuevo_nombre):#si el nombre no contiene letras se da aviso de este error
                              print("El nombre debe contener solo letras\n")#vuelve a preguntar por el nuevo nombre hasta que se ingrese bien
                           else:
                              admin.editar_platos(menu,id_p,nuevo_nombre=nuevo_nombre)#si pasa las validaciones el nombre se agrega correctamente
                              break#y se rompe el ciclo para nombre
                        elif op==2:#editar el precio
                           nuevo_precio = input("ingrese el Nuevo precio del plato: ")#se pide el nuevo precio(int)
                           if nuevo_precio.isdigit():#se verifica que el nuevo precio sea un digito o sea numerico,sin puntos ni espacios
                              nuevo_precio=int(nuevo_precio)#de ser un digito lo convierte de str a entero
                              if nuevo_precio>0:#si este entero es mayor a 0
                                 admin.editar_platos(menu,id_p,nuevo_precio=nuevo_precio)#el nuevo precio se agrega correctamente
                                 break#y se rompe el ciclo
                              elif nuevo_precio<=0:#en caso de que el entero sea inferior o igual a 0 
                                 print("El precio debe ser mayor a 0")#se muestra un mensaje con ese error
                           elif nuevo_precio=="":#si el precio es vacio se deja como estaba antes
                                plato.precio=plato.precio#se hace la asignacion correspondiente
                                print(f"El precio del plato {plato.nombre} quedo igual: {plato.precio}\n")#se muestra el mensaje
                                break#se rompre el ciclo
                           else:
                              print("El precio debe ser un numero\n")#en caso de ingresar valores diferentes a numeros
                              continue#vuelve al menu 
                        elif op==3:#editar la categoria del plato
                           nueva_categoria=input('Ingrese la nueva categoria del plato: ')#se pide ingresar la nueva categoria
                           if nueva_categoria=="":#si la categoria queda vacia se deja como estaba antes
                              print(f"La categoria del plato {plato.nombre} quedo igual: {plato.nombre}")#se muestra un mensaje de esto
                              break#se rompe el ciclo 
                           if not es_letras_y_espacios(nueva_categoria):#se hace una validacion para verificar que solo sean letras dentro de categoria
                              print("La categoria debe contener solo letras\n")#en caso de que no se muestra un mensaje de esto
                           else:#en caso de que la validacion sea correcta
                              admin.editar_platos(menu, id_p,nueva_categoria=nueva_categoria)#de procede a cambiar el estado de categoria
                              break
                        elif op==4:#volver al menu anterior
                           break#se rompe el codigo

                    
                    print("Plato actualizado correctamente \n")
                    admin.ver_menu(menu)#muestra como quedo el menu con los cambios que se hicieron en editar
                    
                elif op == 5:#ver menu
                    admin.ver_menu(menu)#muestra la lista actual de platos(delegado al objeto menu)


                elif op==6:#buscar un plato 
                   admin.ver_menu(menu)#muestra los platos con sus IDs 
                   try:
                     id_p=int(input('Ingrese el ID del plato a buscar: '))#pide el ID a buscar
                   except:
                      print('Opcion invalida')#en caso de ingresar letras o vacios o caracteres especiales
                      continue
                   plato = menu.buscar_platos(id_p)#llama a la funcion buscar platos de menu
                   #para verificar que el plato buscado este en el menu

                   if plato is None:#si el plato no esta lanza un error
                      print('Plato no encontrado')
                      continue
                   # Mostrar información del plato
                   print("\n--- INFORMACIÓN DEL PLATO ---")#en caso contrario muestra la informacion del plato
                   print(plato.mostrar_informacion())
                   
                elif op == 7:#volver al menu principal
                  break#rompe el ciclo del menu administrado y vuelve al menu principal

        # ------------------- MESERO --------------------
        elif opcion == 2:# Si el usuario elige 2 en el menú principal, entramos al módulo Mesero.
            CLAVE_MESERO='mese123'#clave de acceso para el mesero

            while True:#ciclo para validar que se ingrese un nombre correctamente
               nombre=input("Ingrese su nombre mesero: ")
               if not es_letras_y_espacios(nombre) or nombre is None:#verificacion de los datos para nombre 
                  print("Verifique los datos del nombre")
               else:
                  break
            while True:#ciclo para verificar que se ingrese el documento correctamente
               documento=input(f"Mesero {nombre} ingrese su numero de documento: ")
               if documento.isdigit():
                  documento=int(documento)
                  break
               else:
                  print("El documento debe ser un valor unicamente numerico")
                  continue
            while True:#ciclo para verificar que se ingrese el telefono correctamente
               telefono=input(f"Mesero {nombre} ingrese su numero de telefono: ")
               if telefono.isdigit():
                    telefono=int(telefono)
                    break
               else:
                     print("El telefono debe ser un valor unicamente numerico")
                     continue
            try:
              clave=input('Ingrese la clave de acceso para mesero: ')#se recibe una clave ingresada por el usuario
            except:
              print('Opcion invalida')#en caso de vacios, numeros o caracteres especiales
              continue
            if clave != CLAVE_MESERO:#si la clave ingresada es distinta a la esperada se denegara el acceso
              print('Clave incorrecta, acceso denegado')
              continue
            print('Clave correcta, Bienvenido mesero')# en caso de coincidir se accede al menu mesero

            id_mese=menu.generar_id_meseros()#generador de id para el mesero
            # sub-menu del administrador con sus distintas opciones
            mesero = Mesero(nombre,documento,telefono,id_mese)# Creamos una instancia Mesero por defecto para usar sus métodos.
            pedidos = {}
            print(f"El mesero: {mesero.nombre} esta usando el sistema")
            # Diccionario donde se almacenan pedidos creados por el mesero:
            #   - claves: id_pedido (int)
            #   - valores: objeto Pedido
            while True:#bucle del submenu
               print("\n--- MENU MESERO ---")
               print("1) Crear pedido")
               print("2) Buscar Pedido")
               print("3) Eliminar Pedido")
               print("4) Editar Pedido")
               print("5) Ver Pedidos")
               print("6) Entregar Pedido")
               print("7) Ver menú")
               print("8) Volver")

               try:
                    op = int(input("Opción: "))#determina la accion dentro del menu MESERO
               except:
                    print("Opción inválida.")
                    continue

               if op < 1 or op > 8:
                  print("Opción inválida.Opcion fuera de rango")
                  continue

               if op == 1:#crear pedido
                 if menu.platos_disponibles()=="":
                   print("No se puede crear pedidos porque el menu esta vacio")
                   continue
                 while True:#ciclo para validar que se ingrese un nombre correctamente
                  nombre=input("Ingrese el nombre del cliente: ")
                  if not es_letras_y_espacios(nombre) or nombre is None:#verificacion de los datos para nombre 
                     print("Verifique los datos del nombre")
                  else:
                     break
                 while True:#ciclo para verificar que se ingrese el documento correctamente
                  documento=input(f"Ingrese el  numero de documento del cliente {nombre}: ")
                  if documento=="":
                    documento=0
                    break
                  if documento.isdigit():
                   documento=int(documento)
                   break
                  else:
                   print("El documento debe ser un valor unicamente numerico")
                   continue
                 while True:#ciclo para verificar que se ingrese el telefono correctamente
                   telefono=input(f"Ingrese el numero de telefono del {nombre}: ")
                   if telefono=="":
                     telefono=0
                     break
                   if telefono.isdigit():
                    telefono=int(telefono)
                    break
                   else:
                     print("El telefono debe ser un valor unicamente numerico")
                     continue
                 while True:
                     mesa=input(f"Ingrese un numero de mesa: ")
                     if mesa=="":
                        print("Ingrese un numero de mesa valido por vacio")
                        continue
                     if mesa.isdigit():
                        mesa=int(mesa)
                        break
                     else:
                        print("Ingrese un numero de mesa valido desde else")
                        continue
                   

                #id_p =  menu.generar_id_pedidos() #generador de ID automtico ID pedidos
               cliente= Cliente(nombre,documento, telefono,id_cliente=menu.generar_id_clientes())#creamos un cliente temporal que sera propietario del pedido
                #antes de crear el pedido verificar si hay platos

               #crea el pedido
                
                  #bucle para agregar platos al pedido recien creado
                  #1)pedir platos antes que hacer el pedido
               platos_temporales=[]
               while True:
                  if menu.platos_disponibles()=="":#si no hay platos disponibles no dejara pasar el sistema
                       print("No se pueden agregar platos aun , MENU vacio")
                     
                       break
                  
                  print(f"\n---agregar platos al pedido de la mesa {mesa}---")#en caso contrario si lo hara
                  print("-----------------Platos disponibles-----------------------")
                  platos_disponibles=menu.platos_disponibles()
                  print(platos_disponibles)
                  print("Ingrese los IDs de los platos a agregar o '0' para terminar de agregar platos")
                  try:
                     id_plato = int(input("ID plato: "))# id_plato (int) identifica el plato dentro del menú.
                  except:
                      print("ID invalido. Intente de nuevo")
                      continue
                  #mesero oprime 0 sin platos agregados

                  if id_plato == 0 :# Si se ingresa 0, se finaliza la carga de platos 
                        if not platos_temporales:
                          print(f"El pedido de la mesa {mesa} no tiene platos agregados")
                          print("No se pueden crear pedidos vacios")
                          while True:
                             pregunta=input(f"A) Agregar platos al pedido {id_p}\nS) Salir\nIngrese una opcion: ").lower()
                             if pregunta=="a":
                              #se vuelven a mostrar los platoas disponibles
                              break
                        
                             elif pregunta=="s":
                               print("Pedido cancelado.No se creo ningun pedido")
                               #No se crea ningun ID
                               platos_temporales=[]#limpiar por si acaso
                               break
                             else:
                                print("Opcion invalida")
                                continue
                          if pregunta=="s":#si eligio salir, salir del ciclo principal
                            break
                          continue #si eligio a, continua el while del ciclo principal
                        else:
                           print("Finalizando carga de platos")
                           break
                  #si ingresa in ID normal -> agrega un plato
                  plato=menu.buscar_platos(id_plato)
                  if plato is None:
                        print("Plato no encontrado")
                        continue
                  if plato.disponibilidad=="No Disponible":
                        print(f"Plato {plato.nombre} no disponible")
                        continue
                  try:
                        cantidad=int(input("Cantidad: "))
                    
                  except:
                        print("Cantidad invalida")
                        continue
                  platos_temporales.append((plato,cantidad))
                  print(f"{cantidad} platos de {plato.nombre} agregado(s)")
                  #solo ahora se crea el pedido REAL si hay platos
               if platos_temporales:
                     id_p =  menu.generar_id_pedidos() #generador de ID automtico ID pedidos
                     pedido= mesero.tomar_pedido(id_p, cliente, mesa)#mesero.tomar_pedido devuelve el objeto Pedido creado
                     pedidos[id_p] = pedido#guardamos el obejto Pedido en el diccionario 'pedidos' usando id_p como clave
                        
                     for plato, cantidad in platos_temporales:
                        #intentar agregar el plato al pedido
                        mesero.agregar_plato_a_pedido(pedido,plato,cantidad)
                     print(f"El total del pedido {id_p} es de: {pedido.calcular_total()}")
               else:
                        print("No se creo ningun pedido")

#INICIO DE COMENTARIO GIGANTE


"""       elif op == 2:#permitir agregar platos a un pedido ya existente(opcional)
            try:
                id_p =  menu.generar_id_pedidos() #generador de ID automtico ID pedidos
            except:
                        print("ID invalido")
                        continue

            if id_p not in pedidos:# Si el pedido no existe, pedimos crear primero (opción 1).
                      print("Ese pedido no existe. Cree el pedido primero (Opcion 1)")
                      continue

            try:
                        id_plato = int(input("ID plato: "))#id del plato a buscar para ser agregado
                        cantidad = int(input("Cantidad: "))#cantidad de ese plato
            except:
                        print("Datos inválidos.")#en caso de ingresar datos no esperados
                        continue


            plato = menu.buscar_platos(id_plato)#buscar que el plato exista
            if plato is None:
                        print("Plato no encontrado.")#en caso de no ser encontrado
                        continue

            mesero.agregar_plato_a_pedido(pedidos[id_p], plato, cantidad)
# Agregamos el plato al pedido existente en el diccionario 'pedidos'

        elif op == 3:#eliminar plato de un pedido
                    try:
                        id_p = int(input("ID del Pedido: "))#identificador del pedido a buscar para eliminarle platos
                    except:
                        print("ID de pedido invalido.")#respuesta nno esperada
                        continue

                    if id_p not in pedidos:#en caso de que el pedido no exista
                      print('Ese pedido no existe. Cree el pedido primero (Opcion 1)')
                      continue

                    try:
                        id_plato=int(input("ID plato: "))#identificador del plato a eliminar
                    except:
                      print("ID de plato invalido")#indentificador no correcto
                      continue

                    mesero.eliminar_plato_de_pedido(pedidos[id_p],id_plato)
                    # Delegación: mesero llama a Pedido.eliminar_plato_pedido.

        elif op == 4:#ver total de un pedido en especifico
                    try:
                      id_p = int(input("ID pedido: "))#identificador del pedido a revisar
                    except:
                      print("ID inválido.")#en caso de una respuesta no esperada
                      continue

                    if id_p not in pedidos:#en caso de que el pedido no exista
                      print("Ese pedido no existe.")
                      continue

                    total = pedidos[id_p].calcular_total()# Pedido.calcular_total() recalcula self.total y lo retorna
                    print(f"El total del pedido {id_p} es: ${total}")# Se muestra el total al mesero.


        elif op == 5:#entregar pedido
                    try:
                      id_p = int(input("ID del pedido a entregar: "))
                    except:
                      print("ID inválido.")
                      continue

                    if id_p not in pedidos:
                      print("Ese pedido no existe. Cree el pedido primero (Opción 1)")
                      continue

                    pedido_obj = pedidos[id_p]# Obtenemos el objeto Pedido desde el diccionario.

                    pedido_obj.entregar()
                    # Llamamos Pedido.entregar() que:
                    #  - revisa la bandera entregado (para evitar entregas repetidas),
                    #  - si no fue entregado, marca entregado=True y cambia estado a 'Entregado'.


        elif op == 6:
                    mesero.ver_menu(menu)# 6) Ver menú (ayuda al mesero para mostrar los platos disponibles/registrados)

        elif op == 7:#volver al menu principal
                    break

        # ------------------- CLIENTE --------------------

        elif opcion == 3:# Módulo Cliente: permite que el cliente cree y gestione sus pedidos.
          #cliente = Cliente("Cliente", 0, 0)# Creamos un objeto Cliente temporal para usar sus métodos.
          pedidos_cliente = {}# Diccionario separado para pedidos creados por clientes (clave: id_pedido, valor: Pedido).


          while True:#bucle del submenu cliente
            print("\n--- MENU CLIENTE ---")
            print("1) Ver menú")
            print("2) Crear pedido")
            print("3) Agregar plato")
            print("4) Eliminar plato")
            print("5) Ver total")
            print("6) Ver resumen")
            print("7) Confirmar pedido")
            print("8) Volver")

            try:
              op = int(input("Opción: "))#esta es la opcion del menu cliente
            except:
              print("Opción inválida.")#caracteres no esperados
              continue

            if op < 1 or op > 8:
              print("Opción inválida. Opción fuera de rango.")
              continue

              # 1) Ver menú
            if op == 1:
              cliente.ver_menu(menu)# Muestra todos los platos del menú (delegado a Menu.mostrar_menu).

            # 2) Crear pedido
            elif op == 2:
              try:
                id_p = int(input("ID del pedido: "))
              except:
                print("ID inválido.")
                continue

              if id_p in pedidos_cliente:
                print("Ese pedido ya existe.")
                continue

              try:
                mesa = int(input("Mesa: "))
              except:
                print("Mesa inválida.")
                continue

              pedido = Pedido(id_p, cliente, mesa)
              # Crea el objeto Pedido con id, referencia al cliente y número de mesa
              pedidos_cliente[id_p] = pedido
              print(f"Pedido {id_p} creado correctamente para la mesa {mesa}.")

            # agregar platos al crear el pedido (bucle de ingreso inmediato)
              while True:
                print("\n--- Agregar platos al pedido ---")
                print("Ingrese ID del plato o 0 para terminar.")
                try:
                    id_plato = int(input("ID plato: "))#id del plato a agregar
                except:
                    print("ID inválido.")
                    continue

                if id_plato == 0:
                    print("Terminando ingreso de platos...")#deja de ingresar platos
                    break

                plato = menu.buscar_platos(id_plato)
                if plato is None:#si el plato no esta disponible, no se permite agregarlo
                    print("Plato no encontrado.")
                    continue

                if not plato.disponibilidad:#si el plato no esta disponible no se permite agregarlo
                    print(f"Plato {plato.nombre} no disponible.")
                    continue

                try:
                    cantidad = int(input("Cantidad: "))#se pide la cantidad para el plato a agregar
                except:
                    print("Cantidad inválida.")
                    continue

                pedido.agregar_plato(plato, cantidad)
# Delegación: Pedido.agregar_plato gestiona validaciones y agrega PlatoPedido.

              total = pedido.calcular_total()
              print(f"Total actual del pedido: ${total}")
# Si el cliente confirma de inmediato, cambiamos su estado.
              confirmar = input("¿Desea confirmar el pedido? (s/n): ").lower()
              if confirmar == "s":
                pedido.cambiar_estado_pedido("Confirmado")
                print(f"Pedido {id_p} confirmado.")
              else:
                print("Pedido guardado en edición.")

        # 3) Agregar plato (a pedido ya existente)
            elif op == 3:
             try:
                id_p = int(input("ID del pedido: "))#id del pedido al que se le van agregar platos
             except:
                print("ID inválido.")
                continue

            # aquí VALIDAMOS existencia y mostramos el mensaje correcto
             if id_p not in pedidos_cliente:# Validación: no permitir operar sobre pedidos inexistentes.
                print("Ese pedido no existe.")
                continue

             pedido = pedidos_cliente[id_p]

             if pedido.estado.lower() == "confirmado":# No se pueden agregar platos a pedidos ya confirmados.
                print("No puede agregar platos a un pedido confirmado.")
                continue

             try:
                id_plato = int(input("ID plato: "))
             except:
                print("ID de plato inválido.")
                continue

             plato = menu.buscar_platos(id_plato)
             if plato is None:
                print("Plato no encontrado.")
                continue

             try:
                cantidad = int(input("Cantidad: "))
             except:
                print("Cantidad inválida.")
                continue

             pedido.agregar_plato(plato, cantidad)

        # 4) Eliminar plato
            elif op == 4:
             try:
                id_p = int(input("ID del pedido: "))
             except:
                print("ID inválido.")
                continue

             if id_p not in pedidos_cliente:
                print("Ese pedido no existe.")
                continue

             pedido = pedidos_cliente[id_p]# No se puede eliminar de pedidos confirmados.
             if pedido.estado.lower() == "confirmado":
                print("No puede eliminar platos de un pedido confirmado.")
                continue

             try:
                id_plato = int(input("ID del plato a eliminar: "))
             except:
                print("ID inválido.")
                continue

             pedido.eliminar_plato_pedido(id_plato)

        # 5) Ver total
            elif op == 5:
             try:
                id_p = int(input("ID del pedido: "))
             except:
                print("ID inválido.")
                continue

             if id_p not in pedidos_cliente:
                print("Ese pedido no existe.")
                continue

             total = pedidos_cliente[id_p].calcular_total()# Calcula y retorna el total actual del pedido.
             print(f"El total del pedido {id_p} es: ${total}")

        # 6) Ver resumen
            elif op == 6:
             try:
                id_p = int(input("ID del pedido: "))
             except:
                print("ID inválido.")
                continue

             if id_p not in pedidos_cliente:
                print("Ese pedido no existe.")
                continue

             pedido = pedidos_cliente[id_p]
             # Mostrar un resumen legible del pedido:
             print("\n--- RESUMEN DEL PEDIDO ---")
             print(f"Pedido: {pedido.id_pedido}")
             print(f"Mesa: {pedido.mesa}")
             print(f"Estado: {pedido.estado}")
             print("Platos:")
             if not pedido.platos_pedidos:
              # Si la lista de platos del pedido está vacía, indicarlo.
                print("No hay platos en el pedido.")
             else:
                for p in pedido.platos_pedidos:
                  # Iterar y mostrar cada PlatoPedido con su subtotal (precio * cantidad).
                    print(f"- {p.plato.nombre} x {p.cantidad} = ${p.plato.precio * p.cantidad}")
             print(f"TOTAL: ${pedido.calcular_total()}")# Imprime el total final llamando al método de Pedido.

        # 7) Confirmar pedido
            elif op == 7:
             try:
                id_p = int(input("ID del pedido a confirmar: "))
             except:
                print("ID inválido.")
                continue

             if id_p not in pedidos_cliente:
                print("Ese pedido no existe.")
                continue

             pedido = pedidos_cliente[id_p]
             if pedido.estado.lower() == "confirmado":# Evita confirmar más de una vez.
                print("Ese pedido ya está confirmado.")
                continue

             pedido.cambiar_estado_pedido("Confirmado")
             print(f"Pedido {id_p} confirmado.")

        # 8) Volver al menu principal
            elif op == 8:
             break

        #salir del sistema
        elif opcion == 4:# Si el usuario elige 4 en el menú principal, imprimimos un mensaje y salimos
            print("Gracias por usar el sistema.")
            break
#se crea el menu y arranca el sistema
menu=Menu()
#menuSistema(menu)"""
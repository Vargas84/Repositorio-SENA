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
            CLAVE_ADMINISTRADOR='admi123'
            try:
              clave= input('Ingrese la clave del Administrador: ')#se pide clave para acceder a las funciones unicas de administrador
            except: 
              print('Opcion invalida')#en caso de ingresar numeros o vacios o caracteres especiales
              continue
          
            if clave != CLAVE_ADMINISTRADOR:#si la clave es incorrecta
              print('Clave incorrecta, Acceso denegado')
              continue #vuelve al menu principal

            print('Clave correcta, Bienvenido administrador')#clave correcta da permiso al menu de administrador
            admin = Administrador(1, "ADMIN", 0, 0)#se crea un administrador por defecto
            # sub-menu del administrador con sus distintas opciones
            while True:# bucle del submenu administrador que se repite hasta que seleccione la opcion de volver
                print("\n--- MENU ADMINISTRADOR ---")
                print("1) Agregar plato")
                print("2) Eliminar plato")
                print("3) Cambiar disponibilidad")
                print("4) Editar plato")
                print("5) Ver menú")
                print("6) Buscar plato")
                print("7) Volver")

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
                    try:
                        #id_p=menu.generar_id()
                        nombre = input("Nombre: ")#nombre del plato a registrar
                        precio = int(input("Precio: "))#precio del plato
                        categoria = input("Categoría: ")#etiqueta del plato
                        id_p= menu.generar_id() #generador de ID automtico ID plato
                        if precio<=0 or not es_letras_y_espacios(nombre) or  not es_letras_y_espacios(categoria) :#se evaluan los valores ingresados con la funcion
                           #para verificar las cadenas y su cotenido
                           print("No se puede agregar un plato, valores inconsistentes, asegurese que el precio no sea menor que 0 \n" \
                           "y que el nombre/categoria solo contengan letras y espacios")
                        else:#si se pasan las respectivas pruebas se agrega el plato 
                          admin.agregar_platos(menu, Plato(id_p, nombre, precio, categoria, True))
                        # Creamos la instancia Plato con disponibilidad True por defecto y delegamos
                        # al administrador para agregarlo al objeto menu.
                          print(f'Plato agregado con ID automatico: {id_p}')
                    except:
    # Si falla la lectura de datos (p. ej. precio no es int), se maneja el error y se vuelve al submenú.
                        print("Error: verfique los datos ingresados.")
                        continue

                elif op == 2:#eliminar plato
                    try:
                        admin.ver_menu(menu)#muestra el menu para saber que ID(plato) quiere eliminar
                        admin.eliminar_platos(menu, int(input("ID del plato a eliminar: ")))#Pide el ID, lo convierte a int
        # y delega la eliminación al administrador/Menu.
                    except:
                        print("ID inválido.")#en caso de no ingresar una opcion correcta
                        continue

                elif op == 3:#cambiar disponibilidad
                    try:
                        admin.ver_menu(menu)#muestra el menu para saber que ID(plato) quiere cambiar disponibilidad
      #Pide el ID del plato y llama al método que invierte su disponibilidad.
                        admin.cambiar_disponibilidad_plato(menu, int(input("ID del plato a cambiar disponibilidad: ")))
                    except:
                        print("ID inválido.")#encaso de ingresar un ID no valido
                        continue

                elif op == 4:#Editar plato (aquí el flujo pide el id y luego un nuevo precio y opcionalmente cambia disponibilidad)
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
                    
                    while True:
                        print(f'¿Que desea editar del plato {plato.nombre}?')
                        print("1) Editar el nombre")
                        print("2) Editar el precio")
                        print("3) Editar la categoria")
                        print("4) Volver al menu anterior")

                        try:
                          op=int(input("Ingrese la opcion de edicion: "))
                        except:
                           print("Error. Entrada invalida")
                           continue
                        
                        if op<1 or op>4:
                           print("Error: Opcion fuera de rango")
                           continue
                        elif op==1:
                           nuevo_nombre=input('Ingrese el nuevo nombre del plato: ')#se pide un nuevo nombre
                           if not es_letras_y_espacios(nuevo_nombre):
                              print("El nombre debe contener solo letras\n")
                           else:
                              admin.editar_platos(menu,id_p,nuevo_nombre=nuevo_nombre)
                        elif op==2:
                           nuevo_precio = input("ingrese el Nuevo precio del plato: ")#se pide el nuevo precio(int)
                           if nuevo_precio.isdigit():
                              nuevo_precio=int(nuevo_precio)
                              if nuevo_precio>0:
                                 admin.editar_platos(menu,id_p,nuevo_precio=nuevo_precio)
                                 break
                              elif nuevo_precio<=0:
                                 print("El precio debe ser mayor a 0")
                           elif nuevo_precio=="":
                                plato.precio=plato.precio
                                print(f"El precio del plato {plato.nombre} quedo igual: {plato.precio}")
                           else:
                              print("El precio debe ser un numero")
                        elif op==3:
                           nueva_categoria=input('Ingrese la nueva categoria del plato: ')
                           if not es_letras_y_espacios(nueva_categoria):
                              print("La categoria debe contener solo letras\n")
                           admin.editar_platos(menu, id_p,nueva_categoria=nueva_categoria) 
                        elif op==4:#volver al menu anterior
                           break

                    admin.ver_menu(menu)#muestra como quedo el menu con los cambios que se hicieron en editar
                    print("Plato actualizado correctamente \n")
                    
                elif op == 5:#ver menu
                    admin.ver_menu(menu)#muestra la lista actual de platos(delegado al objeto menu)


                elif op==6:#buscar un plato 
                   admin.ver_menu(menu)
                   try:
                     id_p=int(input('Ingrese el ID del plato a buscar: '))
                   except:
                      print('Opcion invalida')
                      continue
                   plato = menu.buscar_platos(id_p)

                   if plato is None:
                      print('Plato no encontrado')
                      continue
                   # Mostrar información del plato
                   print("\n--- INFORMACIÓN DEL PLATO ---")
                   print(plato.mostrar_informacion())
                   
                elif op == 7:#volver al menu principal
                  break#rompe el ciclo del meni administrado y vuelve al menu principal

        # ------------------- MESERO --------------------
        elif opcion == 2:# Si el usuario elige 2 en el menú principal, entramos al módulo Mesero.
            CLAVE_MESERO='mese123'#clave de acceso para el mesero
            try:
              clave=input('Ingrese la clave de acceso para mesero: ')#se recibe una clave ingresada por el usuario
            except:
              print('Opcion invalida')#en caso de vacios, numeros o caracteres especiales
              continue
            if clave != CLAVE_MESERO:#si la clave ingresada es distinta a la esperada se denegara el acceso
              print('Clave incorrecta, acceso denegado')
              continue
            print('Clave correcta, Bienvenido mesero')# en caso de coincidir se accede al menu mesero
            mesero = Mesero("Pedro", 123456789, 30000000, 1)# Creamos una instancia Mesero por defecto para usar sus métodos.
            pedidos = {}
            # Diccionario donde se almacenan pedidos creados por el mesero:
            #   - claves: id_pedido (int)
            #   - valores: objeto Pedido
            while True:#bucle del submenu
                print("\n--- MENU MESERO ---")
                print("1) Crear pedido")
                print("2) Agregar plato")
                print("3) Eliminar plato")
                print("4) Ver total")
                print("5) Entregar pedido")
                print("6) Ver menú")
                print("7) Volver")

                try:
                    op = int(input("Opción: "))#determina la accion dentro del menu MESERO
                except:
                    print("Opción inválida.")
                    continue

                if op < 1 or op > 7:
                  print("Opción inválida.Opcion fuera de rango")
                  continue

                if op == 1:#crear pedido
                  try:
                        id_p =  menu.generar_id() #generador de ID automtico ID pedidos
                       #id_p identificara el pediod en el diccionario pedidos
                        mesa = int(input("Mesa: "))
                  except:
                        print("Datos inválidos.")
                        continue

                  if id_p in pedidos:#se verifica si no existe ya un pedido con ese id
                    print("Ese pedido ya existe.")
                    continue

                  cliente= Cliente("Cliente Mesa", 0, 0)#creamos un cliente temporal que sera propietario del pedido
                  pedido= mesero.tomar_pedido(id_p, cliente, mesa)#mesero.tomar_pedido devuelve el objeto Pedido creado
                  pedidos[id_p] = pedido#guardamos el obejto Pedido en el diccionario 'pedidos' usando id_p como clave
                  print(f'Pedido creado con ID automatico: {id_p}')
                  #bucle para agregar platos al pedido recien creado
                  while True:
                    print("\n---agregar platos al pedido---")
                    print("Ingrese los datos del plato a agregar o '0' para terminar de agregar platos")
                    try:
                     id_plato = int(input("ID plato: "))# id_plato (int) identifica el plato dentro del menú.
                    except:
                     print(" ID invalido. Intente de nuevo")
                     continue
                    if id_plato == 0:# Si se ingresa 0, se finaliza la carga de platos para este pedido recién creado.
                     print("Finalizando ingreso de platos al pedido")
                     print(f'el total es de $ {pedido.calcular_total()}') #Mostramos el total calculado invocando pedido.calcular_total()
                     break


                    #1) buscar el plato
                    plato=menu.buscar_platos(id_plato)
                    if plato is None:# menu.buscar_platos devuelve el objeto Plato o None si no existe.
                     print("Plato no encontrado.")
                     continue

                    if plato.disponibilidad == False:# Si el plato existe pero no está disponible, no se puede agregar.
                     print(f"Plato {plato.nombre } no disponible.No se puede agregar")
                     continue

                    try:
                     cantidad= int(input("Cantidad: "))# cantidad (int) es cuántas unidades del plato se van a agregar al pedido.
                    except:
                     print("Cantidad invalida. Intente de nuevo")
                     continue


                  #intentar agregar el plato al pedido
                    mesero.agregar_plato_a_pedido(pedido,plato,cantidad)
                    # Delegación: mesero llama a Pedido.agregar_plato internamente.


                #al salir del sub-bucle, mostramos el total parcial
                  pedido.calcular_total()
                elif op == 2:#permitir agregar platos a un pedido ya existente(opcional)
                    try:
                        id_p = int(input("ID pedido: "))
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
          cliente = Cliente("Cliente", 0, 0)# Creamos un objeto Cliente temporal para usar sus métodos.
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
#menuSistema(menu)
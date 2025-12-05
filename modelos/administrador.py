from .plato import Plato
from .menu import Menu
from .usuarios import Usuario
#
class Administrador(Usuario):#clase hija de la clase Usuario
#el administrador tiene permisos para gestionar el menu: agregar,
#eliminar, cambiar disponibilidad, editar precios y ver el menu
  def __init__(self,id_administrador,nombre,documento,telefono):
    super().__init__(nombre,documento,telefono)#se llama al constructor
    #de la clase padre (Usuario) para inicializar nombre,documento y telefono
    self.id_administrador=id_administrador
    self.nombre=nombre
    self.documento=documento
    self.telefono=telefono
    self.siguiente_id=1


  #GESTION DEL MENU---Funciones del administrador
  def agregar_platos(self,menu,plato):
    #funcion que permite al administrador agregar un objeto Plato al objeto Menu
    #aca no se valida nada, el controlador (menuSistema) pidio y valido los datos
    #antes
      menu.agregar_plato(plato)#se llama la funcion agregar_plato() del objeto Menu


  def eliminar_platos(self,menu,id_plato):
    #funcion que permite al admnistrador eliminar un plato del menu por su ID
    #internamente llama al metodo elimininar_plato() de Menu, ya que recorre la lista
    # y elimina el plato
    menu.eliminar_plato(id_plato)# se llama la funcion eliminar platos de la clase MENU


  def ver_menu(self, menu):#el administrador puede vizualizar los platos del MENU
    menu.mostrar_menu()#se llama la funcion mostrar menu de la clase MENU

  def cambiar_disponibilidad_plato(self, menu, id_plato):#el administrador es el unico que puede cambiar el estado
  #de los platos si estan o no disponibles
    for plato in menu.platos:# reccorre la lista que guarda los platos en la clase MENU
        if plato.id_plato == id_plato:# y busca por id_plato,
            plato.cambiarDisponibilidad()#si lo encuentra se llama a la funcion cambiarDisponibilidad() del objeto Plato
            print(f'Disponibilidad del plato {plato.nombre} cambiada a {plato.disponibilidad}')
            return
    print('Plato no encontrado')#en caso contrario se lanzara un mensaje de error


  def editar_platos(self,menu,id_plato,nuevo_precio=None,nuevo_nombre=None,nueva_categoria=None):#funcion que ayuda al menuSistema a hacer validaciones
    #el administrador puede editar el precio de los platos
    plato=menu.buscar_platos(id_plato) #busca el objeto plato con el ID
    if plato is None:#si el plato no existe
       print("Error el plato no existe")
    if nuevo_nombre is not None:#editar nombre si el plato
       try:
         plato.nombre=nuevo_nombre#entra a asignar el nuevo nombre
         print(f"Nombre del plato actualizado a: {nuevo_nombre}")#envia un mensaje de actualizacion
       except:
         print("Error: ingrese datos correctos para nombre dese la funcion")#en caso de ingresar numeros
    if nuevo_nombre=="":#si se deja un vacio el sistema dejara el nombre que tiene sin modificarlo
          plato.nombre=plato.nombre#se asigna nuevamente el mismo nombre
          print(f"El nombre del plato {plato.nombre} quedo igual: {plato.nombre}")#se da aviso de esta asignacion

    if nuevo_precio is not None:#editar precio si no es nulo el valor
          plato.precio=nuevo_precio#se asigna el nuevo precio
          print(f"Precio actualizado a: {nuevo_precio}")#se da aviso de esta actualizacion 
    if nuevo_precio=="":#si el nuevo precio es vacio el sistema dejara el mismo precio que tenia
       plato.precio=plato.precio#se asigna el mismo precio
       print(f"El precio del plato {plato.nombre} quedo igual: {plato.precio}")#se da aviso de esta asignacion



    if nueva_categoria is not None:#editar categoria si no es nulo el valor
        plato.categoria=nueva_categoria#se le asigna la nueva categoria
        print(f'Categoria actualizada a: {nueva_categoria}')#se da aviso de la asignacion    
    if nueva_categoria=="":#en caso de quedar en vacio el espacio el sistema dejara la misma categoria
          plato.categoria=plato.categoria#asignacion a la categoria que estaba
          print(f"La categoria del plato quedo igual {plato.categoria}")#aviso de esa asignacion
       
    


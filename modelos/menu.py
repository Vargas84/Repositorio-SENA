from .plato import Plato
class Menu:#controla la manera en la que se muestra y utiliza el menu al los usuarios
  def __init__(self):
    self.platos=[]#lista de donde se almacenan todos los platos,inicialmente vacia
    self.siguiente_id=1 #Nuevo: contador de IDs
    # los platos son agregados por el administrador

  def generar_id(self):#generador de IDs para el menu
    id_generado=self.siguiente_id #el id generado es igual al valor actual del id
    self.siguiente_id+=1 #el ultimo id se aumenta una vez ya generado
    return id_generado #retorna este valor
#
  def agregar_plato(self,plato):#se agrega cada plato a la lista del menu
  #no realiza validaciones porque asumimos que el controlador (menuSistema)
  #ya pidio y valido los datos antes de crear el obejto plato
    self.platos.append(plato)#recibe un objeto Plato y lo agrega a la lista de platos
    print(f'El plato {plato.nombre} fue agregado correctamente al menu')

  def mostrar_menu(self):#se muestran los platos que hay en el menu y su informacion
    print('MENU DEL DIA')
    for plato in self.platos:#recorre la lista
      if not self.platos:#si no hay platos cargados en el menu
        print('No hay platos en el menu')
        return
      print(plato.mostrar_informacion())#se muestra el plato y su informacion con ayuda del
      #metodo mostrar_informacion() de Plato con el nombre/precio/categoria y disponibilidad
    print(' ')

  def eliminar_plato(self,id_plato):# se elimina platos de la lista self.platos segun el id_plato
    for plato in self.platos:#recorremos la lista buscando el primer plato cuyo id_plato coincida
       if plato.id_plato==id_plato:
        self.platos.remove(plato)#lo removemos de la lista para que deje de aparecer
        #en futuros listados de menu
        print(f'Plato {plato.nombre} eliminado correctamente')
        plato.eliminado=True#ademas se marca como eliminado el Plato para indicar quee fue eliminado
        #esto nos ayuda en caso de que haya referencias al obejto en pedidos
        break #salimos de la funcion para no buscar mas
    else:
      print('Plato no encontrado')#si no seencuentra ese ID
    print(' ')

  def buscar_platos(self,id_plato):#busca los platos por su ID y retorna la informacion del ese plato en especifico
    #print('Platos encontrados:')
    for plato in self.platos:#recorre la lista de platos uno por uno
      if plato.id_plato==id_plato:
        return plato #cuando encuentra un plato cuyo id coincide, lo retorna
    return None # Si recorre toda la lista y no encuentra nada, devuelve None
    #para que el que este llamando a la funcion pueda verificae y actuar con un mensaje de alerta

  def platos_disponibles(self):#solo mostrara los platos con disponibilidad en el menu
  #util para mostrarle a un cliente que platos puede pedir en ese momento
    print(' ')
    print('Platos disponibles:')
    for plato in self.platos:#recorremos la lista de platos
      if plato.disponibilidad==True:#verificamos la propiedad disponibilidad del objeto Plato
        print(plato.mostrar_informacion())#se imprime la nformacion del plato si esta disponible
    print(' ')

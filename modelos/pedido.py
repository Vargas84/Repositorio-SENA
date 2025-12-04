from .plato_pedido import PlatoPedido
class Pedido:
  def __init__(self,id_pedido,usuario,mesa,estado='En proceso'):#,usuario,fecha,hora,estado='Proceso'):
#
    self.id_pedido=id_pedido
    self.usuario=usuario
    self.platos_pedidos=[]#guarda los platos y sus cantidades
    self.total=0#acumulador deel total calculado ( se recalcula con calcular_total)
    self.estado=estado
    self.mesa=mesa
    self.entregado=False#controla si ya fue entregado
    # Bandera para indicar si el pedido ya fue entregado.
    # Es distinto de 'estado' y facilita comprobaciones booleanas.



  def agregar_plato(self,plato,cantidad):#agrega platos al pedido de un cliente
  # El llamador debería haber buscado el plato con menu.buscar_platos()
  # y verificar que no sea None, pero repetimos la verificación aquí.
    if plato is None:
      print('Plato no encontrado')#si el plato no existe no se puede agregar
      return
    if plato.eliminado==True:# si el plato esta eliminado no se puede agregar
    # esto para prevenir inconsistencias si el administrador elimina un plato
    # mientras hay pedidos en curso
      print(f'Plato {plato.nombre} eliminado no se puede agregar')#si el plato esta eliminado tampoco se puede agregar
      return
    if plato.disponibilidad==False:#si el plato existe pero no esta disponible,
    # no se puede agregar
      print(f'Plato {plato.nombre} no disponible no se puede agregar')
      return
    #si paso todas las validaciones se agrega mediante
    # el objeto PlatoPedido y se agrega a la lista interna del pedido
    plato_pedido=PlatoPedido(plato,cantidad)
    self.platos_pedidos.append(plato_pedido)
    print(f'Plato {plato.nombre} agregado correctamente')

  def eliminar_plato_pedido(self,id_plato):#se elimina un plato del pedido
    for plato_pedido in self.platos_pedidos:# se recorre la lista interna
      if plato_pedido.plato.id_plato==id_plato:# elimina el primer PlatoPedido cuyo plato.id_plato coincida con id_plato
        self.platos_pedidos.remove(plato_pedido)# si lo encuentra lo elimina de la lista y muestra un mensaje de confirmacion
        print(f'Plato {plato_pedido.plato.nombre} eliminado correctamente')
        break
    else:
      print('Plato no encontrado') # de lo contrario muestra un mensaje de 'No encontrado'



  def actualizar_cantidad_platos(self,id_plato,nueva_cantidad):
    for plato_pedido in self.platos_pedidos:# se reccorre la lista de self.platos_pedidos
      if plato_pedido.plato.id_plato==id_plato:# busca el PlatoPedido por id_plato
         plato_pedido.cantidad=nueva_cantidad# y actualiza su campo cantidad
         print(f'La nueva cantidad del plato {plato_pedido.plato.nombre} en el pedido es {plato_pedido.cantidad}')
         break
    else:
     print('Plato no encontrado')#si no lo encuentra, informa al usuario

  def calcular_total(self):#recalcula el total del pedido
          #Lógica:
          #total = sum(plato.precio * cantidad for cada PlatoPedido)
    self.total=0 #reiniciamos el calculador antes de sumar
    for plato_pedido in self.platos_pedidos:
  # Cada plato_pedido.plato tiene el atributo precio, multiplicamos por cantidad.
      self.total+=plato_pedido.plato.precio*plato_pedido.cantidad
    return self.total

  def cambiar_estado_pedido(self,nuevo_estado):
        #Cambia el campo textual 'estado' y muestra un mensaje informativo.
        #Es una forma centralizada de actualizar el estado (por ejemplo:
        #En proceso' -> 'Confirmado' -> 'Entregado').
    self.estado=nuevo_estado
    print(f'El estado del pedido {self.id_pedido} fue cambiado a {self.estado}')

  def mostrar_pedido(self):# muestra un resumen simple del pedido
     print(f'Pedido {self.id_pedido} pertenece a {self.usuario.nombre} y contiene {[plato_pedido.plato.nombre for plato_pedido in self.platos_pedidos]}')

  def entregar(self):#marca el pedido como entregado. Primero verifica la bandera entregado
  # para evitar entregar multiples veces el mismo pedido
    if self.entregado:
      print(f'El pedido {self.id_pedido} ya fue entregado')#si ya fue entregado informa y no hace cambios
      return
    #si no, marca entregado= True, marcamos la banderita y actualizamos el estado textual
    self.entregado=True
    self.cambiar_estado_pedido('Entregado')# y cambia el estado a entregado reutulizando
    # la funcion cambiar_estado_pedido
    print(f'El pedido {self.id_pedido} fue entregado')

  def confirmar(self):# marca el pedido como confirmado (por el cliente). Se protege contra
  # confirmar varias veces comprobando el estado actual
    if self.estado.lower()=="confirmado":# usamos lower para comparar sin importar mayusculas o minusculas
      print(f'El pedido {self.id_pedido} ya fue confirmado')# en caso de que ya este confirmado se muestra
      # un mesnaje y no se ejecuta nada
      return

    self.estado="Confirmado"# en caso de que no este confirmado o se esta hciendo por 1 vez
    # cambiamos el estado textal a 'confirmado'
    print(f'El pedido {self.id_pedido} fue confirmado exitosamente')

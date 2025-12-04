from .pedido import Pedido
from .plato import Plato
from .usuarios import Usuario
#
class Cliente(Usuario):
  #representa al cliente puede ver el menu, crear sus propios pedidos, agregar o eliminar platos
  # a su pedido, ver el total y ver el resumen
  def __init__(self,nombre,documento,telefono):
    super().__init__(nombre,documento,telefono)
    self.nombre=nombre
    self.documento=documento
    self.telefono=telefono

  def ver_menu(self,menu):
      menu.mostrar_menu()#el cliente puede ver el menu

  def crear_pedido(self,id_pedido,mesa):
    #crea un objeto Pedido con el cliente como usuario
      pedido=Pedido(id_pedido,self,mesa)#el cliente puede crear un pedido , un objeto de tipo Pedido
      print(f'Pedido {id_pedido} creado correctamente')
      return pedido #devuelve el Pedido para que el controlador(Menu sistema) lo guarde

  def agregar_plato_a_pedido(self,pedido,plato,cantidad):#el cliente puede agregar el
    #el plato a un pedido
    #permite que el cliente agregue un plato a su pedido delegando
    #a la clase Pedido(responsable de las validaciones)
      pedido.agregar_plato(plato,cantidad)

  def eliminar_plato(self, pedido, id_plato):
        pedido.eliminar_plato_pedido(id_plato)#el cliente puede eliminar un plato
        #de un pedido
        #delegacion a la clase pedido

  def ver_total(self, pedido):
    #Delegacion para calcular el total desde la clase Pedido
        pedido.calcular_total()#el cliente puede ver el total del pedido

  def ver_resumen(self, pedido):
    #muestra resumen del pedido (delegacion a Pedido)
        pedido.mostrar_pedido()#el cliente puede ver el resumen de su pedido


from .pedido import Pedido
from .plato import Plato
from .usuarios import Usuario
#
class Mesero(Usuario):
  #representa al mesero. quien toma pedidos, agrega o elimina platos de estos pedidos
  # y puede hacer entrega de estos pedidos
    def __init__(self, nombre,documento,telefono, id_mesero):
        super().__init__(nombre,documento,telefono)
        self.id_mesero = id_mesero
        self.nombre=nombre
        self.documento=documento
        self.telefono=telefono

    def tomar_pedido(self,id_pedido,cliente,mesa):#el mesero puede tomar pedidos
    #crea un objeto Pedido con id_pedido, el cliente y la mesa
      pedido=Pedido(id_pedido,cliente,mesa)
      print(f'Pedido {id_pedido} creado para mesa {mesa}/Cliente {cliente.nombre}')# se muestra un mensaje de la creacion del pedido
      return pedido #devuelve el objeto pedido para que el controlador(Menu) lo almacene,
      #Devuelve el objeto pedido para uso externo


    def agregar_plato_a_pedido(self, pedido, plato, cantidad):#el mesero debe agregar el plato a un pedido
        pedido.agregar_plato(plato, cantidad)#recibe un objeto Pedido(instancia de pedido) y delega la accion de
        #agregar el plato a la propia clase Pedido llamando su metodo
        #el cual recibe un palto y una cantidad como parametros

    def eliminar_plato_de_pedido(self, pedido, id_plato):#el mesero debe poder eliminar un plato de un pedido
        pedido.eliminar_plato_pedido(id_plato)#recibe un objeto Pedido y le pide eliminar el plato por un id_plato

    def entregar_pedido(self, pedido):
      #marca el pedido como entregado usando el metodo que ya existe
      #en la clase Pedido (cambiar_estado_pedido)
        pedido.cambiar_estado_pedido("Entregado")# una vez el pedido esta confirmado , el estado cambia

    def ver_menu(self, menu):
        menu.mostrar_menu()# el mesero debe poder ver el menu

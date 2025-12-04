
class PlatoPedido:# esta clase intermedia une la clase Plato y la clase pedido
#porque aca podemos agregar platos y las cantidades de ese plato
#cada elemento de self.platos_pedidos en Pedido sera una instancia de esta clase
  def __init__(self,plato,cantidad):
    self.plato=plato#referencia al objeto Plato
    self.cantidad=cantidad# numero que indica cuantas unidades del plato se pidieron
#
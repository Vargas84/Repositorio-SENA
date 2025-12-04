
class Plato:#Clase que crea los platos que se muestran en el menu
# y que tambien van relacionadas a pedido
  def __init__(self,id_plato,nombre,precio,categoria,disponibilidad):
    self.id_plato=id_plato#identifica al plato
    self.nombre=nombre
    self.precio=precio
    self.categoria=categoria
    self.disponibilidad=disponibilidad#indica si se puede no pedir
    self.eliminado=False

  def mostrar_informacion(self):#se muestra la informacion de cada plato de acuerdo a su disponibilidad
    if self.disponibilidad==True:
      return f'ID: {self.id_plato} /Nombre:{self.nombre}/ Precio:{self.precio}/ Categoria:{self.categoria}/ Disponibilidad: Disponible'
    else:
     return f'ID: {self.id_plato} /Nombre:{self.nombre}/ Precio:{self.precio}/ Categoria:{self.categoria}/ Disponibilidad: No Disponible'


  def cambiarDisponibilidad(self):#se cambia la disponibilidad de cada plato
    if self.disponibilidad==True:
      self.disponibilidad=False
    else:
      self.disponibilidad=True
      #
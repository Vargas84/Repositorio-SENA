
class Plato:#Clase que crea los platos que se muestran en el menu
# y que tambien van relacionadas a pedido
  def __init__(self,id_plato,nombre,precio,categoria,disponibilidad):
    self.id_plato=id_plato#identifica al plato
    self.nombre=nombre
    self.precio=precio
    self.categoria=categoria
    self.disponibilidad="Disponible"#indica si se puede no pedir
    self.eliminado=False

  def mostrar_informacion(self):#se muestra la informacion de cada plato de acuerdo a su disponibilidad
    if self.disponibilidad=="Disponible":
      return f'ID: {self.id_plato} /Nombre:{self.nombre}/ Precio:{self.precio}/ Categoria:{self.categoria}/ Disponibilidad: {self.disponibilidad}'
    else:
     return f'ID: {self.id_plato} /Nombre:{self.nombre}/ Precio:{self.precio}/ Categoria:{self.categoria}/ Disponibilidad: {self.disponibilidad}'


  def cambiarDisponibilidad(self):#se cambia la disponibilidad de cada plato
    if self.disponibilidad=="Disponible":
      self.disponibilidad="No Disponible"
    else:
      self.disponibilidad="Disponible"
      #

class Usuario:#Clase padre para crear las clases hijas como Administrador/Cliente/Mesero
#todas los demas roles (Administrador,Mesero,Cliente) heredan de esta clase para
#reutilizar atributos basicos #
  def __init__(self,nombre,documento,telefono):
    #al usar este constructor en las subclases
    #nos aseguramos de inicializar correctamente estos atributos
    self.nombre=nombre
    self.documento=documento
    self.telefono=telefono

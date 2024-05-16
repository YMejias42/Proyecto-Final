# Cursor para ejecutar consultas SQL
  cursor = mariadb()
# Función para mostrar todas las mesas disponibles
def mostrar_mesas_disponibles():
  query = "SELECT * FROM Mesas"
  cursor.execute(query)
  mesas = cursor.fetchall()
  print("Mesas Disponibles:")
  for mesa in mesas:
    print(f"Número: {mesa[1]}, Capacidad: {mesa[2]}")
# Función para agregar un nuevo cliente
def agregar_cliente(nombre, telefono):
  query = "INSERT INTO Clientes (nombre, telefono) VALUES (%s, %s)"
  cursor.execute(query, (nombre, telefono))
  db_connection.commit()
  print("Cliente agregado exitosamente.")
# Función para realizar un pedido
def realizar_pedido(mesa_id, cliente_id, detalle_pedido):
  query = "INSERT INTO Pedidos (mesa_id, cliente_id, detalle_pedido) VALUES
(%s, %s, %s)"
  cursor.execute(query, (mesa_id, cliente_id, detalle_pedido))
  db_connection.commit()
print("Pedido realizado con éxito.")
# Función principal
def main():
  print("Bienvenido al Sistema de Administración de Restaurantes")

  while True:
    print("\nOpciones:")
    print("1. Mostrar mesas disponibles")
    print("2. Agregar nuevo cliente")
    print("3. Realizar pedido")
    print("4. Salir")

opcion = input("Seleccione una opción: ")

  if opcion == "1":
    mostrar_mesas_disponibles()
  elif opcion == "2":
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    agregar_cliente(nombre, telefono)
  elif opcion == "3":
    mesa_id = input("Ingrese el ID de la mesa: ")
    cliente_id = input("Ingrese el ID del cliente: ")
    detalle_pedido = input("Ingrese los detalles del pedido: ")
    realizar_pedido(mesa_id, cliente_id, detalle_pedido)
  elif opcion == "4":
    print("¡Hasta luego!")
    break
  else:
  print("Opción no válida. Por favor, seleccione una opción válida.")
    
if _name_ == "_main_":
  main()

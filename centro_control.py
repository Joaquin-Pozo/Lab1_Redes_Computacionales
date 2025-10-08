# Servidor TCP - Centro de Control (Recibe reportes y los almacena en un historial)
import socket

HOST = '127.0.0.1'
PORT = 8001
historial = []

# Crea un socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print("CONTROL: Esperando conexión de la Estación Espacial...")

    conn, addr = servidor.accept()
    with conn:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            # Almacena los reportes en historial
            if data.startswith("REPORTE:"):
                reporte = data.split("REPORTE:")[1].strip()
                historial.append(reporte)
                conn.sendall("Reporte almacenado. Todo bajo control, Estación.\n".encode('utf-8'))
            # Muestra los reportes almacenados
            elif data.strip() == "CONSULTAR":
                if historial:
                    registros = "=== HISTORIAL DE COMUNICACIONES ===\n" + "\n".join(historial)
                # Si no hay nada almacenado aun, muestra mensaje de aviso
                else:
                    registros = "=== HISTORIAL DE COMUNICACIONES ===\n" + "(No hay reportes todavía)\n"
                conn.sendall(registros.encode('utf-8'))
            # Finaliza la ejecucion del servidor
            elif data.strip() == "MISION_COMPLETA":
                conn.sendall("Comunicación finalizada. Buen trabajo, astronautas.\n".encode('utf-8'))
                break
            # Si el cliente envia un mensaje distinto, avisa error
            else:
                conn.sendall("Mensaje inválido.\nUtilice 'REPORTE:', 'CONSULTAR' o 'MISION_COMPLETA'.\n".encode('utf-8'))
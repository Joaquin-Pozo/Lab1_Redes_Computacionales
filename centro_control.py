# Servidor TCP - Centro de Control (Recibe reportes y los almacena en un historial)
import socket

HOST = '127.0.0.1'
PORT = 8001
historial = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print("CONTROL: Esperando conexión de la Estación Espacial...")

    conn, addr = servidor.accept()
    with conn:
        print(f'CONTROL: Conectado con {addr}')
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            if data.startswith("REPORTE:"):
                reporte = data.split("REPORTE:")[1].strip()
                historial.append(reporte)
                conn.sendall("Reporte almacenado. Todo bajo control, Estación.\n".encode('utf-8'))
            elif data.strip() == "CONSULTAR":
                if historial:
                    registros = "=== HISTORIAL DE COMUNICACIONES ===\n" + "\n".join(historial)
                else:
                    registros = "=== HISTORIAL DE COMUNICACIONES ===\n" + "(No hay reportes todavía)\n"
                conn.sendall(registros.encode('utf-8'))
            elif data.strip() == "MISION_COMPLETA":
                conn.sendall("Comunicación finalizada. Buen trabajo, astronautas.\n".encode('utf-8'))
                break
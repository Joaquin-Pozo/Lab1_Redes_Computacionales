# Servidor UDP - Sistema de Alertas (Recibe alertas y responde inmediatamente sin almacenar información)
import socket

HOST = '127.0.0.1'
PORT = 8002

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
    servidor.bind((HOST, PORT))
    print("ALERTAS: Esperando alertas rápidas...")

    while True:
        data, addr = servidor.recvfrom(1024)
        mensaje = data.decode('utf-8')
        if mensaje == "base_segura":
            respuesta = f'Sistema: Modo emergencia desactivado. Mantente seguro allá arriba.'
            servidor.sendto(respuesta.encode('utf-8'), addr)
            break
        respuesta = f'Alerta: CONFIRMADO: {mensaje}'
        servidor.sendto(respuesta.encode('utf-8'), addr)
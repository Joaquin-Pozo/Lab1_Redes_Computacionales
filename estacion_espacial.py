# Cliente - Estación Espacial Internacional (Se comunica con el Sistema de Alertas mediante socket UDP y con el Centro de Control mediante TCP)
import socket

HOST = '127.0.0.1'
# Para socket TCP
tcp_port = 8001
# Para socket UDP
udp_port = 8002

# Menú de inicio: permite realizar una conexión al servidor a la vez
while opcion != 0:
    print("====================================================================")
    print("¡Bienvenido al Centro de Comando Espacial!\n")
    print("Ingrese el número de las siguientes opciones para avanzar\n")
    print("1. Sistema de Alertas\n")
    print("2. Centro de Control\n")
    print("0. Finalizar la ejecución del programa\n")
    opcion = int(input())
    if opcion == 0:
        break
    elif opcion == 1:
        # Se conecta al servidor TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_tcp:
            cliente_tcp.connect((HOST, tcp_port))
            print("ESTACIÓN: Conectado al Centro de Control (TCP)")
    elif opcion == 2:
        # Se conecta al servidor UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente_udp:
            print("ALERTAS: Conectado el Sistema de Alertas (UDP)")
    else:
        print("Opción inválida. Ingrese nuevamente\n")
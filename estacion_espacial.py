# Cliente - Estación Espacial Internacional (Se comunica con el Sistema de Alertas mediante socket UDP y con el Centro de Control mediante TCP)
import socket

HOST = '127.0.0.1'
# Para socket TCP
tcp_port = 8001
# Para socket UDP
udp_port = 8002
# Almacena la opción seleccionada para navegar por el menú
opcion = -1

# Menú de inicio: permite realizar una conexión al servidor a la vez
while opcion != 3:
    print("====================================================================")
    print("¡Bienvenido al Centro de Comando Espacial!\n")
    print("Seleccione una de las siguientes opciones para avanzar:")
    print("1. Conectarse al Centro de Control (TCP)")
    print("2. Conectarse al Sistema de Alertas (UDP)")
    print("3. Finalizar la ejecución del programa")
    opcion = int(input())
    if opcion == 1:
        # Se conecta al servidor TCP
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_tcp:
                cliente_tcp.connect((HOST, tcp_port))
                print("\n=== ESTACIÓN: Conectado al Centro de Control (TCP) ===\n")
                while True:
                    mensaje = input("Astronauta> ")
                    cliente_tcp.sendall((mensaje + "\n").encode('utf-8'))
                    respuesta = cliente_tcp.recv(1024).decode('utf-8')
                    print(f"Centro de Control: {respuesta.strip()}")
                    
                    if mensaje.strip() == "MISION_COMPLETA":
                        break

        # No se pudo conectar el servidor TCP -> Muestra error
        except ConnectionRefusedError:
            print("No se pudo conectar al Centro de Control.\n")

    elif opcion == 2:
        try:
            # Se conecta al servidor UDP
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente_udp:
                # Espera un max de 1 segundo por respuesta 
                cliente_udp.settimeout(1.0)
                print("\n=== ALERTAS: Conectado el Sistema de Alertas (UDP) ===\n")
                while True:
                    mensaje = input("Emergencia> ")
                    cliente_udp.sendto(mensaje.encode('utf-8'), (HOST, udp_port))

                    try:
                        print(f"Alerta: {cliente_udp.recv(1024).decode('utf-8')}")
                    
                    # Pasó el tiempo de espera -> No se pudo conectar al servidor
                    except socket.timeout:
                        print("No se pudo conectar con el Sistema de Alertas.\n")
                        break

                    if mensaje.strip() == "base_segura":
                        print(cliente_udp.recv(1024).decode('utf-8'))
                        break
        # Omite error -> Confirmacion de conexion realizada por socket.timeout
        except Exception:
            pass
            
    elif opcion == 3:
        # Cierra las conexiones de ambos servidores (en caso de que hayan quedado abiertas)
        print("\nFinalizando conexiones activas...")

        # Para TCP: envia su mensaje de cierre
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_tcp:
                cliente_tcp.connect((HOST, tcp_port))
                mensaje  = "MISION_COMPLETA"
                cliente_tcp.sendall((mensaje + "\n").encode('utf-8'))
        except Exception:
            # Si el servidor ya está cerrado, omite error
            pass

        # Para UDP: envia su mensaje de cierre
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente_udp:
                mensaje = "base_segura"
                cliente_udp.sendto(mensaje.encode('utf-8'), (HOST, udp_port))
        except Exception:
            # Si el servidor ya está cerrado, omite error
            pass

        print("Servidores notificados. Cerrando estación...\n")

        print("Finalizando programa. Buen trabajo, astronautas.\n")
        break

    else:
        print("Opción inválida. Intente nuevamente\n")
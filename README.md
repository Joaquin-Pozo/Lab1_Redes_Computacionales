# Laboratorio 1 - Redes Computacionales
<img src="logo_usach.svg" alt="escudo usach" width="60" align="center"> **Universidad de Santiago de Chile (USACH)**

Estudiante: Joaquín Pozo

Rut: 20.237059-4

En este laboratorio se implementa una comunicación **cliente-servidor** utilizando sockets **UDP** y **TCP** de manera local.

El objetivo es simular la interacción entre una ***Estación Espacial Internacional*** y su Centro de Control en la Tierra.

---

### Instrucciones para ejecutar cada programa (Unix/Linux).

1. Abre tres terminales en el directorio del proyecto.

2. En la primera terminal, ejecuta el servidor TCP:
```bash
python3 centro_control.py
```

3. En la segunda terminal, ejecuta el servidor UDP:
```bash
python3 sistema_alertas.py
```

4. En la tercera terminal, ejecuta al cliente:
```bash
python3 estacion_espacial.py
```

---

### Ejemplo de uso.

#### Servidor TCP: centro_control.py

El servidor TCP es el encargado de recibir reportes y almacenarlos en un historial.

Comandos válidos:
> **REPORTE:** <***mensaje***>
>
>> Almacena un reporte en el historial de reportes.
>
> **CONSULTAR**
>> Muestra todos los reportes ingresados.
>
> **MISION_COMPLETA**
>> Finaliza la conexión con el servidor.

Ejemplo de ejecución desde el cliente:
```yaml
Astronauta> REPORTE: Orbitando la Tierra a una velocidad constante de 28.000 km/hr.
Centro de Control: Reporte almacenado. Todo bajo control, Estación.

Astronauta> CONSULTAR
Centro de Control: === HISTORIAL DE COMUNICACIONES ===
1. Orbitando la Tierra a una velocidad constante de 28.000 km/hr.

Astronauta> MISION_COMPLETA
Centro de Control: Comunicación finalizada. Buen trabajo, astronautas.
```

#### Servidor UDP: sistema_alertas.py

El servidor UDP es el encargado de recibir alertas y responder inmediatamente sin almacenar la información.

Comandos válidos:
> **base_segura**
>
>> Finaliza la conexión con el servidor.

Ejemplo de uso desde el cliente:
```makefile
Emergencia> Lluvia de meteoros excepcionalmente brillante colisionando con la Estación Espacial.
Alerta: CONFIRMADO: Lluvia de meteoros excepcionalmente brillante colisionando con la Estación Espacial.

Emergencia> base_segura
Alerta: Sistema: Modo emergencia desactivado. Mantente seguro allá arriba.
```
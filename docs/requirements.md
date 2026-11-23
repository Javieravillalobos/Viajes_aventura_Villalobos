# Requerimientos del Sistema - Viajes Aventura

## 1. Requerimientos Funcionales (RF)

| ID | Nombre | Descripción | Prioridad | Criterio de Aceptación |
| :--- | :--- | :--- | :---: | :--- |
| **RF-01** | Registro e inicio de sesión | El cliente debe poder registrarse con sus datos y autenticarse en el sistema[cite: 2, 13]. | Alta | Al ingresar correo y contraseña válidos, accede al menú; si son incorrectos, muestra error en español[cite: 2, 9]. |
| **RF-02** | Gestión de destinos (CRUD) | El administrador puede registrar, listar, modificar y eliminar destinos turísticos[cite: 2, 13]. | Alta | Al crear un destino con nombre y costo base, este aparece listado inmediatamente en la consulta de destinos[cite: 2, 13]. |
| **RF-03** | Creación de paquetes | El administrador crea paquetes combinando uno o más destinos, definiendo fechas, cupos y costo total[cite: 2, 13]. | Alta | Al seleccionar 2 destinos, el paquete se guarda y calcula su costo sumando los valores asociados[cite: 2, 13]. |
| **RF-04** | Consulta de disponibilidad | Los usuarios pueden consultar paquetes disponibles por fechas y cupos[cite: 2, 13]. | Media | El listado solo muestra paquetes con fecha vigente y cupos mayores a 0[cite: 2, 13]. |
| **RF-05** | Reserva de paquetes | Un cliente autenticado puede reservar un paquete turístico disponible[cite: 2, 13]. | Alta | Al confirmar, se descuenta 1 cupo del paquete y la reserva queda guardada en la base de datos[cite: 2, 13]. |
| **RF-06** | Historial de reservas | El cliente puede consultar el historial de sus reservas realizadas[cite: 2, 13]. | Media | El sistema muestra únicamente las reservas asociadas al ID del cliente conectado (paquete, fecha y monto)[cite: 2, 13]. |

## 2. Requerimientos No Funcionales (RNF)

| ID | Nombre | Descripción | Prioridad | Criterio de Aceptación |
| :--- | :--- | :--- | :---: | :--- |
| **RNF-01** | Seguridad de credenciales | Las contraseñas deben almacenarse encriptadas mediante hashing seguro[cite: 6, 13]. | Alta | En la tabla `users` de SQLite se guarda un hash y nunca la contraseña en texto plano[cite: 6, 9, 13]. |
| **RNF-02** | Validación de datos | El sistema debe validar formato y tipo de datos ingresados por el usuario[cite: 13]. | Alta | Ante datos inválidos (ej. letras en precios o correo sin `@`), el sistema no se cae y muestra aviso[cite: 13]. |
| **RNF-03** | Estándar y arquitectura | Código y BD en inglés; interfaz en español; separación en capas (presentación, lógica, persistencia). | Media | El proyecto tiene carpetas separadas por capa y nombres de tablas/variables en inglés[cite: 9]. |
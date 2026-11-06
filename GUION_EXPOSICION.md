# 🎤 GUION DE EXPOSICIÓN — TECNOLOGÍA BLOCKCHAIN
### Cómo defender tu proyecto en 10 minutos y sacarte 100 con el Ing. Hermes Rodriguez

---

## 💡 Las 4 Metáforas Clave (Para hablar en cristiano sin enredarte)

Si te pones nervioso con la matemática de SHA-256, usa estas 4 comparaciones con el docente:

1. **La Función Hash = "La Huella Digital del Bloque":**  
   > *"Ingeniero, un hash es como la huella digital humana. No importa si el bloque tiene 1 renglón o un millón de transacciones, su huella siempre mide 64 caracteres. Y si alguien le cambia una sola letra o un centavo, la huella digital cambia por completo (Efecto Avalancha)."*

2. **El Nonce y Proof of Work = "La Combinación de un Candado":**  
   > *"Minar no es magia. Es como tener un candado con clave numérica y empezar a probar desde 0, 1, 2, 3... hasta que hace 'click' y abre. En nuestro código, el candado abre cuando el hash empieza con '000'. El número de intentos que tomó abrirlo es el 'Nonce'."*

3. **El Previous Hash = "La Fila de Fichas de Dominó":**  
   > *"Cada bloque sella en su interior la huella del bloque que tiene detrás. Si un atacante entra al bloque 2 y le cambia el dinero, su huella cambia, el bloque 3 ya no lo reconoce, el enlace se rompe y toda la fila hacia adelante queda invalidada."*

4. **El Consenso = "La Regla de la Mayoría Trabajadora":**  
   > *"Si dos computadoras tienen versiones distintas de la verdad, ¿a quién le creemos? A la cadena más larga. ¿Por qué? Porque la más larga representa a la mayoría de mineros que gastaron más electricidad y trabajo legítimo."*

---

## ⏱️ Estructura de la Defensa (Minuto a Minuto)

```
[0:00 - 2:00]  → Introducción teórica y objetivo (Parte I)
[2:00 - 5:00]  → DEMO EN VIVO CON LA GUI (Parte II) ⭐ Momento cumbre
[5:00 - 8:00]  → Caso de Estudio: Ganadería en Beni / Bolivia (Parte III)
[8:00 - 10:00] → Conclusión y Cierre
[10:00 - 15:00]→ Preguntas y Respuestas del Docente
```

---

## 🎬 Guion Paso a Paso para la Demo en Vivo (Minutos 2 a 5)

Abre la pantalla (`py gui.py`) proyectada en la pizarra o televisor y sigue estos 4 pasos exactos:

### PASO 1: Presentar la Cadena Sana
* **Acción:** Muestra la pantalla inicial con las tarjetas en color gris/azul y el semáforo verde arriba.
* **Lo que dices:**  
  > *"Ingeniero, aquí tenemos nuestra blockchain activa. En pantalla vemos el Bloque Génesis (índice 0) y tres transacciones reales. Noten que todos los hashes propios empiezan con '000' porque cumplieron la Prueba de Trabajo (Proof of Work), y cada bloque está unido al anterior mediante el campo 'Hash Anterior'. Arriba vemos el semáforo en VERDE: Cadena 100% íntegra."*

---

### PASO 2: Minar un Nuevo Bloque en Vivo
* **Acción:** Escribe en la izquierda `Remitente: Juan`, `Receptor: Pedro`, `Monto: 300` y dale clic a **⛏️ MINAR Y AÑADIR BLOQUE**.
* **Lo que dices:**  
  > *"Vamos a agregar una nueva transacción. Al hacer clic en 'Minar', la computadora empieza a iterar el contador Nonce miles de veces por segundo en segundo plano hasta encontrar un hash con tres ceros... ¡Listo! Tomó alrededor de 15,000 intentos y se añadió el Bloque #4 al final de la cadena de forma segura."*

---

### PASO 3: El Hackeo y la Detección de Fraude (LA PRUEBA CLAVE)
* **Acción:** Haz clic en el botón rojo **🚨 2. Simular Ataque (Hackear Bloque 2)**.
* **Lo que dices:**  
  > *"Ahora simularemos un ataque informático. Un hacker entra a la memoria del Bloque 2 y cambia la transacción de 25 Bs a 9,999 Bs. Observen la pantalla: el Bloque 2 inmediatamente se vuelve ROJO y el enlace se quiebra."*
* **Acción:** Haz clic en **🔍 1. Validar Cadena Completa**.
* **Lo que dices:**  
  > *"Al ejecutar el algoritmo de validación `is_valid()`, el sistema recalcula el hash del bloque 2. Como los datos cambiaron, el hash calculado ya no coincide con el almacenado. El sistema lanza la alerta de fraude y rechaza la cadena. Queda demostrado el principio de inmutabilidad."*

---

### PASO 4: Resolver con Consenso de Nakamoto (+5 Puntos Extra)
* **Acción:** Haz clic en **⭐ 3. Consenso: Cadena más Larga**.
* **Lo que dices:**  
  > *"Como mejora opcional, implementamos la regla de consenso de Nakamoto. Si este nodo fue hackeado o se quedó atrás, se comunica con la red. Simulamos que el Nodo B tiene una cadena válida más larga con 6 bloques. Al aplicar el consenso, nuestro nodo descarta la versión manipulada y sincroniza la cadena más larga y válida, volviendo a estar en VERDE."*

---

## 🎯 Respuestas a las Preguntas Trampa del Docente

* **P: "¿Por qué el hacker no puede simplemente recalcular el hash del bloque 2 para que no se note?"**
  * **R:** *"Porque para que ese nuevo hash sea aceptado por la red, tendría que volver a minarlo (gastar trabajo) y además tendría que volver a minar el bloque 3, el 4 y todos los siguientes antes de que el resto del mundo agregue otro bloque. Se necesitaría más del 51% del poder de cómputo de toda la red, lo que económicamente es casi imposible."*

* **P: "¿Por qué en tu caso de estudio en el Beni eligieron Blockchain de Consorcio y no una pública como Bitcoin?"**
  * **R:** *"Porque en la trazabilidad de ganado y tierras entre FEGABENI, SENASAG y frigoríficos se manejan datos comerciales privados y se necesita alta velocidad sin pagar comisiones en criptomonedas. Una red de consorcio permite que solo las entidades autorizadas validen los registros."*

* **P: "¿Cuál es la diferencia entre el Bloque Génesis y los demás?"**
  * **R:** *"El Bloque Génesis es el único que está 'hardcodeado' o creado por configuración inicial. Su `previous_hash` es '0' porque no existe ningún bloque previo en la historia del sistema."*


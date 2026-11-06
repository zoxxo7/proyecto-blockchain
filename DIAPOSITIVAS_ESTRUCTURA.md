# 📊 ESTRUCTURA DE DIAPOSITIVAS (POWERPOINT / CANVA)
### Trabajo Práctico: Tecnología Blockchain
**Asignatura:** Tecnologías Emergentes | **Docente:** Ing. Hermes Rodriguez Rivero  
**Tiempo total:** 10 minutos de presentación + 5 minutos de preguntas

---

### Diapositiva 1: Portada
* **Institución:** Universidad Autónoma del Beni "José Ballivián"
* **Facultad:** Facultad de Ingeniería y Tecnología
* **Carrera:** Ingeniería de Sistemas (Licenciatura - Trinidad)
* **Título:** TECNOLOGÍA BLOCKCHAIN: Fundamentos, Demostración Práctica y Casos de Uso
* **Asignatura:** Tecnologías Emergentes (CIS-ACO-o15310)
* **Docente:** Ing. Hermes Rodriguez Rivero
* **Estudiantes:**
  * Zafnat Josue Mamani Limachi
  * Jose Carlos Caity Roca
* **Lugar y Fecha:** Trinidad – Beni – Bolivia | 2/2026

---

### Diapositiva 2: ¿Qué es una Blockchain? (Fundamentos)
* **Concepto:** Libro contable digital distribuido, inmutable y descentralizado.
* **Componentes clave:**
  * **Bloque:** Unidad que almacena transacciones y metadatos.
  * **Hash (SHA-256):** Huella digital matemática única de 64 caracteres.
  * **Previous Hash:** El eslabón criptográfico que une cada bloque con el anterior.
  * **Inmutabilidad:** Alterar el pasado rompe matemáticamente toda la cadena.

---

### Diapositiva 3: Criptografía y Proof of Work (PoW)
* **Función Hash Criptográfica:**
  * Determinista, resistente a colisiones y con **efecto avalancha**.
* **Proof of Work (Prueba de Trabajo):**
  * Mecanismo para evitar el spam y la falsificación mediante costo computacional.
  * **El Nonce:** Contador que se incrementa hasta hallar un hash que inicie con cierta dificultad (ej. `000...`).
  * **PoW vs. PoS:** Gasto energético/cómputo frente a retención de capital económico.

---

### Diapositiva 4: Tipologías de Blockchain y Smart Contracts
* **Cuadro Rápido:**
  * *Pública:* Abierta y descentralizada (Bitcoin, Ethereum).
  * *Privada:* Cerrada y controlada por una sola empresa.
  * *De Consorcio:* Federada entre entidades con intereses comunes (Bancos, Cadenas logísticas).
* **Contratos Inteligentes (Smart Contracts):**
  * Programas autónomos e inmutables que se ejecutan solos: *"SI ocurre X, ENTONCES transferir Y"*.

---

### Diapositiva 5: Demostración Práctica (Mini Blockchain en Python)
* **Arquitectura del Código:**
  * `block.py` ➔ Estructura de bloque con SHA-256 y Nonce.
  * `mining.py` ➔ Algoritmo de minería Proof of Work.
  * `blockchain.py` ➔ Gestión de cadena, bloque génesis y validación `is_valid()`.
  * `gui.py` ➔ Simulador visual interactivo.
* *(Aquí se minimiza la presentación y se pasa a la pantalla del simulador `py gui.py` por 3 minutos).*

---

### Diapositiva 6: Caso de Estudio Internacional (IBM Food Trust)
* **El Problema Global:** Rastrear alimentos contaminados tomaba de 6 a 8 días en sistemas tradicionales.
* **Solución Blockchain:** Red de consorcio (Hyperledger Fabric) entre Walmart, Nestlé y Carrefour.
* **Resultado:** Reducción del tiempo de trazabilidad de 6 días a **2.2 segundos**.
* **Análisis Crítico:** ¿Era necesaria Blockchain? 
  * Técnicamente una base de datos centralizada era más rápida, pero las empresas competidoras **desconfían unas de otras**; blockchain ofreció gobernanza neutral.

---

### Diapositiva 7: Propuesta Local para el Beni — *BeniTrace*
* **Problemática en el Beni:**
  * 1. Abigeato (robo de ganado) y falsificación de guías SENASAG.
  * 2. Nuevas exigencias europeas (EUDR) que exigen certificar carne libre de deforestación.
* **Propuesta *BeniTrace*:**
  * Red de consorcio: FEGABENI + SENASAG + Frigoríficos + Aduanas.
  * Arete RFID al nacer ➔ Registro inmutable de vacunación y traslado ➔ Código QR en la carne de exportación.
  * **Impacto:** Cero ganado robado faenado y acceso a mercados internacionales premium.

---

### Diapositiva 8: Conclusiones
* Blockchain no es solo criptomonedas: es una tecnología de **auditoría, confianza e inmutabilidad**.
* No reemplaza a las bases de datos relacionales en velocidad, sino en escenarios de **desconfianza entre partes**.
* La combinación de SHA-256, Proof of Work y Consenso de la Cadena más Larga garantiza matemáticamente que el fraude sea económicamente inviable.

---

### Diapositiva 9: Espacio para Preguntas
* *¡Muchas gracias por su atención!*
* **Preguntas y Comentarios del Docente y Compañeros.**


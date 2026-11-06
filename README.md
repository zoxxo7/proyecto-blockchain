# 🔗 Mini Blockchain en Python
### Trabajo Práctico — Tecnologías Emergentes | Universidad del Beni — 2026

---

## 👥 Integrantes del Grupo

| Nombre completo | Rol en el TP |
|---|---|
| [Nombre 1] | Programación (Parte II) |
| [Nombre 2] | Marco Teórico (Parte I) |
| [Nombre 3] | Caso de Estudio (Parte III) |
| [Nombre 4] | Presentación y diapositivas (Parte IV) |

---

## 📋 Descripción del Proyecto

Implementación de una **mini blockchain educativa** desde cero en Python, sin ninguna librería externa.  
El sistema demuestra los conceptos fundamentales de la tecnología blockchain:

- ✅ Estructura de bloques con hash SHA-256
- ✅ Minería con Proof of Work (PoW)
- ✅ Validación de integridad de la cadena
- ✅ Detección de manipulación (ataque simulado)
- ⭐ Consenso de Nakamoto entre dos nodos (punto extra)

---

## 🗂️ Estructura de Archivos

```
proyecto de blockchange/
│
├── block.py          → Clase Block: estructura de cada bloque con SHA-256
├── blockchain.py     → Clase Blockchain: cadena, validación y consenso
├── mining.py         → Algoritmo Proof of Work (minería)
├── main.py           → Script principal: demo completa de las 4 partes
├── README.md         → Este archivo
└── screenshots/      → Capturas de pantalla de la ejecución
```

---

## ⚙️ Requisitos

| Requisito | Versión mínima |
|---|---|
| Python | 3.8 o superior |
| Librerías externas | **Ninguna** (solo librerías estándar de Python) |

Librerías estándar utilizadas (ya vienen con Python):
- `hashlib` — cálculo de hash SHA-256
- `datetime` — timestamp de cada bloque
- `json` — serialización de datos
- `time` — pausas visuales en la demo

---

## ▶️ Cómo Ejecutar

### 1. Verificar que tenés Python instalado
```bash
py --version
```
Deberías ver algo como: `Python 3.12.8`

### 2. Ir a la carpeta del proyecto
```bash
cd "e:\2026\UNI 2026\7MO\TECNOLOGIAS EMERGENTES\proyecto de blockchange"
```

### 3. Ejecutar el programa
```bash
py main.py
```

> ⏱️ **Nota:** La ejecución tarda entre 15 y 30 segundos porque la minería de cada bloque con dificultad 4 requiere miles de intentos. ¡Eso es intencional! Así funciona la minería real.

---

## 🧩 Descripción de Cada Archivo

### `block.py` — Clase Block
Define la estructura de un bloque individual:
- `index`: número de orden en la cadena
- `timestamp`: fecha y hora de creación
- `data`: transacción o dato almacenado
- `previous_hash`: enlace al bloque anterior
- `nonce`: contador para la minería
- `hash`: huella digital SHA-256 del bloque

### `mining.py` — Proof of Work
Implementa el algoritmo de minería:
- Incrementa el `nonce` hasta que el hash empiece con `"0000"`
- Muestra en pantalla cuántos intentos tomó

### `blockchain.py` — Clase Blockchain
Gestiona la cadena completa:
- Crea el **Bloque Génesis** automáticamente
- Mina y agrega nuevos bloques con `add_block()`
- Valida toda la cadena con `is_valid()`
- Resuelve conflictos entre nodos con `resolve_conflict()` ⭐

### `main.py` — Demo Principal
Ejecuta las 4 partes del trabajo práctico en orden:

| Parte | Descripción |
|---|---|
| **Parte 1** 🏗️ | Construye la cadena con 5 transacciones |
| **Parte 2** 🔍 | Valida la cadena — resultado: ✅ VÁLIDA |
| **Parte 3** 🔴 | Simula un hackeo y lo detecta — resultado: ❌ DETECTADO |
| **Parte 4** ⭐ | Consenso de Nakamoto entre Nodo A y Nodo B |

---

## 🔬 Conceptos Demostrados

### 1. SHA-256 y Efecto Avalancha
Cambiar **un solo carácter** en los datos de un bloque produce un hash completamente diferente:
```
Datos originales:  "Carlos → Diana: 25 Bs"   → Hash: 00006e2f8075dd9b...
Datos falsificados: "Carlos → Diana: 9999 Bs" → Hash: 58d471b724cc9bc5...
```

### 2. Proof of Work
El minero debe encontrar un `nonce` tal que el hash empiece con `"0000"`:
```
Bloque #1 → minado en 178,604 intentos → Hash: 00005196c3f82b0c...
Bloque #2 → minado en  40,215 intentos → Hash: 00006e2f8075dd9b...
```

### 3. Inmutabilidad de la Cadena
Al modificar un bloque, el hash almacenado **ya no coincide** con el hash recalculado → el sistema detecta la trampa inmediatamente.

### 4. Consenso de Nakamoto ⭐
Ante dos versiones de la cadena, todos los nodos adoptan la **más larga y válida**:
```
Nodo A: 3 bloques  ███
Nodo B: 6 bloques  ██████
→ Nodo A adopta la cadena de Nodo B ✅
```

---

## 📸 Capturas de Pantalla

Ver carpeta `screenshots/` con las siguientes capturas:
1. `01_construccion.png` — Minería de los 5 bloques
2. `02_validacion.png` — Cadena válida ✅
3. `03_ataque.png` — Hackeo detectado ❌
4. `04_consenso.png` — Nodo A adopta cadena de Nodo B ⭐

---

## 📚 Referencias Bibliográficas

1. Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://bitcoin.org/bitcoin.pdf
2. Antonopoulos, A. M. (2017). *Mastering Bitcoin: Programming the Open Blockchain* (2nd ed.). O'Reilly Media.
3. Buterin, V. (2014). *Ethereum White Paper: A Next-Generation Smart Contract and Decentralized Application Platform*. https://ethereum.org/en/whitepaper/
4. National Institute of Standards and Technology. (2015). *FIPS PUB 180-4: Secure Hash Standard (SHS)*. U.S. Department of Commerce.

---

## 🏆 Puntuación Objetivo

| Componente | Puntos |
|---|---|
| Parte I — Investigación Teórica | 20 pts |
| **Parte II — Implementación (este código)** | **40 pts** |
| **⭐ Consenso de Nakamoto (extra)** | **+5 pts** |
| Parte III — Caso de Estudio | 25 pts |
| Parte IV — Exposición | 15 pts |
| **TOTAL** | **105 pts** |


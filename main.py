"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          TRABAJO PRÁCTICO — TECNOLOGÍAS EMERGENTES                          ║
║          Mini Blockchain en Python — Implementación Completa                ║
║                                                                              ║
║  Autores  : Zafnat Josue Mamani Limachi & Jose Carlos Caity Roca            ║
║  Carrera  : Ingeniería de Sistemas (UAB - Trinidad, Beni)                   ║
║  Materia  : Tecnologías Emergentes (Docente: Ing. Hermes Rodriguez)          ║
║  Gestión  : 2/2026                                                           ║
║                                                                              ║
║  DESCRIPCIÓN:                                                                ║
║  Este script demuestra el funcionamiento completo de una blockchain          ║
║  educativa implementada desde cero en Python, sin librerías externas.        ║
║  Cubre: construcción de bloques, minería (Proof of Work), validación         ║
║  de integridad, simulación de un ataque (hackeo) y consenso entre nodos.    ║
║                                                                              ║
║  EJECUCIÓN:                                                                  ║
║      python main.py                                                          ║
║                                                                              ║
║  REQUISITOS:                                                                 ║
║      Python 3.8+  (sin librerías externas adicionales)                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import time
from blockchain import Blockchain


# ══════════════════════════════════════════════════════════════════════════════
#  UTILIDADES DE PRESENTACIÓN
# ══════════════════════════════════════════════════════════════════════════════

def encabezado(titulo: str, simbolo: str = "═"):
    """Imprime un encabezado visual decorado para separar secciones."""
    linea = simbolo * 70
    print(f"\n{linea}")
    print(f"  {titulo}")
    print(f"{linea}\n")


def pausa(segundos: float = 0.6):
    """Pequeña pausa para que la lectura de la terminal sea más cómoda."""
    time.sleep(segundos)


# ══════════════════════════════════════════════════════════════════════════════
#  PARTE 1 — CONSTRUCCIÓN DE LA BLOCKCHAIN
# ══════════════════════════════════════════════════════════════════════════════

def parte1_construccion():
    """
    PARTE 1: Construcción de la Blockchain (RF-01, RF-02, RF-03)
    ─────────────────────────────────────────────────────────────
    Se crea una blockchain nueva y se le agregan 5 bloques con
    transacciones simuladas entre personas. Cada bloque es minado
    con Proof of Work (dificultad=4, el hash debe empezar con '0000').

    Returns:
        Blockchain: La cadena construida con 6 bloques (génesis + 5).
    """
    encabezado("🏗️  PARTE 1 — CONSTRUCCIÓN DE LA BLOCKCHAIN")

    print("  ► Creando la blockchain con dificultad de minería = 4...")
    print("    (El hash de cada bloque debe comenzar con '0000')\n")
    pausa()

    # ── Crear la blockchain (esto genera el Bloque Génesis automáticamente) ──
    bc = Blockchain(difficulty=4)

    print("  ► Bloque Génesis creado automáticamente ✅")
    print("    Es el primer bloque de toda la cadena.")
    print("    Su 'previous_hash' es '0' porque no tiene bloque anterior.\n")
    pausa()

    # ── Lista de transacciones a agregar ──
    transacciones = [
        {
            "id":          "TX-001",
            "descripcion": "Alice → Bob: 100 Bs",
            "remitente":   "Alice",
            "receptor":    "Bob",
            "monto":       100,
            "moneda":      "Bs"
        },
        {
            "id":          "TX-002",
            "descripcion": "Bob → Carlos: 50 Bs",
            "remitente":   "Bob",
            "receptor":    "Carlos",
            "monto":       50,
            "moneda":      "Bs"
        },
        {
            "id":          "TX-003",
            "descripcion": "Carlos → Diana: 25 Bs",
            "remitente":   "Carlos",
            "receptor":    "Diana",
            "monto":       25,
            "moneda":      "Bs"
        },
        {
            "id":          "TX-004",
            "descripcion": "Diana → Eduardo: 75 Bs",
            "remitente":   "Diana",
            "receptor":    "Eduardo",
            "monto":       75,
            "moneda":      "Bs"
        },
        {
            "id":          "TX-005",
            "descripcion": "Eduardo → Alice: 30 Bs",
            "remitente":   "Eduardo",
            "receptor":    "Alice",
            "monto":       30,
            "moneda":      "Bs"
        },
    ]

    # ── Agregar cada transacción como un bloque minado ──
    print(f"  ► Agregando {len(transacciones)} transacciones a la cadena...\n")
    for tx in transacciones:
        print(f"  💸 Procesando transacción: {tx['descripcion']}")
        bc.add_block(tx)
        pausa(0.3)

    print("\n  ✅ ¡Blockchain construida exitosamente!")
    print(f"     Total de bloques en la cadena: {len(bc.chain)}")
    print(f"     (1 Génesis + {len(transacciones)} transacciones)\n")
    pausa()

    # ── Mostrar todos los bloques ──
    print("  ► Visualizando la cadena completa:")
    bc.print_chain()

    return bc


# ══════════════════════════════════════════════════════════════════════════════
#  PARTE 2 — VALIDACIÓN DE LA CADENA ÍNTEGRA
# ══════════════════════════════════════════════════════════════════════════════

def parte2_validacion(bc: Blockchain):
    """
    PARTE 2: Validación de la Cadena (RF-04)
    ─────────────────────────────────────────
    Se verifica que todos los bloques sean válidos:
      • Que el hash almacenado coincida con el hash recalculado.
      • Que el 'previous_hash' de cada bloque coincida con el hash
        real del bloque anterior.

    Args:
        bc (Blockchain): La blockchain a validar.
    """
    encabezado("🔍 PARTE 2 — VALIDACIÓN DE LA CADENA ÍNTEGRA")

    print("  ► Iniciando validación completa de la cadena...")
    print("    Se verificará bloque a bloque la integridad de los datos.\n")
    pausa()

    print("  ► ¿Qué verifica el algoritmo?")
    print("    1. Para cada bloque: recalcula su hash y lo compara con el almacenado.")
    print("       Si son distintos → el bloque fue MODIFICADO.")
    print("    2. Compara el 'previous_hash' con el hash real del bloque anterior.")
    print("       Si son distintos → la CADENA fue ALTERADA en ese punto.\n")
    pausa()

    resultado = bc.is_valid()

    if resultado:
        print("\n  🎉 RESULTADO: La cadena es COMPLETAMENTE VÁLIDA.")
        print("     Ningún bloque ha sido manipulado.")
        print("     La blockchain está íntegra y confiable.\n")
    else:
        print("\n  🚨 RESULTADO: La cadena está COMPROMETIDA.\n")

    pausa()


# ══════════════════════════════════════════════════════════════════════════════
#  PARTE 3 — SIMULACIÓN DE ATAQUE (HACKEO)
# ══════════════════════════════════════════════════════════════════════════════

def parte3_ataque(bc: Blockchain):
    """
    PARTE 3: Simulación de Ataque — Hackeo y Detección (RF-05)
    ────────────────────────────────────────────────────────────
    Se simula que un atacante modifica los datos del Bloque #2
    directamente en memoria (sin recalcular el hash).

    Luego se ejecuta la validación para demostrar que el sistema
    DETECTA automáticamente la manipulación y rechaza la cadena.

    Concepto clave:
        Al cambiar los datos del bloque, el hash almacenado ya no
        coincide con el hash recalculado → DETECCIÓN INMEDIATA.

    Args:
        bc (Blockchain): La blockchain (será manipulada en este paso).
    """
    encabezado("🔴 PARTE 3 — SIMULACIÓN DE ATAQUE (HACKEO)")

    print("  ► ESCENARIO:")
    print("    Un atacante quiere modificar una transacción en la blockchain")
    print("    para cambiar el monto enviado y quedarse con más dinero.")
    print("    Accede directamente al Bloque #2 y altera sus datos.\n")
    pausa()

    # ── Mostrar el estado ANTES del ataque ──
    bloque_objetivo = bc.chain[2]
    print("  ► ESTADO ANTES DEL ATAQUE:")
    print(f"    Bloque #2 — Datos originales : {bloque_objetivo.data['descripcion']}")
    print(f"    Bloque #2 — Monto original   : {bloque_objetivo.data['monto']} Bs")
    print(f"    Bloque #2 — Hash almacenado  : {bloque_objetivo.hash[:35]}...")
    pausa()

    # ── EJECUTAR EL ATAQUE ──
    print("\n  🔴 EJECUTANDO EL ATAQUE...")
    print("    El atacante modifica directamente los datos del Bloque #2:")
    print("    Cambia el monto de 25 Bs → 9,999 Bs\n")
    pausa(0.8)

    # Modificación maliciosa — NO recalculamos el hash (eso es el truco)
    bc.chain[2].data = {
        "id":          "TX-003-HACKEADA",
        "descripcion": "Carlos → Diana: 9999 Bs  ← DATO FALSIFICADO",
        "remitente":   "Carlos",
        "receptor":    "Diana",
        "monto":       9999,          # ← Monto falsificado (era 25)
        "moneda":      "Bs"
    }

    # ── Mostrar el estado DESPUÉS del ataque ──
    print("  ► ESTADO DESPUÉS DEL ATAQUE:")
    print(f"    Bloque #2 — Datos ALTERADOS  : {bc.chain[2].data['descripcion']}")
    print(f"    Bloque #2 — Monto FALSIFICADO: {bc.chain[2].data['monto']} Bs")
    print(f"    Bloque #2 — Hash almacenado  : {bc.chain[2].hash[:35]}...")
    print(f"    Bloque #2 — Hash real ahora  : {bc.chain[2].calculate_hash()[:35]}...")
    print("\n    ⚠️  NOTA: El atacante NO puede actualizar el hash almacenado")
    print("    porque tendría que re-minar TODOS los bloques siguientes,")
    print("    lo que requeriría más poder computacional que toda la red.\n")
    pausa()

    # ── Ejecutar la validación para detectar el ataque ──
    print("  ► Ejecutando validación de la cadena para detectar el ataque...\n")
    pausa(0.5)

    resultado = bc.is_valid()

    if not resultado:
        print("\n  🛡️  RESULTADO: ¡ATAQUE DETECTADO EXITOSAMENTE!")
        print("     El sistema identificó que el Bloque #2 fue MANIPULADO.")
        print("     La blockchain RECHAZA esta cadena como inválida.")
        print("     En una red real, este nodo sería descartado por los demás.\n")
    else:
        print("\n  ⚠️  El ataque pasó desapercibido (esto no debería ocurrir).\n")

    pausa()


# ══════════════════════════════════════════════════════════════════════════════
#  PARTE 4 — ⭐ EXTRA: CONSENSO DE NAKAMOTO (2 NODOS)
# ══════════════════════════════════════════════════════════════════════════════

def parte4_consenso():
    """
    PARTE 4 ⭐ EXTRA (+5 pts): Consenso de Nakamoto — Regla de la Cadena más Larga
    ─────────────────────────────────────────────────────────────────────────────────
    Se simulan DOS nodos independientes (Nodo A y Nodo B) con distintas
    versiones de la blockchain. Nodo B tiene más bloques (cadena más larga).

    Se aplica el 'Consenso de Nakamoto': ante una discrepancia, el nodo
    con la cadena más CORTA adopta la cadena más LARGA y válida.

    Este es el mecanismo real que usa Bitcoin para resolver conflictos
    cuando dos mineros encuentran bloques válidos al mismo tiempo (fork).
    """
    encabezado("⭐ PARTE 4 — EXTRA: CONSENSO DE NAKAMOTO (2 NODOS)")

    print("  ► CONCEPTO: Consenso de Nakamoto")
    print("    En una red blockchain real, distintos nodos pueden tener")
    print("    versiones distintas de la cadena (por ejemplo, si dos mineros")
    print("    encuentran bloques válidos casi al mismo tiempo — 'fork').")
    print("    La solución: todos los nodos adoptan la cadena MÁS LARGA válida.")
    print("    La cadena más larga representa más trabajo computacional.\n")
    pausa()

    # ── Crear NODO A: cadena corta (2 bloques de transacciones) ──
    print("  ► Creando NODO A (cadena corta)...")
    nodo_a = Blockchain(difficulty=3)   # Dificultad 3 para ser más rápido en la demo

    nodo_a.add_block({
        "id":          "TX-A01",
        "descripcion": "Pedro → María: 200 Bs",
        "monto":       200
    })
    nodo_a.add_block({
        "id":          "TX-A02",
        "descripcion": "María → José: 80 Bs",
        "monto":       80
    })

    print(f"  ✅ NODO A construido — {len(nodo_a.chain)} bloques en total\n")
    pausa(0.4)

    # ── Crear NODO B: cadena larga (5 bloques de transacciones) ──
    print("  ► Creando NODO B (cadena larga — más trabajo acumulado)...")
    nodo_b = Blockchain(difficulty=3)

    nodo_b.add_block({
        "id":          "TX-B01",
        "descripcion": "Lucía → Marcos: 500 Bs",
        "monto":       500
    })
    nodo_b.add_block({
        "id":          "TX-B02",
        "descripcion": "Marcos → Sofía: 150 Bs",
        "monto":       150
    })
    nodo_b.add_block({
        "id":          "TX-B03",
        "descripcion": "Sofía → Andrés: 300 Bs",
        "monto":       300
    })
    nodo_b.add_block({
        "id":          "TX-B04",
        "descripcion": "Andrés → Valentina: 90 Bs",
        "monto":       90
    })
    nodo_b.add_block({
        "id":          "TX-B05",
        "descripcion": "Valentina → Lucía: 420 Bs",
        "monto":       420
    })

    print(f"  ✅ NODO B construido — {len(nodo_b.chain)} bloques en total\n")
    pausa(0.4)

    # ── Mostrar el estado antes del consenso ──
    print(f"  {'─'*60}")
    print(f"  ESTADO ANTES DEL CONSENSO:")
    print(f"  {'─'*60}")
    print(f"    NODO A: {len(nodo_a.chain)} bloques  {'█' * len(nodo_a.chain)}")
    print(f"    NODO B: {len(nodo_b.chain)} bloques  {'█' * len(nodo_b.chain)}")
    print(f"\n    Nodo B tiene más trabajo acumulado (cadena más larga).")
    print(f"    Por el Consenso de Nakamoto, Nodo A debe adoptar la cadena de Nodo B.\n")
    pausa()

    # ── Aplicar el consenso ──
    print("  ► Nodo A ejecuta 'resolve_conflict' con la cadena de Nodo B...")
    pausa(0.5)

    adoptado = nodo_a.resolve_conflict(nodo_b)

    # ── Mostrar el estado después del consenso ──
    print(f"  {'─'*60}")
    print(f"  ESTADO DESPUÉS DEL CONSENSO:")
    print(f"  {'─'*60}")
    print(f"    NODO A: {len(nodo_a.chain)} bloques  {'█' * len(nodo_a.chain)}")
    print(f"    NODO B: {len(nodo_b.chain)} bloques  {'█' * len(nodo_b.chain)}")

    if adoptado:
        print(f"\n  🎉 Nodo A adoptó exitosamente la cadena de Nodo B.")
        print(f"     Ambos nodos ahora tienen {len(nodo_a.chain)} bloques — ¡la red está sincronizada!")
    else:
        print(f"\n  ✅ Nodo A ya tenía la cadena más larga — no hubo cambio.")

    pausa()

    # ── Validar que la cadena adoptada es válida ──
    print("\n  ► Verificando que la cadena adoptada por Nodo A es válida...")
    nodo_a.is_valid()
    pausa()

    # ── Mostrar la cadena final del Nodo A ──
    print("  ► Cadena final de NODO A (después del consenso):")
    nodo_a.print_chain()


# ══════════════════════════════════════════════════════════════════════════════
#  RESUMEN FINAL
# ══════════════════════════════════════════════════════════════════════════════

def resumen_final():
    """
    Muestra un resumen de todo lo demostrado en el trabajo práctico.
    """
    encabezado("📊 RESUMEN FINAL — LO QUE DEMOSTRAMOS HOY")

    resumen = [
        ("RF-01", "Clase Block",        "Cada bloque almacena datos + hash SHA-256 propio + hash anterior."),
        ("RF-02", "Clase Blockchain",   "La cadena se inicia con el Bloque Génesis y crece con add_block()."),
        ("RF-03", "Proof of Work",      "Cada bloque es MINADO: se busca un hash que empiece con '0000'."),
        ("RF-04", "Validación",         "is_valid() recorre toda la cadena y detecta cualquier alteración."),
        ("RF-05", "Simulación ataque",  "Al modificar datos de un bloque, is_valid() detecta la trampa."),
        ("RF-06", "Consenso (EXTRA)",   "resolve_conflict() adopta la cadena más larga entre dos nodos."),
    ]

    print(f"  {'REQUISITO':<8}  {'COMPONENTE':<20}  {'QUÉ SE DEMOSTRÓ'}")
    print(f"  {'─'*8}  {'─'*20}  {'─'*40}")
    for req, comp, desc in resumen:
        print(f"  {req:<8}  {comp:<20}  {desc}")

    print(f"\n  {'═'*70}")
    print(f"  🏆 PUNTUACIÓN OBJETIVO:")
    print(f"     Parte II base  → 40 puntos")
    print(f"     Consenso extra → +5 puntos")
    print(f"     TOTAL          → 45 puntos de la Parte II")
    print(f"  {'═'*70}\n")

    print("  ► CONCEPTOS CLAVE DEMOSTRADOS:")
    print("    • SHA-256:    Cambiar 1 carácter en los datos cambia el hash por completo.")
    print("    • PoW:        Encontrar un hash válido requiere muchos intentos (costoso).")
    print("    • Inmutabilidad: Cambiar un bloque ROMPE todos los bloques siguientes.")
    print("    • Consenso:   La red siempre adopta la cadena con más trabajo acumulado.\n")


# ══════════════════════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Encabezado de bienvenida ──
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*15 + "🔗 MINI BLOCKCHAIN EN PYTHON 🔗" + " "*21 + "║")
    print("║" + " "*10 + "Trabajo Práctico — Tecnologías Emergentes" + " "*17 + "║")
    print("║" + " "*20 + "Universidad del Beni — 2026" + " "*21 + "║")
    print("╚" + "═"*68 + "╝")

    print("\n  Este programa demuestra el funcionamiento de una blockchain")
    print("  implementada desde cero en Python, usando SHA-256 y Proof of Work.\n")
    pausa(1.0)

    # ══════════════════════════════════════════════
    #  PARTE 1: Construir la blockchain
    # ══════════════════════════════════════════════
    blockchain_principal = parte1_construccion()

    # ══════════════════════════════════════════════
    #  PARTE 2: Validar la cadena íntegra
    # ══════════════════════════════════════════════
    parte2_validacion(blockchain_principal)

    # ══════════════════════════════════════════════
    #  PARTE 3: Simular un ataque y detectarlo
    # ══════════════════════════════════════════════
    parte3_ataque(blockchain_principal)

    # ══════════════════════════════════════════════
    #  PARTE 4: Consenso de Nakamoto (EXTRA +5 pts)
    # ══════════════════════════════════════════════
    parte4_consenso()

    # ══════════════════════════════════════════════
    #  RESUMEN FINAL
    # ══════════════════════════════════════════════
    resumen_final()

    print("  ✅ Programa finalizado. ¡Gracias por correr la demo!")
    print("     Para volver a ejecutar: python main.py\n")


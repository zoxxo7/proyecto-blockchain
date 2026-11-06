"""
mining.py — Proof of Work (Minería)
=====================================
Implementa el algoritmo de Prueba de Trabajo (PoW).
El minero debe encontrar un nonce tal que el hash del bloque
comience con una cantidad determinada de ceros ('0' * difficulty).
Esto requiere muchos intentos y hace costoso falsificar la cadena.
"""

from block import Block


def mine_block(block: Block, difficulty: int) -> Block:
    """
    Mina un bloque aplicando el algoritmo Proof of Work.

    El algoritmo incrementa el 'nonce' del bloque y recalcula su hash
    en cada intento, hasta que el hash resultante comience con el número
    de ceros definido por 'difficulty'. Esto simula la minería real
    de Bitcoin y otras criptomonedas.

    Args:
        block (Block):      El bloque a minar (se modifica en el lugar).
        difficulty (int):   Número de ceros con que debe comenzar el hash.
                            Mayor dificultad = más tiempo de minería.

    Returns:
        Block: El mismo bloque, ahora con nonce y hash válidos.

    Ejemplo:
        difficulty=4 → el hash debe empezar con "0000"
        difficulty=2 → el hash debe empezar con "00"
    """
    # El prefijo objetivo: tantos ceros como indique 'difficulty'
    target   = "0" * difficulty
    intentos = 0

    print(f"  ⛏️  Minando bloque #{block.index} (dificultad={difficulty})...")

    # Bucle de minería: incrementar nonce hasta encontrar hash válido
    while not block.hash.startswith(target):
        block.nonce += 1
        block.hash   = block.calculate_hash()
        intentos     += 1

    # Hash válido encontrado
    print(f"  ✅ Bloque #{block.index} minado en {intentos:,} intentos")
    print(f"     Hash: {block.hash}\n")

    return block


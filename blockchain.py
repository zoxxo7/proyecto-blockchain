"""
blockchain.py — Clase Blockchain (Cadena de Bloques)
======================================================
Gestiona la cadena completa de bloques: creación, minería,
validación de integridad y resolución de conflictos entre nodos.
"""

from block import Block
from mining import mine_block


class Blockchain:
    """
    Representa la cadena de bloques completa.

    La cadena siempre comienza con el Bloque Génesis (índice 0),
    creado automáticamente al instanciar la clase. Cada bloque
    nuevo es minado antes de agregarse, y la validación verifica
    que ningún bloque haya sido manipulado.

    Atributos:
        chain (list):       Lista de bloques que forman la cadena.
        difficulty (int):   Dificultad de minería (ceros en el hash).
    """

    def __init__(self, difficulty: int = 4):
        """
        Inicializa la blockchain creando el Bloque Génesis.

        Args:
            difficulty (int): Número de ceros que debe tener el hash
                              al inicio. Por defecto es 4.
        """
        self.difficulty = difficulty
        # Crear el primer bloque automáticamente al iniciar
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        """
        Crea el Bloque Génesis: el primer bloque de la cadena.

        El Bloque Génesis es especial:
        - Su índice es 0.
        - Su 'previous_hash' es "0" (no tiene bloque anterior).
        - Se mina con dificultad 1 para ser rápido.

        Returns:
            Block: El bloque génesis ya minado.
        """
        genesis = Block(
            index=0,
            data="🌐 Bloque Génesis — Inicio de la Cadena",
            previous_hash="0"
        )
        # Minamos con dificultad baja para que sea instantáneo
        mine_block(genesis, difficulty=1)
        return genesis

    def get_last_block(self) -> Block:
        """
        Retorna el último bloque de la cadena.

        Returns:
            Block: El bloque más reciente.
        """
        return self.chain[-1]

    def add_block(self, data) -> Block:
        """
        Crea, mina y agrega un nuevo bloque a la cadena.

        El nuevo bloque enlaza con el último bloque existente
        a través de su campo 'previous_hash'.

        Args:
            data (any): Los datos o transacción a almacenar.

        Returns:
            Block: El bloque recién agregado y minado.
        """
        last   = self.get_last_block()
        nuevo  = Block(
            index         = last.index + 1,
            data          = data,
            previous_hash = last.hash
        )
        # Minar el bloque antes de agregarlo
        mine_block(nuevo, self.difficulty)
        self.chain.append(nuevo)
        return nuevo

    def is_valid(self) -> bool:
        """
        Valida la integridad completa de la cadena.

        Recorre todos los bloques (excepto el génesis) y verifica:
          1. Que el hash almacenado coincida con el hash recalculado.
             (Detecta si los datos del bloque fueron modificados)
          2. Que el 'previous_hash' coincida con el hash real del
             bloque anterior. (Detecta si el orden fue alterado)

        Returns:
            bool: True si la cadena es válida, False si fue manipulada.
        """
        for i in range(1, len(self.chain)):
            bloque_actual   = self.chain[i]
            bloque_anterior = self.chain[i - 1]

            # ── Verificación 1: integridad del hash del bloque actual ──
            if bloque_actual.hash != bloque_actual.calculate_hash():
                print(
                    f"  ❌ ALERTA: Hash inválido en Bloque #{bloque_actual.index}\n"
                    f"     Hash almacenado : {bloque_actual.hash[:30]}...\n"
                    f"     Hash recalculado: {bloque_actual.calculate_hash()[:30]}...\n"
                    f"     → Los datos de este bloque fueron MODIFICADOS."
                )
                return False

            # ── Verificación 2: enlace con el bloque anterior ──
            if bloque_actual.previous_hash != bloque_anterior.hash:
                print(
                    f"  ❌ ALERTA: Enlace roto entre Bloque #{i-1} y Bloque #{i}\n"
                    f"     previous_hash almacenado: {bloque_actual.previous_hash[:30]}...\n"
                    f"     Hash real del anterior  : {bloque_anterior.hash[:30]}...\n"
                    f"     → La cadena fue ALTERADA en este punto."
                )
                return False

        # Si pasó todas las verificaciones, la cadena es válida
        print(f"  ✅ Cadena completamente válida ({len(self.chain)} bloques verificados).")
        return True

    def print_chain(self):
        """
        Imprime todos los bloques de la cadena de forma visual.
        """
        print(f"\n{'═'*60}")
        print(f"  🔗 CADENA DE BLOQUES ({len(self.chain)} bloques)")
        print(f"{'═'*60}")
        for bloque in self.chain:
            print(bloque)
        print(f"{'═'*60}\n")

    def resolve_conflict(self, other_blockchain: "Blockchain") -> bool:
        """
        ⭐ EXTRA (+5 pts): Consenso de Nakamoto — Regla de la cadena más larga.

        Si la cadena del otro nodo es más larga Y válida, adoptamos
        esa cadena (reemplazamos la nuestra). Esto simula cómo los
        nodos de Bitcoin resuelven conflictos entre versiones distintas
        de la blockchain.

        Args:
            other_blockchain (Blockchain): La blockchain del otro nodo.

        Returns:
            bool: True si adoptamos la cadena del otro nodo, False si no.
        """
        otra_cadena   = other_blockchain.chain
        nuestra_long  = len(self.chain)
        otra_long     = len(otra_cadena)

        print(f"\n{'─'*60}")
        print(f"  🔄 RESOLUCIÓN DE CONFLICTO (Consenso de Nakamoto)")
        print(f"     Nuestra cadena : {nuestra_long} bloques")
        print(f"     Otra cadena    : {otra_long} bloques")
        print(f"{'─'*60}")

        # Verificar si la otra cadena es más larga y válida
        if otra_long > nuestra_long and other_blockchain.is_valid():
            self.chain = otra_cadena
            print(f"  🔄 Nuestra cadena fue REEMPLAZADA por la cadena más larga del otro nodo.")
            print(f"     Nueva longitud: {len(self.chain)} bloques\n")
            return True
        else:
            print(f"  ✅ Nuestra cadena ya es la más larga o la otra no es válida.")
            print(f"     No se realizó ningún cambio.\n")
            return False


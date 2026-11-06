"""
test_blockchain.py — Pruebas Unitarias Automatizadas
====================================================
Verifica el correcto funcionamiento de cada componente de la blockchain:
  1. Integridad del Bloque y cálculo SHA-256
  2. Proof of Work (dificultad configurable)
  3. Creación del Bloque Génesis
  4. Enlaces de la cadena (previous_hash)
  5. Detección automática de manipulaciones (anti-fraude)
  6. Regla de consenso de Nakamoto (cadena más larga)

EJECUCIÓN:
    py test_blockchain.py
    o
    py -m unittest test_blockchain.py
"""

import unittest
from block import Block
from blockchain import Blockchain
from mining import mine_block


class TestBlockchain(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba: crea una blockchain limpia con dificultad baja."""
        self.bc = Blockchain(difficulty=2)

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 1: Estructura del Bloque y SHA-256 (RF-01)
    # ──────────────────────────────────────────────────────────────────────────
    def test_01_block_hash_integrity(self):
        """Verifica que el hash del bloque se calcule correctamente con SHA-256."""
        bloque = Block(index=1, data="Prueba Unitaria", previous_hash="000abc")
        hash_esperado = bloque.calculate_hash()
        
        self.assertEqual(bloque.hash, hash_esperado)
        self.assertEqual(len(bloque.hash), 64, "El hash SHA-256 debe tener 64 caracteres.")
        self.assertEqual(bloque.previous_hash, "000abc")
        self.assertEqual(bloque.index, 1)

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 2: Proof of Work (RF-03)
    # ──────────────────────────────────────────────────────────────────────────
    def test_02_proof_of_work(self):
        """Verifica que la minería genere un hash con los ceros iniciales requeridos."""
        dificultad = 3
        bloque = Block(index=1, data="Minando bloque", previous_hash="000")
        mine_block(bloque, difficulty=dificultad)

        prefijo_esperado = "0" * dificultad
        self.assertTrue(
            bloque.hash.startswith(prefijo_esperado),
            f"El hash debe comenzar con '{prefijo_esperado}'"
        )
        self.assertGreaterEqual(bloque.nonce, 0)

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 3: Bloque Génesis y Cadena Inicial (RF-02)
    # ──────────────────────────────────────────────────────────────────────────
    def test_03_genesis_block(self):
        """Verifica que la blockchain nazca con el Bloque Génesis (índice 0)."""
        genesis = self.bc.chain[0]
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.previous_hash, "0")
        self.assertEqual(len(self.bc.chain), 1)

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 4: Enlaces y Validación de Cadena Válida (RF-04)
    # ──────────────────────────────────────────────────────────────────────────
    def test_04_valid_chain(self):
        """Verifica que al agregar bloques la cadena permanezca 100% válida."""
        self.bc.add_block({"remitente": "Alice", "receptor": "Bob", "monto": 100})
        self.bc.add_block({"remitente": "Bob", "receptor": "Carlos", "monto": 50})
        
        self.assertEqual(len(self.bc.chain), 3) # Génesis + 2 bloques
        self.assertTrue(self.bc.is_valid(), "La cadena agregada legítimamente debe ser válida.")

        # Verificar que el previous_hash del bloque 2 sea el hash del bloque 1
        self.assertEqual(self.bc.chain[2].previous_hash, self.bc.chain[1].hash)

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 5: Detección de Fraude / Ataque Simulado (RF-05)
    # ──────────────────────────────────────────────────────────────────────────
    def test_05_tamper_detection(self):
        """Verifica que cualquier modificación no autorizada invalide la cadena."""
        self.bc.add_block("Transacción 1")
        self.bc.add_block("Transacción 2 (Original)")
        self.bc.add_block("Transacción 3")

        # Antes de hackear: es válida
        self.assertTrue(self.bc.is_valid())

        # ATAQUE: Modificar directamente los datos del Bloque 2 sin recalcular hash
        self.bc.chain[2].data = "Transacción 2 (HACKEADA / FALSIFICADA)"

        # Después de hackear: debe fallar la validación
        self.assertFalse(
            self.bc.is_valid(),
            "La validación DEBE retornar False cuando se alteran los datos de un bloque."
        )

    # ──────────────────────────────────────────────────────────────────────────
    #  PRUEBA 6: Consenso de Nakamoto / Cadena más Larga (RF-06 ⭐ Extra)
    # ──────────────────────────────────────────────────────────────────────────
    def test_06_nakamoto_consensus(self):
        """Verifica que ante dos nodos se adopte la cadena válida más larga."""
        nodo_a = Blockchain(difficulty=2)
        nodo_b = Blockchain(difficulty=2)

        # Nodo A tiene 2 bloques (Génesis + 1)
        nodo_a.add_block("TX Nodo A")

        # Nodo B tiene 4 bloques (Génesis + 3)
        nodo_b.add_block("TX Nodo B - 1")
        nodo_b.add_block("TX Nodo B - 2")
        nodo_b.add_block("TX Nodo B - 3")

        self.assertEqual(len(nodo_a.chain), 2)
        self.assertEqual(len(nodo_b.chain), 4)

        # Nodo A resuelve conflicto contra Nodo B
        adoptado = nodo_a.resolve_conflict(nodo_b)

        self.assertTrue(adoptado, "Nodo A debió adoptar la cadena de Nodo B.")
        self.assertEqual(len(nodo_a.chain), 4, "Nodo A ahora debe tener 4 bloques.")
        self.assertTrue(nodo_a.is_valid(), "La cadena adoptada debe ser válida.")


if __name__ == "__main__":
    print("\n" + "═"*70)
    print("  🧪 EJECUTANDO PRUEBAS UNITARIAS DE LA BLOCKCHAIN")
    print("═"*70)
    unittest.main(verbosity=2)

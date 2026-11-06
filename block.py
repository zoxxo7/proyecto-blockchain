"""
block.py — Clase Block (Bloque)
================================
Define la estructura de cada bloque en la cadena.
Cada bloque contiene sus datos y un hash SHA-256 calculado
a partir de todos sus campos, garantizando integridad.
"""

import hashlib
import datetime
import json


class Block:
    """
    Representa un bloque individual dentro de la blockchain.

    Atributos:
        index (int):          Número de orden del bloque en la cadena.
        timestamp (str):      Fecha y hora exacta de creación (ISO 8601).
        data (any):           Datos o transacciones almacenadas en el bloque.
        previous_hash (str):  Hash SHA-256 del bloque anterior (enlace de la cadena).
        nonce (int):          Contador usado en la minería (Proof of Work).
        hash (str):           Hash SHA-256 calculado con todos los campos.
    """

    def __init__(self, index: int, data, previous_hash: str):
        """
        Inicializa un nuevo bloque con sus datos básicos.

        Args:
            index (int):         Posición del bloque en la cadena.
            data (any):          Datos o transacciones a almacenar.
            previous_hash (str): Hash del bloque anterior.
        """
        self.index         = index
        self.timestamp     = datetime.datetime.now().isoformat()
        self.data          = data
        self.previous_hash = previous_hash
        self.nonce         = 0
        # El hash se calcula al final, cuando ya tenemos todos los campos
        self.hash          = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calcula el hash SHA-256 del bloque usando todos sus campos.

        La cadena que se hashea combina: index + timestamp + data +
        previous_hash + nonce. Cualquier cambio en uno de estos campos
        producirá un hash completamente distinto (efecto avalancha).

        Returns:
            str: Hash SHA-256 en formato hexadecimal (64 caracteres).
        """
        # Serializar todos los campos a una cadena de texto
        block_string = json.dumps({
            "index":         self.index,
            "timestamp":     self.timestamp,
            "data":          self.data,
            "previous_hash": self.previous_hash,
            "nonce":         self.nonce
        }, sort_keys=True)

        # Calcular y retornar el hash SHA-256
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        """
        Representación legible del bloque para impresión en pantalla.

        Returns:
            str: Descripción formateada del bloque con todos sus campos.
        """
        return (
            f"\n  📦 BLOQUE #{self.index}\n"
            f"  ├─ Timestamp    : {self.timestamp}\n"
            f"  ├─ Datos        : {self.data}\n"
            f"  ├─ Nonce        : {self.nonce}\n"
            f"  ├─ Hash Anterior: {self.previous_hash[:20]}...\n"
            f"  └─ Hash Propio  : {self.hash[:20]}...\n"
        )


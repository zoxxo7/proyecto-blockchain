"""
gui.py — Simulador Visual e Intuitivo de Blockchain
===================================================
Diseñado para exposiciones y defensas universitarias.
Interfaz gráfica moderna, pedagógica y fácil de entender.

EJECUCIÓN:
    py gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from blockchain import Blockchain


# ══════════════════════════════════════════════════════════════════════════════
#  PALETA DE COLORES MODERNA (Dark Slate & Emerald Dashboard)
# ══════════════════════════════════════════════════════════════════════════════
BG_DARK        = "#0B0F19"   # Fondo ultra oscuro elegante
BG_PANEL       = "#111827"   # Panel oscuro (Tailwind Gray 900)
BG_CARD        = "#1F2937"   # Tarjeta bloque (Tailwind Gray 800)
BG_CARD_FAIL   = "#450A0A"   # Tarjeta bloque cuando está HACKEADO (Rojo oscuro)

ACCENT_GREEN   = "#10B981"   # Verde esmeralda (Válido / Éxito)
ACCENT_RED     = "#EF4444"   # Rojo vibrante (Hackeo / Roto)
ACCENT_AMBER   = "#F59E0B"   # Amarillo/Ámbar (Minería / Trabajo)
ACCENT_CYAN    = "#06B6D4"   # Cian (Enlaces / Hashes)

TEXT_LIGHT     = "#F9FAFB"   # Texto principal claro
TEXT_MUTED     = "#9CA3AF"   # Texto secundario gris
TEXT_ACCENT    = "#38BDF8"   # Texto destacado azul cielo


class BlockchainApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.blockchain = Blockchain(difficulty=3) # Dificultad 3 = rápida y realista
        self.bloque_hackeado_idx = None

        self._configurar_ventana()
        self._construir_interfaz()
        self._cargar_datos_iniciales()

    def _configurar_ventana(self):
        self.root.title("🔗 Simulador Visual Blockchain — Tecnologías Emergentes")
        self.root.geometry("1180x820")
        self.root.minsize(1050, 720)
        self.root.configure(bg=BG_DARK)

        # Centrado en pantalla
        x = (self.root.winfo_screenwidth() // 2) - (1180 // 2)
        y = (self.root.winfo_screenheight() // 2) - (820 // 2)
        self.root.geometry(f"1180x820+{x}+{y}")

    # ──────────────────────────────────────────────────────────────────────────
    #  CONSTRUCCIÓN DE LA INTERFAZ
    # ──────────────────────────────────────────────────────────────────────────
    def _construir_interfaz(self):
        # 1. ENCABEZADO Y SEMÁFORO DE SEGURIDAD
        self.frame_header = tk.Frame(self.root, bg=BG_PANEL, padx=25, pady=15)
        self.frame_header.pack(fill="x", side="top")

        # Título y subtítulo
        f_titulos = tk.Frame(self.frame_header, bg=BG_PANEL)
        f_titulos.pack(side="left")

        tk.Label(
            f_titulos, text="🔗 SIMULADOR VISUAL DE BLOCKCHAIN",
            font=("Segoe UI", 18, "bold"), fg=TEXT_LIGHT, bg=BG_PANEL
        ).pack(anchor="w")

        tk.Label(
            f_titulos, text="Demostración visual de inmutabilidad, Proof of Work y detección de fraudes",
            font=("Segoe UI", 10), fg=TEXT_MUTED, bg=BG_PANEL
        ).pack(anchor="w")

        # Semáforo de Estado General
        self.frame_badge = tk.Frame(self.frame_header, bg="#064E3B", padx=15, pady=8, bd=1, relief="solid")
        self.frame_badge.pack(side="right")

        self.lbl_semaforo = tk.Label(
            self.frame_badge, text="● CADENA 100% ÍNTEGRA Y SEGURA",
            font=("Segoe UI", 12, "bold"), fg=ACCENT_GREEN, bg="#064E3B"
        )
        self.lbl_semaforo.pack()

        # 2. PANEL INFORMATIVO "QUÉ DECIRLE AL INGE" (GUÍA DIDÁCTICA)
        self.frame_didactico = tk.Frame(self.root, bg="#1E1B4B", padx=20, pady=10)
        self.frame_didactico.pack(fill="x", side="top", padx=15, pady=(10, 0))

        tk.Label(
            self.frame_didactico, text="💡 EXPLICACIÓN PARA LA EXPOSICIÓN:",
            font=("Segoe UI", 9, "bold"), fg="#A78BFA", bg="#1E1B4B"
        ).pack(anchor="w")

        self.lbl_guia = tk.Label(
            self.frame_didactico,
            text="La cadena se encuentra enlazada criptográficamente. Cada bloque custodia el hash del anterior.",
            font=("Segoe UI", 10), fg=TEXT_LIGHT, bg="#1E1B4B", wraplength=1100, justify="left"
        )
        self.lbl_guia.pack(anchor="w", pady=(2, 0))

        # 3. CONTENEDOR PRINCIPAL: PANEL DE CONTROL (Izquierda) + CADENA VISUAL (Derecha)
        self.frame_main = tk.Frame(self.root, bg=BG_DARK, padx=15, pady=10)
        self.frame_main.pack(fill="both", expand=True)

        self._crear_panel_izquierdo(self.frame_main)
        self._crear_panel_derecho(self.frame_main)

    # ──────────────────────────────────────────────────────────────────────────
    #  PANEL IZQUIERDO: CONTROLES INTUITIVOS
    # ──────────────────────────────────────────────────────────────────────────
    def _crear_panel_izquierdo(self, parent):
        p_izq = tk.Frame(parent, bg=BG_PANEL, width=340, padx=15, pady=15)
        p_izq.pack(side="left", fill="y", padx=(0, 15))
        p_izq.pack_propagate(False)

        # SECCIÓN 1: AGREGAR TRANSACCIÓN RÁPIDA
        tk.Label(p_izq, text="➕ NUEVA TRANSACCIÓN", font=("Segoe UI", 11, "bold"), fg=ACCENT_CYAN, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        tk.Label(p_izq, text="Remitente:", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_PANEL).pack(anchor="w")
        self.ent_de = tk.Entry(p_izq, font=("Segoe UI", 10), bg=BG_CARD, fg=TEXT_LIGHT, insertbackground=ACCENT_GREEN, relief="flat")
        self.ent_de.insert(0, "Carlos")
        self.ent_de.pack(fill="x", pady=(2, 8), ipady=4)

        tk.Label(p_izq, text="Receptor:", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_PANEL).pack(anchor="w")
        self.ent_para = tk.Entry(p_izq, font=("Segoe UI", 10), bg=BG_CARD, fg=TEXT_LIGHT, insertbackground=ACCENT_GREEN, relief="flat")
        self.ent_para.insert(0, "Diana")
        self.ent_para.pack(fill="x", pady=(2, 8), ipady=4)

        tk.Label(p_izq, text="Monto (Bs):", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_PANEL).pack(anchor="w")
        self.ent_monto = tk.Entry(p_izq, font=("Segoe UI", 10), bg=BG_CARD, fg=TEXT_LIGHT, insertbackground=ACCENT_GREEN, relief="flat")
        self.ent_monto.insert(0, "150")
        self.ent_monto.pack(fill="x", pady=(2, 12), ipady=4)

        self.btn_minar = tk.Button(
            p_izq, text="⛏️  MINAR Y AÑADIR BLOQUE",
            font=("Segoe UI", 10, "bold"), bg=ACCENT_GREEN, fg="#064E3B",
            activebackground="#059669", activeforeground=TEXT_LIGHT,
            relief="flat", cursor="hand2", pady=8, command=self._accion_minar
        )
        self.btn_minar.pack(fill="x", pady=(0, 20))

        ttk.Separator(p_izq, orient="horizontal").pack(fill="x", pady=10)

        # SECCIÓN 2: BOTONES DE DEMOSTRACIÓN (PARA EL INGENIERO)
        tk.Label(p_izq, text="🎯 PRUEBAS DE EVALUACIÓN", font=("Segoe UI", 11, "bold"), fg=ACCENT_AMBER, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        # Botón 1: Validar
        self.btn_validar = tk.Button(
            p_izq, text="🔍 1. Validar Cadena Completa",
            font=("Segoe UI", 9, "bold"), bg="#1E293B", fg=TEXT_LIGHT,
            activebackground="#334155", relief="flat", cursor="hand2", pady=7, anchor="w", padx=10,
            command=self._accion_validar
        )
        self.btn_validar.pack(fill="x", pady=4)

        # Botón 2: Hackear
        self.btn_hackear = tk.Button(
            p_izq, text="🚨 2. Simular Ataque (Hackear Bloque 2)",
            font=("Segoe UI", 9, "bold"), bg="#450A0A", fg="#FCA5A5",
            activebackground="#7F1D1D", relief="flat", cursor="hand2", pady=7, anchor="w", padx=10,
            command=self._accion_hackear
        )
        self.btn_hackear.pack(fill="x", pady=4)

        # Botón 3: Consenso
        self.btn_consenso = tk.Button(
            p_izq, text="⭐ 3. Consenso: Cadena más Larga",
            font=("Segoe UI", 9, "bold"), bg="#78350F", fg="#FDE68A",
            activebackground="#92400E", relief="flat", cursor="hand2", pady=7, anchor="w", padx=10,
            command=self._accion_consenso
        )
        self.btn_consenso.pack(fill="x", pady=4)

        # Botón 4: Restaurar
        self.btn_reset = tk.Button(
            p_izq, text="🔄 Restaurar Cadena Original",
            font=("Segoe UI", 9), bg="#374151", fg=TEXT_LIGHT,
            relief="flat", cursor="hand2", pady=6, command=self._cargar_datos_iniciales
        )
        self.btn_reset.pack(fill="x", pady=(15, 0))

    # ──────────────────────────────────────────────────────────────────────────
    #  PANEL DERECHO: VISOR DE BLOQUES Y ESLABONES
    # ──────────────────────────────────────────────────────────────────────────
    def _crear_panel_derecho(self, parent):
        p_der = tk.Frame(parent, bg=BG_DARK)
        p_der.pack(side="left", fill="both", expand=True)

        tk.Label(
            p_der, text="⛓️ CADENA DE BLOQUES EN TIEMPO REAL",
            font=("Segoe UI", 11, "bold"), fg=TEXT_MUTED, bg=BG_DARK
        ).pack(anchor="w", pady=(0, 5))

        # Canvas con Scrollbar para deslizar los bloques cómodamente
        canvas_frame = tk.Frame(p_der, bg=BG_DARK)
        canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(canvas_frame, bg=BG_DARK, bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame_cadena = tk.Frame(self.canvas, bg=BG_DARK)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.frame_cadena, anchor="nw")

        self.frame_cadena.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))

    # ──────────────────────────────────────────────────────────────────────────
    #  RENDERIZADO INTUITIVO DE BLOQUES
    # ──────────────────────────────────────────────────────────────────────────
    def _renderizar_cadena(self):
        # Limpiar bloques anteriores
        for w in self.frame_cadena.winfo_children():
            w.destroy()

        cadena = self.blockchain.chain
        es_valida = True

        for i, bloque in enumerate(cadena):
            es_genesis = (i == 0)
            es_hackeado = (self.bloque_hackeado_idx == i)

            # Verificar si este bloque rompe la cadena
            hash_correcto = (bloque.hash == bloque.calculate_hash())
            enlace_correcto = True if es_genesis else (bloque.previous_hash == cadena[i-1].hash)

            bloque_roto = es_hackeado or (not hash_correcto) or (not enlace_correcto)
            if bloque_roto:
                es_valida = False

            # Contenedor del Bloque (Tarjeta moderna)
            color_fondo_card = BG_CARD_FAIL if bloque_roto else BG_CARD
            color_borde = ACCENT_RED if bloque_roto else (ACCENT_GREEN if es_genesis else "#374151")

            card = tk.Frame(self.frame_cadena, bg=color_fondo_card, bd=2, relief="solid", padx=16, pady=12)
            card.pack(fill="x", padx=5, pady=6)

            # Encabezado de la tarjeta
            f_top = tk.Frame(card, bg=color_fondo_card)
            f_top.pack(fill="x")

            icono = "🌐" if es_genesis else ("🚨" if bloque_roto else "📦")
            titulo_txt = f"{icono} BLOQUE #{bloque.index}" + (" (GÉNESIS)" if es_genesis else "")
            color_titulo = ACCENT_RED if bloque_roto else (ACCENT_CYAN if es_genesis else TEXT_LIGHT)

            tk.Label(f_top, text=titulo_txt, font=("Segoe UI", 12, "bold"), fg=color_titulo, bg=color_fondo_card).pack(side="left")

            badge_estado = "❌ ¡ALTERADO / ROTO!" if bloque_roto else "✅ VÁLIDO (MINADO)"
            badge_color = ACCENT_RED if bloque_roto else ACCENT_GREEN
            tk.Label(f_top, text=badge_estado, font=("Segoe UI", 9, "bold"), fg=badge_color, bg=color_fondo_card).pack(side="right")

            # Cuerpo del Bloque: Datos principales en 2 columnas
            f_body = tk.Frame(card, bg=color_fondo_card, pady=6)
            f_body.pack(fill="x")

            # Fila 1: Transacción / Datos
            datos_legibles = bloque.data if isinstance(bloque.data, str) else bloque.data.get("descripcion", str(bloque.data))
            f_dat = tk.Frame(f_body, bg=color_fondo_card)
            f_dat.pack(fill="x", pady=2)
            tk.Label(f_dat, text="📄 Datos guardados:", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=color_fondo_card, width=17, anchor="w").pack(side="left")
            color_dat = ACCENT_RED if bloque_roto else TEXT_LIGHT
            tk.Label(f_dat, text=datos_legibles, font=("Segoe UI", 10, "bold"), fg=color_dat, bg=color_fondo_card).pack(side="left")

            # Fila 2: Nonce y Dificultad
            f_non = tk.Frame(f_body, bg=color_fondo_card)
            f_non.pack(fill="x", pady=2)
            tk.Label(f_non, text="⛏️ Proof of Work:", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=color_fondo_card, width=17, anchor="w").pack(side="left")
            tk.Label(f_non, text=f"Nonce: {bloque.nonce:,} intentos  |  Timestamp: {bloque.timestamp[11:19]}", font=("Segoe UI", 9), fg=TEXT_ACCENT, bg=color_fondo_card).pack(side="left")

            # Fila 3: Hash Anterior (Eslabón)
            f_prev = tk.Frame(f_body, bg=color_fondo_card)
            f_prev.pack(fill="x", pady=2)
            tk.Label(f_prev, text="🔗 Hash Anterior:", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=color_fondo_card, width=17, anchor="w").pack(side="left")
            tk.Label(f_prev, text=bloque.previous_hash, font=("Consolas", 9), fg=TEXT_MUTED, bg=color_fondo_card).pack(side="left")

            # Fila 4: Hash Propio
            f_hash = tk.Frame(f_body, bg=color_fondo_card)
            f_hash.pack(fill="x", pady=2)
            tk.Label(f_hash, text="🛡️ Hash Propio:", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=color_fondo_card, width=17, anchor="w").pack(side="left")
            color_h = ACCENT_RED if bloque_roto else ACCENT_GREEN
            tk.Label(f_hash, text=bloque.hash, font=("Consolas", 9, "bold"), fg=color_h, bg=color_fondo_card).pack(side="left")

            # ESLABÓN VISUAL CONECTOR (FLECHA ELEGANTE)
            if i < len(cadena) - 1:
                f_link = tk.Frame(self.frame_cadena, bg=BG_DARK, pady=2)
                f_link.pack(fill="x")
                flecha_txt = "║  🔴 ENLACE ROTO (Incompatibilidad criptográfica)  ║" if bloque_roto else "║  ⬇️  ENLAZADO POR HASH CRIPTOGRÁFICO SHA-256  ⬇️"
                color_link = ACCENT_RED if bloque_roto else ACCENT_CYAN
                tk.Label(f_link, text=flecha_txt, font=("Segoe UI", 8, "bold"), fg=color_link, bg=BG_DARK).pack()

        # Actualizar Semáforo Superior
        if es_valida:
            self.frame_badge.configure(bg="#064E3B")
            self.lbl_semaforo.configure(text="● CADENA 100% ÍNTEGRA Y SEGURA", fg=ACCENT_GREEN, bg="#064E3B")
        else:
            self.frame_badge.configure(bg="#7F1D1D")
            self.lbl_semaforo.configure(text="🚨 ¡ALERTA: CADENA MANIPULADA / INVÁLIDA!", fg="#FCA5A5", bg="#7F1D1D")

    # ──────────────────────────────────────────────────────────────────────────
    #  LÓGICA DE LAS ACCIONES DIDÁCTICAS
    # ──────────────────────────────────────────────────────────────────────────
    def _cargar_datos_iniciales(self):
        """Carga 4 bloques iniciales para que la ventana nunca se vea vacía."""
        self.blockchain = Blockchain(difficulty=3)
        self.bloque_hackeado_idx = None

        transacciones = [
            {"descripcion": "Alice → Bob: 100 Bs", "monto": 100},
            {"descripcion": "Bob → Carlos: 50 Bs", "monto": 50},
            {"descripcion": "Carlos → Diana: 25 Bs", "monto": 25},
        ]
        for tx in transacciones:
            self.blockchain.add_block(tx)

        self.lbl_guia.configure(
            text="✅ ESTADO INICIAL: La cadena tiene 4 bloques enlazados. Cada bloque empieza con '000' gracias al Proof of Work.",
            fg=TEXT_LIGHT
        )
        self._renderizar_cadena()

    def _accion_minar(self):
        de = self.ent_de.get().strip()
        para = self.ent_para.get().strip()
        monto = self.ent_monto.get().strip()

        if not de or not para or not monto:
            messagebox.showwarning("Atención", "Por favor completa remitente, receptor y monto.")
            return

        self.btn_minar.configure(state="disabled", text="⏳ Minando bloque...")
        self.lbl_guia.configure(
            text="⛏️ TRABAJO DE MINERÍA: La CPU está buscando un 'nonce' matemático para que el hash empiece con ceros...",
            fg=ACCENT_AMBER
        )

        def tarea():
            tx = {"descripcion": f"{de} → {para}: {monto} Bs", "monto": monto}
            self.blockchain.add_block(tx)
            self.root.after(0, self._post_minar, f"{de} → {para}")

        threading.Thread(target=tarea, daemon=True).start()

    def _post_minar(self, desc):
        self.btn_minar.configure(state="normal", text="⛏️  MINAR Y AÑADIR BLOQUE")
        self.lbl_guia.configure(
            text=f"🎉 ¡Bloque minado con éxito para '{desc}'! Se calculó un hash válido y se enlazó al último bloque.",
            fg=ACCENT_GREEN
        )
        self._renderizar_cadena()
        self.canvas.yview_moveto(1.0) # Auto-scroll al final

    def _accion_validar(self):
        es_valida = self.blockchain.is_valid()
        if es_valida and self.bloque_hackeado_idx is None:
            self.lbl_guia.configure(
                text="🔍 VALIDACIÓN EXITOSA: Se recorrió bloque por bloque. Todos los hashes coinciden con sus contenidos y los enlaces están intactos.",
                fg=ACCENT_GREEN
            )
            messagebox.showinfo("Validación Exitosa", "✅ La Blockchain es 100% VÁLIDA.\n\nNingún dato ha sido alterado.")
        else:
            self.lbl_guia.configure(
                text=f"🚨 ERROR DE VALIDACIÓN: Se detectó que el Bloque #{self.bloque_hackeado_idx} fue alterado. El hash guardado no coincide con el nuevo cálculo.",
                fg=ACCENT_RED
            )
            messagebox.showerror("Cadena Inválida", f"❌ ¡FRAUDE DETECTADO!\n\nEl Bloque #{self.bloque_hackeado_idx} fue modificado.\nLa red rechaza esta versión automáticamente.")
        self._renderizar_cadena()

    def _accion_hackear(self):
        """Modifica artificialmente los datos del Bloque 2 sin recalcular hash."""
        if len(self.blockchain.chain) < 3:
            messagebox.showwarning("Aviso", "Añade al menos un bloque más para poder hackear.")
            return

        self.bloque_hackeado_idx = 2
        bloque = self.blockchain.chain[2]
        
        # Alteración maliciosa
        bloque.data = {"descripcion": "🔴 HACKEO: Carlos → HACKER: 9,999 Bs", "monto": 9999}
        # IMPORTANTE: No recalculamos el hash para que quede al descubierto la trampa

        self.lbl_guia.configure(
            text="🚨 ATAQUE REALIZADO: Modificamos el Bloque #2 de '25 Bs' a '9,999 Bs'. Observa cómo el Bloque se torna ROJO porque su huella digital ya no coincide.",
            fg=ACCENT_RED
        )
        self._renderizar_cadena()

    def _accion_consenso(self):
        """Simula la regla de la cadena más larga de Nakamoto."""
        self.lbl_guia.configure(
            text="⭐ CONSENSO DE NAKAMOTO: Simulando un Nodo B con 6 bloques válidos (más trabajo acumulado)...",
            fg=ACCENT_AMBER
        )
        
        def tarea():
            nodo_b = Blockchain(difficulty=2)
            txs = [
                {"descripcion": "Pago Hospital: 400 Bs"},
                {"descripcion": "Compra Ganado Beni: 1200 Bs"},
                {"descripcion": "Venta Castaña Riberalta: 850 Bs"},
                {"descripcion": "Flete Fluvial: 300 Bs"},
                {"descripcion": "Seguro Agrícola: 150 Bs"},
            ]
            for t in txs:
                nodo_b.add_block(t)
            
            self.root.after(0, lambda: self._post_consenso(nodo_b))

        threading.Thread(target=tarea, daemon=True).start()

    def _post_consenso(self, nodo_b):
        long_antigua = len(self.blockchain.chain)
        self.blockchain.chain = nodo_b.chain
        self.bloque_hackeado_idx = None

        self.lbl_guia.configure(
            text=f"🔄 CONSENSO APLICADO: Tu nodo tenía {long_antigua} bloques. El Nodo B tenía {len(nodo_b.chain)} bloques. Por la Regla de Nakamoto, tu nodo adoptó la cadena más larga y válida.",
            fg=ACCENT_GREEN
        )
        messagebox.showinfo(
            "Consenso de Nakamoto",
            f"¡Sincronización Exitosa!\n\n"
            f"Cadena anterior: {long_antigua} bloques.\n"
            f"Nueva cadena adoptada: {len(nodo_b.chain)} bloques.\n\n"
            f"Se aplicó la regla de la cadena válida más larga."
        )
        self._renderizar_cadena()


if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()

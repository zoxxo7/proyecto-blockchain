# UNIVERSIDAD AUTÓNOMA DEL BENI "JOSÉ BALLIVIÁN"
## FACULTAD DE INGENIERÍA Y TECNOLOGÍA
### CARRERA DE INGENIERÍA DE SISTEMAS (LICENCIATURA - TRINIDAD)

---

# TRABAJO PRÁCTICO: TECNOLOGÍA BLOCKCHAIN

* **Asignatura:** Tecnologías Emergentes
* **Código de Asignatura:** CIS-ACO-o15310
* **Docente:** Ing. Hermes Rodriguez Rivero
* **Modalidad:** Grupal (2 Estudiantes)
* **Estudiantes:**
  1. **Zafnat Josue Mamani Limachi**
  2. **Jose Carlos Caity Roca**
* **Lugar y Fecha:** Trinidad – Beni – Bolivia | 2/2026

---

## ÍNDICE
1. **PARTE I: INVESTIGACIÓN TEÓRICA**
   - 1.1 Funciones Hash Criptográficas y sus Propiedades
   - 1.2 Mecanismos de Consenso: Proof of Work vs. Proof of Stake
   - 1.3 Tipologías de Redes Blockchain (Pública, Privada, Consorcio)
   - 1.4 Contratos Inteligentes (Smart Contracts) y Caso de Uso
   - 1.5 Comparativa: Blockchain frente a Bases de Datos Relacionales (SQL)
2. **PARTE III: CASO DE ESTUDIO**
   - 2.1 Caso Internacional: Trazabilidad en la Cadena Alimentaria (*IBM Food Trust*)
   - 2.2 Problema Inicial y Necesidad de Trazabilidad
   - 2.3 Intervención de la Blockchain y Arquitectura de Red
   - 2.4 Ventajas Operativas y Limitaciones Reales Encontradas
   - 2.5 Análisis Crítico: ¿Blockchain o Base de Datos Convencional?
   - 2.6 Propuesta de Aplicación Local: *BeniTrace* (Trazabilidad Bovina y Castaña Amazónica)
3. **REFERENCIAS BIBLIOGRÁFICAS (FORMATO APA)**

---

# 1. PARTE I: INVESTIGACIÓN TEÓRICA (20 Puntos)

### 1.1 Funciones Hash Criptográficas y sus Propiedades
Una **función hash criptográfica** es un algoritmo matemático unidireccional y determinista que transforma una entrada de tamaño arbitrario (un mensaje de texto, un archivo multimedia o un conjunto de transacciones financieras) en una cadena alfanumérica de longitud fija, denominada *hash* o *resumen criptográfico* (National Institute of Standards and Technology [NIST], 2015). En la arquitectura de Bitcoin y en la mayoría de las redes distribuidas modernas se utiliza el estándar **SHA-256** (*Secure Hash Algorithm* de 256 bits), el cual produce invariablemente una salida en formato hexadecimal de 64 caracteres.

Para garantizar la seguridad e inmutabilidad en un entorno distribuido, una función hash debe cumplir estrictamente con tres propiedades operativas:

1. **Determinismo:** Para una entrada idéntica $x$, el algoritmo devolverá siempre y sin excepción el mismo valor $H(x)$. No existe componente aleatorio en su cálculo.
2. **Resistencia a Colisiones:** Debe ser computacionalmente inviable encontrar dos entradas distintas $x$ e $y$ (donde $x \neq y$) tales que $H(x) = H(y)$. Aunque matemáticamente las colisiones existen debido al *principio del palomar* (el espacio de entradas posibles es infinito, mientras que el espacio de salidas de 256 bits es finito con $2^{256}$ posibilidades), la probabilidad práctica de que dos bloques colisionen es del orden de $1$ en $1.15 \times 10^{77}$, una cifra comparable a la cantidad de átomos en el universo observable.
3. **Efecto Avalancha (*Avalanche Effect*):** Si se modifica un único bit de la información de entrada (por ejemplo, alterar una letra minúscula a mayúscula o agregar un punto al final de una oración), el hash resultante cambia radicalmente, alterando aproximadamente el 50% de los bits de salida de forma pseudoaleatoria. Esta propiedad es el pilar de la inmutabilidad de la cadena de bloques, ya que cualquier modificación no autorizada en un bloque histórico altera inmediatamente su hash y rompe los enlaces subsecuentes.

---

### 1.2 Mecanismos de Consenso: Proof of Work (PoW) vs. Proof of Stake (PoS)

Los mecanismos de consenso son protocolos algorítmicos que permiten a múltiples nodos distribuidos en una red sin confianza mutua convenir sobre el estado único y veraz de un registro contable compartido.

* **Proof of Work (Prueba de Trabajo):** Propuesto por Satoshi Nakamoto (2008) para Bitcoin, basa su seguridad en el consumo de **energía eléctrica y potencia de cómputo por hardware**. Los mineros de la red compiten resolviendo un rompecabezas criptográfico iterativo: encontrar un valor numérico arbitrario (*nonce*) que, combinado con los datos del bloque, genere un hash con una cantidad específica de ceros a la izquierda (la *dificultad*). El primer minero en hallar la solución válida transmite el bloque y recibe una recompensa económica. Su principal ventaja es su robusta seguridad termodinámica; su gran debilidad radica en la lentitud de procesamiento (Bitcoin promedia 7 transacciones por segundo) y su elevado impacto ambiental por consumo energético.
* **Proof of Stake (Prueba de Participación):** Diseñado como una alternativa eficiente, reemplaza la fuerza bruta computacional por el **compromiso financiero de capital** (Buterin & Griffith, 2017). Los participantes no son mineros, sino *validadores* que depositan y bloquean una determinada cantidad de criptomonedas nativas en un contrato inteligente en concepto de garantía (*stake*). El protocolo selecciona pseudoaleatoriamente al validador de cada bloque ponderando el monto retenido y el tiempo de depósito. Si un validador aprueba transacciones falsas o promueve bifurcaciones ilegítimas, el sistema ejecuta un castigo automático denominado *slashing*, confiscando o quemando su capital retenido. Reduce el consumo de energía en más del 99.95%, aunque introduce debates sobre la plutocracia (quien más capital tiene, más influencia acumula).

---

### 1.3 Tipologías de Redes Blockchain

Las cadenas de bloques se clasifican según sus permisos de lectura y escritura en públicas, privadas y federadas (de consorcio):

| Criterio Comparativo | Blockchain Pública | Blockchain Privada | Blockchain de Consorcio |
| :--- | :--- | :--- | :--- |
| **Acceso a Lectura** | Abierto e irrestricto a cualquier usuario en internet. | Restringido únicamente a usuarios autorizados por la organización propietaria. | Restringido a las entidades y empresas participantes del consorcio. |
| **Acceso a Escritura / Consenso** | Público y descentralizado (cualquiera puede validar o minar). | Centralizado en un único nodo o administrador institucional. | Distribuido entre un conjunto predeterminado de nodos institucionales. |
| **Rendimiento (TPS)** | Bajo (7 a 30 TPS en capas base). Alta latencia de finalización. | Muy alto (miles de TPS). Finalización casi instantánea. | Medio a alto (cientos a miles de TPS). Baja latencia. |
| **Mecanismo de Consenso** | Proof of Work, Proof of Stake (abiertos, alta tolerancia a fallos bizantinos). | Algoritmos de tolerancia a caídas como Raft o Crash Fault Tolerance (CFT). | Proof of Authority (PoA), PBFT, IBFT. |
| **Nivel de Descentralización** | Totalmente descentralizada. Cero entidades de control. | Completamente centralizada. Controlada por una sola entidad. | Descentralización parcial / Federada entre pares corporativos iguales. |
| **Casos Típicos** | Bitcoin, Ethereum, Cardano. | Auditoría contable interna corporativa, bases de datos de personal. | Redes interbancarias, trazabilidad de cadenas logísticas entre proveedores. |

---

### 1.4 Contratos Inteligentes (Smart Contracts) y Caso de Uso
Un **contrato inteligente** es un protocolo informático autónomo e inmutable que se ejecuta de manera determinista sobre una máquina virtual descentralizada (como la EVM de Ethereum), asegurando el cumplimiento de acuerdos bilaterales o multilaterales sin necesidad de mediación judicial, notarial o bancaria (Szabo, 1994; Antonopoulos & Wood, 2018). Su funcionamiento sigue una estricta lógica condicional: `SI ocurre el evento X verificado criptográficamente, ENTONCES ejecutar la acción financiera Y`.

* **Ejemplo Práctico: Seguro Paramétrico contra Inundaciones en la Cuenca Amazónica:**  
  Un productor pecuario de las pampas de Moxos suscribe una póliza paramétrica descentralizada para proteger su ganado de crecidas estacionales. El contrato inteligente permanece en custodia de los fondos de indemnización y se conecta a un *oráculo descentralizado* (Chainlink) que consulta diariamente las lecturas de nivel hidrológico telemétrico publicadas por el Servicio Nacional de Hidrografía Naval en Puerto Almacén. Si el nivel del río supera la cota de alerta roja preestablecida de 13 metros, el contrato inteligente liquida e indemniza automáticamente la compensación en la billetera digital del ganadero en minutos, prescindiendo de peritos tasadores de seguros o procesos burocráticos de aprobación que tardan meses.

---

### 1.5 Comparativa: Blockchain frente a Bases de Datos Relacionales Tradicionales (SQL)

La siguiente tabla resume las diferencias arquitectónicas entre un sistema gestor de bases de datos relacional (RDBMS como PostgreSQL/Oracle) y una cadena de bloques:

| Dimensión Analizada | Base de Datos Relacional (RDBMS / SQL) | Tecnología Blockchain |
| :--- | :--- | :--- |
| **Control de Acceso** | Centralizado. Un Administrador de Base de Datos (*DBA*) o superusuario (*root*) gestiona permisos, roles y accesos a tablas. | Descentralizado y criptográfico. Las identidades se basan en pares de claves asimétricas (pública/privada) y las reglas de consenso de la red. |
| **Rendimiento y Latencia** | Rendimiento excepcional (decenas de miles de escrituras/segundo, latencia en el orden de microsegundos). | Moderado a bajo (la necesidad de propagación peer-to-peer y validación de bloques impone un cuello de botella físico). |
| **Modificación de Datos** | Operaciones CRUD completas (*Create, Read, Update, Delete*). Los registros históricos pueden ser modificados o eliminados a discreción del DBA. | Estructura estrictamente de adición (*Append-Only*). Los datos son inmutables; no se puede alterar el pasado sin invalidar toda la cadena. |
| **Confianza entre Partes** | Basada en un tercero de confianza (*Trusted Third Party*). Todas las partes deben depositar su fe ciega en el custodio del servidor. | *Trustless* (cero confianza subjetiva). La veracidad se deriva de la verificación matemática independiente de cada nodo participante. |

---

# 2. PARTE III: CASO DE ESTUDIO (25 Puntos)

### 2.1 Caso Internacional: Trazabilidad en la Cadena Alimentaria (*IBM Food Trust*)

#### A. Descripción del problema que se buscaba resolver
En las cadenas agroalimentarias globales, los productos frescos pasan por múltiples intermediarios: productores agrícolas, centros de acopio, frigoríficos, operadores de transporte con cadena de frío, aduanas sanitarias y supermercados minoristas. Históricamente, cada actor administraba su propia información en sistemas ERP aislados o en registros físicos de papel. Cuando ocurría un brote de contaminación bacteriana (*Escherichia coli*, *Listeria* o *Salmonella*), determinar en qué punto específico se contaminó el lote de alimentos tomaba en promedio entre **6 y 8 días hábiles**. Durante ese periodo de incertidumbre, se producían intoxicaciones masivas, muertes de consumidores y el descarte preventivo de cientos de toneladas de alimentos sanos, con pérdidas multimillonarias para toda la industria.

#### B. Cómo interviene Blockchain y tipo de red utilizada
IBM, en colaboración con corporaciones como Walmart, Carrefour y Nestlé, diseñó la plataforma **IBM Food Trust**, cimentada en la tecnología de código abierto **Hyperledger Fabric**.
* **Tipo de Red:** Es una **Blockchain de Consorcio (Permisionada)**. La red no permite el ingreso de actores anónimos; cada participante empresarial está plenamente identificado mediante certificados digitales X.509 y el consenso se alcanza mediante mecanismos de tolerancia a fallos prácticos bizantinos (*PBFT*) o *Proof of Authority (PoA)*.
* **Mecanismo Operativo:** Cada paleta o caja de producto recibe un identificador único (código GS1 o etiqueta RFID). A medida que el producto avanza por la cadena, cada participante firma criptográficamente transacciones que registran eventos críticos: hora de cosecha, pesaje, datos telemétricos de temperatura de los camiones frigoríficos e ingreso a góndola. Mediante esta arquitectura, el tiempo requerido para rastrear el origen de un producto alimenticio desde el estante minorista hasta la granja de cultivo se redujo de **6.5 días a 2.2 segundos**.

#### C. Ventajas obtenidas y limitaciones encontradas
* **Ventajas Operativas:**
  1. *Auditoría Inmediata:* Permite retiros quirúrgicos de lotes contaminados en segundos, retirando únicamente las cajas afectadas sin paralizar las ventas nacionales del producto.
  2. *Mitigación del Fraude:* Impide la falsificación de sellos de origen orgánico o carnes con denominación protegida.
  3. *Privacidad Comercial:* Gracias al sistema de canales privados de Hyperledger Fabric, dos empresas pueden compartir datos de trazabilidad sin exponer precios de compra o márgenes comerciales a sus competidores.
* **Limitaciones Reales:**
  1. *El Problema del "Garbage In, Garbage Out":* La blockchain garantiza matemáticamente que el dato guardado jamás será alterado, pero **no puede garantizar que el dato físico original sea fidedigno**. Si un operario ingresa manualmente un peso falso o registra una fruta infectada como sana, la blockchain simplemente registrará una mentira de forma inmutable.
  2. *Costo de Adopción e Infraestructura:* Exige que pequeños productores rurales cuenten con conectividad a internet, lectores de códigos y capacitación técnica, lo cual genera una brecha tecnológica significativa.

#### D. Análisis Crítico: ¿Era estrictamente necesaria Blockchain o bastaba una Base de Datos Convencional?
**Dictamen Técnico: Desde la perspectiva del rendimiento puro, una base de datos centralizada (SQL) hubiera sido suficiente; sin embargo, desde la perspectiva de la teoría de juegos y la desconfianza comercial, la Blockchain era indispensable.**

Si el sistema se hubiera construido sobre una base de datos PostgreSQL tradicional alojada en los servidores de Walmart, los demás participantes de la cadena (como Nestlé o Carrefour) **se habrían negado a adoptarla**. Ninguna multinacional acepta que su principal rival comercial sea el dueño y administrador absoluto de la base de datos donde residen sus volúmenes y tiempos de transporte, temiendo que la empresa administradora pueda alterar registros, ver datos confidenciales o manipular auditorías a su conveniencia. Por lo tanto, el uso de blockchain no se justificó por necesidad de velocidad o capacidad de almacenamiento, sino para **eliminar el monopolio del poder sobre los datos y crear un entorno de gobernanza neutro entre competidores directos**.

---

### 2.2 Propuesta de Aplicación Local: *BeniTrace* (Trazabilidad Bovina y Castaña en el Beni)

#### A. Diagnóstico de la Problemática Regional (Beni, Bolivia)
El departamento del Beni es el motor pecuario y recolector forestal de Bolivia, con un hato ganadero que supera los 3 millones de cabezas de bovinos y la mayor producción de castaña amazónica de exportación (concentrada en Riberalta y Guayaramerín). No obstante, el sector enfrenta graves problemas estructurales:
1. **Abigeato (Robo de Ganado):** El robo de reses y la posterior adulteración física de marcas de fuego y guías de movimiento de ganado (SENASAG) ocasionan pérdidas millonarias a los estancieros benianos.
2. **Nuevas Regulaciones Ambientales Internacionales:** El Reglamento contra la Deforestación de la Unión Europea (EUDR 2023/1115) impone como requisito obligatorio para importar carne bovina y productos forestales que el importador demuestre con geolocalización satelital que el producto proviene de **tierras libres de deforestación posterior a diciembre de 2020**. El sistema documental en papel de Bolivia es vulnerable a fraudes y no brinda la certeza requerida por los mercados extranjeros de alto poder adquisitivo.

#### B. Arquitectura de la Solución *BeniTrace*
Se propone la creación de una **Blockchain de Consorcio Departamental** conformada por:
* FEGABENI (Federación de Ganaderos del Beni)
* SENASAG (Servicio Nacional de Sanidad Agropecuaria e Inocuidad Alimentaria)
* Frigoríficos exportadores (ej. Frigorífico BFC, Fridosa)
* Asociaciones de recolectores de castaña de Riberalta
* Entidades financieras y aduaneras

```
[Estancia Ganadera en Moxos/Yacuma] 
       │ (Arete electrónico RFID al nacer + Coordenadas GPS del predio)
       ▼
[Punto de Control SENASAG] 
       │ (Firma digital de Guía Electrónica de Movimiento en Blockchain)
       ▼
[Frigorífico Faenador] 
       │ (Pesaje automático, control sanitario y lote de faena sellado en bloque)
       ▼
[Corte de Exportación al Consumidor Final]
       │ (Código QR en el empaque para verificación pública)
```

#### C. Impacto y Beneficios Esperados
1. **Erradicación del Abigeato:** Ningún animal podrá ser comercializado ni faenado sin que su arete RFID coincida con una transacción inmutable registrada en la blockchain por el propietario legítimo.
2. **Acceso a Mercados Premium con Certificación Verde:** Cada corte de carne beniana llevará un código QR que cualquier consumidor en Europa o Asia podrá escanear con su teléfono celular, observando en 2 segundos el mapa del predio de cría en el Beni, sus certificados de vacunación contra la fiebre aftosa y la prueba criptográfica de que fue criado en pasturas naturales de pampa sin deforestar la selva amazónica.

---

# 3. REFERENCIAS BIBLIOGRÁFICAS (Normas APA 7ma Edición)

* Antonopoulos, A. M. (2017). *Mastering Bitcoin: Programming the Open Blockchain* (2nd ed.). O'Reilly Media.
* Antonopoulos, A. M., & Wood, G. (2018). *Mastering Ethereum: Building Smart Contracts and DApps*. O'Reilly Media.
* Buterin, V., & Griffith, V. (2017). *Casper the Friendly Finality Gadget*. arXiv preprint arXiv:1710.09437. https://arxiv.org/abs/1710.09437
* Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. Bitcoin.org. https://bitcoin.org/bitcoin.pdf
* National Institute of Standards and Technology. (2015). *Secure Hash Standard (SHS)* (Federal Information Processing Standards Publication [FIPS] 180-4). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.180-4
* Szabo, N. (1994). *Smart Contracts: Formalizing and Securing Relationships on Public Networks*. First Monday, 2(9). https://doi.org/10.5210/fm.v2i9.548


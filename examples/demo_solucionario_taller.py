# -*- coding: utf-8 -*-
"""
Ejemplo de referencia: Generación de un Solucionario de Taller / Examen Práctico UFPS.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ufps_academic_studio import WorkshopSolution

ws = WorkshopSolution(
    title="SOLUCIONARIO: TALLER 4 - TECNOLOGÍA EN LA VIDA REAL",
    course="INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
    student_name="Andrés Camilo Martínez Vanegas",
    student_code="192977",
    date="Noviembre 2026",
    activity="TALLER EVALUATIVO (40%)"
)

ws.add_exercise(
    num=1,
    title="Optimización de Consultas en Bases de Datos Relacionales",
    statement="Una entidad bancaria reporta que una consulta sobre la tabla de transacciones (con 50 millones de registros) tarda 14 segundos en completarse. Proponga la solución ingenieril.",
    solution=r"""
    <p>1. <strong>Diagnóstico:</strong> La ausencia de índices sobre la columna <code>fecha_transaccion</code> y <code>cuenta_origen_id</code> obliga al motor SQL a realizar un escaneo secuencial completo (Full Table Scan) de complejidad $\mathcal{O}(n)$.</p>
    <p>2. <strong>Solución:</strong> Se crea un índice compuesto B-Tree sobre ambas columnas y se particiona la tabla por rangos mensuales:</p>
    <pre><code>CREATE INDEX idx_transacciones_cuenta_fecha ON transacciones(cuenta_origen_id, fecha_transaccion);</code></pre>
    <p>3. <strong>Resultado:</strong> El costo de ejecución cae a un index scan de $\mathcal{O}(\log n)$, reduciendo el tiempo de respuesta a 8 milisegundos.</p>
    """,
    exam_tip="En la sustentación, menciona siempre la diferencia entre un Full Table Scan y una búsqueda por índice B-Tree."
)

ws.add_exercise(
    num=2,
    title="Mitigación de Vulnerabilidades en APIs REST",
    statement="Diseñe un mecanismo defensivo para proteger un endpoint de autenticación contra ataques de fuerza bruta y DDoS distribuido.",
    solution="""
    <p>Se implementa una arquitectura de limitación de tasa (Rate Limiting) con el algoritmo Token Bucket respaldado en Redis en memoria. Cada IP tiene asignado un límite de 5 intentos por minuto. Si se excede, el API Gateway retorna inmediatamente un código HTTP <code>429 Too Many Requests</code> con cabecera <code>Retry-After: 60</code>.</p>
    """,
    exam_tip="El docente suele preguntar qué código HTTP se devuelve ante exceso de peticiones: es 429, no 403 ni 500."
)

output_pdf = "/tmp/demo_solucionario_ufps.pdf"
success = ws.render(output_pdf)
if success:
    sz = os.path.getsize(output_pdf) / 1024
    print(f"✓ Solucionario UFPS generado exitosamente: {output_pdf} ({sz:.1f} KB)")
else:
    print("✗ Error al generar el solucionario")

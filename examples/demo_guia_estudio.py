# -*- coding: utf-8 -*-
"""
Ejemplo de referencia: Generación de una Guía de Estudio Oral para Tablero UFPS.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ufps_academic_studio import StudyGuide

guide = StudyGuide(
    module_num=2,
    title="RECORRIDO EN PREORDEN (PREORDER TRAVERSAL)",
    student_name="Estudiante 2 (Andrés Martínez)",
    time_range="03:30 – 07:00 min",
    role_name="Recorridos en Profundidad",
    course="MATEMÁTICAS DISCRETAS",
    activity="EXPOSICIÓN MAGISTRAL EN TABLERO",
    subtitle="Definición formal recursiva, técnica gráfica del contorno por la izquierda y algoritmo iterativo con pilas LIFO."
)

guide.add_theory(
    "1. FUNDAMENTACIÓN MATEMÁTICA FORMAL (KENNETH ROSEN, SEC. 11.3)",
    "<p>El recorrido en preorden visita los nodos en la secuencia <strong>Raíz → Subárbol Izquierdo → Subárbol Derecho</strong>. "
    "En términos de la función recursiva formal: si el árbol está vacío, finaliza; de lo contrario, procesa la raíz $r$, "
    "luego llama recursivamente a $T_1$, y sucesivamente hasta $T_k$.</p>"
)

guide.add_blackboard_box(
    "¿QUÉ DIBUJAR EN EL TABLERO CON MARCADOR?",
    [
        "Dibuja el árbol binario de 7 nodos en el cuadrante superior izquierdo.",
        "Con marcador rojo, traza la curva de contorno bordeando el flanco izquierdo de cada nodo.",
        "Construye una tabla de 3 columnas para registrar el estado de la Pila LIFO en cada paso."
    ]
)

guide.add_speech_box(
    "GUION ORAL CRONOMETRADO (03:30 – 05:00 MIN)",
    "Buenos días, profesor y compañeros. En este módulo explicaré el recorrido en preorden. "
    "Observen cómo la técnica del contorno nos permite deducir la secuencia inmediatamente: "
    "al rodear el árbol en sentido antihorario, cada nodo es registrado en el instante exacto en que tocamos su flanco izquierdo."
)

guide.add_trap_box(
    "¿Por qué en el algoritmo iterativo se debe apilar primero el hijo derecho y luego el izquierdo?",
    "Porque la pila es una estructura LIFO (Last In, First Out). Al apilar el hijo derecho primero, "
    "el hijo izquierdo queda en el tope de la pila y será desapilado y procesado antes, respetando el orden R-I-D."
)

guide.add_trace_table(
    headers=["Paso", "Acción Realizada", "Estado de la Pila LIFO", "Salida Acumulada"],
    rows=[
        ["1", "Desapilar Raíz A", "[C, B]", "A"],
        ["2", "Desapilar B (Izquierdo)", "[C, E, D]", "A → B"],
        ["3", "Desapilar D (Hoja)", "[C, E]", "A → B → D"]
    ]
)

guide.add_transition(
    next_speaker="Estudiante 3",
    transition_text="Habiendo comprendido cómo Preorden visita la raíz antes que a sus hijos, mi compañero nos presentará el Recorrido en Inorden y su propiedad matemática en Árboles Binarios de Búsqueda."
)

output_pdf = "/tmp/demo_guia_ufps.pdf"
success = guide.render(output_pdf)
if success:
    sz = os.path.getsize(output_pdf) / 1024
    print(f"✓ Guía de estudio UFPS generada exitosamente: {output_pdf} ({sz:.1f} KB)")
else:
    print("✗ Error al generar la guía de estudio")


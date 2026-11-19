---
name: ufps-academic-studio
description: >-
  Diseño, maquetación y generación integral de documentos académicos en PDF (guías de estudio oral en tablero,
  trabajos de investigación formal en APA 7ma edición, solucionarios) y presentaciones panorámicas 16:9
  (PowerPoint PPTX con plantilla institucional UFPS, badges de orador cronometrados y diagramas técnicos vectoriales
  sin AI-slop) para la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña.
---

# UFPS Academic Studio: Suite Editorial Universitaria Versátil

`ufps-academic-studio` es el estándar y motor oficial para la generación de entregables académicos de excelencia (calificación 5.0) en la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**, específicamente en el Plan de Estudios de **Ingeniería de Sistemas** y ciencias afines.

La skill proporciona una API unificada en Python (`AcademicPaper`, `StudyGuide`, `WorkshopSolution`, `SlideDeck`, `UFPSDiagram`) que permite generar los cuatro formatos académicos fundamentales en una sola pasada, sin requerir scripts auxiliares desechables ni maquetar HTML crudo manualmente.

---

## 1. Los 4 Formatos Académicos Soportados

| Formato | Clase Python | Casos de Uso Típicos | Características Clave de Diseño |
| :--- | :--- | :--- | :--- |
| **1. Trabajo de Investigación Formal** | `AcademicPaper` | Parciales teóricos (40%), proyectos finales, papers e informes de fin de materia. | Portada institucional formal con tabla de autores y códigos UFPS en rojo, índice analítico con puntos de relleno, encabezados institucionales (`@top-left`, `@top-right`), ecuaciones numeradas `(1)`, tarjetas comparativas de 3 columnas, figuras APA 7ma y referencias con sangría francesa. |
| **2. Guía de Estudio Oral en Tablero** | `StudyGuide` | Exposiciones magistrales en tarima sin diapositivas (ej. Matemáticas Discretas). | Ficha técnica de orador y tiempo asignado, caja de pizarra (`.blackboard-box`) con instrucciones de marcador, guion oral cronometrado (`.speech-box`), batería de preguntas trampa de defensa 5.0 (`.trap-box`), tablas de traza y frase de transición entre compañeros. |
| **3. Solucionario de Taller / Examen** | `WorkshopSolution` | Solución de talleres prácticos (ej. Taller 4), guías de ejercicios matemáticos o de código. | Encabezado institucional compacto, tarjetas de ejercicios numeradas (`.exercise-box`), enunciados en recuadro neutro, desarrollo técnico paso a paso con código y cajas verdes de tips de evaluación docente. |
| **4. Presentación Panorámica 16:9** | `SlideDeck` | Sustentaciones grupales con proyección (ej. Segundo Parcial de Introducción). | Plantilla oficial UFPS de 17 diapositivas con sello Icontec/IQNET, badges de orador cronometrados (`MÓDULO XX \| ESTUDIANTE [00:00 - 03:00]`), diagramas técnicos vectoriales (4:3 / 1200x900) y cero texto blanco sobre fondos claros. |

---

## 2. Identidad Visual y Tokens Institucionales

- **Paleta Cromática Oficial:**
  - `UFPS_RED`: `#C8102E` (Rojo UFPS oficial para acentos, divisores H1, códigos de estudiante y badges).
  - `SLATE_TITLE`: `#0F172A` (Títulos principales, fondos de pizarra escolar, contraste máximo).
  - `SLATE_BODY`: `#1E293B` / `#334155` (Texto de cuerpo técnico justificado, line-height 1.48).
  - `SLATE_MUTED`: `#64748B` (Subtítulos, encabezados de pie de página, roles).
  - `BORDER_SUBTLE`: `#CBD5E1` / `#E2E8F0` (Bordes de retículas y tablas).
  - `CHALK_CYAN`: `#38BDF8` (Tiza cian en cajas de pizarra escolar).

- **Márgenes y Paginación (@page):**
  - Formato: Carta (*Letter*), márgenes de `17mm 15mm 17mm 15mm`.
  - Primera página (`@page:first`): Márgenes de `14mm`, cabeceras y pies suprimidos para la portada.
  - Páginas interiores: Encabezados automáticos y pie con `Página counter(page) de counter(pages)`.

---

## 3. Guía de Uso por Formato

### 3.1. Formato 1: Trabajo de Investigación Formal (APA 7ma Edición)
```python
from ufps_academic_studio import AcademicPaper

paper = AcademicPaper(
    title="INTELIGENCIA ARTIFICIAL Y TRANSFORMACIÓN DIGITAL",
    subtitle="Fundamentos Epistemológicos, Arquitecturas de Software y Prototipo RAG en Rust",
    activity="DOCUMENTO DE INVESTIGACIÓN · SEGUNDO PARCIAL (40%)",
    course="INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
    teacher="Docente de la Asignatura",
    date="Noviembre de 2026",
    authors=[
        {"name": "Andrés Camilo Martínez Vanegas", "role": "Líder", "code": "192977", "module": "Fundamentos e Historia"},
        {"name": "Juan Diego Antonio Sánchez Clavijo", "role": "", "code": "192969", "module": "Ecosistema Técnico (ML, Transformers)"}
    ]
)

paper.add_section("1. INTRODUCCIÓN", "<p>Texto formal...</p>")
paper.add_section("2. OBJETIVOS")
paper.add_subsection("2.1 Objetivo General", "<p>Analizar el impacto...</p>")

# Matriz comparativa de 3 fases continuas
paper.add_comparative_cards([
    {"title": "1. Digitización", "content": "<p>De analógico a binario.</p>"},
    {"title": "2. Digitalización", "content": "<p>Automatización Cloud/ERP.</p>"},
    {"title": "3. Transformación", "content": "<p>Decisiones con IA en tiempo real.</p>"}
])

# Ecuaciones centradas con numeración correlativa
paper.add_equation("Attention(Q, K, V) = softmax ( \\frac{Q \\cdot K^T}{\\sqrt{d_k}} ) \\cdot V", num=1)

# Referencias con sangría francesa estricta
paper.add_references([
    "Russell, S. J., & Norvig, P. (2020). <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson.",
    "Universidad Francisco de Paula Santander [UFPS]. (2019). <em>Acuerdo No. 051 de 2019</em>. Consejo Superior."
])

paper.render("00_TRABAJO_ESCRITO.pdf")
```

---

### 3.2. Formato 2: Guía Individual de Estudio Oral para Tablero
```python
from ufps_academic_studio import StudyGuide

guide = StudyGuide(
    module_num=2,
    title="RECORRIDO EN PREORDEN (PREORDER TRAVERSAL)",
    student_name="Estudiante 2 (Andrés Martínez)",
    time_range="03:30 – 07:00 min",
    role_name="Recorridos en Profundidad",
    course="MATEMÁTICAS DISCRETAS",
    activity="EXPOSICIÓN MAGISTRAL EN TABLERO",
    subtitle="Definición formal recursiva, técnica gráfica del contorno por la izquierda y algoritmo con pilas LIFO."
)

guide.add_theory(
    "1. FUNDAMENTACIÓN MATEMÁTICA (KENNETH ROSEN, SEC. 11.3)",
    "<p>El recorrido en preorden visita los nodos en la secuencia <strong>Raíz → Izquierdo → Derecho</strong>.</p>"
)

# Qué dibujar con marcador en la pizarra
guide.add_blackboard_box(
    "¿QUÉ DIBUJAR EN EL TABLERO CON MARCADOR?",
    [
        "Traza el árbol binario de 7 nodos en el cuadrante superior izquierdo.",
        "Con marcador rojo, traza la curva de contorno por el flanco izquierdo de cada nodo.",
        "Dibuja la tabla de seguimiento de la Pila LIFO."
    ]
)

# Guion oral cronometrado
guide.add_speech_box(
    "GUION ORAL (03:30 – 05:00 MIN)",
    "Buenos días, profesor y compañeros. En este módulo explicaré el recorrido en preorden..."
)

# Pregunta trampa y respuesta 5.0
guide.add_trap_box(
    "¿Por qué se apila primero el hijo derecho y luego el izquierdo?",
    "Porque la pila es LIFO; al apilar el derecho primero, el izquierdo queda en el tope y se procesa antes."
)

guide.add_transition(
    next_speaker="Estudiante 3",
    transition_text="Cedo la palabra a mi compañero para explicar el recorrido en Inorden."
)

guide.render("02_Guia_Preorden.pdf")
```

---

### 3.3. Formato 3: Solucionario de Taller / Examen Práctico
```python
from ufps_academic_studio import WorkshopSolution

ws = WorkshopSolution(
    title="SOLUCIONARIO: TALLER 4 - TECNOLOGÍA EN LA VIDA REAL",
    course="INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
    student_name="Andrés Camilo Martínez Vanegas",
    student_code="192977"
)

ws.add_exercise(
    num=1,
    title="Optimización de Consultas en Bases de Datos",
    statement="Una consulta sobre 50 millones de registros tarda 14 segundos. Proponga la solución.",
    solution="<p>Se implementa un índice compuesto B-Tree y particionamiento mensual, reduciendo el costo a 8 ms.</p>",
    exam_tip="Explica en sustentación la diferencia entre Full Table Scan y búsqueda por índice B-Tree."
)

ws.render("Taller_4_Solucion.pdf")
```

---

### 3.4. Formato 4: Presentación Panorámica 16:9 (PPTX)
```python
from ufps_academic_studio import SlideDeck, UFPSDiagram

# Diagrama vectorial limpio sin AI-slop
UFPSDiagram.flow(
    title="PIPELINE DE MLOPS EN PRODUCCIÓN",
    steps=[
        {"title": "DataOps", "desc": "Ingesta y validación de esquemas", "color": "#C8102E"},
        {"title": "ModelOps", "desc": "Entrenamiento distribuido y tracking", "color": "#38BDF8"},
        {"title": "DevOps", "desc": "Despliegue Canary y monitoreo", "color": "#4ADE80"}
    ],
    output_png="assets/mlops_flow.png"
)

# Presentación
deck = SlideDeck(title="Segundo Parcial: IA y Transformación Digital")
deck.add_slide(
    title="Pipeline de MLOps en Producción",
    subtitle="Orquestación integral de arquitecturas cognitivas",
    speaker="Juan David Pérez",
    time_range="06:00 - 09:00",
    module_num=3,
    bullets=[
        "Automatización integral de ingeniería de características.",
        "Monitoreo continuo de Data Drift y Concept Drift en la nube."
    ],
    diagram_image_path="assets/mlops_flow.png"
)
deck.save("Presentacion_Final.pptx")
```

---

## 4. Checklist Editorial (Zero-Slop & Zero-Gap)

1. **Cero Páginas en Blanco Intermedias:** Todos los componentes atómicos (`.card`, `.blackboard-box`, `.trap-box`, `.comparative-grid-3`, tablas) utilizan `break-inside: avoid !important`.
2. **Cero Encabezados Solos:** Los títulos (`h1`, `h2`, `h3`, `h4`) llevan `break-after: avoid !important`.
3. **Contraste 100% Accesible:** Prohibido el texto blanco sobre fondos claros; los textos sobre fondos oscuros usan blanco puro o tiza cian (`#38BDF8`).
4. **Cero Ilustraciones IA Alucinadas:** Los gráficos de diapositivas e informes son diagramas vectoriales limpios (4:3 o 16:9) generados con `UFPSDiagram`.

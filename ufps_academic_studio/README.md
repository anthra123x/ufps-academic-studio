# Paquete Nativo UFPS Academic Studio (ufps_academic_studio)

## 1. Proposito y alcance
El paquete `ufps_academic_studio` es el nucleo programatico en Python de la suite editorial. Proporciona una interfaz orientada a objetos de alto nivel para que el agente y los desarrolladores generen documentos academicos institucionales en PDF y presentaciones PPTX 16:9 en una sola pasada, sin requerir scripts auxiliares desechables ni maquetar HTML de forma manual. Implementa los 4 formatos fundamentales de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña: trabajos de investigacion formal (APA 7ma edicion), guias de estudio oral en tablero, solucionarios tecnicos y diapositivas panoramicas.

## 2. Contratos y API

### Exportaciones Principales (`__init__.py`)
- `AcademicPaper`: Clase para maquetacion de papers, monografias e informes de investigacion formal de 10 a 20 paginas con portada institucional, indice analitico, reticulas comparativas y bibliografia APA.
- `StudyGuide`: Clase para generacion de guias individuales de preparacion oral en tablero escolar (sin diapositivas), con fichas tecnicas, cajas de pizarra, guiones cronometrados y preguntas trampa de calificacion 5.0.
- `WorkshopSolution`: Clase para elaboracion de solucionarios tecnicos de talleres y examenes practicos con tarjetas de ejercicios, enunciados neutros y recomendaciones de evaluacion docente.
- `SlideDeck`: Clase para construccion de presentaciones panoramicas 16:9 basadas en la plantilla institucional de 17 diapositivas UFPS Seccional Ocaña con sellos Icontec/IQNET y badges de orador.
- `UFPSDiagram`: Generador de diagramas vectoriales limpios (flujo, matriz, arquitectura) en resolucion 1200x900 px (4:3) para erradicar imagenes sinteticas alucinadas (Zero AI-Slop).
- `compile_pdf(html_content, output_path, css_extra="")`: Funcion de compilacion headless directa a traves de Chromium/Brave o WeasyPrint.

### Modulo `core/`
- `core.compiler.compile_html_to_pdf(html_content: str, output_path: str, css_extra: str = "") -> bool`:
  Compila HTML a PDF inyectando estilos base institucionales mediante navegadores Chromium/Brave Headless con banderas de impresion de precision (`--no-pdf-header-footer`, `--run-all-compositor-stages-before-draw`).
- `core.diagrams.UFPSDiagram`:
  - `flow(title: str, steps: list, output_png: str) -> str`: Genera diagramas horizontales de proceso/pipeline.
  - `matrix(title: str, items: list, output_png: str) -> str`: Genera matrices tecnicas en cuadricula de alta densidad.
- `core.tokens`:
  Define tokens constantes: `UFPS_RED`, `UFPS_RED_ALT`, `SLATE_TITLE`, `SLATE_BODY`, `SLATE_MUTED`, `BORDER_SUBTLE`, `CHALK_CYAN`, `BG_BLACKBOARD`, `BG_CARD`, `BG_ALERT`, `BG_EXCELLENCE`.

### Modulo `formats/`
- `formats.paper.AcademicPaper(title, subtitle, activity, course, teacher, date, authors)`:
  - `add_section(title, content="")`
  - `add_subsection(title, content="")`
  - `add_paragraph(text)`
  - `add_comparative_cards(cards: list)`
  - `add_equation(latex_code: str, num: int)`
  - `add_table(headers: list, rows: list, caption: str)`
  - `add_figure(image_path: str, caption: str, note: str)`
  - `add_references(references: list)`
  - `render(output_path: str)`
- `formats.guide.StudyGuide(module_num, title, student_name, time_range, role_name, course, activity, subtitle)`:
  - `add_theory(title, content)`
  - `add_blackboard_box(title, instructions: list)`
  - `add_speech_box(title, text)`
  - `add_trap_box(question, answer_5_0)`
  - `add_transition(next_speaker, transition_text)`
  - `render(output_path: str)`
- `formats.workshop.WorkshopSolution(title, course, student_name, student_code, subtitle)`:
  - `add_exercise(num, title, statement, solution, exam_tip)`
  - `render(output_path: str)`
- `formats.presentation.SlideDeck(title, template_pptx)`:
  - `add_slide(title, subtitle, speaker, time_range, module_num, bullets, diagram_image_path)`
  - `save(output_path: str)`

## 3. Dependencias
- Internas: Utiliza las hojas de estilo institucionales de `styles/ufps_base.css` y la plantilla base `templates/ufps_panoramica_base.pptx`.
- Externas de sistema:
  - Python 3.8+ (`subprocess`, `tempfile`, `pathlib`, `zipfile`, `xml.etree.ElementTree`).
  - Navegador basado en Chromium (`brave`, `chromium`, `google-chrome`) para renderizado PDF y generacion de diagramas matriciales.

## 4. Mapa de archivos
- `ufps_academic_studio/__init__.py`: Punto de entrada del paquete; exporta las clases de formato, diagramas y compilacion.
- `ufps_academic_studio/core/compiler.py`: Abstraccion del motor de renderizado HTML a PDF sin dependencias de servidor.
- `ufps_academic_studio/core/diagrams.py`: Motor vectorial de generacion de diagramas limpios de ingenieria (Zero AI-Slop).
- `ufps_academic_studio/core/tokens.py`: Definicion canonica de colores institucionales y geometria de impresion.
- `ufps_academic_studio/formats/paper.py`: Implementacion de la clase `AcademicPaper` para trabajos formales APA 7ma edicion.
- `ufps_academic_studio/formats/guide.py`: Implementacion de la clase `StudyGuide` para guias individuales de exposicion oral en pizarra.
- `ufps_academic_studio/formats/workshop.py`: Implementacion de la clase `WorkshopSolution` para solucionarios de talleres y examenes.
- `ufps_academic_studio/formats/presentation.py`: Implementacion de la clase `SlideDeck` para manipulacion OpenXML de diapositivas 16:9.
- `ufps_academic_studio/styles/ufps_base.css`: Hoja de estilo maestra compilada con todas las directivas de paginacion `@page`, reglas de corte estricto `break-inside: avoid` y componentes semanticos institucionales.

## 5. Logica y flujo
1. **Instanciacion**: El agente instancia la clase correspondiente al entregable requerido (`AcademicPaper`, `StudyGuide`, `WorkshopSolution` o `SlideDeck`).
2. **Construccion Semantica**: Se anaden secciones, bloques comparativos, tablas de traza o cajas de pizarra mediante llamadas sucesivas a la API fluida de la clase.
3. **Inyeccion de Estilos Base**: Al llamar al metodo `render()`, la clase consolida el marcado semantico dentro del esqueleto HTML institucional, acoplando `styles/ufps_base.css`.
4. **Compilacion Headless**: `core.compiler` guarda el HTML en memoria temporal y orquesta el navegador Chromium en modo headless con directivas `--no-pdf-header-footer` y `--run-all-compositor-stages-before-draw`, produciendo el PDF final en una sola ejecucion.
5. **Limpieza Autonoma**: Los archivos intermedios temporales son eliminados inmediatamente al finalizar la compilacion.

## 6. Decisiones de diseno y gotchas
- **Cero archivos intermedios huerfanos**: El paquete genera y destruye los archivos temporales de forma transparente con `tempfile.NamedTemporaryFile`, manteniendo limpios los espacios de trabajo.
- **Disciplina estricta de saltos de pagina**: No se debe aplicar `break-inside: avoid` a contenedores globales extensos (como el `body` o secciones completas), sino exclusivamente a componentes atomicos (`.card`, `.blackboard-box`, `.trap-box`, `.comparative-grid-3`, `tr`, `pre`). Los encabezados (`h1`, `h2`, `h3`, `h4`) llevan siempre `break-after: avoid !important`.
- **Ecuaciones en crudo**: Al incluir notacion matematica o codigo en expresiones regulares, deben emplearse cadenas crudas (`r"..."`) en Python para evitar advertencias de escape `SyntaxWarning`.

## 7. Estado y ultimos cambios
- Creacion del paquete unificado `ufps_academic_studio` con modularizacion en `core`, `formats` y `styles`.
- Integracion del patron de diseno exacto del documento maestro de 17 paginas (`AcademicPaper`).
- Implementacion de `StudyGuide` con soporte para fichas tecnicas, cajas de pizarra escolar y preguntas trampa.
- Implementacion de `WorkshopSolution` para talleres practicos con enunciados compactos y tips docentes.
- Implementacion de `SlideDeck` con control de contrastes OpenXML y badges de orador cronometrados.

## 8. Como verificar
Ejecutar la validacion de sintaxis y los scripts de prueba en `examples/`:
```bash
python3 -m py_compile ufps_academic_studio/*.py ufps_academic_studio/core/*.py ufps_academic_studio/formats/*.py
python3 -c "import ufps_academic_studio; print('Paquete importado exitosamente')"
```


# Modulo de Plantillas Editoriales (templates)

## 1. Proposito y alcance
El modulo `templates` centraliza las estructuras base para documentos academicos impresos y presentaciones digitales institucionales. Define el modelo de cajas CSS Paged Media para guias de estudio oral y trabajos formales bajo estandares APA 7ma edicion, asi como la plantilla OpenXML base en proporcion panorámica 16:9 con acreditaciones de calidad Icontec e IQNET.

## 2. Contratos y API

### `common_styles.css`
- Regla de impresion: `@page { size: letter; margin: 18mm 16mm 18mm 16mm; }`
- Encabezados dinamicos:
  - `@top-left`: Denominacion institucional UFPS Seccional Ocaña.
  - `@top-right`: Asignatura y evaluacion mediante variable `--doc-header-right`.
  - `@bottom-left`: Titulo del modulo mediante variable `--doc-footer-left`.
  - `@bottom-right`: Numeracion formal con funcion `counter(page)` de `counter(pages)`.
- Clases componentes: `.header-badge`, `.doc-title`, `.doc-subtitle`, `.meta-grid`, `.meta-col`, `.blackboard-box`, `.speech-box`, `.trap-box`, `.trace-table`, `.apa-reference`, `.formula-box`.

### `research_paper.html`
- Variables de sustitucion de plantilla:
  - `{{ title }}`: Titulo del informe.
  - `{{ common_css }}`: Contenido inyectado de `common_styles.css`.
  - `{{ authors }}`: Lista estructurada de autores.
  - `{{ professor }}`: Nombre del docente titular.
  - `{{ date }}`: Fecha de emision academica.
  - `{{ table_of_contents }}`: Indice sincronizado.
  - `{{ content_body }}`: Cuerpo del informe academico.

### `study_guide.html`
- Variables de sustitucion de plantilla:
  - `{{ mod_num }}`: Numero ordinal de modulo.
  - `{{ role_name }}`: Rol especifico asignado en la defensa.
  - `{{ main_title }}`: Titulo tematico del modulo.
  - `{{ sub_title }}`: Subtitulo o eje de competencia.
  - `{{ student_name }}`: Nombre del estudiante evaluado.
  - `{{ time_range }}`: Intervalo cronometrado en minutos y segundos.
  - `{{ content_body }}`: Secciones de pizarra, guion y preguntas trampa.

### `ufps_panoramica_base.pptx`
- Geometria OpenXML:
  - Ancho de diapositiva: 12192000 EMUs (13.333 pulgadas).
  - Alto de diapositiva: 6858000 EMUs (7.5 pulgadas).
  - Proporcion: Widescreen 16:9.
  - Logotipo UFPS Seccional Ocaña integrado con acreditacion en pie de diapositiva.

## 3. Dependencias
- Internas: Consumido por `scripts/compile_pdf.py` y `scripts/pptx_engine.py`.
- Recursos estaticos: `assets/logo_ufpso.png` y `assets/logo_ufps.png` vinculados relativamente en los documentos HTML.
- Externas: Motores de renderizado CSS compatibles con Paged Media Module Level 3 (Brave, Chromium, WeasyPrint).

## 4. Mapa de archivos
- `templates/common_styles.css`: Hoja de estilos universal con tipografia de sistema, paleta institucional y definiciones de impresion `@page`.
- `templates/study_guide.html`: Plantilla semantica HTML para guias de sustentacion oral en tablero sin diapositivas.
- `templates/research_paper.html`: Plantilla HTML para articulos, monografias e informes de investigacion formal con portada institucional y tabla de contenido en dos fases.
- `templates/ufps_panoramica_base.pptx`: Presentacion maestra OpenXML de 17 diapositivas con maquetacion institucional UFPS.

## 5. Logica y flujo
1. El usuario o agente selecciona la plantilla segun el tipo de entrega (PDF de guia oral, PDF formal APA o presentacion PPTX).
2. Se inyecta el contenido contextual en los marcadores de sustitucion.
3. Para documentos PDF, `compile_pdf.py` procesa el marcado aplicando `common_styles.css`. Las directivas `page-break-inside: avoid` protegen las cajas didacticas de divisiones huerfanas entre paginas.
4. Para diapositivas, `pptx_engine.py` lee `ufps_panoramica_base.pptx`, modifica los nodos XML de texto e inserta los diagramas vectoriales generados.

## 6. Decisiones de diseno y gotchas
- **Evitacion de saltos de pagina inadecuados**: Todos los bloques didacticos (`.blackboard-box`, `.trap-box`, `.trace-table`) implementan `break-inside: avoid; page-break-inside: avoid;` para garantizar que ninguna tabla o caja tecnica se corte en dos hojas.
- **Tipografia de sistema**: Se utiliza una pila de fuentes sin serifa de alta legibilidad (`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`) para evitar fallos de renderizado de fuentes web en entornos sin conexion a internet.

## 7. Estado y ultimos cambios
- Normalizacion de estilos Paged Media `@page` para compatibilidad dual Chromium/WeasyPrint.
- Integracion de la plantilla maestra panorámica 16:9 con acreditacion institucional.

## 8. Como verificar
Inspeccionar integridad de la plantilla PPTX y validar la sintaxis CSS:
```bash
python3 -c "import zipfile; z = zipfile.ZipFile('templates/ufps_panoramica_base.pptx'); print('Archivos en PPTX:', len(z.namelist()))"
test -f templates/common_styles.css && echo "common_styles.css presente y accesible"
```


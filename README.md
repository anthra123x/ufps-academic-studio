# UFPS Academic Studio

Ecosistema editorial y suite de automatizacion tecnica para el diseno, maquetacion y generacion programatica de documentos academicos en formato PDF (guias de sustentacion oral en tablero, articulos de investigacion formal bajo normas APA 7ma edicion, solucionarios) y presentaciones panoramicas 16:9 en Microsoft PowerPoint (OpenXML) con identidad visual institucional de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña.

---

## 1. Descripcion General y Arquitectura

UFPS Academic Studio articula un conjunto de especificaciones normativas, hojas de estilo CSS Paged Media, esquemas de diseno estructurados y utilidades nativas en Python 3 para producir artefactos academicos de alta fidelidad. El sistema esta optimizado para ejecucion desatendida en entornos Linux y como skill para agentes autonomos Antigravity, eliminando por completo la dependencia de suites ofimaticas propietarias y erradicando artefactos graficos generados por modelos difusivos de inteligencia artificial («AI-slop»).

```
+-----------------------------------------------------------------------------------+
|                            UFPS ACADEMIC STUDIO                                   |
+-----------------------------------------------------------------------------------+
|  ENTRADAS DE CONTENIDO           SISTEMA DE DISENO             MOTORES TECNICOS   |
|  - Guiones orales y tableros     - references/DESIGN_SYSTEM.md - compile_pdf.py   |
|  - Articulos y monografias APA   - references/design_tokens.json- pptx_engine.py  |
|  - Diagramas de ingenieria       - scripts/design_tokens.py    - diagram_generator|
+---------------------------------+-----------------------------+-------------------+
                                  |
                                  v
+-----------------------------------------------------------------------------------+
|                           PROCESAMIENTO Y COMPILACION                             |
|  - Resolucion CSS Paged Media Level 3 (@page) via Chromium Headless / WeasyPrint  |
|  - Manipulacion DOM XML directa sobre paquetes PresentationML (DrawingML)         |
|  - Renderizado vectorial de diagramas CSS Grid a PNG 1200x900 px                  |
+-----------------------------------------------------------------------------------+
                                  |
                                  v
+-----------------------------------------------------------------------------------+
|                           ARTEFACTOS DE SALIDA FORMAL                             |
|  - Documentos PDF Carta con cabeceras institucionales y proteccion de saltos      |
|  - Presentaciones PPTX 16:9 con badges de orador cronometrados y sellos Icontec   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Mapa de Modulos

De acuerdo con las politicas de organizacion del repositorio, cada componente funcional dispone de su documentacion tecnica local:

| Modulo | Ruta en Workspace | Responsabilidad Tecnica | Documentacion Local |
| :--- | :--- | :--- | :--- |
| **Scripts** | `scripts/` | Motores ejecutables en Python para compilacion PDF, procesamiento OpenXML y renderizado de diagramas. | [scripts/README.md](file:///home/omicron/Documentos/ufps-academic-studio/scripts/README.md) |
| **Plantillas** | `templates/` | Plantillas base HTML, CSS Paged Media y archivo maestro OpenXML PPTX en proporcion 16:9. | [templates/README.md](file:///home/omicron/Documentos/ufps-academic-studio/templates/README.md) |
| **Referencias** | `references/` | Especificaciones normativas de identidad institucional, manual de diseno y tokens JSON. | [references/README.md](file:///home/omicron/Documentos/ufps-academic-studio/references/README.md) |
| **Recursos Graficos** | `assets/` | Logotipos institucionales vectoriales y matriciales de la UFPS Seccional Ocaña con canal alfa. | [assets/README.md](file:///home/omicron/Documentos/ufps-academic-studio/assets/README.md) |

---

## 3. Identidad Institucional y Tokens de Diseno

El sistema aplica de manera estricta los lineamientos de acreditacion institucional de la UFPS Seccional Ocaña. Los valores son consumidos desde `references/design_tokens.json` y `scripts/design_tokens.py`.

### 3.1. Paleta Cromatica Estandar

| Token | Variable / Clave | Valor Hexadecimal | Definicion Funcional |
| :--- | :--- | :---: | :--- |
| **UFPS Red** | `UFPS_RED` | `#C8102E` | Rojo institucional primario (Pantone 186 C). Acentos, separadores, distintivos. |
| **UFPS Red Alt** | `UFPS_RED_ALT` | `#CC0000` | Variante de alto contraste para fondos oscuros o elementos de impacto. |
| **Slate Title** | `SLATE_TITLE` | `#0F172A` | Azul pizarra profundo. Tipografia de maxima jerarquia (H1) y fondo de tableros. |
| **Slate Body** | `SLATE_BODY` | `#1E293B` | Gris azulado oscuro. Cuerpo de texto tecnico, parrafos y celdas de tablas. |
| **Slate Muted** | `SLATE_MUTED` | `#64748B` | Gris intermedio. Metadatos, subtitulos, marcas de tiempo y notas al pie. |
| **Border Subtle** | `BORDER_SUBTLE`| `#CBD5E1` | Gris claro neutro. Reticulas de tablas y delimitadores de seccion. |
| **Card Background**| `BG_CARD` | `#F8FAFC` | Fondo para tarjetas de conceptos tecnicos y cajas de guion oral. |
| **Blackboard Background** | `BG_BLACKBOARD` | `#0F172A` | Fondo simulador de pizarra escolar oscura para explicaciones graficas. |
| **Chalk Cyan** | `BORDER_CHALK` | `#38BDF8` | Cian brillante para destacar trazos simulados de marcador o tiza. |
| **Alert Background** | `BG_ALERT` | `#FEF2F2` | Fondo de cajas de contingencia, objeciones docentes y preguntas trampa. |
| **Alert Border** | `BORDER_ALERT` | `#EF4444` | Borde de advertencia para puntos criticos de evaluacion individual. |
| **Success Background** | `BG_SUCCESS` | `#F0FDF4` | Indicador de respuesta definitiva de maxima calificacion (5.0). |

### 3.2. Pila Tipografica Institucional
- Pila de Interfaz y Documentos: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- Pila de Codigo y Traza Algoritmica: `ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, monospace`

---

## 4. Componentes y Motores de Automatizacion

### 4.1. Compilador de Documentos PDF (`scripts/compile_pdf.py`)
Compila documentos HTML estructurados hacia formato PDF utilizando el estandar CSS Paged Media Module Level 3.
- **Deteccion Automatica de Navegadores**: Localiza binarios instalados en el sistema en el orden: `brave`, `brave-browser`, `chromium`, `chromium-browser`, `google-chrome`, `google-chrome-stable`.
- **Modo de Impresion de Precision**: Ejecuta el motor Chromium con las banderas tecnicas:
  - `--headless`: Operacion desatendida sin servidor de despliegue grafico X11.
  - `--disable-gpu`: Estabilidad en contenedores y servidores virtuales.
  - `--run-all-compositor-stages-before-draw`: Garantiza la finalizacion del layout y evaluacion CSS antes de la rasterizacion.
  - `--no-pdf-header-footer`: Suprime la inyeccion de marcas de agua por defecto del navegador (URLs, fecha y hora).
  - `--print-to-pdf`: Exportacion directa a flujo vectorial PDF.
- **Mecanismo de Respaldo**: En caso de no contar con un navegador basado en Chromium o especificarse explicitamente, el script conmuta a WeasyPrint mediante su API en Python o CLI.

### 4.2. Motor de Diapositivas OpenXML (`scripts/pptx_engine.py`)
Permite crear y modificar presentaciones PowerPoint widescreen (16:9) sobre la plantilla oficial `templates/ufps_panoramica_base.pptx` sin dependencias externas pesadas, operando directamente sobre la especificacion ECMA-376 (OpenXML).
- **Dimensiones Exactas en EMUs (English Metric Units)**:
  - Ancho de Diapositiva: `12192000` EMUs ($12192000 / 914400 = 13.333$ pulgadas).
  - Alto de Diapositiva: `6858000` EMUs ($6858000 / 914400 = 7.500$ pulgadas).
- **Validacion de Contraste**: Analiza los nodos `a:rPr` y `a:solidFill` del arbol DrawingML para certificar que ningun texto con valor `#FFFFFF` se ubique sobre fondos claros, asegurando legibilidad en proyectores de aula.
- **Estructura de Badges de Orador**: Inyecta distintivos superiores que ordenan las intervenciones de los estudiantes:
  ```
  MODULO [XX] | [NOMBRE DEL ESTUDIANTE] [[MM:SS] - [MM:SS]]
  ```

### 4.3. Generador de Diagramas Vectoriales de Ingenieria (`scripts/diagram_generator.py`)
Erradica la dependencia de imagenes generadas por IA que introducen textos ilegibles o esquemas ficticios.
- Transforma marcado semantico HTML5 y CSS Grid en diagramas tecnicos de resolucion 1200x900 px (proporcion 4:3 para insercion lateral en diapositivas 16:9).
- Emplea fondos pizarra `#0F172A` con acentos cian `#38BDF8` y rojo `#C8102E`, generando diagramas reproducibles de arquitecturas, flujos de datos y estructuras de algoritmos.

---

## 5. Plantillas Editoriales

### 5.1. `templates/common_styles.css`
Contiene las definiciones de impresion universales:
- Dimension de pagina: Carta (`letter`) con margenes de `18mm 16mm 18mm 16mm`.
- Encabezados fijos en `@page`:
  - `@top-left`: Denominacion formal de la universidad y plan de estudios.
  - `@top-right`: Asignatura y periodo academico.
  - `@bottom-left`: Nombre especifico del documento o modulo.
  - `@bottom-right`: Numeracion sincronizada mediante `counter(page)` de `counter(pages)`.
- Clases de cajas didacticas:
  - `.blackboard-box`: Caja de pizarra con borde cian para instrucciones de dibujo en tablero.
  - `.speech-box`: Caja con franja lateral roja para transcripcion textual del guion oral segundo a segundo.
  - `.trap-box`: Caja de advertencia para preguntas de evaluacion compleja docente y sus respuestas de 5.0.
  - `.trace-table`: Tabla de trazabilidad de algoritmos con cabecera oscura y filas alternas.

### 5.2. `templates/study_guide.html`
Estructura semantica para guias de preparacion de sustentacion individual en tablero, optimizada para exposiciones directas sin apoyo de diapositivas.

### 5.3. `templates/research_paper.html`
Plantilla para documentos de investigacion formal conforme a normas APA 7ma edicion, incluyendo portada institucional con escudo oficial, indice general y tablas de contenido estructuradas.

### 5.4. `templates/ufps_panoramica_base.pptx`
Archivo maestro OpenXML con 17 diapositivas preconfiguradas, respetando el escudo a color UFPS en la esquina superior derecha (`x=9454331, y=314675, cx=2405046, cy=650058`) y la acreditacion de calidad institucional en el pie.

---

## 6. Instalacion y Uso

### 6.1. Requisitos del Sistema
- Sistema Operativo: Linux (x86_64 / aarch64).
- Python: Version 3.8 o superior.
- Navegador: Chromium, Brave o Google Chrome disponible en el `PATH`.
- Utilidades opcionales: `poppler-utils` (para comando `pdfinfo`), `weasyprint`.

### 6.2. Vinculacion como Skill de Antigravity
Para que el agente reconozca automaticamente la suite editorial en cualquier espacio de trabajo:

```bash
mkdir -p "$HOME/.gemini/config/skills"
ln -sf "/home/omicron/Documentos/ufps-academic-studio" "$HOME/.gemini/config/skills/ufps-academic-studio"
```

### 6.3. Compilacion de Documentos PDF

```bash
# Compilacion automatica (preferencia Chromium)
python3 scripts/compile_pdf.py entrada.html salida.pdf

# Compilacion forzando motor WeasyPrint
python3 scripts/compile_pdf.py entrada.html salida.pdf weasyprint
```

### 6.4. Generacion de Diagramas Tecnicos

```bash
python3 scripts/diagram_generator.py diagrama.html assets/diagrama_red.png 1200 900
```

### 6.5. Validacion e Inspeccion de Diapositivas PPTX

```bash
python3 scripts/pptx_engine.py templates/ufps_panoramica_base.pptx
```

---

## 7. Protocolos de Verificacion Pre-Entrega

Antes de consolidar o publicar cualquier entrega academica, deben ejecutarse las siguientes comprobaciones tecnicas:

1. **Documentos PDF**:
   - Ejecutar `pdfinfo salida.pdf` para auditar el conteo de paginas y confirmar ausencia de paginas finales en blanco.
   - Certificar que todos los encabezados posean la regla CSS `page-break-after: avoid;`.
   - Certificar que las cajas didacticas (`.blackboard-box`, `.trap-box`, `.trace-table`) posean `page-break-inside: avoid;` para prevenir divisiones inadecuadas entre hojas.
2. **Presentaciones PPTX**:
   - Comprobar que no existan cuadros de texto con fuentes blancas sobre fondo blanco o contenedores claros.
   - Comprobar que no existan directivas de recorte forzado `a:srcRect` que mutilen los diagramas integrados.
   - Asegurar que ningun elemento textual ocupe las coordenadas reservadas para el escudo UFPS y la acreditacion Icontec.

---

## 8. Licencia y Creditos

Desarrollado para la comunidad academica de la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**, Facultad de Ingenieria, Plan de Estudios de Ingenieria de Sistemas.

Los recursos graficos institucionales pertenecen a sus respectivos titulares y su uso esta reservado para fines academicos e investigativos.

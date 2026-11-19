# Skill Antigravity: UFPS Academic Studio

Skill técnica y suite editorial especializada para agentes de inteligencia artificial en el ecosistema Google Antigravity (App, CLI e IDE). Esta skill capacita al agente para asumir el rol de arquitecto editorial universitario, automatizando el diseño, maquetación y generación programática de **documentos académicos en PDF** (guías de sustentación oral en tablero, trabajos de investigación formal bajo normas APA 7ma edición, solucionarios técnicos) y **presentaciones panorámicas 16:9 en Microsoft PowerPoint (OpenXML)** con la identidad visual institucional y estándares de acreditación de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña.

---

## 1. Ficha Técnica de la Skill

| Parámetro | Definición Técnica |
| :--- | :--- |
| **Identificador (Skill Name)** | `ufps-academic-studio` |
| **Manifiesto de Instrucciones** | [SKILL.md](file:///home/omicron/Documentos/ufps-academic-studio/SKILL.md) |
| **Ecosistema Compatible** | Google Antigravity (App, CLI, IDE), agentes autónomos basados en LLM |
| **Rol Asumido por el Agente** | Especialista Editorial Académico / Ingeniero de Maquetación Institucional |
| **Área Disciplinar Primaria** | Facultad de Ingeniería, Plan de Estudios de Ingeniería de Sistemas |
| **Formatos de Salida** | PDF Carta (CSS Paged Media Level 3), PPTX Widescreen 16:9 (OpenXML nativo) |
| **Dependencias del Agente** | Python 3.8+, binario de navegación Chromium/Brave Headless |

---

## 2. Criterios de Activación de la Skill (Triggers)

El agente Antigravity activa esta skill de manera autónoma cuando el usuario introduce consultas relacionadas con:

1. **Documentación Académica Impresa y Digital en PDF:**
   - Elaboración de guías de preparación individual para defensas orales en tablero sin diapositivas.
   - Redacción de monografías, informes técnicos y artículos de investigación bajo normas APA 7ma edición.
   - Maquetación de solucionarios de exámenes prácticos y talleres (algoritmia, estructuras de datos, matemáticas discretas, redes).
2. **Presentaciones Institucionales en Diapositivas (PPTX 16:9):**
   - Diapositivas en formato panorámico utilizando la plantilla oficial UFPS Seccional Ocaña con sellos Icontec e IQNET.
   - Inclusión de distintivos de orador cronometrados (*Speaker Badges*) para coordinar intervenciones grupales.
   - Generación de diagramas vectoriales de ingeniería en alta definición (1200x900 px) bajo la directiva «Zero AI-Slop» (sustitución estricta de imágenes deformadas generadas por IA).

---

## 3. Instalación y Descubrimiento en Antigravity

Para habilitar la skill en el entorno global del usuario o en un espacio de trabajo específico:

### 3.1. Instalación Global (Recomendada)
Permite que cualquier sesión o ventana de Antigravity reconozca la skill automáticamente:

```bash
mkdir -p "$HOME/.gemini/config/skills"
ln -sf "/home/omicron/Documentos/ufps-academic-studio" "$HOME/.gemini/config/skills/ufps-academic-studio"
```

### 3.2. Instalación en Espacio de Trabajo
Para proyectos específicos que gestionan sus propias directivas de agente:

```bash
mkdir -p .gemini/skills
ln -sf "/home/omicron/Documentos/ufps-academic-studio" ".gemini/skills/ufps-academic-studio"
```

---

## 4. Protocolo Operativo del Agente (Agent Workflow)

Cuando la skill es activada, el agente ejecuta el siguiente flujo determinista:

```
+-----------------------------------------------------------------------------------+
|                        PROTOCOLO OPERATIVO DEL AGENTE                             |
+-----------------------------------------------------------------------------------+
|  1. CLASIFICACION DEL ARTEFACTO                                                   |
|     - Evaluar si la entrega es Documento PDF o Presentacion PPTX                  |
|     - Consultar variables institucionales en references/design_tokens.json        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  2. MAQUETACION SEGUN PLANTILLA                                                   |
|     - PDF Guia Oral: templates/study_guide.html + common_styles.css               |
|     - PDF Investigacion APA: templates/research_paper.html + common_styles.css    |
|     - PPTX Panoramica: templates/ufps_panoramica_base.pptx                        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  3. COMPOSICION VECTORIAL TECNICA (ZERO AI-SLOP)                                  |
|     - Prohibido solicitar o generar imagenes generativas alucinadas              |
|     - Compilar diagramas HTML/CSS Grid via scripts/diagram_generator.py (4:3)    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  4. PROCESAMIENTO Y COMPILACION                                                   |
|     - Documentos PDF: scripts/compile_pdf.py (Chromium Headless / WeasyPrint)     |
|     - Presentaciones: scripts/pptx_engine.py (Manipulacion OpenXML directa)       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  5. AUDITORIA PRE-ENTREGA                                                         |
|     - PDF: Verificar recuento con pdfinfo y proteccion de saltos de pagina        |
|     - PPTX: Certificar ausencia de texto blanco sobre fondo blanco (contraste)    |
+-----------------------------------------------------------------------------------+
```

---

## 5. Mapa de Módulos del Repositorio

Estructura interna de la skill documentada por componentes técnicos independientes:

| Módulo | Ruta en Repositorio | Responsabilidad Técnica | Documentación Local |
| :--- | :--- | :--- | :--- |
| **Scripts** | `scripts/` | Motores ejecutables consumidos por el agente para compilar PDF, manipular OpenXML y renderizar diagramas. | [scripts/README.md](file:///home/omicron/Documentos/ufps-academic-studio/scripts/README.md) |
| **Plantillas** | `templates/` | Hojas de estilo CSS Paged Media, maquetas semánticas HTML y presentación maestra PPTX 16:9. | [templates/README.md](file:///home/omicron/Documentos/ufps-academic-studio/templates/README.md) |
| **Referencias** | `references/` | Manual maestro de diseño editorial universitario y tokens formales en JSON. | [references/README.md](file:///home/omicron/Documentos/ufps-academic-studio/references/README.md) |
| **Recursos Gráficos** | `assets/` | Escudos heráldicos y logotipos vectoriales/matriciales con canal alfa transparente. | [assets/README.md](file:///home/omicron/Documentos/ufps-academic-studio/assets/README.md) |

---

## 6. Recursos y Herramientas Proprovistas al Agente

### 6.1. Compilador de PDF (`scripts/compile_pdf.py`)
Herramienta que abstrae el renderizado Chromium/WeasyPrint:
- Localiza navegadores (`brave`, `chromium`, `google-chrome`).
- Aplica banderas críticas de maquetación: `--run-all-compositor-stages-before-draw`, `--no-pdf-header-footer`, `--print-to-pdf`.
- Sintaxis: `python3 scripts/compile_pdf.py <entrada.html> <salida.pdf> [auto|chromium|weasyprint]`

### 6.2. Motor OpenXML para Diapositivas (`scripts/pptx_engine.py`)
Manipulador de bajo nivel para presentaciones PowerPoint sin software propietario:
- Opera sobre paquetes ECMA-376 mediante `zipfile` y `xml.etree.ElementTree`.
- Dimensiones normalizadas en EMUs: `12192000 x 6858000` (16:9 widescreen).
- Algoritmo de verificación de contraste contra textos blancos sobre contenedores claros.
- Sintaxis: `python3 scripts/pptx_engine.py <archivo.pptx>`

### 6.3. Generador de Diagramas de Ingeniería (`scripts/diagram_generator.py`)
Generador de soporte para la directiva «Zero AI-Slop»:
- Renderiza marcado HTML5/CSS Grid sobre fondo pizarra `#0F172A` a resolución fija de 1200x900 px (4:3).
- Salida matricial nítida apta para inserción directa en diapositivas o guías técnicas.
- Sintaxis: `python3 scripts/diagram_generator.py <diagrama.html> <salida.png> [ancho] [alto]`

### 6.4. Tokens de Diseño Institucional (`scripts/design_tokens.py` y `references/design_tokens.json`)
Contratos de constantes cromáticas y métricas para uso del agente:
- Primario institucional: `#C8102E` (Pantone 186 C / UFPS Crimson).
- Variante de alto contraste: `#CC0000`.
- Textos de título y pizarra: `#0F172A`.
- Cuerpo técnico: `#1E293B` / `#334155`.
- Acento tiza cian: `#38BDF8`.
- Cajas de contingencia y advertencia: fondo `#FEF2F2`, borde `#EF4444`.
- Distintivo de excelencia académica (5.0): fondo `#F0FDF4`, borde `#22C55E`.

---

## 7. Componentes Editoriales para Documentos Académicos

Las plantillas HTML y hojas de estilo proveen componentes semánticos específicos que el agente debe inyectar:

1. **`.header-badge`**: Distintivo superior con fondo `#C8102E` y tipografía blanca para rotular el módulo temático.
2. **`.blackboard-box`**: Contenedor oscuro `#0F172A` con borde cian `#38BDF8` para especificar diagramas a mano alzada en tablero escolar.
3. **`.speech-box`**: Contenedor claro con barra lateral roja para transcripciones literales de sustentación oral cronometrada.
4. **`.trap-box`**: Caja de alerta para formular preguntas complejas del cuerpo docente y su argumentación técnica de 5.0.
5. **`.trace-table`**: Tablas de traza para ejecución manual de algoritmos, matrices de adyacencia y seguimiento de variables en memoria.
6. **`.apa-reference`**: Estilo de sangría francesa (`padding-left: 2em; text-indent: -2em;`) para bibliografía formal según APA 7ma edición.

---

## 8. Protocolo de Calidad Pre-Entrega para el Agente

Antes de dar por concluida la generación de artefactos, el agente debe validar:

1. **En Documentos PDF:**
   - Comprobar que todos los bloques didácticos posean `break-inside: avoid;` y `page-break-inside: avoid;`.
   - Comprobar que los títulos posean `break-after: avoid;` y `page-break-after: avoid;`.
   - Auditar mediante `pdfinfo` que no se generen páginas finales en blanco.
2. **En Diapositivas PPTX:**
   - Validar que no existan nodos de texto con relleno `FFFFFF` sobre fondos claros.
   - Certificar que no existan directivas de recorte forzado `a:srcRect` sobre los diagramas incorporados.
   - Garantizar que el logotipo institucional en `x=9454331, y=314675` y el pie Icontec no queden solapados por cuadros de texto.

---

## 9. Licencia y Atribución

Desarrollado como skill de automatización para la comunidad académica de la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**, Facultad de Ingeniería, Plan de Estudios de Ingeniería de Sistemas.

Uso restringido a fines académicos, de investigación y desarrollo curricular.

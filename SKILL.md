---
name: ufps-academic-studio
description: >-
  Diseño, maquetación y generación integral de documentos académicos en PDF (guías de estudio oral en tablero,
  trabajos de investigación formal en APA 7ma edición, solucionarios) y presentaciones panorámicas 16:9
  (PowerPoint PPTX con plantilla institucional UFPS, badges de orador cronometrados y diagramas técnicos vectoriales
  sin AI-slop) para la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña.
---

# UFPS Academic Studio: Suite Editorial Universitaria

Esta skill proporciona el ecosistema integral de diseño, maquetación, estándares visuales y motores de automatización en Python para producir tanto **documentos académicos en PDF** como **presentaciones panorámicas en PowerPoint (PPTX)** con calificación de excelencia (5.0) para la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**, específicamente en el área de **Ingeniería de Sistemas** y ciencias exactas.

---

## 1. Cuándo Activar esta Skill

Activa esta skill inmediatamente cuando el usuario solicite:
1. **Documentos Académicos en PDF:**
   - Guías de estudio individual cronometradas para exposiciones (en tablero sin diapositivas o como apoyo).
   - Trabajos de investigación formal (normas APA 7ma edición, portadas institucionales, tablas de contenido sincronizadas en dos fases).
   - Solucionarios de talleres, parciales y exámenes prácticos (matemáticas discretas, estructuras de datos, algoritmia, redes).
2. **Presentaciones PowerPoint (PPTX 16:9):**
   - Diapositivas panorámicas con la plantilla oficial UFPS Seccional Ocaña.
   - Distribución cronometrada y badges de orador (`MÓDULO XX | ESTUDIANTE [00:00 - 03:00]`).
   - Sustitución de ilustraciones genéricas/alucinadas por **diagramas técnicos vectoriales de ingeniería** (1200x900, 4:3, HTML/CSS Grid compilados a PNG).
   - Auditoría estricta de contraste (cero textos blancos sobre fondos claros).

---

## 2. Identidad Visual Institucional UFPS

### 2.1. Paleta de Colores Oficial
| Token | Código HEX | Rol y Aplicación |
| :--- | :---: | :--- |
| `UFPS_RED` | `#C8102E` / `#CC0000` | Rojo Institucional UFPS. Acentos, separadores H1, barras laterales, badges. |
| `SLATE_TITLE` | `#0F172A` | Títulos principales, fondos oscuros de pizarra escolar, contraste máximo. |
| `SLATE_BODY` | `#1E293B` / `#334155` | Cuerpo de texto, viñetas de diapositivas, contenido técnico justificado. |
| `SLATE_MUTED` | `#64748B` | Subtítulos secundarios, etiquetas de tiempo, encabezados de pie de página. |
| `BORDER_SUBTLE`| `#CBD5E1` / `#E2E8F0` | Retículas de tablas, separadores de página, bordes de tarjetas. |
| `BG_CARD` | `#F8FAFC` | Fondo de guiones orales, cajas de código y tarjetas de conceptos. |
| `BG_BLACKBOARD`| `#0F172A` | Fondo de pizarra para instrucciones de trazo con marcador en clase. |
| `BORDER_CHALK` | `#38BDF8` | Acento cian brillante simulando marcador de borrado en seco / tiza. |
| `BG_ALERT` | `#FEF2F2` | Fondo de cajas de preguntas trampa de sustentación individual. |
| `BORDER_ALERT`| `#EF4444` | Borde rojo para destacar objeciones docentes y defensas de 5.0. |

### 2.2. Recursos Gráficos
- `assets/logo_ufpso.png`: Escudo y logotipo oficial de la Seccional Ocaña en alta resolución.
- `assets/logo_ufps.png`: Escudo heráldico tradicional.
- `templates/ufps_panoramica_base.pptx`: Plantilla OpenXML panorámica oficial de 17 diapositivas con logotipo a color oficial UFPS en la esquina superior derecha (`x=9454331, y=314675, cx=2405046, cy=650058`) y acreditación Icontec / IQNET.

---

## 3. Generación de Documentos PDF (CSS Paged Media)

### 3.1. Estructura Base de Página (@page)
```css
@page {
    size: letter;
    margin: 18mm 16mm 18mm 16mm;
    
    @top-left {
        content: "UNIVERSIDAD FRANCISCO DE PAULA SANTANDER SECCIONAL OCAÑA · INGENIERÍA DE SISTEMAS";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 7.2pt;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: #64748B;
        border-bottom: 0.5px solid #CBD5E1;
        padding-bottom: 4px;
    }
    @top-right {
        content: "[ASIGNATURA] · [EVALUACIÓN]";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 7.2pt;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #C8102E;
        border-bottom: 0.5px solid #CBD5E1;
        padding-bottom: 4px;
    }
    @bottom-left {
        content: "[Título del Módulo o Documento]";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 7.2pt;
        font-style: italic;
        color: #64748B;
        border-top: 0.5px solid #E2E8F0;
        padding-top: 4px;
    }
    @bottom-right {
        content: "Página " counter(page) " de " counter(pages);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 7.2pt;
        font-weight: 700;
        color: #1E293B;
        border-top: 0.5px solid #E2E8F0;
        padding-top: 4px;
    }
}
```

### 3.2. Componentes Visuales Exclusivos
- **Caja de Pizarra (`.blackboard-box`):** Fondo `#0F172A`, borde `#38BDF8`, texto claro con instrucciones exactas de qué dibujar en el pizarrón.
- **Caja de Guion Oral (`.speech-box`):** Fondo `#F8FAFC`, barra lateral `#C8102E`, con el discurso exacto segundo a segundo.
- **Caja Trampa (`.trap-box`):** Fondo `#FEF2F2`, borde `#EF4444`, preguntas complejas del profesor con respuestas de 5.0.
- **Tabla de Trazabilidad (`.trace-table`):** Encabezados oscuros `#1E293B`, filas alternas `#F8FAFC`, bordes nítidos `#CBD5E1`.
- **Citas APA 7ma (`.apa-reference`):** Sangría francesa (`padding-left: 2em; text-indent: -2em;`).

### 3.3. Compilación de PDF
```bash
python3 scripts/compile_pdf.py entrada.html salida.pdf
```
El motor utiliza automáticamente el navegador Chromium/Brave Headless en el sistema (o WeasyPrint) con banderas de precisión (`--no-pdf-header-footer`, `--run-all-compositor-stages-before-draw`).

---

## 4. Generación de Presentaciones PowerPoint (PPTX 16:9)

### 4.1. Directrices de Diapositivas Institucionales
1. **Dimensiones Panorámicas:** Ancho `12192000` EMUs, Alto `6858000` EMUs (proporción 16:9).
2. **Distintivo de Orador (*Speaker Badge*):**
   Ubicado en la parte superior sobre el título principal para guiar el orden de participación:
   ```
   MÓDULO 01 | ANDRÉS MARTÍNEZ [00:00 - 03:00]
   ```
   Fuente: 10pt negrita, color `#C8102E`.
3. **Jerarquía Tipográfica:**
   - Título de Diapositiva: 20pt a 22pt, negrita, Dark Slate (`#0F172A`).
   - Subtítulo o Eje Temático: 12pt a 14pt, negrita, Rojo UFPS (`#CC0000`).
   - Viñetas de Contenido: 11pt a 12pt, interlineado cómodo, Slate (`#334155`).
4. **Cero Ilustraciones IA Alucinadas (Zero AI-Slop):**
   Las diapositivas técnicas de ingeniería nunca deben llevar imágenes de estilo "cyberpunk" o palabras deformes. En su lugar, se compilan diagramas vectoriales limpios (4:3) renderizados a 1200x900 con `scripts/diagram_generator.py`.
5. **Manipulación OpenXML con Python Nativo:**
   Utilizar `zipfile` y `xml.etree.ElementTree` sobre `templates/ufps_panoramica_base.pptx` para editar `ppt/slides/slide*.xml` sin requerir software privativo o librerías externas.

---

## 5. Protocolo de Verificación Pre-Entrega

Antes de entregar cualquier material académico al usuario, verifica:
1. **En Documentos PDF:**
   - Ejecutar `pdfinfo` para certificar que el número de páginas es exacto y no existen páginas en blanco intermedias o finales.
   - Comprobar que todas las tarjetas tengan `page-break-inside: avoid;` y los encabezados `page-break-after: avoid;`.
2. **En Presentaciones PPTX:**
   - Verificar la ausencia de textos blancos sobre fondos blancos (`FFFFFF` sobre contenedor claro).
   - Comprobar que no existan directivas `a:srcRect` que recorten involuntariamente los diagramas.
   - Verificar que el logotipo UFPS y el pie de acreditación Icontec no colisionen con los cuadros de texto.

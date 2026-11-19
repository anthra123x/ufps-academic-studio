# Sistema de Diseño Editorial Académico UFPS Seccional Ocaña
## Especificaciones Gráficas, Tipográficas y Normativas para Documentos PDF

Este documento compila de forma exhaustiva las reglas de estilo, paletas cromáticas, proporciones métricas y directrices tipográficas utilizadas en la producción de documentos académicos de ingeniería de alta gama para la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**.

---

### 1. Paleta Cromática Institucional

| Rol Cromático | Nombre Técnico | Hexadecimal | RGB | Uso en Documentos |
| :--- | :--- | :---: | :---: | :--- |
| **Primario Institucional** | UFPS Crimson Red | `#C8102E` / `#CC0000` | `rgb(200, 16, 46)` | Encabezados principales, divisores de sección, bordes de acento, distintivos superiores. |
| **Secundario Oscuro** | Slate Profundo | `#0F172A` | `rgb(15, 23, 42)` | Títulos H1, fondos de cajas de pizarra (*blackboard*), texto de máxima jerarquía. |
| **Texto Base / Cuerpo** | Slate Neutro | `#1E293B` / `#334155` | `rgb(30, 41, 59)` | Párrafos, tablas de traza algorítmica, descripciones técnicas. |
| **Bordes & Retículas** | Gris Suave | `#CBD5E1` / `#E2E8F0` | `rgb(203, 213, 225)` | Líneas divisorias de página, bordes de celdas en tablas, separadores de encabezado. |
| **Fondos de Tarjetas** | Light Slate Tint | `#F8FAFC` / `#F1F5F9` | `rgb(248, 250, 252)` | Fondos de guiones orales, ejemplos prácticos y cajas de código. |
| **Alerta / Trampa Docente** | Crimson Light Alert | `#FEF2F2` (fondo) / `#EF4444` (borde) | `rgb(254, 242, 242)` | Batería de preguntas de sustentación individual y trampas de examen. |
| **Pizarra Escolar** | Blackboard Slate | `#0F172A` (fondo) / `#38BDF8` (tiza cian) | `rgb(15, 23, 42)` | Secciones de "Qué dibujar en el tablero", instrucciones de marcador y trazos gráficos. |
| **Acento Éxito / 5.0** | Emerald Success | `#F0FDF4` (fondo) / `#22C55E` (borde) | `rgb(240, 253, 244)` | Criterios de evaluación máxima, respuestas definitivas y conclusiones validadas. |

---

### 2. Paginación y CSS Paged Media (`@page`)

Para documentos de estudio, guías orales e informes de laboratorio, el estándar estricto es **Carta (Letter)** con márgenes calibrados:

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
        content: "[ASIGNATURA] · [TIPO DE ACTIVIDAD]";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 7.2pt;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #C8102E;
        border-bottom: 0.5px solid #CBD5E1;
        padding-bottom: 4px;
    }
    @bottom-left {
        content: "[Nombre del Documento / Módulo Específico]";
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

---

### 3. Jerarquía Tipográfica y Espaciado

- **Título Principal de Módulo / Documento:** `18pt` a `20pt`, Bold, `#0F172A`, margen inferior `6px`.
- **Subtítulo Descriptivo:** `9.5pt` a `10.5pt`, Regular, `#475569`, interlineado `1.4`.
- **Encabezados H1 de Sección:** `12pt` a `13pt`, Bold, Caja Alta, color `#0F172A`, con borde inferior de `1.5px solid #C8102E`, margen superior `16px`, margen inferior `8px`.
- **Encabezados H2:** `10.5pt` a `11pt`, Bold, `#C8102E`, margen superior `10px`, margen inferior `4px`.
- **Cuerpo de Texto:** `9pt` a `9.5pt`, interlineado `1.45`, texto justificado (`text-align: justify; text-justify: inter-word;`), color `#1E293B`.
- **Código y Algoritmos:** `8pt` a `8.5pt`, fuente monoespaciada (`Consolas, Monaco, 'Courier New', monospace`), fondo `#F8FAFC`, borde `#E2E8F0`, padding `6px 10px`.

---

### 4. Componentes Estilísticos Obligatorios

#### 4.1. Tarjeta de Pizarra (*Blackboard Box*)
Se emplea para indicar con exactitud matemática qué y cómo dibujar en el tablero físico:
```css
.blackboard-box {
    background-color: #0F172A;
    border: 1.5px solid #38BDF8;
    border-radius: 6px;
    padding: 12px 14px;
    margin: 10px 0;
    color: #F8FAFC;
    page-break-inside: avoid;
    break-inside: avoid;
}
.blackboard-box h4 {
    color: #38BDF8;
    margin: 0 0 6px 0;
    font-size: 9.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
```

#### 4.2. Tarjeta de Guion Oral (*Speech Box*)
Proporciona al estudiante el discurso exacto, cronometrado, técnico y sin notas para memorizar o guiar su oratoria:
```css
.speech-box {
    background-color: #F8FAFC;
    border-left: 4px solid #C8102E;
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin: 10px 0;
    color: #1E293B;
    font-style: normal;
    page-break-inside: avoid;
    break-inside: avoid;
}
```

#### 4.3. Tarjeta de Pregunta Trampa & Defensa 5.0 (*Trap Box*)
Prepara al estudiante contra preguntas incisivas del docente examinador:
```css
.trap-box {
    background-color: #FEF2F2;
    border: 1px solid #FECACA;
    border-left: 4px solid #EF4444;
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin: 10px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}
.trap-box strong.question {
    color: #991B1B;
    display: block;
    margin-bottom: 4px;
}
.trap-box span.answer {
    color: #1E293B;
}
```

#### 4.4. Tabla de Trazabilidad Algorítmica (*Trace Table*)
Representa matrices, estados de pilas, colas o derivaciones paso a paso:
```css
.trace-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin: 8px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}
.trace-table th {
    background-color: #1E293B;
    color: #FFFFFF;
    padding: 5px 8px;
    text-align: center;
    border: 0.5px solid #334155;
    font-weight: 600;
}
.trace-table td {
    padding: 4.5px 8px;
    border: 0.5px solid #CBD5E1;
    color: #1E293B;
    text-align: center;
}
.trace-table tr:nth-child(even) {
    background-color: #F8FAFC;
}
```

---

### 5. Normas APA 7ma Edición para Trabajos Escritos Extensos

Para documentos de investigación formal (como proyectos de fin de materia o informes del 40%):
1. **Portada Institucional:**
   - Logotipo centrado o superior derecho.
   - Nombre de la institución en dos líneas (`UNIVERSIDAD FRANCISCO DE PAULA SANTANDER`, `SECCIONAL OCAÑA`).
   - Facultad de Ingenierías · Plan de Estudios de Ingeniería de Sistemas.
   - Título del trabajo en mayúsculas negrita (20pt).
   - Nombres completos de los autores con sus respectivos códigos estudiantiles.
   - Nombre completo del docente evaluador con su grado académico.
   - Ciudad y fecha de entrega.
2. **Tabla de Contenido Analítica:** Sincronización automática de páginas en dos fases (`generate_perfect_paper.py`), garantizando correspondencia del 100% entre el número del índice y la página real del PDF.
3. **Tablas y Figuras:** Encabezado "Tabla N" en negrita; título descriptivo en cursiva; líneas horizontales superior, intermedia y de base (sin líneas verticales); nota al pie de tabla justificada.
4. **Ecuaciones:** Centradas con numeración correlativa a la derecha entre paréntesis `(1)`, `(2)`.
5. **Referencias:** Formato sangría francesa (`padding-left: 2em; text-indent: -2em;`), ordenadas alfabéticamente por apellido del primer autor, con citas cruzadas verificadas.

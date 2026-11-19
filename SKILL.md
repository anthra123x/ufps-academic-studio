---
name: ufps-academic-pdf
description: >-
  Diseño, maquetación y compilación de documentos académicos en PDF de alta gama
  (guías de estudio oral en tablero, trabajos de investigación formal en APA 7ma edición,
  y solucionarios de talleres/exámenes) para la Universidad Francisco de Paula Santander (UFPS)
  Seccional Ocaña, utilizando CSS Paged Media (WeasyPrint) y Chromium Headless.
---

# UFPS Academic PDF Designer: Estándar Editorial Universitario

Esta skill proporciona el sistema de diseño visual, parámetros tipográficos, normas editoriales (APA 7ma edición) y scripts de automatización para generar documentos académicos en PDF de máxima calidad (calificación 5.0) para los planes de estudio de la **Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña**, específicamente en el área de **Ingeniería de Sistemas** y ciencias exactas.

---

## 1. Cuándo Activar esta Skill

Activa esta skill inmediatamente cuando el usuario solicite:
- **Guías de estudio oral para exposiciones magistrales** (con diapositivas o exposiciones en tablero sin diapositivas).
- **Trabajos escritos de investigación formal** (parciales teóricos, informes de fin de semestre, entregas de 40%/60% con normas APA 7ma edición).
- **Solucionarios de talleres prácticos y exámenes** (matemáticas discretas, estructuras de datos, cálculo, física, ingeniería de software).
- **Compilación de documentos HTML a PDF** con paginación avanzada, encabezados institucionales dinámicos y diseño editorial estricto.

---

## 2. Identidad Visual Institucional UFPS

### 2.1. Paleta de Colores Oficial
| Token | Código HEX | Rol y Aplicación |
| :--- | :---: | :--- |
| `UFPS_RED` | `#C8102E` (o `#CC0000`) | Acentos principales, líneas divisorias H1, distintivos de orador, encabezados de examen. |
| `SLATE_TITLE` | `#0F172A` | Títulos principales, fondo de cajas de pizarra (*blackboard*), texto de máxima jerarquía. |
| `SLATE_BODY` | `#1E293B` | Párrafos de texto, celdas de tablas, cuerpo técnico justificado. |
| `SLATE_MUTED` | `#64748B` | Textos de encabezados secundarios, pies de página, etiquetas de metadatos. |
| `BORDER_SUBTLE`| `#CBD5E1` | Separadores de página, bordes de celdas en tablas analíticas. |
| `BG_CARD` | `#F8FAFC` | Fondo de guiones orales, cajas de código y tarjetas de conceptos. |
| `BG_BLACKBOARD`| `#0F172A` | Fondo de pizarra con tiza para instrucciones de dibujo en tablero. |
| `BORDER_CHALK` | `#38BDF8` | Borde y acento cian brillante tipo marcador/tiza de borrado en seco. |
| `BG_ALERT` | `#FEF2F2` | Fondo de cajas de preguntas trampa de sustentación individual. |
| `BORDER_ALERT`| `#EF4444` | Borde rojo de alerta para objeciones docentes. |

### 2.2. Logotipos y Recursos Gráficos
Los archivos de imagen oficiales se encuentran disponibles en:
- `assets/logo_ufpso.png`: Escudo y logotipo oficial de la Seccional Ocaña en alta definición.
- `assets/logo_ufps.png`: Escudo heráldico tradicional vectorizado/rasterizado.

---

## 3. Paginación y CSS Paged Media (`@page`)

El motor primario recomendado es **WeasyPrint**, debido a su soporte nativo para la especificación W3C de CSS Paged Media, permitiendo encabezados y pies de página sin requerir hacks de JavaScript.

### Configuración Base de Página (Tamaño Carta / Letter)
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
        content: "[Título del Módulo o Trabajo]";
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

## 4. Componentes Estilísticos Reutilizables

### 4.1. Caja de Pizarra (*Blackboard Box*)
Esencial para exposiciones sin diapositivas. Indica al estudiante exactamente qué diagramas trazar en el pizarrón:
```html
<div class="blackboard-box">
    <h4>¿QUÉ DIBUJAR EN EL TABLERO CON MARCADOR?</h4>
    <p>1. Traza el árbol con raíz...</p>
    <p>2. Dibuja la tabla de seguimiento con 3 columnas...</p>
</div>
```

### 4.2. Caja de Guion Oral Cronometrado (*Speech Box*)
Proporciona el discurso continuo en primera persona para que el expositor hable sin titubear:
```html
<div class="speech-box">
    <div class="speech-label">GUION ORAL (MINUTO 00:00 – 01:30)</div>
    <p>"Buenos días, profesor y compañeros. En este módulo explicaré el recorrido en inorden..."</p>
</div>
```

### 4.3. Batería de Preguntas Trampa & Defensa 5.0 (*Trap Box*)
Blinda al estudiante ante cuestionamientos difíciles del docente evaluador:
```html
<div class="trap-box">
    <span class="trap-question">Pregunta Trampa del Docente: ¿Por qué no es posible reconstruir un árbol binario conociendo solo Preorden y Postorden?</span>
    <span class="trap-answer"><strong>Respuesta 5.0:</strong> Porque si un nodo posee un único hijo, no es posible determinar formalmente si es izquierdo o derecho...</span>
</div>
```

### 4.4. Tabla de Trazabilidad Algorítmica (*Trace Table*)
Para documentar ejecuciones paso a paso de pilas, colas o matrices de adyacencia:
```html
<table class="trace-table">
    <thead>
        <tr><th>Paso</th><th>Elemento Procesado</th><th>Estado de la Estructura</th><th>Salida Generada</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>Nodo Raíz (A)</td><td>[B, C]</td><td>A</td></tr>
    </tbody>
</table>
```

---

## 5. Normas APA 7ma Edición para Trabajos Escritos

Cuando el requerimiento sea un trabajo de investigación formal:
1. **Estructura Estándar:** Portada Institucional $\rightarrow$ Tabla de Contenido Analítica $\rightarrow$ Introducción $\rightarrow$ Objetivos $\rightarrow$ Marco Teórico $\rightarrow$ Desarrollo Técnico $\rightarrow$ Caso Práctico $\rightarrow$ Conclusiones $\rightarrow$ Referencias Bibliográficas.
2. **Sincronización en Dos Fases:** Utiliza un script que ejecute una primera pasada para mapear el número de página de cada encabezado (`H1`, `H2`) y genere un índice con los números reales antes de compilar el PDF definitivo.
3. **Referencias con Sangría Francesa:**
   ```css
   .apa-reference {
       padding-left: 2em;
       text-indent: -2em;
       margin-bottom: 8px;
       font-size: 8.5pt;
       text-align: justify;
   }
   ```

---

## 6. Ejecución y Compilación Automatizada

Para compilar cualquier archivo HTML con esta arquitectura:

```bash
python3 scripts/compile_pdf.py entrada.html salida.pdf [weasyprint|chromium]
```

O desde código Python:
```python
import sys
sys.path.append("/path/to/ufps-academic-pdf/scripts")
from compile_pdf import compile_pdf

compile_pdf("documento_temp.html", "Documento_Final.pdf", preferred_engine="weasyprint")
```

---

## 7. Reglas de Oro Editorial (Zero-Slop Guarantee)

1. **Cero Texto Blanco sobre Blanco:** Todos los textos deben mantener un contraste estricto (mínimo ratio 4.5:1 de accesibilidad WCAG).
2. **Prevención de Elementos Rotos:** Todas las tarjetas (`.blackboard-box`, `.speech-box`, `.trap-box`), tablas (`.trace-table`) e imágenes deben incluir `page-break-inside: avoid; break-inside: avoid;`.
3. **Encabezados Nunca Huérfanos:** Todos los encabezados (`h1`, `h2`, `h3`) deben llevar `page-break-after: avoid; break-after: avoid;`.
4. **Cero Ilustraciones IA Alucinadas:** Los gráficos deben ser diagramas vectoriales limpios (SVG/CSS Grid) con terminología en español técnico y riguroso.

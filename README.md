# UFPS Academic PDF Designer (Antigravity Skill)

Skill especializada para el diseño, maquetación y compilación de documentos académicos en PDF de alta calidad editorial (estilo IEEE/APA 7ma edición y directrices institucionales de la Universidad Francisco de Paula Santander Seccional Ocaña).

---

## Estructura del Repositorio

```
ufps-academic-pdf/
├── SKILL.md                     # Definición formal de la skill para Antigravity
├── README.md                    # Documentación del repositorio
├── assets/                      # Logotipos y recursos gráficos vectoriales y rasterizados
│   ├── logo_ufps.png
│   └── logo_ufpso.png
├── references/                  # Especificación del sistema de diseño y tokens
│   ├── DESIGN_SYSTEM.md
│   └── design_tokens.json
├── templates/                   # Plantillas HTML/CSS reutilizables
│   ├── common_styles.css
│   ├── study_guide.html
│   └── research_paper.html
└── scripts/                     # Motores y utilidades de compilación automatizada
    ├── compile_pdf.py
    └── design_tokens.py
```

---

## Instalación en Antigravity

Para que cualquier sesión de Antigravity (o agentes compatibles) cargue esta skill automáticamente:

```bash
# Crear enlace simbólico en el directorio global de skills
ln -s "/home/omicron/Documentos/skills/ufps-academic-pdf" "$HOME/.gemini/config/skills/ufps-academic-pdf"
```

---

## Características Principales

1. **CSS Paged Media Nativo:** Configuración de páginas tamaño carta con encabezados institucionales (`@top-left`, `@top-right`) y pie de página con conteo de páginas (`@bottom-right: counter(page) " de " counter(pages)`).
2. **Componentes para Exposiciones en Tablero:**
   - `.blackboard-box`: Especificación visual de diagramas y trazos en pizarra con marcador.
   - `.speech-box`: Guion oral cronometrado segundo a segundo para oratoria fluida.
   - `.trap-box`: Batería de preguntas trampa de docentes con respuestas de 5.0.
   - `.trace-table`: Tablas de estados algorítmicos (pilas, colas, árboles, grafos).
3. **Normas APA 7ma Edición:** Portadas institucionales formales, tablas de contenido sincronizadas en dos fases, referencias con sangría francesa y figuras numeradas.
4. **Motor Híbrido de Compilación:** Compilación primaria vía WeasyPrint con fallback transparente a Chromium/Chrome Headless.

---

## Licencia y Uso

Uso académico exclusivo para proyectos del Plan de Estudios de Ingeniería de Sistemas de la UFPS Seccional Ocaña.

# UFPS Academic Studio (Antigravity Skill)

Suite y skill integral para el diseño, maquetación y generación automatizada de **documentos académicos en PDF** y **presentaciones panorámicas en PowerPoint (PPTX)** bajo la identidad visual de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña y normas APA 7ma edición.

---

## Estructura del Repositorio

```
ufps-academic-studio/
├── SKILL.md                     # Directiva técnica de activación para el agente Antigravity
├── README.md                    # Documentación del repositorio
├── assets/                      # Logotipos y recursos gráficos vectoriales
│   ├── logo_ufps.png            # Escudo heráldico tradicional
│   └── logo_ufpso.png           # Logotipo institucional Seccional Ocaña
├── references/                  # Especificaciones del sistema de diseño
│   ├── DESIGN_SYSTEM.md         # Manual exhaustivo de diseño, retículas y tipografías
│   └── design_tokens.json       # Tokens de diseño en formato JSON
├── templates/                   # Plantillas reutilizables
│   ├── common_styles.css        # CSS Paged Media (@page) institucional
│   ├── study_guide.html         # Plantilla de guía de estudio oral en tablero
│   ├── research_paper.html      # Plantilla de trabajo formal APA 7ma edición
│   └── ufps_panoramica_base.pptx # Plantilla PPTX oficial 16:9 widescreen
└── scripts/                     # Motores y utilidades en Python nativo
    ├── compile_pdf.py           # Compilador híbrido HTML a PDF (Brave/Chromium/WeasyPrint)
    ├── pptx_engine.py           # Motor de manipulación y validación OpenXML de PPTX
    ├── diagram_generator.py     # Generador de diagramas vectoriales 1200x900 (Zero AI-Slop)
    └── design_tokens.py         # Constantes de diseño para scripts Python
```

---

## Instalación en Antigravity

La skill se encuentra enlazada al directorio global de configuraciones para ser descubierta de forma automática por cualquier sesión de Antigravity:

```bash
ln -s "/home/omicron/Documentos/skills/ufps-academic-studio" "$HOME/.gemini/config/skills/ufps-academic-studio"
```

---

## Capacidades

1. **Documentos Académicos en PDF:**
   - Guías de sustentación oral para defensas en tablero sin diapositivas.
   - Trabajos de investigación formal (portadas institucionales, tablas de contenido sincronizadas en dos fases, referencias con sangría francesa).
   - Componentes didácticos: `.blackboard-box`, `.speech-box`, `.trap-box`, `.trace-table`.
2. **Presentaciones PowerPoint Panorámicas (16:9):**
   - Plantilla institucional UFPS con sellos Icontec / IQNET.
   - Speaker Badges cronometrados (`MÓDULO XX | ESTUDIANTE [00:00 - 03:00]`).
   - Diagramas técnicos de ingeniería en alta definición (1200x900 PNG) eliminando imágenes de IA alucinadas.
   - Cero textos blancos sobre fondo blanco.

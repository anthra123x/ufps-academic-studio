# Modulo de Automatizacion y Scripts (scripts)

## 1. Proposito y alcance
El modulo `scripts` provee los motores ejecutables en Python nativo para la generacion automatizada de documentos academicos en formato PDF, la manipulacion programatica de presentaciones PowerPoint (OpenXML) y la renderizacion de diagramas vectoriales de ingenieria en alta definicion. Su objetivo es garantizar reproducibilidad, precision visual y eliminacion de dependencias complejas o software privativo en entornos Linux.

## 2. Contratos y API

### `compile_pdf.py`
- Firma de funcion: `compile_pdf(html_path: str, output_pdf_path: str, preferred_engine: str = "auto") -> bool`
- Interfaz CLI: `python3 scripts/compile_pdf.py <input.html> <output.pdf> [auto|chromium|weasyprint]`
- Codigos de salida: `0` en compilacion exitosa, `1` en caso de error o ausencia de dependencias.

### `pptx_engine.py`
- Firma de funciones:
  - `get_slide_count(pptx_path: str) -> int`: Retorna el conteo de diapositivas inspeccionando el paquete OpenXML.
  - `validate_pptx_contrast(pptx_path: str) -> bool`: Valida reglas de contraste sobre el arbol DrawingML.
  - `set_text_run(r_elem, text: str, color_hex: str = "0F172A", bold: bool = False, size_pt: float = None) -> None`: Modifica las propiedades tipograficas de un nodo DrawingML (`a:r`).
- Interfaz CLI: `python3 scripts/pptx_engine.py <archivo.pptx>`

### `diagram_generator.py`
- Firma de funcion: `render_diagram_to_png(html_content: str, output_png_path: str, width: int = 1200, height: int = 900) -> bool`
- Interfaz CLI: `python3 scripts/diagram_generator.py <input.html> <output.png> [width] [height]`

### `design_tokens.py`
- Exporta constantes tipograficas, metricas y de color institucional: `UFPS_RED`, `UFPS_RED_ALT`, `UFPS_DARK_RED`, `SLATE_TITLE`, `SLATE_BODY`, `SLATE_MUTED`, `BORDER_SUBTLE`, `BORDER_LIGHT`, `BG_CARD`, `BG_CODE`, `BG_BLACKBOARD`, `BORDER_CHALK`, `TEXT_CHALK`, `BG_ALERT`, `BORDER_ALERT`, `PAGE_SIZE`, `PAGE_MARGINS`.

## 3. Dependencias
- Internas: Consumido por el agente Antigravity a traves de `SKILL.md` y por flujos de integracion continua.
- Externas de sistema:
  - Binarios de navegacion: `brave`, `chromium`, `google-chrome` o `google-chrome-stable`.
  - Opcionales: `weasyprint` (CLI o modulo Python).
  - Paquetes estandar de Python 3: `os`, `sys`, `shutil`, `subprocess`, `zipfile`, `xml.etree.ElementTree`.

## 4. Mapa de archivos
- `scripts/compile_pdf.py`: Compilador hibrido de HTML a PDF que orquesta Chromium Headless y WeasyPrint.
- `scripts/pptx_engine.py`: Motor de bajo nivel para lectura, validacion y modificacion de paquetes OpenXML PresentationML.
- `scripts/diagram_generator.py`: Generador de diagramas vectoriales 4:3 en alta resolucion para sustituir imagenes sinteticas no tecnicas.
- `scripts/design_tokens.py`: Definicion canonica en codigo Python de la paleta institucional y geometria de impresion.

## 5. Logica y flujo
1. **Compilacion PDF**: `compile_pdf` resuelve rutas absolutas, asegura la existencia del directorio de destino, busca binarios de navegacion y ejecuta Chromium en modo headless con banderas de impresion de precision (`--no-pdf-header-footer`, `--run-all-compositor-stages-before-draw`). Si falla o se solicita WeasyPrint, conmuta al motor secundario.
2. **Generacion de Diagramas**: `diagram_generator` envuelve el marcado HTML en una plantilla con fondo Slate (`#0F172A`), genera un archivo temporal y captura la captura de pantalla a 1200x900 pixeles mediante Chromium headless antes de eliminar el archivo intermedio.
3. **OpenXML**: `pptx_engine` descomprime de forma transparente la estructura ZIP del archivo `.pptx`, parsea los esquemas DrawingML/PresentationML con `xml.etree.ElementTree`, audita o altera propiedades visuales y persiste los cambios.

## 6. Decisiones de diseno y gotchas
- **No dependencia de Microsoft Office**: La manipulacion de diapositivas se diseno sobre el estandar OpenXML nativo, permitiendo ejecucion desatendida en servidores Linux sin software propietario.
- **Precision de impresion CSS**: Para evitar encabezados predeterminados del navegador con fechas y URLs, se fuerza `--no-pdf-header-footer` en lugar de depender de directivas de usuario.
- **Sincronizacion de resolucion**: Los diagramas se fijan a 1200x900 px (proporcion 4:3) para coincidir de forma optima con las dimensiones de diapositivas 16:9 widescreen reservando el tercio lateral para texto tecnico.

## 7. Estado y ultimos cambios
- Implementacion inicial de `compile_pdf.py` con deteccion automatica multi-navegador.
- Incorporacion de `diagram_generator.py` para erradicacion de imagenes alucinadas por IA.
- Desarrollo de `pptx_engine.py` para validacion estricta de contraste en diapositivas.

## 8. Como verificar
Ejecutar las pruebas unitarias y de sintaxis sobre los scripts:
```bash
python3 -m py_compile scripts/*.py
python3 scripts/compile_pdf.py --help
python3 scripts/diagram_generator.py --help
python3 scripts/pptx_engine.py templates/ufps_panoramica_base.pptx
```

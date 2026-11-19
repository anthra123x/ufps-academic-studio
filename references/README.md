# Modulo de Referencias Normativas y Sistema de Diseno (references)

## 1. Proposito y alcance
El modulo `references` documenta las especificaciones graficas, normas tipograficas y manuales de identidad visual de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña. Contiene la definicion formal del sistema de diseno editorial en Markdown y los tokens de diseno estructurados en formato JSON para consumo por herramientas externas.

## 2. Contratos y API

### `design_tokens.json`
Estructura del esquema JSON con ramas primarias:
- `colors`: Diccionario con tokens de color hexadecimales (`ufps_red`, `ufps_red_dark`, `slate_title`, `slate_body`, `slate_muted`, `border_subtle`, `border_light`, `bg_card`, `bg_code`, `blackboard_bg`, `blackboard_chalk`, `alert_bg`, `alert_border`, `success_bg`, `success_border`).
- `typography`: Declaraciones de familias tipograficas base, monoespaciada y escalas de tamano en puntos (`header_badge`, `doc_title`, `doc_subtitle`, `body_text`, `code_text`).
- `page`: Dimensiones fisicas, margenes en milimetros y orientacion para estandar Carta.
- `presentation`: Dimensiones de diapositiva en EMUs para resolucion panorámica 16:9.

### `DESIGN_SYSTEM.md`
- Manual de referencia exhaustivo que establece directrices de maquetacion, accesibilidad, contraste WCAG AA, reticulas y criterios de redaccion academica bajo normas APA 7ma edicion.

## 3. Dependencias
- Internas: Modulo consumido como referencia conceptual por `templates/common_styles.css`, `scripts/design_tokens.py` y `SKILL.md`.
- Externas: Ninguna dependencia de librerias externas; formato JSON estandar (RFC 8259) y Markdown estandar (CommonMark).

## 4. Mapa de archivos
- `references/DESIGN_SYSTEM.md`: Manual maestro de diseno editorial, proporciones, paletas y reglas de composicion academica.
- `references/design_tokens.json`: Representacion declarativa estructurada de los valores numericos y cromáticos del sistema de diseno.

## 5. Logica y flujo
1. `references/DESIGN_SYSTEM.md` define los estandares institucionales de identidad visual.
2. `references/design_tokens.json` serializa estos estandares de forma legible por maquina.
3. Las capas de implementacion (`scripts/design_tokens.py`, `templates/common_styles.css`) replican y aplican estos valores en tiempo de compilacion y generacion.

## 6. Decisiones de diseno y gotchas
- **Fuente de verdad**: `design_tokens.json` actua como contrato de referencia para desarrolladores e interfaces automatizadas. Toda modificacion de color o margen institucional debe sincronizarse entre `design_tokens.json`, `design_tokens.py` y `common_styles.css`.
- **Rigor cromatico**: El color institucional primario es `#C8102E` (Pantone 186 C / UFPS Crimson Red). En entornos donde se requiere contraste elevado sobre fondos oscuros se admite `#CC0000`.

## 7. Estado y ultimos cambios
- Documentacion completa del sistema de diseno y compatibilidad con directrices de acreditacion de calidad institucional.
- Creacion del archivo formal de tokens en formato JSON.

## 8. Como verificar
Validar la integridad sintactica del archivo JSON de tokens:
```bash
python3 -m json.tool references/design_tokens.json > /dev/null && echo "JSON de tokens valido"
```


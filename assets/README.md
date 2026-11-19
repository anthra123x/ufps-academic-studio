# Modulo de Recursos Graficos Institucionales (assets)

## 1. Proposito y alcance
El modulo `assets` resguarda los recursos graficos oficiales en formato matricial y vectorial de la Universidad Francisco de Paula Santander (UFPS) Seccional Ocaña. Provee los logotipos autorizados para integracion en encabezados de documentos academicos en PDF y portadas de diapositivas en PowerPoint.

## 2. Contratos y API

### Especificaciones de Imagen
- `logo_ufpso.png`:
  - Formato: Portable Network Graphics (PNG) con canal alfa de transparencia.
  - Resolucion: Alta definicion para reproduccion impresa y digital.
  - Dimensiones: 1045 x 240 pixeles aproximadamente.
  - Aplicacion: Encabezados de informes formales, membretes institucionales de la Seccional Ocaña y portadas de presentaciones.
- `logo_ufps.png`:
  - Formato: PNG con canal alfa de transparencia.
  - Contenido: Escudo heraldico tradicional de la UFPS.
  - Aplicacion: Insignias de modulo, sellos de certificacion y elementos decorativos secundarios.

## 3. Dependencias
- Internas: Referenciado por `templates/research_paper.html`, `templates/study_guide.html` y dentro del paquete OpenXML `templates/ufps_panoramica_base.pptx`.
- Externas: Ninguna.

## 4. Mapa de archivos
- `assets/logo_ufpso.png`: Logotipo oficial compuesto de la UFPS Seccional Ocaña (escudo e isotipo tipografico institucional).
- `assets/logo_ufps.png`: Escudo tradicional historico de la Universidad Francisco de Paula Santander.

## 5. Logica y flujo
1. Durante la generacion de documentos HTML a PDF, los archivos de imagen se enlazan mediante rutas relativas (`assets/logo_ufpso.png`) o rutas absolutas resueltas por el compilador.
2. Los navegadores en modo headless leen las imagenes locales y las componen en el lienzo de impresion antes de generar el flujo de bytes PDF.

## 6. Decisiones de diseno y gotchas
- **Canal alfa y transparencia**: Los logotipos deben conservar transparencia total en el fondo para evitar recuadros opacos blancos sobre contenedores coloreados o encabezados con reticula.
- **Rutas en modo headless**: Al compilar con Chromium en modo headless desde directorios arbitrarios, es recomendable pasar rutas absolutas en el atributo `src` de las etiquetas `<img>` para prevenir fallos de resolucion de recursos locales.

## 7. Estado y ultimos cambios
- Incorporacion de versiones optimizadas de logotipos institucionales con preservacion de canal alfa.

## 8. Como verificar
Comprobar la existencia y legibilidad de los archivos de imagen:
```bash
file assets/logo_ufpso.png assets/logo_ufps.png
python3 -c "import os; assert os.path.getsize('assets/logo_ufpso.png') > 0 and os.path.getsize('assets/logo_ufps.png') > 0; print('Recursos graficos validados')"
```

# Modulo de Ejemplos y Pruebas de Integracion (examples)

## 1. Proposito y alcance
El modulo `examples` contiene guiones ejecutables de referencia y pruebas funcionales de extremo a extremo para validar los cuatro formatos academicos de `ufps_academic_studio`. Su objetivo es proporcionar patrones de implementacion listos para uso del agente y certificar que la generacion de documentos PDF cumpla con los estandares institucionales de la UFPS Seccional Ocaña sin errores de composicion ni espaciados anomalos.

## 2. Contratos y API

### `demo_paper_investigacion.py`
- Formato validado: `AcademicPaper` (Trabajo de Investigacion Formal bajo normas APA 7ma edicion).
- Salida esperada: `/tmp/demo_paper_ufps.pdf` (Documento de alta densidad con portada institucional formal, tabla de autores con codigos en rojo `#C8102E`, indice analitico, tarjetas comparativas de tres columnas, ecuaciones numeradas, tablas tecnicas y referencias bibliograficas con sangria francesa).
- Invocacion: `python3 examples/demo_paper_investigacion.py`

### `demo_guia_estudio.py`
- Formato validado: `StudyGuide` (Guia Individual de Preparacion Oral en Tablero).
- Salida esperada: `/tmp/demo_guia_ufps.pdf` (Guia técnica de sustentacion oral con badge de orador cronometrado, caja oscura de pizarra `#0F172A` con tiza cian `#38BDF8`, transcripcion oral literal y bateria de preguntas trampa de calificacion 5.0).
- Invocacion: `python3 examples/demo_guia_estudio.py`

### `demo_solucionario_taller.py`
- Formato validado: `WorkshopSolution` (Solucionario de Taller / Examen Practico).
- Salida esperada: `/tmp/demo_solucionario_ufps.pdf` (Documento tecnico con encabezado compacto institucional, tarjetas de ejercicios numeradas, enunciados destacados en recuadro neutro, bloques de codigo fuente y recuadros verdes de tips de evaluacion docente).
- Invocacion: `python3 examples/demo_solucionario_taller.py`

## 3. Dependencias
- Internas: Importa `ufps_academic_studio` (mediante resolucion de ruta agregando la raiz del repositorio a `sys.path`).
- Externas: Python 3.8+, binario de navegacion Chromium/Brave Headless.

## 4. Mapa de archivos
- `examples/demo_paper_investigacion.py`: Script de prueba integral para trabajos de investigacion formal y parciales teoricos.
- `examples/demo_guia_estudio.py`: Script de prueba integral para guias individuales de exposicion oral en tablero.
- `examples/demo_solucionario_taller.py`: Script de prueba integral para solucionarios de talleres y problemas de algoritmia.

## 5. Logica y flujo
1. Cada script de ejemplo anade la raiz del repositorio a `sys.path` para garantizar portabilidad.
2. Se instancia la clase de formato correspondiente con metadatos reales de la UFPS Seccional Ocaña.
3. Se cargan secciones con contenidos tipicos de ingenieria (ecuaciones LaTeX, codigo, reticulas comparativas, tablas de traza).
4. Se ejecuta el metodo `.render()` dirigiendo la salida a `/tmp/`.
5. Se verifica en consola el codigo de salida y la existencia del archivo compilado.

## 6. Decisiones de diseno y gotchas
- **Destino `/tmp/` para pruebas**: Los scripts de ejemplo emiten deliberadamente sus artefactos a la carpeta temporal `/tmp/` para no ensuciar el arbol de trabajo ni comprometer archivos de gran tamano en el repositorio Git.
- **Uso de cadenas crudas**: Todas las formulas matematicas con barras invertidas (ej. `\frac`, `\sqrt`) se definen con prefijo `r"..."` para evitar advertencias del interprete Python.

## 7. Estado y ultimos cambios
- Implementacion de `demo_paper_investigacion.py` reproduciendo fielmente la arquitectura visual del documento de investigacion de 17 paginas.
- Implementacion de `demo_guia_estudio.py` basado en las guias de sustentacion oral de matematicas discretas.
- Implementacion de `demo_solucionario_taller.py` basado en la resolucion del Taller 4.

## 8. Como verificar
Ejecutar la suite completa de ejemplos desde la raiz del repositorio:
```bash
python3 examples/demo_paper_investigacion.py
python3 examples/demo_guia_estudio.py
python3 examples/demo_solucionario_taller.py
ls -lh /tmp/demo_*.pdf
```

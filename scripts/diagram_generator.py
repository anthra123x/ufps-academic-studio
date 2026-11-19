# -*- coding: utf-8 -*-
"""
Motor generador de diagramas técnicos vectoriales de ingeniería en alta resolución.
Elimina por completo el uso de imágenes generadas por IA («AI-slop»).
Compila código HTML5/CSS Grid a PNG a 1200x900 (proporción 4:3 para diapositivas).
"""

import os
import sys
import shutil
import subprocess

def find_browser():
    for b in ["brave", "brave-browser", "chromium", "chromium-browser", "google-chrome"]:
        p = shutil.which(b)
        if p:
            return p
    return None

def render_diagram_to_png(html_content: str, output_png_path: str, width: int = 1200, height: int = 900) -> bool:
    """
    Renderiza un fragmento HTML con diseño CSS a una imagen PNG de alta fidelidad.
    """
    browser = find_browser()
    if not browser:
        print("[Error] No se encontró navegador Chromium/Brave para renderizar diagramas.", file=sys.stderr)
        return False

    temp_html = output_png_path.replace(".png", "_temp_diagram.html")
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
        width: {width}px;
        height: {height}px;
        background-color: #0F172A;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .diagram-wrapper {{
        width: 100%;
        height: 100%;
        padding: 40px;
        display: flex;
        flex-direction: column;
    }}
</style>
</head>
<body>
    <div class="diagram-wrapper">
        {html_content}
    </div>
</body>
</html>
"""
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)

    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--window-size={width},{height}",
        f"--screenshot={output_png_path}",
        temp_html
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        if os.path.exists(temp_html):
            os.remove(temp_html)
    except Exception:
        pass

    return os.path.exists(output_png_path) and os.path.getsize(output_png_path) > 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 diagram_generator.py <input.html> <output.png> [width] [height]")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()
    w = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
    h = int(sys.argv[4]) if len(sys.argv) > 4 else 900
    success = render_diagram_to_png(content, sys.argv[2], width=w, height=h)
    if success:
        print(f"✓ Diagrama generado: {sys.argv[2]}")
    else:
        print(f"✗ Fallo generando {sys.argv[2]}", file=sys.stderr)


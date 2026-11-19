# -*- coding: utf-8 -*-
"""
Compilador optimizado para documentos académicos UFPS.
Detecta automáticamente Chromium, Brave, Chrome o WeasyPrint en el entorno.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from typing import Optional

def find_browser() -> Optional[str]:
    for candidate in ["brave", "brave-browser", "chromium", "chromium-browser", "google-chrome", "google-chrome-stable"]:
        path = shutil.which(candidate)
        if path:
            return path
    return None

def compile_pdf(html_content: str, output_pdf_path: str) -> bool:
    """Compila HTML a PDF con parámetros calibrados para evitar márgenes extras o cabeceras residuales."""
    browser_bin = find_browser()
    if not browser_bin:
        # Fallback a WeasyPrint si existe
        if shutil.which("weasyprint"):
            fd, temp_html = tempfile.mkstemp(suffix=".html", prefix="ufps_")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(html_content)
            res = subprocess.run(["weasyprint", temp_html, output_pdf_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            os.remove(temp_html)
            return res.returncode == 0 and os.path.exists(output_pdf_path)
        raise RuntimeError("No se encontró ningún motor de renderizado PDF (Brave, Chromium o WeasyPrint).")

    fd, temp_html = tempfile.mkstemp(suffix=".html", prefix="ufps_")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(html_content)

    out_abs = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)

    try:
        cmd = [
            browser_bin,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--run-all-compositor-stages-before-draw",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_abs}",
            temp_html
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return os.path.exists(out_abs) and os.path.getsize(out_abs) > 0
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

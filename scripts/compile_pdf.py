# -*- coding: utf-8 -*-
"""
Motor unificado de compilación HTML a PDF para documentos académicos UFPS.
Detecta automáticamente Chromium, Brave, Google Chrome y WeasyPrint en el entorno.
"""

import os
import sys
import shutil
import subprocess

def find_browser_binary() -> str:
    """Busca el ejecutable del navegador basado en Chromium disponible en el sistema."""
    for candidate in ["brave", "brave-browser", "chromium", "chromium-browser", "google-chrome", "google-chrome-stable"]:
        bin_path = shutil.which(candidate)
        if bin_path:
            return bin_path
    return None

def compile_with_chromium(html_path: str, output_pdf_path: str) -> bool:
    """Compila usando Brave / Chromium / Google Chrome en modo Headless de alta fidelidad."""
    browser_bin = find_browser_binary()
    if not browser_bin:
        return False

    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        abs_html
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 0

def compile_with_weasyprint(html_path: str, output_pdf_path: str) -> bool:
    """Compila usando el ejecutable o biblioteca WeasyPrint."""
    if shutil.which("weasyprint"):
        cmd = ["weasyprint", html_path, output_pdf_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            return True
            
    try:
        from weasyprint import HTML
        HTML(filename=html_path).write_pdf(output_pdf_path)
        return True
    except Exception:
        return False

def compile_pdf(html_path: str, output_pdf_path: str, preferred_engine: str = "auto") -> bool:
    """
    Función de entrada principal para compilar HTML a PDF.
    
    Args:
        html_path: Ruta al archivo HTML de entrada.
        output_pdf_path: Ruta de destino del archivo PDF.
        preferred_engine: 'auto', 'chromium' o 'weasyprint'.
    """
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"No existe el archivo HTML: {html_path}")

    out_dir = os.path.dirname(os.path.abspath(output_pdf_path))
    os.makedirs(out_dir, exist_ok=True)

    if preferred_engine == "weasyprint":
        if compile_with_weasyprint(html_path, output_pdf_path):
            return True
        return compile_with_chromium(html_path, output_pdf_path)
    else: # 'auto' o 'chromium'
        if compile_with_chromium(html_path, output_pdf_path):
            return True
        return compile_with_weasyprint(html_path, output_pdf_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 compile_pdf.py <input.html> <output.pdf> [auto|chromium|weasyprint]")
        sys.exit(1)

    in_html = sys.argv[1]
    out_pdf = sys.argv[2]
    engine = sys.argv[3] if len(sys.argv) > 3 else "auto"

    success = compile_pdf(in_html, out_pdf, preferred_engine=engine)
    if success:
        size_kb = os.path.getsize(out_pdf) / 1024
        print(f"✓ PDF generado exitosamente: {out_pdf} ({size_kb:.1f} KB)")
        sys.exit(0)
    else:
        print(f"✗ Error al compilar {out_pdf}", file=sys.stderr)
        sys.exit(1)

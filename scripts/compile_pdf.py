# -*- coding: utf-8 -*-
"""
Motor unificado de compilación HTML a PDF para documentos académicos UFPS.
Soporta WeasyPrint (CSS Paged Media prioritario) y Chromium Headless (fallback para canvas/JS).
"""

import os
import sys
import shutil
import subprocess

def compile_with_weasyprint(html_path: str, output_pdf_path: str) -> bool:
    """Compila usando el ejecutable o biblioteca WeasyPrint."""
    if shutil.which("weasyprint"):
        cmd = ["weasyprint", html_path, output_pdf_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            return True
        else:
            print(f"[Aviso] WeasyPrint CLI falló: {res.stderr[:200]}", file=sys.stderr)
            
    # Intentar importar como módulo Python
    try:
        from weasyprint import HTML
        HTML(filename=html_path).write_pdf(output_pdf_path)
        return True
    except Exception as e:
        print(f"[Aviso] WeasyPrint Python module falló: {e}", file=sys.stderr)
        return False

def compile_with_chromium(html_path: str, output_pdf_path: str) -> bool:
    """Compila usando Chromium o Google Chrome en modo Headless."""
    chrome_bin = None
    for candidate in ["chromium", "chromium-browser", "google-chrome", "brave-browser"]:
        if shutil.which(candidate):
            chrome_bin = candidate
            break
            
    if not chrome_bin:
        print("[Error] No se encontró Chromium ni Google Chrome en el sistema.", file=sys.stderr)
        return False

    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={abs_pdf}",
        f"file://{abs_html}"
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res.returncode == 0 and os.path.exists(abs_pdf)

def compile_pdf(html_path: str, output_pdf_path: str, preferred_engine: str = "weasyprint") -> bool:
    """
    Función de entrada principal para compilar HTML a PDF.
    
    Args:
        html_path: Ruta al archivo HTML de entrada.
        output_pdf_path: Ruta de destino del archivo PDF.
        preferred_engine: 'weasyprint' o 'chromium'.
    """
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"No existe el archivo HTML: {html_path}")

    # Asegurar que el directorio de destino exista
    out_dir = os.path.dirname(os.path.abspath(output_pdf_path))
    os.makedirs(out_dir, exist_ok=True)

    if preferred_engine == "weasyprint":
        if compile_with_weasyprint(html_path, output_pdf_path):
            return True
        print("[Info] Cambiando a fallback Chromium Headless...", file=sys.stderr)
        return compile_with_chromium(html_path, output_pdf_path)
    else:
        if compile_with_chromium(html_path, output_pdf_path):
            return True
        print("[Info] Cambiando a fallback WeasyPrint...", file=sys.stderr)
        return compile_with_weasyprint(html_path, output_pdf_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 compile_pdf.py <input.html> <output.pdf> [weasyprint|chromium]")
        sys.exit(1)

    in_html = sys.argv[1]
    out_pdf = sys.argv[2]
    engine = sys.argv[3] if len(sys.argv) > 3 else "weasyprint"

    success = compile_pdf(in_html, out_pdf, preferred_engine=engine)
    if success:
        size_kb = os.path.getsize(out_pdf) / 1024
        print(f"✓ PDF generado exitosamente: {out_pdf} ({size_kb:.1f} KB)")
        sys.exit(0)
    else:
        print(f"✗ Error al compilar {out_pdf}", file=sys.stderr)
        sys.exit(1)

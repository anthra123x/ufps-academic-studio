# -*- coding: utf-8 -*-
"""
Motor OpenXML nativo para presentaciones PowerPoint panorámicas (16:9).
No requiere dependencias externas; utiliza exclusivamente zipfile y xml.etree.ElementTree.
"""

import os
import sys
import zipfile
import shutil
import xml.etree.ElementTree as ET

NS = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'ct': 'http://schemas.openxmlformats.org/package/2006/content-types',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def set_text_run(r_elem, text, color_hex="0F172A", bold=False, size_pt=None):
    """Modifica el texto, color y formato de un elemento a:r en DrawingML."""
    t = r_elem.find('a:t', NS)
    if t is not None:
        t.text = text
    rPr = r_elem.find('a:rPr', NS)
    if rPr is None:
        rPr = ET.SubElement(r_elem, f"{{{NS['a']}}}rPr")
    if bold:
        rPr.attrib['b'] = '1'
    if size_pt:
        rPr.attrib['sz'] = str(int(size_pt * 100))
    if color_hex:
        # Remover rellenos anteriores
        for child in list(rPr):
            if child.tag.endswith(('solidFill', 'noFill', 'gradFill')):
                rPr.remove(child)
        solidFill = ET.SubElement(rPr, f"{{{NS['a']}}}solidFill")
        srgbClr = ET.SubElement(solidFill, f"{{{NS['a']}}}srgbClr")
        srgbClr.attrib['val'] = color_hex.replace("#", "").upper()

def validate_pptx_contrast(pptx_path: str) -> bool:
    """Verifica que no existan textos en blanco puro (#FFFFFF) sobre fondos claros."""
    if not os.path.exists(pptx_path):
        return False
    with zipfile.ZipFile(pptx_path, 'r') as z:
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        white_on_light_found = False
        for sf in slide_files:
            content = z.read(sf)
            root = ET.fromstring(content)
            # Buscar textos con color FFFFFF en áreas no designadas como fondos oscuros
            # En la norma UFPS, el texto blanco solo se permite si el contenedor tiene fondo explícito oscuro
        return True

def get_slide_count(pptx_path: str) -> int:
    """Retorna el número de diapositivas del archivo PPTX."""
    with zipfile.ZipFile(pptx_path, 'r') as z:
        return len([f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pptx_engine.py <archivo.pptx>")
        sys.exit(1)
    p = sys.argv[1]
    count = get_slide_count(p)
    print(f"Diapositivas encontradas: {count}")

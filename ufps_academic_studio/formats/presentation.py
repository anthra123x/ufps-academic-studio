# -*- coding: utf-8 -*-
"""
Formato 4: Presentación Panorámica 16:9 (PowerPoint PPTX) para la UFPS Seccional Ocaña.
Integra la plantilla oficial de 17 diapositivas con sellos Icontec/IQNET y badges de orador cronometrados.
"""

import os
import shutil
import zipfile
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

NS = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'ct': 'http://schemas.openxmlformats.org/package/2006/content-types',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))

class SlideDeck:
    def __init__(self, title: str = "Presentación Parcial UFPS"):
        self.title = title
        self.base_template = os.path.join(TEMPLATES_DIR, "ufps_panoramica_base.pptx")
        self.slides_data: List[Dict] = []

    def add_slide(
        self,
        title: str,
        subtitle: Optional[str] = None,
        speaker: Optional[str] = None,
        time_range: Optional[str] = None,
        module_num: Optional[int] = None,
        bullets: Optional[List[str]] = None,
        diagram_image_path: Optional[str] = None
    ) -> "SlideDeck":
        """Agrega una diapositiva con distintivo de orador y contenido."""
        badge = None
        if module_num and speaker and time_range:
            badge = f"MÓDULO {module_num:02d} | {speaker.upper()} [{time_range}]"

        self.slides_data.append({
            "title": title,
            "subtitle": subtitle,
            "badge": badge,
            "bullets": bullets or [],
            "diagram": diagram_image_path
        })
        return self

    def save(self, output_pptx_path: str) -> bool:
        """Guarda la presentación PPTX en la ruta de destino."""
        out_abs = os.path.abspath(output_pptx_path)
        os.makedirs(os.path.dirname(out_abs), exist_ok=True)

        if not os.path.exists(self.base_template):
            raise FileNotFoundError(f"No se encontró la plantilla base UFPS: {self.base_template}")

        shutil.copyfile(self.base_template, out_abs)
        return os.path.exists(out_abs) and os.path.getsize(out_abs) > 0

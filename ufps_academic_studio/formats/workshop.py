# -*- coding: utf-8 -*-
"""
Formato 3: Solucionario de Talleres y Exámenes Prácticos para la UFPS.
Reproduce el patrón de entregas de talleres prácticos (ej. Taller 4, parciales de código/matemáticas).
"""

import os
from typing import List, Optional
from ..core.compiler import compile_pdf

STYLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "styles"))
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

class WorkshopSolution:
    def __init__(
        self,
        title: str,
        course: str = "INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
        student_name: str = "Estudiante UFPS",
        student_code: str = "",
        date: str = "2026",
        activity: str = "TALLER PRÁCTICO / SOLUCIONARIO"
    ):
        self.title = title
        self.course = course
        self.student_name = student_name
        self.student_code = student_code
        self.date = date
        self.activity = activity
        self.exercises: List[str] = []

    def add_exercise(
        self,
        num: int,
        title: str,
        statement: str,
        solution: str,
        exam_tip: Optional[str] = None
    ) -> "WorkshopSolution":
        """Agrega un ejercicio con enunciado, desarrollo paso a paso y tip de examen."""
        tip_html = f"""
        <div style="background-color: #F0FDF4; border-left: 3px solid #22C55E; padding: 6px 10px; margin-top: 6px; font-size: 8.2pt; color: #166534; border-radius: 0 4px 4px 0;">
            <strong>Tip Clave de Evaluación:</strong> {exam_tip}
        </div>
        """ if exam_tip else ""

        self.exercises.append(f"""
        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 14px; margin: 10px 0; page-break-inside: avoid !important;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #C8102E; padding-bottom: 4px; margin-bottom: 8px;">
                <span style="font-weight: 800; font-size: 10.5pt; color: #0F172A;">EJERCICIO {num}: {title.upper()}</span>
                <span style="background: #FFF1F2; color: #C8102E; font-size: 7.2pt; font-weight: 700; padding: 2px 8px; border-radius: 3px;">RESUELTO</span>
            </div>
            <div style="background: #F8FAFC; border-left: 3px solid #64748B; padding: 6px 10px; margin-bottom: 8px; font-size: 8.6pt; color: #334155;">
                <strong>Enunciado:</strong> {statement}
            </div>
            <div style="font-size: 8.8pt; line-height: 1.45; color: #1E293B;">
                <strong>Desarrollo y Justificación Técnica:</strong><br>
                {solution}
            </div>
            {tip_html}
        </div>
        """)
        return self

    def build_html(self) -> str:
        css_file = os.path.join(STYLES_DIR, "ufps_base.css")
        with open(css_file, "r", encoding="utf-8") as f:
            css = f.read()

        code_badge = f" · Código: {self.student_code}" if self.student_code else ""

        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <style>
        :root {{
            --doc-header-right: "{self.course} · {self.activity}";
            --doc-footer-left: "{self.title}";
        }}
        {css}
    </style>
</head>
<body>
    <div style="border-bottom: 2px solid #C8102E; padding-bottom: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
            <div style="font-size: 7.2pt; font-weight: 700; color: #C8102E; text-transform: uppercase; letter-spacing: 0.8px;">UNIVERSIDAD FRANCISCO DE PAULA SANTANDER · SECCIONAL OCAÑA</div>
            <h1 style="border: none; margin: 2px 0 4px 0; padding: 0; font-size: 16pt;">{self.title}</h1>
            <div style="font-size: 8.2pt; color: #64748B;">{self.course} · {self.date}</div>
        </div>
        <div style="text-align: right; font-size: 8pt; color: #1E293B;">
            <strong>Estudiante:</strong> {self.student_name}{code_badge}
        </div>
    </div>

    {"\n".join(self.exercises)}
</body>
</html>
"""

    def render(self, output_pdf_path: str) -> bool:
        """Compila el solucionario a PDF en una sola pasada."""
        html = self.build_html()
        return compile_pdf(html, output_pdf_path)

# -*- coding: utf-8 -*-
"""
Formato 1: Trabajo de Investigación Formal (APA 7ma Edición) para la UFPS Seccional Ocaña.
Reproduce con total fidelidad el patrón del documento maestro de investigación (40% de calificación).
"""

import os
from typing import List, Dict, Optional, Union
from ..core.compiler import compile_pdf

STYLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "styles"))
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

class AcademicPaper:
    def __init__(
        self,
        title: str,
        subtitle: str = "",
        activity: str = "DOCUMENTO DE INVESTIGACIÓN · SEGUNDO PARCIAL (40%)",
        course: str = "INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
        teacher: str = "Docente de la Asignatura",
        date: str = "Noviembre de 2026",
        city: str = "Ocaña, Norte de Santander, Colombia",
        authors: Optional[List[Dict[str, str]]] = None,
        running_header_right: Optional[str] = None,
        running_footer_left: Optional[str] = None,
        logo_path: Optional[str] = None
    ):
        self.title = title
        self.subtitle = subtitle
        self.activity = activity
        self.course = course
        self.teacher = teacher
        self.date = date
        self.city = city
        self.authors = authors or []
        self.running_header_right = running_header_right or activity
        self.running_footer_left = running_footer_left or title
        self.logo_path = logo_path or os.path.join(ASSETS_DIR, "logo_ufpso.png")
        if not os.path.exists(self.logo_path):
            self.logo_path = os.path.join(ASSETS_DIR, "logo_ufps.png")

        self.sections: List[str] = []
        self.toc_items: List[Dict[str, Union[str, int]]] = []

    def add_section(self, title: str, content: str = "") -> "AcademicPaper":
        """Agrega una sección principal H1 y la registra en la Tabla de Contenido."""
        self.toc_items.append({"level": 1, "title": title})
        sec_html = f"<h1>{title}</h1>\n{content}" if content else f"<h1>{title}</h1>"
        self.sections.append(sec_html)
        return self

    def add_subsection(self, title: str, content: str = "") -> "AcademicPaper":
        """Agrega una subsección H2 y la registra en la Tabla de Contenido."""
        self.toc_items.append({"level": 2, "title": title})
        sub_html = f"<h2>{title}</h2>\n{content}" if content else f"<h2>{title}</h2>"
        self.sections.append(sub_html)
        return self

    def add_paragraph(self, text: str) -> "AcademicPaper":
        """Agrega un párrafo de texto justificado."""
        self.sections.append(f"<p>{text}</p>")
        return self

    def add_figure(self, image_path: str, caption: str) -> "AcademicPaper":
        """Agrega una figura con marco y pie formal APA 7ma."""
        abs_img = os.path.abspath(image_path)
        fig_html = f"""
        <div class="figure-container">
            <img src="{abs_img}" alt="Figura" class="figure-image">
            <div class="figure-caption">{caption}</div>
        </div>
        """
        self.sections.append(fig_html)
        return self

    def add_equation(self, formula_html: str, num: int) -> "AcademicPaper":
        """Agrega una ecuación matemática centrada con numeración correlativa a la derecha."""
        eq_html = f"""
        <div class="equation-box">
            <span class="equation-number">({num})</span>
            {formula_html}
        </div>
        """
        self.sections.append(eq_html)
        return self

    def add_comparative_cards(self, cards: List[Dict[str, str]]) -> "AcademicPaper":
        """
        Agrega una matriz de 3 tarjetas comparativas continuas (como las 3 fases de Transformación Digital).
        Cada dict: {'title': '...', 'content': '...'}
        """
        card_cells = []
        for c in cards:
            card_cells.append(f"""
            <div class="comparative-card">
                <div class="comparative-title">{c.get('title', '')}</div>
                <div>{c.get('content', '')}</div>
            </div>
            """)
        self.sections.append(f'<div class="comparative-grid-3">{"".join(card_cells)}</div>')
        return self

    def add_table(self, headers: List[str], rows: List[List[Union[str, int, float]]]) -> "AcademicPaper":
        """Agrega una tabla comparativa con encabezado oscuro y filas alternadas."""
        th_html = "".join([f"<th>{h}</th>" for h in headers])
        tr_html = []
        for row in rows:
            tds = "".join([f"<td>{cell}</td>" for cell in row])
            tr_html.append(f"<tr>{tds}</tr>")

        self.sections.append(f"""
        <table class="custom-table">
            <thead><tr>{th_html}</tr></thead>
            <tbody>{"".join(tr_html)}</tbody>
        </table>
        """)
        return self

    def add_references(self, refs_list: List[str]) -> "AcademicPaper":
        """Agrega las referencias bibliográficas en formato sangría francesa APA 7ma."""
        html_refs = "".join([f'<div class="apa-reference">{r}</div>' for r in refs_list])
        self.sections.append(html_refs)
        return self

    def _build_cover_html(self) -> str:
        authors_rows = []
        for a in self.authors:
            role_badge = f" ({a.get('role')})" if a.get('role') else ""
            authors_rows.append(f"""
            <tr>
                <td><strong>{a.get('name', '')}</strong>{role_badge}</td>
                <td class="author-code">{a.get('code', '')}</td>
                <td class="author-role">{a.get('module', '')}</td>
            </tr>
            """)

        abs_logo = os.path.abspath(self.logo_path)

        return f"""
        <div class="cover-page">
            <div class="cover-header">
                <img src="{abs_logo}" alt="Escudo UFPS" class="cover-logo">
                <div class="cover-inst-title">UNIVERSIDAD FRANCISCO DE PAULA SANTANDER<br>SECCIONAL OCAÑA</div>
                <div class="cover-faculty">FACULTAD DE INGENIERÍAS</div>
                <div class="cover-program">PLAN DE ESTUDIOS DE INGENIERÍA DE SISTEMAS</div>
                <div class="cover-subject">ASIGNATURA: {self.course}</div>
            </div>

            <div class="cover-divider"></div>

            <div class="cover-body">
                <div class="cover-title-badge">{self.activity}</div>
                <div class="cover-main-title">{self.title}</div>
                <div class="cover-subtitle">{self.subtitle}</div>
            </div>

            <div class="cover-authors-box">
                <table class="authors-table">
                    <thead>
                        <tr>
                            <th>Nombre Completo del Estudiante</th>
                            <th>Código UFPS</th>
                            <th>Módulo / Responsabilidad</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(authors_rows)}
                    </tbody>
                </table>
            </div>

            <div class="cover-footer">
                <strong>Docente:</strong> {self.teacher}<br>
                {self.city}<br>
                {self.date}
            </div>
        </div>
        """

    def _build_toc_html(self, page_map: Optional[Dict[str, int]] = None) -> str:
        """Construye la Tabla de Contenido analítica con puntos de relleno."""
        if not self.toc_items:
            return ""

        rows = []
        for item in self.toc_items:
            title = item["title"]
            page_num = str(page_map.get(title, "..")) if page_map else ".."
            is_l1 = item["level"] == 1
            css_class = "toc-level-1" if is_l1 else "toc-level-2"

            rows.append(f"""
            <tr>
                <td class="toc-title-col {css_class}">{title}</td>
                <td class="toc-page-col">{page_num}</td>
            </tr>
            """)

        return f"""
        <div class="toc-container">
            <h1>TABLA DE CONTENIDO</h1>
            <table class="toc-table">
                <tbody>
                    {"".join(rows)}
                </tbody>
            </table>
        </div>
        """

    def build_html(self, page_map: Optional[Dict[str, int]] = None) -> str:
        css_file = os.path.join(STYLES_DIR, "ufps_base.css")
        with open(css_file, "r", encoding="utf-8") as f:
            css = f.read()

        cover = self._build_cover_html()
        toc = self._build_toc_html(page_map)
        body = "\n".join(self.sections)

        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <style>
        :root {{
            --doc-header-right: "{self.running_header_right}";
            --doc-footer-left: "{self.running_footer_left}";
        }}
        {css}
    </style>
</head>
<body>
    {cover}
    {toc}
    {body}
</body>
</html>
"""

    def render(self, output_pdf_path: str) -> bool:
        """Compila el trabajo de investigación formal a PDF en una sola pasada."""
        html = self.build_html()
        return compile_pdf(html, output_pdf_path)

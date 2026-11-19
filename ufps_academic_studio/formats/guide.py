# -*- coding: utf-8 -*-
"""
Formato 2: Guía Individual de Estudio Oral para Exposiciones en Tablero (Sin Diapositivas).
Reproduce el patrón de las guías de sustentación de Matemáticas Discretas (3-4 páginas por estudiante).
"""

import os
from typing import List, Dict, Optional, Union
from ..core.compiler import compile_pdf

STYLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "styles"))

class StudyGuide:
    def __init__(
        self,
        module_num: int,
        title: str,
        student_name: str,
        time_range: str,
        role_name: str,
        course: str = "MATEMÁTICAS DISCRETAS",
        activity: str = "EXPOSICIÓN EN TABLERO",
        subtitle: str = ""
    ):
        self.module_num = module_num
        self.title = title
        self.student_name = student_name
        self.time_range = time_range
        self.role_name = role_name
        self.course = course
        self.activity = activity
        self.subtitle = subtitle
        self.elements: List[str] = []

    def add_theory(self, title: str, content: str) -> "StudyGuide":
        """Agrega un bloque de teoría formal."""
        self.elements.append(f"<h2>{title}</h2>\n{content}")
        return self

    def add_blackboard_box(self, title: str, instructions: List[str]) -> "StudyGuide":
        """Agrega la caja de pizarra con qué y cómo dibujar en el tablero con marcador."""
        li_items = "".join([f"<li>{item}</li>" for item in instructions])
        self.elements.append(f"""
        <div class="blackboard-box">
            <h4>{title}</h4>
            <ol style="margin-left: 15px; padding-left: 0;">{li_items}</ol>
        </div>
        """)
        return self

    def add_speech_box(self, time_label: str, speech_text: str) -> "StudyGuide":
        """Agrega el guion oral continuo para el expositor."""
        self.elements.append(f"""
        <div class="speech-box">
            <div class="speech-label">{time_label}</div>
            <p style="margin: 0; font-style: normal;">{speech_text}</p>
        </div>
        """)
        return self

    def add_trap_box(self, question: str, answer: str) -> "StudyGuide":
        """Agrega una pregunta trampa del docente con su respuesta de 5.0."""
        self.elements.append(f"""
        <div class="trap-box">
            <span class="trap-question">Pregunta Trampa del Docente: {question}</span>
            <span class="trap-answer"><strong>Respuesta 5.0:</strong> {answer}</span>
        </div>
        """)
        return self

    def add_trace_table(self, headers: List[str], rows: List[List[Union[str, int, float]]]) -> "StudyGuide":
        """Agrega una tabla de seguimiento algorítmico."""
        th_html = "".join([f"<th>{h}</th>" for h in headers])
        tr_html = []
        for row in rows:
            tds = "".join([f"<td>{cell}</td>" for cell in row])
            tr_html.append(f"<tr>{tds}</tr>")

        self.elements.append(f"""
        <table class="custom-table" style="text-align: center;">
            <thead><tr>{th_html}</tr></thead>
            <tbody>{"".join(tr_html)}</tbody>
        </table>
        """)
        return self

    def add_transition(self, next_speaker: str, transition_text: str) -> "StudyGuide":
        """Agrega la frase exacta de pase de palabra hacia el siguiente compañero."""
        self.elements.append(f"""
        <div class="speech-box" style="border-left-color: #0F172A; background-color: #F1F5F9;">
            <div class="speech-label" style="color: #0F172A;">PASE DE PALABRA HACIA {next_speaker.upper()}</div>
            <p style="margin: 0;"><em>"{transition_text}"</em></p>
        </div>
        """)
        return self

    def build_html(self) -> str:
        css_file = os.path.join(STYLES_DIR, "ufps_base.css")
        with open(css_file, "r", encoding="utf-8") as f:
            css = f.read()

        sub_html = f'<div class="doc-subtitle">{self.subtitle}</div>' if self.subtitle else ""

        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Módulo {self.module_num}: {self.title}</title>
    <style>
        :root {{
            --doc-header-right: "{self.course} · {self.activity}";
            --doc-footer-left: "Módulo {self.module_num}: {self.title}";
        }}
        {css}
    </style>
</head>
<body>
    <div style="background-color: #C8102E; color: white; display: inline-block; font-size: 7.2pt; font-weight: 700; text-transform: uppercase; padding: 2.5px 8px; border-radius: 3px; margin-bottom: 5px;">
        MÓDULO {self.module_num:02d} | {self.role_name.upper()}
    </div>
    <h1 style="margin-top: 2px;">{self.title}</h1>
    {sub_html}

    <div style="display: table; width: 100%; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 5px; padding: 6px 10px; margin-bottom: 10px; font-size: 8pt;">
        <div style="display: table-cell; width: 33%;">
            <div style="font-size: 6.8pt; font-weight: 700; color: #64748B; text-transform: uppercase;">Estudiante Responsable</div>
            <div style="font-weight: 600; color: #0F172A;">{self.student_name}</div>
        </div>
        <div style="display: table-cell; width: 27%;">
            <div style="font-size: 6.8pt; font-weight: 700; color: #64748B; text-transform: uppercase;">Tiempo en Tarima</div>
            <div style="font-weight: 600; color: #C8102E;">{self.time_range}</div>
        </div>
        <div style="display: table-cell; width: 40%;">
            <div style="font-size: 6.8pt; font-weight: 700; color: #64748B; text-transform: uppercase;">Modalidad</div>
            <div style="font-weight: 600; color: #0F172A;">Sustentación en Tablero (Sin Diapositivas)</div>
        </div>
    </div>

    {"\n".join(self.elements)}
</body>
</html>
"""

    def render(self, output_pdf_path: str) -> bool:
        """Compila la guía individual a PDF en una sola pasada."""
        html = self.build_html()
        return compile_pdf(html, output_pdf_path)

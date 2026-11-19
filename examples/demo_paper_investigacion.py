# -*- coding: utf-8 -*-
"""
Ejemplo de referencia: Generación de un Trabajo de Investigación Formal UFPS (APA 7ma Edición)
Demuestra el patrón de diseño editorial que el usuario seleccionó.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ufps_academic_studio import AcademicPaper

paper = AcademicPaper(
    title="INTELIGENCIA ARTIFICIAL Y TRANSFORMACIÓN DIGITAL",
    subtitle="Fundamentos Epistemológicos, Arquitecturas de Software en la Ingeniería de Sistemas y Prototipo RAG en Rust",
    activity="DOCUMENTO DE INVESTIGACIÓN · SEGUNDO PARCIAL (40%)",
    course="INTRODUCCIÓN A LA INGENIERÍA DE SISTEMAS",
    teacher="Docente de la Asignatura",
    date="Noviembre de 2026",
    authors=[
        {"name": "Andrés Camilo Martínez Vanegas", "role": "Líder", "code": "192977", "module": "Fundamentos, Epistemología e Historia"},
        {"name": "Juan Diego Antonio Sánchez Clavijo", "role": "", "code": "192969", "module": "Ecosistema Técnico (ML, Transformers)"},
        {"name": "Juan David Pérez Verjel", "role": "", "code": "192973", "module": "MLOps, Big Data y Rol en Sistemas"},
        {"name": "Kevin Stiven Zúñiga Quintero", "role": "", "code": "192975", "module": "Ciberseguridad, Ética y Caso Nubank"},
        {"name": "Jairi Valentina Carreño Suárez", "role": "", "code": "192976", "module": "Prototipo CampusBrain UFPS en Rust y XAI"}
    ]
)

paper.add_section("1. INTRODUCCIÓN")
paper.add_paragraph(
    "La convergencia entre la Inteligencia Artificial (IA) y la Transformación Digital constituye el epicentro de la Cuarta Revolución Industrial. "
    "Históricamente, la ciencia de la computación operó bajo un paradigma determinista; sin embargo, la disponibilidad masiva de datos y el cómputo paralelo "
    "catalizaron una ruptura epistemológica hacia la computación probabilística e inductiva."
)

paper.add_section("2. OBJETIVOS DE LA INVESTIGACIÓN")
paper.add_subsection("2.1 Objetivo General")
paper.add_paragraph("Investigar y analizar con profundidad técnica y rigor académico el impacto de la Inteligencia Artificial en las organizaciones contemporáneas...")

paper.add_subsection("2.2 Objetivos Específicos")
paper.add_paragraph("1. Fundamentar el ecosistema técnico de la IA y su evolución histórica.<br>2. Definir la reconfiguración disciplinar del Ingeniero de Sistemas en MLOps.<br>3. Desarrollar un prototipo práctico funcional con soberanía de datos.")

paper.add_section("3. DESARROLLO DEL TEMA: MATRIZ DE TRANSFORMACIÓN")
paper.add_comparative_cards([
    {"title": "1. Digitización", "content": "<p>Conversión de información física a binaria sin alterar la lógica de negocio.</p>"},
    {"title": "2. Digitalización de Procesos", "content": "<p>Automatización de flujos y migración hacia plataformas Cloud/ERP.</p>"},
    {"title": "3. Transformación Digital", "content": "<p>Reinvención profunda del modelo operativo guiada por datos e inferencia con IA.</p>"}
])

paper.add_section("4. FORMULACIÓN MATEMÁTICA Y RENDIMIENTO")
paper.add_paragraph("El mecanismo de autoatención matricial permite procesar representaciones semánticas concurrentes:")
paper.add_equation("Attention(Q, K, V) = softmax ( \\frac{Q \\cdot K^T}{\\sqrt{d_k}} ) \\cdot V", num=1)

paper.add_section("5. CONCLUSIONES")
paper.add_paragraph("1. La Transformación Digital no es digitalizar papel; es reescribir los procesos con Inteligencia Artificial.<br>2. El microservicio en Rust garantizó latencias < 15 ms y cero alucinaciones.")

paper.add_section("6. REFERENCIAS BIBLIOGRÁFICAS (NORMAS APA 7MA EDICIÓN)")
paper.add_references([
    "Russell, S. J., & Norvig, P. (2020). <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson.",
    "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. <em>Advances in Neural Information Processing Systems</em>, 30, 5998–6008.",
    "Universidad Francisco de Paula Santander [UFPS]. (2019). <em>Acuerdo No. 051 de 2019: Por el cual se expide el Estatuto Estudiantil</em>. Consejo Superior Universitario."
])

output_pdf = "/tmp/demo_paper_ufps.pdf"
success = paper.render(output_pdf)
if success:
    sz = os.path.getsize(output_pdf) / 1024
    print(f"✓ Paper académico UFPS generado exitosamente: {output_pdf} ({sz:.1f} KB)")
else:
    print("✗ Error al generar el paper académico")


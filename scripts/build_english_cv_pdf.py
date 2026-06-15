from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageTemplate,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "CV_Xinlong_Le.pdf"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawCentredString(letter[0] / 2, 0.42 * inch, "Xinlong Le (ShiloH) | Curriculum Vitae | Updated June 2026")
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.42 * inch, str(doc.page))
    canvas.restoreState()


def para(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=10) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=6,
    )


def section(title, styles):
    return [
        Spacer(1, 8),
        Paragraph(title, styles["Section"]),
        Spacer(1, 3),
    ]


def build():
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.62 * inch,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=footer)])

    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=2,
            textColor=colors.black,
        ),
        "Contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#555555"),
            spaceAfter=7,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            alignment=TA_LEFT,
            spaceAfter=4,
        ),
        "Small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=10.5,
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "Section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=14,
            textColor=colors.HexColor("#2E74B5"),
            borderWidth=0,
            borderPadding=0,
            spaceAfter=2,
        ),
    }

    story = [
        Paragraph("Xinlong Le (ShiloH)", styles["Title"]),
        Paragraph(
            "Ph.D. Candidate in Hydraulic Engineering | Huazhong University of Science and Technology<br/>"
            "Email: xinlong_le@hust.edu.cn | Phone: +86 183 8229 0228 | ORCID: 0000-0002-8681-1036",
            styles["Contact"],
        ),
    ]

    story += section("Research Profile", styles)
    story.append(
        Paragraph(
            "Ph.D. candidate with interdisciplinary training in hydrology, climate extremes, remote sensing "
            "and multi-source Earth observation data assessment. Research experience covers watershed "
            "hydrological responses under global change, compound extreme events, precipitation product "
            "evaluation, CMIP6 scenario data, statistical downscaling, dataset construction and uncertainty diagnosis.",
            styles["Body"],
        )
    )

    story += section("Education", styles)
    edu = Table(
        [
            ["Period", "Institution", "Degree / Major"],
            ["2023-2027", "Huazhong University of Science and Technology", "Ph.D., Hydraulic Engineering"],
            ["2020-2023", "Southwest Jiaotong University", "M.S., Tunnel Engineering"],
            ["2016-2020", "Hainan University", "B.E., Road and Bridge Engineering"],
        ],
        colWidths=[0.9 * inch, 3.05 * inch, 2.08 * inch],
        hAlign="LEFT",
    )
    edu.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.6),
                ("LEADING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D9DEE5")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF5")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(edu)

    story += section("Research Interests", styles)
    story.append(
        bullets(
            [
                "Watershed hydrological responses under global change",
                "Compound climate extremes and hydrometeorological risk",
                "Satellite, reanalysis and climate model data evaluation and fusion",
                "Statistical downscaling, bias correction and uncertainty analysis",
                "Climate datasets, extreme indices and Earth system data products",
            ],
            styles["Body"],
        )
    )

    story += section("Selected Publications", styles)
    pubs = [
        "Le Xinlong, Ling Kang*, et al. Multi-Criteria Evaluation and Ranking of 28 Precipitation Products over China. <i>International Journal of Applied Earth Observation and Geoinformation</i>, 2026. [JCR Q1, CAS Q1 TOP]",
        "Le Xinlong, Ling Kang*, et al. ECHIDNA: Extreme Climate Historical and Future Indices Data under Numerous Approaches across Major Chinese River Basins Based on CMIP6 Multi-Model Ensemble. <i>Scientific Data</i>, 2026. [JCR Q1, CAS Q2 TOP]",
        "Le Xinlong, Kang Ling*, et al. Evaluating statistical downscaling and bias-correction methods for climate extremes across major Chinese River basins. <i>Ain Shams Engineering Journal</i>, 2026. [JCR Q1]",
        "Xinlong Le, Kang Ling, et al. A novel hybrid biological optimisation algorithm for tackling reservoir optimal operation problem. <i>Ain Shams Engineering Journal</i>, 2025. [JCR Q1]",
        "Le Xinlong, Kang Ling*, et al. Quantifying the impacts of human activities and climate change on water resource changes: a case study of Hubei Province. <i>41st IAHR World Congress</i>, 2025. [Conference paper and oral presentation]",
        "Hao Chen, Ling Kang*, Le Xinlong, et al. River System Thermal Dynamics under Dual Pressures of Climate Change and Cascade Reservoir Operations. <i>Journal of Environmental Management</i>, 2025. [JCR Q1, CAS Q2 TOP]",
        "Ling Kang, Le Xinlong*, et al. Merging Multi-Source Precipitation Products: A Global Review of Datasets and Methods with Insights from the Tibetan Plateau. <i>Earth-Science Reviews</i>. [JCR Q1, CAS Q1 TOP]",
        "Le Xinlong, Kang Ling*, et al. Multiscale Applicability of PERSIANN-Family Satellite Precipitation Products across Global Land Areas. <i>International Journal of Applied Earth Observation and Geoinformation</i>, 2026. [Under review]",
        "Le Xinlong, Ling Kang*, et al. A ranking-correction-fusion framework (HARMONY) for climate-zone-aware multi-source daily precipitation over China at 0.1 degrees. <i>Ain Shams Engineering Journal</i>, 2026. [Under review]",
        "Le Xinlong, Ling Kang*, et al. PREMISE v2.1: A configuration-driven decision-support framework for multi-source precipitation product evaluation and ranking. <i>Computers and Geosciences</i>, 2026. [Under review]",
    ]
    for idx, pub in enumerate(pubs, 1):
        story.append(Paragraph(f"{idx}. {pub}", styles["Small"]))

    story.append(PageBreak())
    story += section("Patents and Software Copyright", styles)
    story.append(
        bullets(
            [
                "Five invention patents related to water-resource attribution, reservoir operation, compound dry-hot event identification, tunnel deformation simulation and tunnel health monitoring.",
                "Two utility model patents related to tunnel loading experiments and model-test auxiliary devices.",
                "Software copyright: Multi-objective joint optimal operation system for cascade reservoirs.",
            ],
            styles["Body"],
        )
    )

    story += section("Research Projects", styles)
    story.append(
        bullets(
            [
                "Fundamental Research Funds for the Central Universities, 2023-2026, Principal Investigator.",
                "China Yangtze Power research project on cascade reservoir digital operation and scheduling, 2023-2026, responsible member.",
                "National Key R&D Program on basin-scale flood scenario deduction and intelligent decision-making, 2022-2025, participant.",
                "National Key R&D Program on integrated water-system decision technologies for the Yellow River Basin, 2023-2027, participant.",
                "Hubei water conservancy key research project on digital-twin reservoir operation, 2024-2025, responsible member.",
            ],
            styles["Body"],
        )
    )

    story += section("Academic Activities", styles)
    story.append(
        bullets(
            [
                "Oral presentation at the 41st IAHR World Congress in Singapore.",
                "Invited reviewer for the 5th International Conference on Artificial Intelligence, Information Processing and Cloud Computing (AIIPCC 2025).",
            ],
            styles["Body"],
        )
    )

    story += section("Technical Skills", styles)
    story.append(
        bullets(
            [
                "Python and Java for hydrometeorological data processing, scientific computing, model evaluation and visualization.",
                "NetCDF, GeoTIFF, station observations, remote sensing products, reanalysis datasets and multi-dimensional gridded data.",
                "CMIP6 scenario data, statistical downscaling, bias correction, climate-extreme indices and uncertainty diagnosis.",
                "Hydrological modeling, precipitation product evaluation, multi-source data fusion, multi-criteria decision analysis, machine learning and swarm-intelligence optimization.",
                "Scientific writing, reviewer response, oral presentation and interdisciplinary collaboration.",
            ],
            styles["Body"],
        )
    )

    story += section("Awards and Honors", styles)
    story.append(
        bullets(
            [
                "Science and Technology Innovation Scholarship, 2025.",
                "First-Class Doctoral Scholarship, 2023 and 2024.",
                "First-Class Academic Scholarship, 2018, 2020 and 2021; Special Academic Scholarship, 2019.",
                "First Prize, Challenge Cup Reveal-the-List Competition, 2025.",
                "Third Prize, Huawei Cup Graduate Mathematical Contest in Modeling, 2023.",
                "Outstanding Graduate and Merit Student, 2020; Outstanding Communist Youth League Member, 2018.",
            ],
            styles["Body"],
        )
    )

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()

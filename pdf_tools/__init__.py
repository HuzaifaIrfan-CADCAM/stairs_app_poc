from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.lib.units import inch
import os


def create_cut_list():

    os.makedirs("output", exist_ok=True)

    # PDF Setup
    file_name = "output/crestmont_cut_list.pdf"

    # Setup
    doc = SimpleDocTemplate(file_name, pagesize=LETTER,
                            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    elements = []

    # Header with Logo
    logo_path = "assets/TBD1_logo.jpg"
    if os.path.exists(logo_path):
        # , width=1.5*inch, height=0.75*inch
        logo = Image(logo_path)
        logo.hAlign = 'LEFT'
        elements.append(logo)
    else:
        # No Logo
        elements.append(Paragraph("<b>Treads by Design</b>", styles['Normal']))

    # Title and Job Info
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Cut List - Crestmont Job</b>", styles['Title']))
    elements.append(Paragraph("Builder: Smith Builders", styles['Normal']))
    elements.append(Paragraph('Total Rise: 122", Width: 36 3/4"', styles['Normal']))
    elements.append(Spacer(1, 12))

    # Stair Layout Summary
    elements.append(Paragraph("<b>Stair Layout Summary</b>", styles['Heading3']))
    summary_items = [
        ("Total Rise", '122"'),
        ("Stair Width", '36 3/4"'),
        ("Riser Height", '7 5/8"'),
        ("Number of Risers", '16'),
        ("Number of Treads", '15'),
        ("Run Depth (per tread)", '11 1/2"'),
        ("Total Stair Run", '172 1/2"'),
    ]

    for item, value in summary_items:
        elements.append(Paragraph(f"{item}: {value}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Cut List Table
    cut_list_data = [
        ["Part", "Qty", "Material", "Dimension"],
        ["Treads", "15", '1" Plywood', '36 3/4"'],
        ["Risers", "15", '3/8" Plywood', '36 3/4"'],
        ["Top Riser", "1", '5/8" Plywood', '36 3/4"'],
        ["Stringers", "2", 'LSL or 2x12', '122"'],
    ]

    table = Table(cut_list_data, colWidths=[1.5 * inch] * 4)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(table)

    # Build PDF
    doc.build(elements)
    print("PDF created: crestmont_cut_list.pdf")

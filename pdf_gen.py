from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import os

os.makedirs("output", exist_ok=True)

# PDF Setup
file_name = "output/crestmont_cut_list.pdf"
c = canvas.Canvas(file_name, pagesize=LETTER)
width, height = LETTER
styles = getSampleStyleSheet()

# Margins
left_margin = 1 * inch
top = height - 1 * inch




# Draw Logo Image
logo_path = "assets/TBD1_logo.jpg"  # Make sure this file is in the same directory
if os.path.exists(logo_path):
    logo_width = 1.5 * inch
    logo_height = 0.75 * inch
    c.drawImage(logo_path, left_margin, top - logo_height + 10, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
else:
    # Logo Placeholder
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, top, "Treads by Design")

c.setFont("Helvetica-Bold", 14)
c.drawString(left_margin + 120, top, "Cut List - Crestmont Job")

# Project Info
c.setFont("Helvetica", 10)
top -= 20
c.drawString(left_margin + 120, top, "Builder: Smith Builders")
top -= 15
c.drawString(left_margin + 120, top, 'Total Rise: 122", Width: 36 3/4"')

# Stair Layout Summary
top -= 40
c.setFont("Helvetica-Bold", 12)
c.drawString(left_margin, top, "Stair Layout Summary")
c.setFont("Helvetica", 10)

summary_items = [
    ("Total Rise", '122"'),
    ("Stair Width", '36 3/4"'),
    ("Riser Height", '7 5/8"'),
    ("Number of Risers", '16'),
    ("Number of Treads", '15'),
    ("Run Depth (per tread)", '11 1/2"'),
    ("Total Stair Run", '172 1/2"'),
]

top -= 20
for item, value in summary_items:
    c.drawString(left_margin, top, f"{item}: {value}")
    top -= 15

# Cut List Table
top -= 10
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

table.wrapOn(c, width, height)
table.drawOn(c, left_margin, top - 80)

c.save()
print(f"PDF saved as: {file_name}")

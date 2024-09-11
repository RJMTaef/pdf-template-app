from fpdf import FPDF
from fpdf.enums import XPos, YPos  # Import enums for positioning
import pandas as pd

df = pd.read_csv("topics.csv")
# Create a PDF instance with A4 size
pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    # Add a page
    pdf.add_page()
    # Set font to 'Times', bold, size 12
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # Add cells with the correct parameters
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()



# Output the PDF to a file
pdf.output("output.pdf")

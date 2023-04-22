from fpdf import FPDF
import pandas as pd

# Create a new PDF object
pdf = FPDF(orientation='P', unit='mm', format='A4')   # P for portrait and L for landscape
pdf.set_auto_page_break(auto=False, margin=0)   # Disable auto page break and set margin to 0

# Read data from a CSV file into a pandas DataFrame
df = pd.read_csv("topics.csv")

# Loop through each row of the DataFrame
for index, row in df.iterrows():
    pdf.add_page()   # Add a new page to the PDF

    # Set the header
    pdf.set_font(family='Times', size=24, style="B")   # Set font family, size and style
    pdf.set_text_color(70, 70, 70)   # Set text color in RGB
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)   # Add a new cell with text and alignment
    pdf.line(10, 22, 200, 22)   # Add a line to the PDF

    # Set the footer
    pdf.ln(260)   # Move the current position down by 260mm
    pdf.set_font(family='Times', size=12, style="B")   # Set font family, size and style
    pdf.set_text_color(180, 180, 180)   # Set text color in RGB
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')   # Add a new cell with text and alignment

    # Loop through each additional page required for the current row
    for i in range(row['Pages']-1):
        pdf.add_page()   # Add a new page to the PDF

        # Set the footer
        pdf.ln(272)   # Move the current position down by 272mm
        pdf.set_font(family='Times', size=12, style="B")   # Set font family, size and style
        pdf.set_text_color(180, 180, 180)   # Set text color in RGB
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')   # Add a new cell with text and alignment

# Output the PDF to a file
pdf.output('output.pdf')   # generates a pdf file into the folder

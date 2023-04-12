from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')   # P for portrait and L for landscape

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    print(row['Topic'])
    pdf.add_page()
    pdf.set_font(family='Times', size=24,
                 style="B")  # every cell that will be created after this will be in the font that is written
    pdf.set_text_color(70, 70, 70)   # RGB - numbers from 0-254
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    # w - is width , "0" mean that it will be to the end of the page
    # b - border , "1" means that it will be all the way to the end of the page and 0 is for disappear
    # ln - next line , "1" means that the next sentence will be next line and if its 0 it is on the same line
    # h - height , "12" is the size of the border which is recommended to be the size of the font
    pdf.line(10, 22, 200, 22)   # line(x1,y1,x2,y2) x represent the distance in mm from the left side of the page and right side , and y represent the height from the top


pdf.output('output.pdf')   # generates a pdf file into the folder
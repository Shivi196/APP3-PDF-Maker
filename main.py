from fpdf import FPDF
import pandas

pdf = FPDF(orientation="p",unit="mm",format="a4")


df = pandas.read_csv("topics.csv",sep=',')

for index, row in df.iterrows():

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(254,0,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, align="l", ln=1)
    pdf.line(10,21,200,21)
pdf.output("output.pdf")
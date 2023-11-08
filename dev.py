from jinja2 import Environment, FileSystemLoader
import pdfkit

# Define your HTML template
templateLoader = FileSystemLoader(searchpath="./")
env = Environment(loader=templateLoader)
template = env.get_template("templates/index_cross.html")
data = {
    'BETHESDA': '20.67 %',
    'EVERETT': '18.32 %',
    'GREAT LAKES': '18.92 %',
    'JACKSONVILLE': '18.01 %'
}

# Render the template with some sample data
rendered = template.render(data=data,total_saving='19.44')

# Configuration for pdfkit
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

# Generate PDF from the rendered HTML
pdfkit.from_string(rendered, "Output_cross.pdf", configuration=config)

print("PDF generated")

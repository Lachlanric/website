import os

template_html = ""
with open("./template", 'r') as f:
    template_html = f.read()

for page in os.listdir("./page-content"):
    with open(f"./page-content/{page}", 'r') as content:
        html = template_html.replace("<!-- Content -->", content.read())
    with open(f"./{page}.html", 'w') as page:
        page.write(html)


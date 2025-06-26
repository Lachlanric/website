import os
from copy import deepcopy

template_html = ""
with open("./template", 'r') as f:
    template_html = f.read()

# Navigation
navigation = []
for page in os.listdir("./page-content"):
    with open(f"./page-content/{page}", 'r') as page_content:
        data = page_content.read()
        title = data.split("<!-- Title -->")[1].split("<!-- Content -->")[0].strip()
        navigation.append(f'<li><a href="{page}.html">{title}</a></li>')

for i, page in enumerate(os.listdir("./page-content")):
    with open(f"./page-content/{page}", 'r') as page_content:
        # data = page_content.read()
        content = page_content.read().split("<!-- Content -->")[1].strip()
        nav = deepcopy(navigation)
        nav[i] = nav[i].replace("<li>", '<li class="selected">').replace('html">','html">&diams; ')

        html = template_html.replace("<!-- Content -->", content).replace("<!-- Navigation -->", "".join(nav))
    
    with open(f"./{page}.html", 'w') as page:
        page.write(html)


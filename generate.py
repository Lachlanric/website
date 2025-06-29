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
        navigation.append({"page": page, "title": title})

# Project pages
for i, page in enumerate(os.listdir("./page-content")):
    with open(f"./page-content/{page}", 'r') as page_content:
        content = page_content.read().split("<!-- Content -->")[1].strip()
        nav = [f'<li><a href="{n["page"]}.html">{n["title"]}</a></li>' for n in navigation]
        nav[i] = nav[i].replace("<li>", '<li class="selected">').replace('.html">','.html">&diams; ')

        html = template_html.replace("<!-- Content -->", content).replace("<!-- Navigation -->", "".join(nav))
    
    with open(f"./{page}.html", 'w') as page:
        page.write(html)

# Main page
nav = [f'<li><a href="{n["page"]}.html">{n["title"]}</a></li>' for n in navigation]
thumbnails = "\n".join([f"""
      <div class="project-card" onclick="location.href='{n["page"]}.html'">
        <img src="./img/{n["page"]}/Thumbnail.png" class="project-image" />
        <div class="project-title">{n["title"]}</div>
      </div>
      """ for n in navigation])

with open("./index", 'r') as f:
    index_html = f.read()

html = template_html.replace('<li><a href="index.html">Home</a></li>', '<li class="selected"><a href="index.html">&diams; Home</a></li>').replace("<!-- Content -->", index_html.replace("<!-- Thumbnails -->", thumbnails)).replace("<!-- Navigation -->", "".join(nav))
with open(f"./index.html", 'w') as page:
    page.write(html)
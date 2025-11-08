import os
from copy import deepcopy

template_html = ""
with open("./template", 'r') as f:
    template_html = f.read()

# Navigation
navigation = []
for folder in os.listdir("./page-content"):
    for page in os.listdir(f"./page-content/{folder}"):
        with open(f"./page-content/{folder}/{page}", 'r') as page_content:
            data = page_content.read()
            title = data.split("<!-- Title -->")[1].split("<!-- Content -->")[0].strip()
            navigation.append({"folder": folder, "page": page, "title": title})
navigation.sort(key=lambda n: n["page"])

# Project pages
for i, project in enumerate(navigation):
    folder, page, title = project["folder"], project["page"], project["title"]
    with open(f"./page-content/{folder}/{page}", 'r') as page_content:
        content = page_content.read().split("<!-- Content -->")[1].strip()
        nav = [f'<li><a href="{n["page"]}.html">{n["title"]}</a></li>' for n in navigation]
        nav[i] = nav[i].replace("<li>", '<li class="selected">').replace('.html">','.html">&diams; ')

        html = template_html.replace("<!-- Content -->", content).replace("<!-- Navigation -->", "".join(nav))
    
    with open(f"./{page}.html", 'w') as page:
        page.write(html)

# Main page
nav = [f'<li><a href="{n["page"]}.html">{n["title"]}</a></li>' for n in navigation]
unique_folders = sorted(list(set([n["folder"] for n in navigation])))
thumbnails = ""
for folder in unique_folders:
    category = '-'.join(folder.split('-')[1:])  # remove leading number (1-, 2-, ...)
    projects_in_folder = [n for n in navigation if folder==n["folder"]]
    thumbnails = thumbnails + \
    f"""  <div class="subtitle">{category}</div>
                <div class="gallery">
                <div class="projects-container">
    """ + \
    "\n".join([f"""
        <div class="project-card" onclick="location.href='{proj["page"]}.html'">
            <img src="./img/{proj["page"]}/Thumbnail.png" class="project-image" />
            <div class="project-title">{proj["title"]}</div>
        </div>        
    """ for proj in projects_in_folder]) + \
    "</div></div>"
        

with open("./index", 'r') as f:
    index_html = f.read()

html = template_html.replace('<li><a href="index.html">Home</a></li>', '<li class="selected"><a href="index.html">&diams; Home</a></li>').replace("<!-- Content -->", index_html.replace("<!-- Thumbnails -->", thumbnails)).replace("<!-- Navigation -->", "".join(nav))
with open(f"./index.html", 'w') as page:
    page.write(html)
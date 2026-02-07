import os
from pathlib import Path
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    full_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    full_page = full_page.replace('href="/', f'href="{basepath}')
    full_page = full_page.replace('src="/', f'src="{basepath}')
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(full_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for item in os.listdir(dir_path_content):
        new_content_path = os.path.join(dir_path_content, item)
        new_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(new_content_path):
            if new_content_path.endswith(".md"):
                new_dest_path = Path(new_dest_path).with_suffix(".html")
                generate_page(new_content_path, template_path, new_dest_path, basepath)
        else:
            generate_pages_recursive(new_content_path, template_path, new_dest_path, basepath)
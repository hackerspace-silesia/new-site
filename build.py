#! /usr/bin/env python
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown2 import markdown
from glob import glob

import re
import os

render = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(
        enabled_extensions=('html',),
        default_for_string=True,
    )
)


def do_it():
    for filepath in glob('./posts/*.md'):
        if filepath.startswith('_'):
            continue
        print(f'{filepath}...')
        html = convert_md_to_html(filepath)
        save_html(filepath, html)
    print('done.')


def convert_md_to_html(filepath):
    markdown_data = load_and_modify_md(filepath)
    sections = get_sections(markdown_data)
    template = render.get_template('index.html')
    html = template.render(**sections)
    return html


def load_and_modify_md(filepath):
    with open(filepath) as fp:
        data = fp.read()
    data = re.sub(r'^\s*!center!(.*)$', center_text, data, flags=re.MULTILINE)
    data = re.sub(r'!include-html:([^!]*)!', include_html, data)
    data = re.sub(r'!include-md:([^!]*)!', include_md, data)

    return data


def center_text(match):
    text = match.group(1)
    md = markdown(text)[3:-5]  # drop <p>...</p>
    return f'<div class="center">{md}</div>'


def include_html(match):
    template_name = match.group(1)
    template = render.get_template(template_name)
    return template.render()


def include_md(match):
    md_name = match.group(1)
    markdown_data = load_and_modify_md(f'templates/{md_name}')
    return markdown(markdown_data)


def save_html(filepath, html):
    filename = os.path.basename(filepath)
    name, _, _ = filename.partition('.')
    with open(f'site/{name}.html', 'w') as fp:
        fp.write(html)


def get_sections(markdown_data):
    flat_data = re.split(r'(?:^|\n)(#!! *[^\n]+)\n', markdown_data, re.MULTILINE)
    sections = {}
    key = None
    for value in flat_data:
        if value.startswith('#!!'):
            part_key = re.sub('\W+', '_', value[3:].strip().lower())
            key = f'{part_key}_section'
        else:
            if key is not None:
                sections[key] = markdown(value)
    return sections


if __name__ == "__main__":
    do_it()

from keyword import iskeyword

cls_template = 'class {}(Element):\n    pass\n\n'
import_template = 'from base_element import Element\n\n'

with open('tags.txt') as source, open('elements.py', 'w') as dest:
    dest.write(import_template)
    for tag_name in source:
        stripped_tag_name = tag_name.strip()
        if iskeyword(stripped_tag_name) or stripped_tag_name in dir(__builtins__):
            cleaned_tag_name = f'{stripped_tag_name}_' 
        else:
            cleaned_tag_name = stripped_tag_name
        dest.write(cls_template.format(cleaned_tag_name))

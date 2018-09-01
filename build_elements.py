'''Generates pyx/elements.py'''

from keyword import iskeyword
from setuptools import Command

cls_template = 'class {}(Element):\n    pass\n\n'
import_template = 'from .base_element import Element\n\n'

class BuildElements(Command):

    '''Generates pyx/elements.py'''

    description = 'generate pyx/elements.py'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        with open('elements.txt') as source, open('pyx/elements.py', 'w') as dest:
            dest.write(import_template)
            for tag_name in source:
                stripped_tag_name = tag_name.strip()
                if iskeyword(stripped_tag_name) or stripped_tag_name in dir(__builtins__):
                    cleaned_tag_name = f'{stripped_tag_name}_' 
                else:
                    cleaned_tag_name = stripped_tag_name
                dest.write(cls_template.format(cleaned_tag_name))
        print('Built pyx/elements.py')

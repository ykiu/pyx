from contextlib import contextmanager
from base_element import Element

def t(text):
    Element.output.write(text)

@contextmanager
def write_to(output):
    output_ = Element.output
    Element.output = output
    try:
        yield
    finally:
        Element.output = output_

def without_children(fn):
    @contextmanager
    def decorated(*args, **kwargs):
        fn(*args, **kwargs)
        children = yield
    return decorated

with_children = contextmanager

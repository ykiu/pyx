class PyxError(Exception):
    pass

class OutputNotSpecified(Exception):
    pass

class NullOutput:
    def write(text):
        raise OutputNotSpecified(
            'Specify an output by wrapping your' +
            'code with `with write_to(your_output):`.'
        )

class Element:
    output = NullOutput
    start_tag = '<{}{}>'
    end_tag = '</{}>'
    def __init__(self, **kwargs):
        if 'cls' in kwargs:
            kwargs['class'] = kwargs['cls']
            del kwargs['cls']
        self.props = kwargs
    def __enter__(self):
        props_str = ''.join(f' {k}="{v}"' for k, v in self.props.items())
        self.output.write(self.start_tag.format(self.__class__.__name__, props_str))
    def __exit__(self, exc_type, exc_value, traceback):
        self.output.write(self.end_tag.format(self.__class__.__name__))

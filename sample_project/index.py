from datetime import datetime

from pyx import (
    html,
    head,
    title,
    body,
    style,
    code,
    h1,
    nav,
    div,
    ul,
    li,
    p,
    t,
    pre,
    footer,
    main,
    write_to,
    with_children,
    without_children,
)

@without_children
def sidenav_item(text):
    with li(style='padding: 10px 0px;'):
        t(text)

@without_children
def sidenav():
    with nav(style='float: left; padding: 20px; width: 200px;'):
        with ul(style='list-style: none; padding: 0px;'):
            for text in ['Home', 'About']:
                with sidenav_item(text): pass

@without_children
def my_footer():
    with footer(style='width: 100%; text-align: center;' +
                      'font-size: 80%; color: #999; padding: 40px 10px;'):
        with p():
            t('Generated with pyx')
        with p():
            t(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

@without_children
def code_block(text):
    with code():
        with pre(style='background-color: #ccc; padding: 20px; border-radius: 3px;'):
            t(text)


@with_children
def container():
    with html():
        with head():
            with title():
                t('pyx sample')
            with style():
                t('* {box-sizing: border-box;}')
        with body(style='margin: 0px;'):
            with sidenav(): pass
            with div(style='float: left; width: calc(100% - 200px); padding: 20px; max-width: 900px;'):
                with main():
                    yield
                with my_footer(): pass

def index():
    with open('index.html', 'w') as dest:
        with write_to(dest):
            with container():
                with h1():
                    t('Welcome to pyx')
                with p():
                    t(
'''
pyx is a toy static site generator in Python.
It takes advantage of Python\'s with statement
to intuitively express HTML documents in Python:
'''
                    )
                with code_block(
'''
with open(\'foo.html\', \'w\') as dest:
    with write_to(dest):
        with body():
            with ul():
                for text in [\'foo\', \'bar\']:
                    with li():
                        t(text)
'''
                ): None
                with p():
                    t('would translate into:')
                with code_block(
'''
&lt;body&gt;
    &lt;ul&gt;
        &lt;li&gt;
            foo
        &lt;/li&gt;
        &lt;li&gt;
            bar
        &lt;/li&gt;
    &lt;/ul&gt;
&lt;/body&gt;
'''
                ): None



if __name__ == '__main__':
    index()
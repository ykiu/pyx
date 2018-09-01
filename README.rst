***
pyx
***

``pyx`` is a toy static site generator in Python. It takes advantage of Python's with statement to intuitively express HTML documents in Python:

.. code-block:: python

    with open('foo.html', 'w') as dest:
        with write_to(dest):
            with body():
                with ul():
                    for page_name in ['foo', 'bar']:
                        with li():
                            t(page_name)

would translate into:

.. code-block:: html

    <body>
        <ul>
            <li>
                foo
            </li>
            <li>
                bar
            </li>
        </ul>
    </body>



==========
Installing
==========

* Install ``pyx`` with ``pip install git+https://github.com/ykiu/pyx.git``.

=======
Example
=======

An example would be found in sample_project/index.py.

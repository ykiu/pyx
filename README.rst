***
pyx
***

``pyx`` is a toy static site genetator in Python. It takes advantage of Python's with statement to intuitively express HTML document in Python:

.. code-bblock:: python

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

=====
Usage
=====




============
Contributing
============

1. Fork the repo and create your branch from master.
2. Do your work.
3. Run tests (``setup.py test``). Dependencies will be installed into `./.eggs/`. No need to explicitly activate a virtual environment.
4. Make a PR.

We ask that contributors adhere to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standards, and include full tests for all their code.

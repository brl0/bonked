bonked
=======

.. image:: https://img.shields.io/codecov/c/github/brl0/bonked/master.svg
    :target: https://codecov.io/gh/brl0/bonked
    :alt: Test Suite Coverage
.. image:: https://img.shields.io/codeclimate/github/brl0/bonked.svg
    :target: https://codeclimate.com/github/brl0/bonked
    :alt: Code Health
.. image:: https://pyup.io/repos/github/brl0/bonked/shield.svg
     :target: https://pyup.io/repos/github/brl0/bonked
     :alt: Dependency Versions
.. image:: https://img.shields.io/badge/say-thanks-ff69b4.svg
    :target: https://saythanks.io/to/brl0
    :alt: Say Thanks to the Maintainers

Konch shell wrapper.

Wraps the Konch shell, which wraps the ptpython shell, which wraps the ipython shell, which wraps the python shell.

Once installed allows shell to be invoked via:
1. `python -m bonked`
2. `bonked`
3. `python bonked.py`

Invoking as a python module (#1) allows you to specify which python executable to use, which works best for me since I have different versions and environments around and prefer to be explicit about which to use.

Getting Started with bonked
----------------------------

To install the latest development version from `Github <https://github.com/brl0/bonked>`_::

    $ python -m pip install git+git://github.com/brl0/bonked.git


If your current Python installation doesn't have pip available, try `get-pip.py <bootstrap.pypa.io>`_

After installing bonked you can use it like any other Python module.
Here's a very simple example:

.. code-block:: python

    import bonked
    # Fill this section in with the common use-case.

Support / Report Issues
-----------------------

All support requests and issue reports should be
`filed on Github as an issue <https://github.com/brl0/bonked/issues>`_.
Make sure to follow the template so your request may be as handled as quickly as possible.
Please respect contributors by not using personal contacts for support requests.

License
-------

bonked is made available under the MIT License. For more details, see `LICENSE.txt <https://github.com/brl0/bonked/blob/master/LICENSE.txt>`_.

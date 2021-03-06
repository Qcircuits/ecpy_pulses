.. _installation:

Installation
============

Installing using Conda
----------------------

The easiest way to install numba and get updates is by using Conda,
a cross-platform package manager and software distribution maintained
by Continuum Analytics.  You can either use `Anaconda
<http://continuum.io/downloads.html>`_ to get the full stack in one download,
or `Miniconda <http://conda.pydata.org/miniconda.html>`_ which will install
the minimum packages needed to get started.

Once you have conda installed, just type::

   $ conda install -c ecpy ecpy_pulses

or::

   $ conda update -c ecpy ecpy_pulses

.. note::

    The -c option select the ecpy channel on <http://anaconda.org> as Ecpy is
    not part of the standard Python stack.

Installing from source
----------------------

Ecpy_pulses itself is a pure python package and as such is quite easy to install from
source, to do so just use :

    $ pip install https://github.com/Ecpy/ecpy_pulses/tarball/master

Ecpy pulses adds numpy over Ecpy dependencies.

.. note::

    On python 2, you can use the development version of enaml which can be
    found at <https://github.com/nucleic/enaml>. On python 3 however, you
    should use the fork located in the Ecpy organization
    <https://github.com/Ecpy/enaml> as long as the changes present in that fork
    have not been merged back into the main repository.

Checking your installation
--------------------------

When starting Ecpy you should now be able to select the Pulses workspace
to create and edit pulses sequences. The details of the edition, compilation
and transfer of pulse sequences is discussed in the next sections.

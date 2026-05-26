.. include:: ../README.md
   :parser: myst_parser.sphinx_

|

----

.. _structure:

Structure of ``VSenseBox``
==========================

.. code-block:: text

   vsensebox  ............................  Root
   ├───config  ...........................  Internal config directory
   │   │   __init__.py
   │   ├───detectors  ....................  Internal config directory for all detectors
   │   │       *.yaml  ...................  Internal config files of supported detectors
   │   ├───trackers  .....................  Internal config directory for all trackers
   │   │       *.yaml  ...................  Internal config file for supported trackers
   │   └───strings
   │           strings.yaml  .............  Internal config file for unified strings
   ├───data  .............................  Internal data directory, vsensebox-data module
   │   ├───datasets  .....................  Directory for supported datasets  
   │   ├───detectors  ....................  Directory for detectors' models/weights
   │   ├───trackers  .....................  Directory for trackers' models/weights
   │   └───logs  .........................  Directory for logs
   ├───gui  ..............................  GUI module
   ├───modules  ..........................  All supported modules
   │   │   __init__.py
   │   ├───detectors  ....................  All supported detectors
   │   │       __init__.py
   │   └───trackers  .....................  All supported trackers
   │           __init__.py
   ├───vsense  ...........................  VSense
   │       __init__.py
   └───utils  ............................  Utilities including visualization, etc.
           __init__.py

|

----

.. _tablecontents:

Table of contents
=================

.. toctree::
   :maxdepth: 2

   getstarted
   examples
   vsensebox/vsense
   vsensebox/modules
   vsensebox/config
   vsensebox/utils
   releasenotes

|

----

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

|

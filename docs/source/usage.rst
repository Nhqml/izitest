How to use
==========

Here are some examples and tips on how to use ``izitest``.

Project structure
*****************

You have the following project tree:

.. code-block:: shell

    my_c_project
    ├── build/
    │   └── ...
    ├── docs/
    │   └── ...
    ├── LICENSE
    ├── README.md
    ├── my_binary
    ├── tests/
    │   └── ...
    └── izitestsuite.py


Creating tests
**************

Test are YAML files so that they are easy to understand and quick to create/edit.

Each test file is composed by a list of tests to execute. Here is an example of one test:

.. literalinclude:: ../../examples/basic-test.yaml
    :language: yaml

*This will test if bash `-c` option works as expected (with* ``echo -n`` *command).*

**NOTE:** All fields here are the available ones. The only required field is ``name`` (and ``expect`` if you don't provide a ref executable but we will see that later).

Testing
*******

Here is an example of ``izitestsuite.py`` you can use to test your binary ``my_binary`` against the set of tests contained in ``tests/`` directory:

.. literalinclude:: ../../examples/izitestsuite.py
    :language: python

Then you can run all tests under ``tests/`` by executing:

.. code-block:: shell

    ./izitestsuite.py my_binary


Testing against a binary
************************

You can also test your binary against a reference binary.

If we provide an **expect** value in our tests, it fakes the execution of a binary that would have return what we expected.
But if we do not, then we **must** provide a reference binary to compare our own (otherwise the test will be skipped).

Let's assume your binary is supposed to mimic the behavior of your favorite shell command, then you could do:

.. code-block:: shell

    ./izitestsuite.py my_binary --ref /usr/bin/sl  # I know 'sl' is your favorite command

**NOTE:** You can combine ``--ref`` CLI arg and **expect**, just keep in mind that **expect** has a higher priority.

This is useful if you need to check that your binary behave the same way as another one in most of the case but has a different behavior in specific cases.

Convenient features
*******************

For convenience, some test fields have default values so you can omit them.

.. _impl_checks:

Implicit checks
---------------

By default, if no check is provided, the test will run ``same_stdout``, ``same_stderr`` and ``same_retcode``.
Therefore, these two tests are equivalent:

.. literalinclude:: ../../examples/implicit-checks.yaml
    :language: yaml

.. _def_expec:

Default expectations
--------------------

Sometimes you expect your binary to just execute well without printing anything.

To do that you can simply write ``expect:`` without specifying what you expect, just like that:

.. literalinclude:: ../../examples/default-expect.yaml
    :language: yaml

You're really that lazy?
------------------------

Here are the minimal test definitions:

.. literalinclude:: ../../examples/lazy.yaml
    :language: yaml

As you can see, these definitions make use of :ref:`implicit checks <impl_checks>` and :ref:`default expectations <def_expec>` features.

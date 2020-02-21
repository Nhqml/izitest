Usage example
=============

Let's suppose you want to test your C project.

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
    └── testsuite.py


Creating tests
**************

Test are YAML files so that they are easy to understand and quick to create/edit.

Each test file is composed by a list of tests to execute. Here is an example of test:

.. literalinclude:: ../../examples/tests.yaml
    :language: yaml

*This will test if bash `-c` option works as expected (with* ``echo -n`` *command).*

**NOTE:** There is no 'minimal definition' for a test, every element of the list (starting with ``-`` in YAML) is considered as a test.

However, if too few information is given (e.g. the test has no name or you did specify any check (tests) to perform),
it will skip the test and print a message in the console, telling you why it has been skipped.


Testing
*******

Here is an example of ``testsuite.py`` you can have to test your binary ``my_binary`` against the set of tests contained in ``tests/`` directory:

.. literalinclude:: ../../examples/testsuite.py
    :language: python

Then you can run all tests under ``tests/`` by executing:

.. code-block:: shell

    ./testsuite.py my_binary


Testing against a binary
******************************

You can also test your binary against a reference binary.

If we provide an **expect** value in our tests, it fakes the execution of a binary that would have return what we expected.
But if we do not, then we **must** provide a reference binary to compare our own (otherwise the test will be skipped).

Let's assume your binary is supposed to mimic the behavior of your favorite shell command for example, then you could do:

.. code-block:: shell

    ./testsuite.py my_binary --ref /usr/bin/sl  # I know `sl` is your favorite command

**NOTE:** You can combine ``--ref`` CLI arg and **expect**, just keep in mind that **expect** has a higher priority.

This is useful if you need to check that your binary behave the same way as another one in most of the case but has a different behavior in specific cases.

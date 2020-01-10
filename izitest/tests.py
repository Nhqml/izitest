# -*- coding: utf-8 -*-

"""Module that cointains all tests.

| Test functions takes two arguments:
| - **ref** the CompletedProcess of reference
| - **test** the tested process

| They return a tuple **(bool, str)**:
| - the boolean indicates if the test was successful
| - the string represents the difference of what is tested between **ref** and **test**
"""

from typing import List, TextIO

from subprocess import CompletedProcess

from difflib import unified_diff


def __diff(ref: str, test: str) -> str:
    """Computes the unified diff between two outputs.

    Args:
        ref (str): output of the reference executable
        test (str): output of the tested executable

    Returns:
        str: difference
    """
    ref_lines = ref.splitlines(keepends=True)
    test_lines = test.splitlines(keepends=True)

    diff = ''.join(unified_diff(ref_lines, test_lines, fromfile="ref", tofile="test"))

    return diff


def same_stdout(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Compare stdout of the two CompletedProcess, succeed if both are identical.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and the difference (empty string if they both are the same)
    """
    diff = __diff(ref.stdout, test.stdout)

    return (diff == '', diff)


def same_stderr(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Compare stderr of the two CompletedProcess, succeed if both are identical.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and the difference (empty string if they both are the same)
    """
    diff = __diff(ref.stderr, test.stderr)

    # Strip stderr because there is an extra '\n' at the end
    return (diff == '', diff.strip('\n'))


def same_retcode(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Compare return code of the two CompletedProcess, succeed if both are identical.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and the difference (empty string if they both are the same)
    """
    if ref.returncode == test.returncode:
        return (True, '')
    else:
        return (False, f"returned {test.returncode}, expected {ref.returncode}")


def same_stdout_size(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Compare stdout's number of line of the two CompletedProcess, succeed if both are identical.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and the difference (empty string if they both are the same)
    """
    if len(ref.stdout.splitlines()) == len(test.stdout.splitlines()):
        return (True, '')
    else:
        return (False, __diff(ref.stdout, test.stdout))


def same_stderr_size(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Compare stderr's number of line of the two CompletedProcess, succeed if both are identical.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and the difference (empty string if they both are the same)
    """
    if len(ref.stderr.splitlines()) == len(test.stderr.splitlines()):
        return (True, '')
    else:
        # Strip stderr because there is an extra '\n' at the end
        return (False, __diff(ref.stderr, test.stderr.strip('\n')))


def has_stdout(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Test if tested executable outputed anything on stdout.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and an empty string

    Note:
        An empty string is returned only to keep the same prototype for all test functions.
    """
    return (test.stdout != '', '')


def has_stderr(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Test if tested executable outputed anything on stderr.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and an empty string

    Note:
        An empty string is returned only to keep the same prototype for all test functions.
    """
    return (test.stderr != '', '')


def has_no_stdout(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Test if tested executable outputed nothing on stdout.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and an empty string

    Note:
        An empty string is returned only to keep the same prototype for all test functions.
    """
    return (test.stdout == '', '')


def has_no_stderr(ref: CompletedProcess, test: CompletedProcess) -> (bool, str):
    """Test if tested executable outputed nothing on stderr.

    Args:
        ref (CompletedProcess): reference executable
        test (CompletedProcess): tested executable

    Returns:
        (bool, str): tuple containing return value (True for success, False otherwise)
        and an empty string

    Note:
        An empty string is returned only to keep the same prototype for all test functions.
    """
    return (test.stderr == '', '')

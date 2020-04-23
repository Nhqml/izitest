$ ./izitestsuite.py --help
usage: izitestsuite.py [-h] [--ref ref] [-q] [-d dir] [-c cat [cat ...]] [-m]
                       [-r [file]]
                       exec

Easily build a test suite.

positional arguments:
  exec                  path to the executable you want to test

optional arguments:
  -h, --help            show this help message and exit
  --ref ref             specify a reference executable
  -q, --quiet           run silently, do not output ANYTHING (even errors)!
  -d dir, --testdir dir
                        path to the test suite directory (default is
                        './tests')
  -c cat [cat ...], --cat cat [cat ...]
                        run only the tests of specified categories
  -m, --memcheck        if set, it will check for any memory leak using
                        valgrind (see https://valgrind.org/)
  -r [file], --report [file]
                        generate an html report (default path is
                        './report.html')

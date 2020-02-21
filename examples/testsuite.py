#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from izitest import *

args = parse_args()
testfiles = discover_testsuite(args.testdir, args.cat)
run_testsuite(args, testfiles)

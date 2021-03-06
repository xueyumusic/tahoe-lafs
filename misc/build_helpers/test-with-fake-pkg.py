#!/usr/bin/env python

# We put a fake "pycryptopp-0.5.13" package on the PYTHONPATH so that
# the build system thinks pycryptopp-0.5.13 is already installed. Then
# we execute 'setup.py trial'. If the build system is too naive/greedy
# about finding dependencies, it will latch onto the
# "pycryptopp-0.5.13" and then will be unable to satisfy the
# requirement (from _auto_deps.py) for pycryptopp >= 0.5.20 (or
# pycryptopp >= 0.5.14, depending on machine architecture). This is
# currently happening on trunk, see #1190. So with trunk, running
# test-with-fake-pkg.py shows a failure, but with the ticket1190
# branch, test-with-fake-pkg.py succeeds.

import os, subprocess, sys

fakepkgdir = 'misc/build_helpers/fakepkgs'
fakepkgname = "pycryptopp"
fakepkgversion = "0.5.13"
testsuite = "allmydata.test.test_backupdb"

pkgdirname = os.path.join(os.getcwd(), fakepkgdir, '%s-%s.egg' % (fakepkgname, fakepkgversion))

try:
    os.makedirs(pkgdirname)
except OSError:
    # probably already exists
    pass

os.environ['PYTHONPATH']=pkgdirname+os.pathsep+os.environ.get('PYTHONPATH','')
sys.exit(subprocess.call([sys.executable, 'setup.py', 'trial', '-s', testsuite], env=os.environ))

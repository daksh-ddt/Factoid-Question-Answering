# -*- coding: utf-8 -*-
import os
import glob
import unittest


def build_test_suite():
    suite = unittest.TestSuite()
    for testcase in glob.glob('case_***.py'):
        modname = os.path.splitext(testcase)[0]
        print 'Adding', modname[5:]
        module = __import__(modname, {}, {}, ['1'])
        suite.addTest(unittest.TestLoader().loadTestsFromModule(module))
    print '\n'
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = build_test_suite()
    runner.run(test_suite)
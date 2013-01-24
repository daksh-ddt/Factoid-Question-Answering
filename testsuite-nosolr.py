# -*- coding: utf-8 -*-

import unittest
import standalonenosolr

class Case1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def runTest(self):
        tester = standalonenosolr.StandAloneTestNoSolr()
        results = tester.runStandAloneTest("who was the first president of the united states?")
        found = 0
        for result in results:
            print 'Result %s' % result[0]
            if result[0].lower() == "george washington":
                found = 1
        assert found == 1

class Case2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def runTest(self):
        tester = standalonenosolr.StandAloneTestNoSolr()
        results = tester.runStandAloneTest("what is the capital of russia?")
        found = 0
        for result in results:
            print 'Result %s' % result[0]
            if result[0].lower() == "moscow":
                found = 1
        assert found == 1

class Case3(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def runTest(self):
        tester = standalonenosolr.StandAloneTestNoSolr()
        results = tester.runStandAloneTest("what is the largest city in idaho?")
        found = 0
        for result in results:
            print 'Result %s' % result[0]
            if result[0].lower() == "boise, idaho":
                found = 1
        assert found == 1

def suite():
    suite1 = unittest.makeSuite(Case1)
    #suite2 = unittest.makeSuite(Case2)
    #suite3 = unittest.makeSuite(Case3)
    #return unittest.TestSuite((suite1, suite2, suite3))
    return unittest.TestSuite(suite1)

if __name__ == "__main__":
    unittest.main()
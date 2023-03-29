import unittest

import HtmlTestRunner

from curs10.alerts import Alerts
from curs10.context_meniu import ContextMenu
from curs10.key_press import Keyboard
from curs9.unit_test import Test
from tema_curs9.tema_unittests import Login


class TestSuite(unittest.TestCase):

    ### numele met este predefinit si NU trebuie schimbat
    def test_suite(self):

    ## am creat un ob al clasei TestSuite
    #prin ob creat (test_to_run) vom accesa met Test
        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)

        ])
        ### facem un test runner HTML care va genera pt noi rapoarte
        ## rap este human-friendly si poate fi inteles si de catre pers care nu stiu cod
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports= True,
            report_name= "My report name",
            report_title ="My first report"
        )
        runner.run(test_to_run)

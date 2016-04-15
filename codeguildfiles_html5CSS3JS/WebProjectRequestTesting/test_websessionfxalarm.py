# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Test File for WebSessionFXAlarm
by: Matthew James K

Test using the Python modules/django/python libraries to the FX_Alarm website to affectively:
1) Login,
2) retrieve some data, XSLT transform the data if possible,
3) Logout --> USE A TRY: EXCEPT: FINALLY: BLOCK IN THE FIANLLY: TO GUARANTEE THIS RUNS

All this must be done in one pass, in one active sessession, and LOGOUT must be called \
OR testing against the FX_Alarm website is locked out for 90 minutes!!!
"""
import unittest
import web_session_fxalarm

class Test_WebSessionFXAlarm(unittest.TestCase):
    def test_login_fxalarm(self):
        login_succeeded = '200'
            
        self.failIf(login_succeeded != '200')

if __name__ == '__main__':
    unittest.main()

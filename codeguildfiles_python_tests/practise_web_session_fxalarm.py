# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild
Code File for WebSessionFXAlarm
by: Matthew James K

Test using the Python modules/django/python libraries to the FX_Alarm website to affectively:
1) Login,
2) retrieve some data, XSLT transform the data if possible,
3) Logout --> USE A TRY: EXCEPT: FINALLY: BLOCK IN THE FIANLLY: TO GUARANTEE THIS RUNS

All this must be done in one pass, in one active sessession, and LOGOUT must be called \
OR testing against the FX_Alarm website is locked out for 90 minutes!!!
"""
import sys
import requests as request
import json

class WebSessionFXAlarm(object):
    """
    Web login, logout, session testing.
    """
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def __eq__(self, **kwargs):
        return super().__eq__(**kwargs)

    def __repr__(self, **kwargs):
        return super().__repr__(**kwargs)

    def login_fxalarm(fx_alarm_site):
        """
        Attempts to login to the FX_Alarm website, and receive a valid session state
        :param 1: fx_alarm_site as the FX_Alarm website to attempt to login to
        :returns: True if the operation succeeded with status 200, otherwise False
        """
        request
        
        return
# end class WebLoginLogoutTest(object):
    
if __name__ == "__main__":
    sys.exit(int(main() or 0))
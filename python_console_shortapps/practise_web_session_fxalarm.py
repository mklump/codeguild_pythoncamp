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

    def login_fxalarm(self, fx_alarm_site):
        """
        This class function attempts to login to the specified fx_alarm_site website,
        AND RECEIVE a valid session state for recieving data.
        :param fx_alarm_site: as the FX_Alarm website to attempt to login to
        :return: True if the operation succeeded with status 200, otherwise False
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        request = requests.post("http://httpbin.org/post", data=payload)
        print(r.text)
        {
          "form": {
            "key2": "value2",
            "key1": "value1"
          },
        }
        return

    def logout_fxalaram(self, fx_alarm_site):
        """
        This class function attempts to logout from the specified FX_Alarm website,
        and be released from what was WHAT WAS A VALID session state that was properly
        receiving HTML DOM object parsable FX daily price acceleration data.
        :param fx_alarm_site: as the FX_Alarm website to attempt to login to
        :return: True if the operation succeeded with status 200, otherwise False
        """
# end class WebLoginLogoutTest(object):
    
if __name__ == "__main__":
    sys.exit(int(main() or 0))
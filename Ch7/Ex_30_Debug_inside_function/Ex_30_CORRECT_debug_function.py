# debugging inside functions

import datetime


def happybirthday(dob, name):
    thetype = type(dob)
    thedate = datetime.datetime.now()
    month = thedate.month
    day = thedate.day
    if thetype == datetime.datetime:
        dobmonth = dob.month
        dobday = dob.day
        if dobmonth == month and \
                dobday == day:
            print('Happy Birthday', name)
        else:
            print('Please enter a birthday')


name = 'Mary Lee'
dob = datetime.datetime(1976, 6, 15)
happybirthday(dob, name)

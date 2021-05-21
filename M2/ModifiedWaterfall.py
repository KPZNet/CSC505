__author__ = "Kenneth Ceglia"
__copyright__ = "Open Source"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kenneth Ceglia"
__email__ = "kenceglia@gmail.com"
__status__ = "Course Work"

""" ModifiedWaterfall enables user to input
    a framework activity by name.
    ModifiedWaterfall returns the activity
    definition and details in a well-formatted
    printout
"""
from datetime import datetime
import time
import json

try:
    #Start for marking execution time
    start_time = time.time()

    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\nDate Time : ", dt_string)

    def waterFallActivity():
        id = 0
        title: str = "not set"
        desc: str = "not set"

        def __init__(self):
            id = 0
            title = "not set"
            desc = "not set"

        def setActivityDescription(_title, _desc):
            desc = _desc
            title = _title

        def printActivity(_activity):
            print('not set')




    #Print out execution time
    print("\n\n\nEXECUTION Time : %s seconds " % (time.time() - start_time))

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("Completed")
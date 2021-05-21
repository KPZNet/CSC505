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

    def findActivity(activity, activities):
        retActivity = None
        for index, a in enumerate(activities):
            act = a['Name']
            if act == activity:
                retActivityIndex = index
                retActivity = a
                break
        return retActivity

    def printOutActivities(activity):
        name = activity['Name']
        description = activity['Description']
        actionsList = activity['Actions']
        inputList = activity['InputActivities']
        outputList = activity['OutputActivities']

        print('\n\n')
        print("*** Waterfall Activity ***")
        print('Name of Activity: {0}'.format(name))
        print('Description: {0}'.format(description))
        print('Inputs to Activity: {0}'.format(inputList))
        print('Outputs of Activity: {0}'.format(outputList))
        print("******************")


    def printOutActivity(activity, waterfallModel):
        activs = wfallmodel['Activities']
        a = findActivity(activity, activs)
        if a != None:
            printOutActivities(a)


    with open("WaterfallCyc.json", "r") as read_file:
        wfallmodel = json.load(read_file)

    inp = ''
    while inp != 'done':
        inp = input('Enter Waterfall Activity :')
        if inp != 'done':
            printOutActivity(inp, wfallmodel)

    #Print out execution time
    print("\n\n\nEXECUTION Time : %s seconds " % (time.time() - start_time))

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("Completed")
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

    def findActivity(activity, wfallmodel):
        """
        Searches list of activities to find
        requested activity and return found
        activity

        :param activity: waterfall activity object
        :param wfallmodel: input waterfall database
        :return: activity object
        """
        activities = wfallmodel['Activities']
        retActivity = None
        for index, a in enumerate(activities):
            act = a['Name']
            if act.upper() == activity.upper():
                retActivity = a
                break
        return retActivity

    def printOutActivities(activity):
        """
        Prints out the waterfall activity in a
        nicely formatted output

        :param activity: Waterfall activity object
        """
        name = activity['Name']
        description = activity['Description']
        actionsList = activity['Actions']
        inputList = activity['InputActivities']
        outputList = activity['OutputActivities']

        print('\n\n')
        print("*** Waterfall Activity ***\n")
        print('Name of Activity: {0}'.format(name))
        print('Description: {0}'.format(description))
        print('Actions: {0}'.format(actionsList))
        print('Inputs to \"{1}\" : {0}'.format(inputList, name))
        print('Outputs of \"{1}\" : {0}\n'.format(outputList, name))
        print("**************************")

    def printOutActivity(activity, waterfallModel):
        """
        Finds the requested waterfall activity
        and, if found, prints out the activity
        in a nicely formatted output

        :param activity: activity name to find
        :param waterfallModel: waterfall activity database
        """
        a = findActivity(activity, waterfallModel)
        if a != None:
            printOutActivities(a)

    with open("WaterfallCyc.json", "r") as read_file:
        wfallmodel = json.load(read_file)

    inp = 'GO'
    exitList = ['DONE', 'EXIT', 'QUIT', 'STOP', 'OVER', 'OUT']
    while False == ( inp.upper() in exitList ):
        inp = input('\nEnter Waterfall Activity : ')
        a = findActivity(inp, wfallmodel)
        if a != None:
            printOutActivity(inp, wfallmodel)
        else:
            print("Activity {0} Not Found".format(inp))

    print('Thank you')
    #Print out execution time
    print("\n\n\nEXECUTION Time : %s seconds " % (time.time() - start_time))

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("Completed")
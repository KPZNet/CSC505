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
import json


class ceglia:

    def findActivity(self, activity, wfallmodel):
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

    def printOutActivities(self, activity):
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

    def printOutActivity(self, activity, waterfallModel):
        """
        Finds the requested waterfall activity
        and, if found, prints out the activity
        in a nicely formatted output

        :param activity: activity name to find
        :param waterfallModel: waterfall activity database
        """
        a = self.findActivity(activity, waterfallModel)
        if a != None:
            self.printOutActivities(a)

    def runInput(self):
        with open("WaterfallCyc.json", "r") as read_file:
            wfallmodel = json.load(read_file)

        inp = 'GO'
        conti = True
        exitList = ['DONE', 'EXIT', 'QUIT', 'STOP', 'OVER', 'OUT']
        while conti:
            inp = input('\nEnter Waterfall Activity : ')
            conti = (False == (inp.upper() in exitList))
            if conti == True:
                a = self.findActivity(inp, wfallmodel)
                if a != None:
                    self.printOutActivity(inp, wfallmodel)
                else:
                    print("Activity {0} Not Found".format(inp))

        print('Thank you')


try:

    c = ceglia()
    c.runInput()

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("")

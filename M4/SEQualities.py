__author__ = "Kenneth Ceglia"
__copyright__ = "Open Source"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kenneth Ceglia"
__email__ = "kenceglia@gmail.com"
__status__ = "Course Work"

""" Manages SW Team member qualities and
    personality traits
"""
import json


class SWTeam:

    def findActivity(self, activity, swqualities):
        print("stub")

    def printOutActivity(self, quality):
        print("stub")

    def printAllTeam(self, swTeam):
        print("ALL Team")

    def runInput(self):
        """
        Run program, ask user for SW Team Member
        and their desired qualities and personality
        traits are printed out
        """

        with open("Qualities.JSON", "r") as read_file:
            swteamlist = json.load(read_file)

        conti = True
        exitList = ['DONE', 'EXIT', 'QUIT', 'STOP', 'OVER', 'OUT', 'Q']
        while conti:
            inp = input('\nEnter SW Team Member : ')
            conti = (False == (inp.upper() in exitList))
            if conti == True:
                a = self.findActivity(inp, swteamlist)
                if a == 'ALL':
                    self.printAllTeam(swteamlist)
                if a != None:
                    self.printOutActivity(a)
                else:
                    print("Activity {0} Not Found".format(inp))

        print('Thank you')


try:

    c = SWTeam()
    c.runInput()

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("")

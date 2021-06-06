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

    def FindTrait(self, input, swqualities):
        quals = swqualities['Qualities']
        trait = quals[input]
        return trait

    def PrintTrait(self, trait):
        for t in trait:
            descript = trait[t]
            print("{0} : {1}".format(t, descript))


    def runInput(self):
        """
        Run program, ask user for SW Team Member
        and their desired qualities and personality
        traits are printed out
        """

        with open("Qualities.JSON", "r") as read_file:
            traitList = json.load(read_file)

        conti = True
        exitList = ['DONE', 'EXIT', 'QUIT', 'STOP', 'OVER', 'OUT', 'Q']
        while conti:
            inp = input('\nEnter Personality Trait : ')
            conti = (False == (inp.upper() in exitList))
            if conti == True:
                a = self.FindTrait(inp, traitList)
                if a != None:
                    self.PrintTrait(a)
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

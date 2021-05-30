__author__ = "Kenneth Ceglia"
__copyright__ = "Open Source"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kenneth Ceglia"
__email__ = "kenceglia@gmail.com"
__status__ = "Course Work"

""" Shopping List prints out
    the psuedo code for the shopping list app
    and the tools used to produce the design
    and models
"""
import json


class ShoppingListApp:


    def GetPrintCode(self):
        print('\nPseudo Code in Blocks\n')
        with open("ShoppingList.JSON", "r") as read_file:
            pcode = json.load(read_file)

        for pc in pcode:
            print('Code Block : {0}'.format(pc) )
            codeLines = pcode[pc]
            for l in codeLines:
                print('\t Line : {0}'.format(l) )

    def GetPrintTools(self):
        print('\nTools Used for Designs and Wireframes\n')
        with open("Tools.JSON", "r") as read_file:
            pTools = json.load(read_file)
        toolList = pTools['ToolList']
        for pc in toolList:
            print('Tool : {0}'.format(pc) )

try:
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\nDate Time : ", dt_string)	

    c = ShoppingListApp()
    c.GetPrintCode()
    c.GetPrintTools()

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("")

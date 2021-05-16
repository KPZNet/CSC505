__author__ = "Kenneth Ceglia"
__copyright__ = "Open Source"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kenneth Ceglia"
__email__ = "kenceglia@gmail.com"
__status__ = "Course Work"

""" PYActivity prints out eight major
    software engineering 
    Umbrella steps that are common to
    most Software Engineering processes.
    Umbrella activites are done continuously 
    throughout the duration of a project
"""
from datetime import date
import time


try:
    #Start for marking execution time
    start_time = time.time()

    UmbrellaActivities = []
    UmbrellaActivities.append("software project tracking")
    UmbrellaActivities.append("risk management")
    UmbrellaActivities.append("software quality assurance")
    UmbrellaActivities.append("measurement")
    UmbrellaActivities.append("software configuration management")
    UmbrellaActivities.append("reusability management")
    UmbrellaActivities.append("work product preparation and production")


    print("\nUmbrella Activities\n\n")
    for i, umbrellaActivity in enumerate(UmbrellaActivities):
        print("{0}: {1} ".format(i+1, umbrellaActivity))


    #Print out execution time
    print("\n\n\nEXECUTION Time : %s seconds " % (time.time() - start_time))

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("Completed")



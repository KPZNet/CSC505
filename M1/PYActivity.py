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
from datetime import datetime
import time


try:
    #Start for marking execution time
    start_time = time.time()

    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\nDate Time : ", dt_string)	


    UmbrellaActivities = []
    UmbrellaActivities.append("Software project tracking")
    UmbrellaActivities.append("Risk management")
    UmbrellaActivities.append("Software quality assurance")
    UmbrellaActivities.append("Technical Reviews")
    UmbrellaActivities.append("Measurement")
    UmbrellaActivities.append("Software configuration management")
    UmbrellaActivities.append("Reusability management")
    UmbrellaActivities.append("Work product preparation and production")

    print("Umbrella Activities\n")
    for i, umbrellaActivity in enumerate(UmbrellaActivities):
        print("{0}: {1} ".format(i+1, umbrellaActivity))


    #Print out execution time
    print("\n\n\nEXECUTION Time : %s seconds " % (time.time() - start_time))

except(Exception) as e:
    print("<<< EXCEPTION >>>")
    print(e)
finally:
    print("Completed")



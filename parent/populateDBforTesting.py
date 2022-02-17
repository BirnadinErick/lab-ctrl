# Imports
import sys

from datetime import datetime
from random import choice, randint, random

from watchdog.models import Child
from smarttasks.models import STask
from error.models import Error


# BEGIN
victims = []

# Populate Children Records
def populateChildren():
    nicknames = "lina.lana.mina.miana.elsa.maya.ralph.poko.soku.bella".split(".")
    for i in range(10):
        c:Child = Child(
            nickname=nicknames[i],
            ip=f"192.168.1.{i}",
            isIPStatic=choice([True, False]),
            nurse_check_interval=randint(1,3),
            nurse_check_type=randint(1,3)
        )

        c.save()
        victims.append(c.nickname)


# Populate STasks Records
def populateSTasks():
    snames = "shutdown.restart.update".split(".")
    for i in range(3):
        s:STask = STask(
            name=snames[i],
            instructions="Hello World this is a test STask"
        )
        s.save()
        victims.append(s.sid)

# Populate Errors Records
def populateErrors(victims_l):
    etitles = "Update Faileds. Shutdown Complete. Errro 2003. Hey There. Access Denied".split(".")
    for i in range(5):
        e:Error = Error(
            title=etitles[i],
            isHandled=False,
            timestamp=datetime.now().timestamp(),
            victim=str(victims_l[i]),
            ecode=choice([
                randint(1001, 1499),
                randint(1501, 1999)
            ])
        )
        e.save()

# END

if __name__ == '__main__':
    if sys.argv[1]:
        print("Populating Children...")
        populateChildren()
        print("Done Children!")
    
    if sys.argv[2]:
        print("Populating Smart Tasks...")
        populateSTasks()
        print("Done Smart Tasks!")
    
    if sys.argv[3]:
        print("Populating Errors...")
        populateErrors()
        print("Done Errors!")

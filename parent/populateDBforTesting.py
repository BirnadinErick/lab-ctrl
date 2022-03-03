# Imports
import sys
from datetime import datetime
from random import choice, randint
import logging

from django.db.models import Model

from watchdog.models import Child
from smarttasks.models import STask
from error.models import Error


# BEGIN
victims = []

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(name)s] %(msg)s"
)
logger = logging.getLogger("Populate_DB")

# check whether input is child or not  
def is_child(obj:Model) -> bool:
    try:
        logger.debug(f"Check the {obj.__str__()}")
        if obj.isalpha:
            logger.debug("Given obj is a child")
            return True
    except AttributeError:
        return False
    except Exception as e:
        logger.warning(e.__str__())
        return None

# Populate Children Records
def populateChildren():
    logger.info("Populating children...")
    nicknames = "lina.lana.mina.miana.elsa.maya.ralph.poko.soku.bella".split(".")
    logger.debug(f"Following children will be populated:-\n\t{nicknames}\n")
    for i in range(10):
        child_nickname = nicknames[i]
        c:Child = Child(
            nickname=child_nickname,
            ip=f"192.168.1.{i}",
            isIPStatic=choice([True, False]),
            nurse_check_interval=randint(1,3),
            nurse_check_type=randint(1,3)
        )
        logger.debug(
            f"""
                Child {i}
                nickname: {c.nickname}
                ip: {c.ip}
                isIPStatic: {c.isIPStatic}
                nurse_check_interval: {c.nurse_check_interval}
                nurse_check_type: {c.nurse_check_type}
            """
        )
        c.save()
        victims.append(c.ip)
        logger.info(f"Appended {c.nickname} to victims list")


# Populate STasks Records
def populateSTasks():
    logger.info("Populating children...")
    snames = "shutdown.restart.update".split(".")
    logger.debug(f"Following STaks will be populated:-\n\t{snames}\n")
    for i in range(3):
        s:STask = STask(
            name=snames[i],
            instructions="Hello World this is a test STask"
        )
        logger.debug(
            f"""
            STasks {i}
                name={snames[i]}
            """
        )
        s.save()
        victims.append(s.sid)
        logger.info(f"Appended {s.sid} to victims list")


# Populate Errors Records
def populateErrors(victims_l):
    logger.info("Populating Errors...")
    etitles = "Update Faileds. Shutdown Complete. Errro 2003. Hey There. Access Denied".split(".")
    logger.debug(f"Following STaks will be populated:-\n\t{etitles}\n")
    for i in range(5):
        etitle, e_time = etitles[i], datetime.now().timestamp()
        I = randint(5,12) # to get STasks also
        e_victim = str(victims_l[I])
        e:Error = Error(
            title=etitle,
            isHandled=False,
            timestamp=e_time,
            victim=e_victim,
            # child -> ecode = (1500, 2000)
            # else stask -> ecode = (1000, 1500)
            ecode=1850 if is_child(e_victim) else 1005
        )
        logger.debug(
            f"""
            Error {i}
                title: {e.title}
                isHandled: False
                timestamp: {e.timestamp}
                victim: {e.victim}
                ecode: {e.ecode}
            """
        )
        e.save()
        logger.info(f"Created {e.eid}!")
  
# END

if __name__ == '__main__':
    if sys.argv[1]:
        populateChildren()
        print("Done Children!")
    
    if sys.argv[2]:
        populateSTasks()
        print("Done Smart Tasks!")
    
    if sys.argv[3]:
        populateErrors(victims)
        print("Done Errors!")

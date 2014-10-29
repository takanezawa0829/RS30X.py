import sys
from os import pardir
sys.path.append(pardir)

from RS30X import RS30XController
import time

id = 1

con = RS30XController()

con.initMemMap(id)

con.move(id, 900)

time.sleep(2)

con.move(id, -900)

time.sleep(2)

con.move(id, 900, 500)

time.sleep(2)

con.move(id, -1200, 1000)

time.sleep(2)

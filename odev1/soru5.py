from random import randint
from datetime import datetime
import time

i = 0
hafta = 1
secilenler = [0,0,0,0,0,0]
for n in secilenler:
    while i < len(secilenler):
        secilen = randint(1,49)
        if secilen not in secilenler:
            secilenler[i] = secilen
            i += 1
    print("{} haftanin sonuçları:".format(hafta))
    print(datetime.date(datetime.random()) ,sorted(secilenler))
    time.sleep(5)
    hafta += 1
    i = 0

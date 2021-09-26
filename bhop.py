import pymem.process
from threading import Thread, currentThread
import keyboard
import time


def BunnyHop():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    dwLocalPlayer = 14296140
    dwForceJump = 86401988
    m_fFlags = 260
    t = currentThread()
    while getattr(t, "do_run", True):
        if pm.read_int(client + dwLocalPlayer):
            a = pm.read_int(client + dwLocalPlayer)
            b = client + dwForceJump
            c = pm.read_int(a + m_fFlags)
            if keyboard.is_pressed("space"):
                if c == 257:
                    pm.write_int(b, 5)
                    time.sleep(0.17)
                    pm.write_int(b, 4)


def main():
    t = Thread(target=BunnyHop)
    t.start()
    time.sleep(5)
    t.do_run = False


if __name__ == "__main__":
    main()

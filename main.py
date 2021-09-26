import pymem
import re

def wh(state):
    try:
        processName = 'csgo.exe'
        pm = pymem.Pymem(processName)
        client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')
        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                                     clientModule).start() + 2
        pm.write_uchar(address, state)
        pm.close_process()
    except:
        print('something went wrong')


wh(1) #2 to off

import time
import ctypes
import pymem
import keyboard
from threading import currentThread

dwClientState = 5804012
dwLocalPlayer = 14296140
m_hMyWeapons = 11784
dwEntityList = 81511860
m_iItemDefinitionIndex = 12218
m_OriginalOwnerXuidLow = 12752
m_iItemIDHigh = 12240
m_nFallbackPaintKit = 12760
m_iAccountID = 12248
m_nFallbackStatTrak = 12772
m_nFallbackSeed = 12764
m_flFallbackWear = 12768

user32 = ctypes.windll.user32

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


def GetWindowText(handle, length=100):
    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value.decode('cp1252')


def GetForegroundWindow():
    return user32.GetForegroundWindow()


def change_skin():
    skins = []
    with open("skins.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            skin = line.split("=")[-1].strip()

            skins.append(int(skin))
    akpaint = skins[0]
    awppaint = skins[1]
    usppaint = skins[2]
    deaglepaint = skins[3]
    glockpaint = skins[4]
    fivepaint = skins[5]
    ppaint = skins[6]
    tecpaint = skins[7]
    mapaint = skins[8]
    mspaint = skins[9]
    galilpaint = skins[10]
    famaspaint = skins[11]
    augpaint = skins[12]
    sgpaint = skins[13]
    scoutpaint = skins[14]
    macpaint = skins[15]
    mpsevpaint = skins[16]
    mpninpaint = skins[17]
    pppaint = skins[18]
    pneunpaint = skins[19]
    umppaint = skins[20]
    magpaint = skins[21]
    novpaint = skins[22]
    sawpaint = skins[23]
    xmpaint = skins[24]
    revolverpaint = skins[25]
    czpaint = skins[26]
    dualiespaint = skins[27]
    p2000paint = skins[28]
    mp5paint = skins[29]
    negevpaint = skins[30]
    m249paint = skins[31]
    g3sg1paint = skins[32]
    scarpaint = skins[33]
    engine_state = pm.read_int(engine + dwClientState)
    t = currentThread()
    while getattr(t, "do_run", True):
        print(100)
        if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            time.sleep(1)
            continue
        local_player = pm.read_int(client + dwLocalPlayer)
        if local_player == 0:
            continue
        for i in range(0, 8):
            my_weapons = pm.read_int(local_player + m_hMyWeapons + (i - 1) * 0x4) & 0xFFF
            weapon_address = pm.read_int(client + dwEntityList + (my_weapons - 1) * 0x10)
            if weapon_address:
                weapon_id = pm.read_short(weapon_address + m_iItemDefinitionIndex)

                weapon_owner = pm.read_int(weapon_address + m_OriginalOwnerXuidLow)
                seed = 420
                if weapon_id == 7:
                    fallbackpaint = akpaint
                    seed = 661
                elif weapon_id == 9:
                    fallbackpaint = awppaint
                    seed = 420
                elif weapon_id == 61:
                    fallbackpaint = usppaint
                    seed = 420
                elif weapon_id == 1:
                    fallbackpaint = deaglepaint
                    seed = 420
                elif weapon_id == 4:
                    fallbackpaint = glockpaint
                    seed = 420
                elif weapon_id == 3:
                    fallbackpaint = fivepaint
                    seed = 420
                elif weapon_id == 36:
                    fallbackpaint = ppaint
                    seed = 420
                elif weapon_id == 30:
                    fallbackpaint = tecpaint
                    seed = 420
                elif weapon_id == 16:
                    fallbackpaint = mapaint
                elif weapon_id == 60:
                    fallbackpaint = mspaint
                elif weapon_id == 13:
                    fallbackpaint = galilpaint
                elif weapon_id == 10:
                    fallbackpaint = famaspaint
                elif weapon_id == 8:
                    fallbackpaint = augpaint
                elif weapon_id == 39:
                    fallbackpaint = sgpaint
                elif weapon_id == 40:
                    fallbackpaint = scoutpaint
                elif weapon_id == 17:
                    fallbackpaint = macpaint
                elif weapon_id == 33:
                    fallbackpaint = mpsevpaint
                elif weapon_id == 34:
                    fallbackpaint = mpninpaint
                elif weapon_id == 26:
                    fallbackpaint = pppaint
                elif weapon_id == 19:
                    fallbackpaint = pneunpaint
                elif weapon_id == 24:
                    fallbackpaint = umppaint
                elif weapon_id == 27:
                    fallbackpaint = magpaint
                elif weapon_id == 35:
                    fallbackpaint = novpaint
                elif weapon_id == 29:
                    fallbackpaint = sawpaint
                elif weapon_id == 25:
                    fallbackpaint = xmpaint
                elif weapon_id == 64:
                    fallbackpaint = revolverpaint
                elif weapon_id == 63:
                    fallbackpaint = czpaint
                elif weapon_id == 2:
                    fallbackpaint = dualiespaint
                elif weapon_id == 32:
                    fallbackpaint = p2000paint
                elif weapon_id == 23:
                    fallbackpaint = mp5paint
                elif weapon_id == 28:
                    fallbackpaint = negevpaint
                elif weapon_id == 14:
                    fallbackpaint = m249paint
                elif weapon_id == 11:
                    fallbackpaint = g3sg1paint
                elif weapon_id == 38:
                    fallbackpaint = scarpaint
                else:
                    continue
                pm.write_int(weapon_address + m_iItemIDHigh, -1)
                pm.write_int(weapon_address + m_nFallbackPaintKit, fallbackpaint)
                pm.write_int(weapon_address + m_iAccountID, weapon_owner)
                pm.write_int(weapon_address + m_nFallbackStatTrak, 187)
                pm.write_int(weapon_address + m_nFallbackSeed, seed)
                pm.write_float(weapon_address + m_flFallbackWear, float(0.000001))
        if keyboard.is_pressed("f6"):
            try:
                pm.write_int(engine_state + 0x174, -1)
            except:
                pass


if __name__ == "__main__":
    change_skin()
import libtcodpy as lib
import variables as var

def handlekeys():
    key = lib.console_check_for_keypress()
    if key.vk == lib.KEY_ENTER and key.lalt:
        # alt + enter: toggle fullscreen
        lib.console_set_fullscreen(not lib.console_is_fullscreen())
    elif key.vk == lib.KEY_ESCAPE:
        # exit game
        return True

    # movement keys
    if lib.console_is_key_pressed(lib.KEY_UP):
        var.playery -= 1
    elif lib.console_is_key_pressed(lib.KEY_DOWN):
        var.playery += 1
    elif lib.console_is_key_pressed(lib.KEY_LEFT):
        var.playerx -= 1
    elif lib.console_is_key_pressed(lib.KEY_RIGHT):
        var.playerx += 1

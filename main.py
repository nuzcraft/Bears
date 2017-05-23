import libtcodpy as lib
import variables as var
from handlekeys import handlekeys
from renderdungeon import renderdungeon

lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GRAYSCALE | lib.FONT_LAYOUT_TCOD)
lib.console_init_root(var.screen_width, var.screen_height, 'Bears', False)
lib.sys_set_fps(var.limit_fps)

while not lib.console_is_window_closed():
    renderdungeon()
    var.player.draw()
    lib.console_blit(var.dungeon_con, 0, var.dungeon_con_y, var.screen_width, var.screen_height, 0, 0, 0)
    lib.console_flush()
    # for some reason, the first run flushes this to screen
    if not var.first_run:
        var.player.clear()
    else:
        var.first_run = 0

    # handle keys and exit if needed
    exit_game = handlekeys()
    if exit_game:
        break

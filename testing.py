"""main game loop"""from bearlibterminal import terminalimport variables as varfrom handle_keys import handle_keysfrom render_map import render_mapterminal.open()while var.player_action != 'exit':    # get the action of the player, if any    var.player_action = handle_keys()    # print the map    render_map()    # print the player    terminal.printf(var.player_x - var.map_offset_x, var.player_y - var.map_offset_y, var.player_char)    # refresh it to the screen    terminal.refresh()    # erase the player    terminal.printf(var.player_x - var.map_offset_y, var.player_y - var.map_offset_y, ' ')    if var.player_action == 'exit':        terminal.close()
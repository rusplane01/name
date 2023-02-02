
def menu():

    menu = True
    mixer.music.load("sounds/menu")
    mixer.music.play()

    while menu:

        for e in event.get():
            if e.type == QUIT:
                menu = False

        time.delay(15)
        pos_x, pos_y = mouse.get_pos()

        win.blit(bg, (0, 0))
        win.blit(gname, (320, 70))

        btn_start.draw(15, 5)
        btn_control.draw(10, 5)
        btn_exit.draw(37, 5)

        for e in event.get():
            if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                menu = False
                res_pos()
                lvl_1()
            
            if btn_control..rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                menu = False
                rules()

            if btn_exit.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                clck.play()
                menu = False
                a = 0

            if e.type == QUIT:
                menu = False
                a = 0
        display.update()

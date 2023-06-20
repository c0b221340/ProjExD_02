import sys
import pygame as pg
import random 

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bom_r = pg.Surface((20,20))
    pg.draw.circle(bom_r,(255, 0, 0),(10,10),10)
    bom_r.set_colorkey((0, 0, 0))
    bom_rx = random.randint(0, WIDTH - 20)
    bom_ry = random.randint(0, HEIGHT - 20)
    bom_rct = bom_r.get_rect()
    bom_rct.center = bom_rx, bom_ry
    clock = pg.time.Clock()
    tmr = 0
    vx = 5
    vy = 5
    # print(f"{bom_rx},{bom_ry}")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bom_r, bom_rct)
        bom_rct.move_ip((vx,vy))
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
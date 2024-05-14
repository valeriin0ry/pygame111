import pygame
pygame.init()
ekraani_pind = pygame.display.set_mode((800, 600))
ekraani_pind.fill((0, 0, 255))
pygame.display.set_caption("Minu esimene pygame")
pygame.draw.circle(ekraani_pind, (0, 128, 0), (400, 250), 100, 0)  
pygame.draw.line(ekraani_pind, (139, 69, 19), (400, 500), (400, 300), 50)
pygame.draw.polygon(ekraani_pind, (169, 169, 169), [(0, 500), (0, 300), (100, 500)], 0)
pygame.draw.ellipse(ekraani_pind, (0, 100, 0), [350, 200, 100, 150], 0)
pygame.draw.rect(ekraani_pind, (0, 255, 0), [0, 500, 800, 100])
pygame.draw.arc(ekraani_pind, (255, 255, 255), [100, 0, 600, 100], 0, 3.14, 20)
pilt1 = pygame.image.load("audi.jpg")
pilt1 = pygame.transform.scale(pilt1, (200, 200))
ekraani_pind.blit(pilt1, (600, 400))
tekst = "Valerii Pygame"
meie_font = pygame.font.SysFont("Times New Roman", 36)
teksti_pilt = meie_font.render(tekst, False, (250, 250, 100))
ekraani_pind.blit(teksti_pilt, (300, 30))
pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()




#ristkylik1 = pygame.Rect(100, 300, 100, 100)
#pygame.draw.rect(ekraani_pind, (0, 255, 0), ristkylik1)



#joon (line): pygame.draw.line(aken, värv, algus_pos, lõpp_pos, paksus)
#ristkülik (rect): pygame.draw.rect(screen, värv, [x, y, w, h], joone_paksus)
#ring (circle): pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
#hulknurk (polygon): pygame.draw.polygon(screen, värv, koordinaatide_loend, joone_paksus)
#ovaal (ellipse): pygame.draw.ellipse(screen, värv, [x, y, r1, r2], joone_paksus)
#kaar (arc): pygame.draw.arc(screen, värv, ristküliku_koordinaadid, start_nurk, lõpp_nurk, joone_paksus)
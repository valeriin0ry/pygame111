import pygame
pygame.init()
ekraani_pind = pygame.display.set_mode((800, 600))
ekraani_pind.fill((135, 206, 250))
pygame.display.set_caption("Minu esimene pygame")
pygame.draw.circle(ekraani_pind, (0, 128, 0), (400, 250), 100, 0)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (200, 100), 40)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (240, 100), 40)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (280, 100), 40)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (220, 140), 40)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (260, 140), 40)
pygame.draw.line(ekraani_pind, (139, 69, 19), (400, 500), (400, 300), 50)
pygame.draw.line(ekraani_pind, (0, 0, 255), (100, 50), (100, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (200, 50), (200, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (300, 50), (300, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (400, 50), (400, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (500, 50), (500, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (600, 50), (600, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (700, 50), (700, 150), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (150, 100), (150, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (250, 100), (250, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (350, 100), (350, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (450, 100), (450, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (550, 100), (550, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (650, 100), (650, 250), 1)
pygame.draw.line(ekraani_pind, (0, 0, 255), (750, 100), (750, 250), 1)
pygame.draw.polygon(ekraani_pind, (169, 169, 169), [(0, 500), (0, 300), (100, 500)], 0)
pygame.draw.ellipse(ekraani_pind, (0, 100, 0), [350, 200, 100, 150], 0)
pygame.draw.rect(ekraani_pind, (0, 255, 0), [0, 500, 800, 100])
pygame.draw.arc(ekraani_pind, (255, 255, 255), [100, 0, 600, 100], 0, 3.14, 20)
pilt1 = pygame.image.load("audi777.png")
pilt1 = pygame.transform.scale(pilt1, (200, 200))
ekraani_pind.blit(pilt1, (600, 400))
tekst = "audi namoknet :("
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
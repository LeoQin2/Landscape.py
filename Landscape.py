import pygame

import time
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

moonx = 200
cloud_x = -20
red = 100
green = 60
blue = 150
size = 40

frame = 0

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        

    if red !=0 and blue == 150:
        red -= 2

    elif green !=0 and red == 0:
        green -= 1

    elif blue !=0 and green == 0:
        blue -= 5

    else:
        red += 2
        green += 1
        blue += 5

    screen.fill((red, green, blue))

#moving
    x = moonx - 320
    y = 1/520* x * x + 75
    moonx += 6

    size += 0.5

    if moonx >= 320:
        size -= 1

    pygame.draw.circle(screen, (255,255,255), (moonx, y), (size))


    if moonx > 680:
        moonx = -40
        size = 20

#cloud
   
    cloud_x += 2
    if cloud_x > 680:
        cloud_x = -80

    pygame.draw.circle(screen, (169,169,169), (cloud_x, 25), (23))
    pygame.draw.circle(screen, (169,169,169), (cloud_x + 15, 34), (23))
    pygame.draw.circle(screen, (169,169,169), (cloud_x + -10, 44), (19))

    if cloud_x > 680:
        cloud_x = -20

    



#Landscape
    Border_points = (
        (0, 304),
        (52, 301),
        (103, 289),
        (161, 285),
        (194, 283),
        (229, 296),
        (291, 312),
        (350, 322),
        (402, 327),
        (449, 336),
        (498, 359),
        (538, 390),
        (580, 420),
        (616, 461),
        (631, 478),
    )

    Triangle = (
        (0, 480),
        (0, 304),
        (640, 480),
    )

    Land = (
        (257, 303),
        (285, 285),
        (314, 279),
        (349, 267),
        (404, 255),
        (454, 246),
        (503, 237),
        (548, 233),
        (624, 209),
        (426, 331),
        (460, 341),
        (507, 365),
        (552, 398),
        (583, 424),
        (613, 457),
        (631, 476),
    )

    Land2 = (
        (416, 260),
        (429, 377),
        (640, 480),
        (640, 205),
    )

    Line = (
        (636, 478),
        (257, 304),
        (233, 298),
        (211, 290),
        (196, 284),
        (100, 289),
        (52, 301),
        (0, 303),
    )

    Line2 = (
        (256, 303),
        (286, 284),
        (314, 280),
        (351, 266),
        (504, 236),
        (513, 237),
        (640, 204),
    )

    Mtn = (
        (0, 167),
        (35, 106),
        (75, 84),
        (105, 83),
        (149, 115),
        (165, 155),
        (183, 197),
        (200, 221),
        (227, 257),
        (237, 285),
        (250, 302),
        (233, 298),
        (211, 290),
        (196, 284),
        (100, 289),
        (52, 301),
        (0, 303),
    )

    Line3 = (
        (0, 167),
        (35, 106),
        (75, 84),
        (105, 83),
        (149, 115),
        (165, 155),
        (183, 197),
        (200, 221),
        (227, 257),
        (237, 285),
        (250, 302),
        (233, 298),
        (211, 290),
        (196, 284),
        (100, 289),
        (52, 301),
        (0, 303),
    )

    Mtn2 = (
        (158, 137),
        (186, 120),
        (207, 111),
        (217, 120),
        (226, 116),
        (236, 120),
        (242, 129),
        (254, 146),
        (264, 151),
        (276, 137),
        (291, 124),
        (310, 123),
        (327, 135),
        (344, 158),
        (352, 151),
        (362, 141),
        (381, 124),
        (392, 139),
        (411, 157),
        (421, 153),
        (453, 139),
        (467, 134),
        (474, 127),
        (478, 123),
        (492, 104),
        (508, 94),
        (523, 92),
        (534, 104),
        (534, 123),
        (546, 139),
        (562, 147),
        (580, 132),
        (596, 121),
        (640, 105),
        (640, 204),
        (513, 237), 
        (504, 236),
        (351, 266),
        (314, 280),
        (286, 284),
        (256, 303),
        (250, 302),
        (237, 285),
        (227, 257),
        (200, 221),
        (183, 197),
        (165, 155),
    )

    Snow = (
        (155, 145),
        (163, 166),
        (166, 181),
        (171, 193),
        (173, 205),
        (175, 217),
        (176, 228),
        (172, 246),
        (167, 266),
        (153, 264),
        (161, 238),
        (154, 201),
        (144, 170),
        (141, 158),
    )

    Sand = (
        (222, 208),
        (252, 228),
        (284, 241),
        (308, 252),
        (332, 261),
        (350, 267),
        (310, 280),
        (286, 283),
        (256, 303),
        (242, 274),
        (237, 249),
)
    mtn3 = (
        (344, 158),
        (345, 175),
        (353, 188),
        (372, 195),
        (376, 210),
        (385, 221),
        (404, 238),
        (422, 252),
    )

    mtn4 = (
        (412, 156),
        (422, 167),
        (440, 186),
        (450, 205),
        (459, 221),
        (478, 242),
    )

    snow2 = (
        (493, 104),
        (508, 96),
        (524, 93),
        (533, 104),
        (525, 122),
        (515, 118),
        (497, 128),
        (498, 118),
    )

    river = (
        (638, 164),
        (634, 175),
        (625, 183),
        (612, 198),
        (585, 209),
        (562, 217),
        (547, 227),
    )

    snow3 = (
        (381, 124),
        (362, 141),
        (368, 142),
        (373, 139),
        (378, 147),
        (382, 141),
        (388, 146),
        (392, 139),
    )

    snow4 = (
        (158, 138),
        (151, 149),
        (157, 160),
        (171, 151),
    )

    forest = (
        (110, 288),
        (125, 274),
        (140, 262),
        (148, 261),
        (179, 258),
        (202, 268),
        (225, 273),
        (241, 282),
        (257, 304),
        (232, 297),
        (196, 284),
    )

    ice = (
        (110, 289),
        (128, 296),
        (153, 292),
        (176, 308),
        (196, 306),
        (234, 306),
        (244, 329),
        (257, 304),
        (199, 283),
    )

    sand2 = (
        (246, 330),
        (254, 339),
        (271, 344),
        (284, 352),
        (292, 369),
        (306, 371),
        (328, 368),
        (341, 385),
        (357, 400),
        (387, 412),
        (408, 425),
        (445, 434),
        (472, 438),
        (497, 440),
        (550, 446),
        (552, 441),
        (257, 304),
    )

    mtn5 = (
        (262, 149),
        (276, 191),
        (299, 195),
        (315, 212),
        (334, 230),
        (364, 263),
    )

    mtn6 = (
        (497, 128),
        (494, 137),
        (486, 175),
        (471, 196),
        (457, 214),
    )

    mtn7 = (
        (524, 122),
        (529, 153),
        (540, 176),
        (556, 197),
        (563, 214),
    )

    mtn8 = (
        (8, 303),
        (15, 276),
        (24, 230),
        (30, 199),
        (47, 174),
        (62, 213),
        (74, 202),
        (84, 228),
        (102, 272),
        (106, 289),
        (97, 290),
        (54, 301),
    )

    snow5 = (
        (280, 136),
        (285, 146),
        (294, 142),
        (303, 149),
        (310, 141),
        (316, 151),
        (324, 143),
        (328, 138),
        (310, 125),
        (291, 126),
    )

    snow6 = (
        (46, 102),
        (54, 116),
        (66, 108),
        (77, 128),
        (88, 109),
        (98, 127),
        (106, 116),
        (121, 132),
        (131, 124),
        (144, 138),
        (150, 117),
        (106, 86),
        (77, 86),
        (35, 108),
    )

    pygame.draw.polygon(screen, (26,169,208), (Border_points))
    pygame.draw.polygon(screen, (26,169,208), (Triangle))
    pygame.draw.polygon(screen, (55,79,47), (Land))
    pygame.draw.polygon(screen, (55,79,47), (Land2))
    pygame.draw.lines(screen, (0,0,0), (False), (Line))
    pygame.draw.lines(screen, (0,0,0), (False), (Line2))
    pygame.draw.polygon(screen, (160,160,160), (Mtn))
    pygame.draw.lines(screen, (0,0,0), (False), (Line3))
    pygame.draw.polygon(screen, (160,160,160), (Mtn2))
    pygame.draw.lines(screen,(0,0,0), (False), (Mtn2))
    pygame.draw.polygon(screen, (255,255,255), (Snow))
    pygame.draw.polygon(screen, (210,180,140), (Sand))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn3))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn4))
    pygame.draw.polygon(screen, (255,255,255), (snow2))
    pygame.draw.lines(screen,(26,169,208), (False), (river), (4))
    pygame.draw.polygon(screen, (255,255,255), (snow3))
    pygame.draw.polygon(screen, (255,255,255), (snow4))
    pygame.draw.polygon(screen, (255,255,255), (forest))
    pygame.draw.polygon(screen, (185,232,234), (ice))
    pygame.draw.polygon(screen, (210,180,140), (sand2))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn5))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn6))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn7))
    pygame.draw.polygon(screen,(105,105,105), (mtn8))
    pygame.draw.lines(screen,(0,0,0), (False), (mtn8))
    pygame.draw.polygon(screen, (255,255,255), (snow5))
    pygame.draw.polygon(screen, (255,255,255), (snow6))



#trees

    Tree1x1x1 = 348
    Tree1x1y1 = 293
    Tree1x1x2 = 356
    Tree1x1y2 = 288
    Tree1x1x3 = 362
    Tree1x1y3 = 298

    Tree1x1 = (
        (Tree1x1x1, Tree1x1y1),
        (Tree1x1x2, Tree1x1y2),
        (Tree1x1x3, Tree1x1y3),
        #(348, 293),
        )


    Tree1x2x1 = 354
    Tree1x2y1 = 297
    Tree1x2x2 = 346
    Tree1x2y2 = 300
    Tree1x2x3 = 358
    Tree1x2y3 = 305

    Tree1x2 = (
        (Tree1x2x1, Tree1x2y1),
        (Tree1x2x2, Tree1x2y2),
        (Tree1x2x3, Tree1x2y3),
        #(354, 297),
        )

    Tree1x3x1 = 350
    Tree1x3y1 = 303
    Tree1x3x2 = 350
    Tree1x3y2 = 308
    Tree1x3x3 = 353
    Tree1x3y3 = 310
    Tree1x3x4 = 355
    Tree1x3y4 = 305
    
    Tree1x3 = (
        (Tree1x3x1, Tree1x3y1),
        (Tree1x3x2, Tree1x3y2),
        (Tree1x3x3, Tree1x3y3),
        (Tree1x3x4, Tree1x3y4),
    )

    pygame.draw.polygon(screen, (36,135,33), (Tree1x1))
    pygame.draw.lines(screen,(0,0,0), (False), (Tree1x1))
    pygame.draw.polygon(screen, (36,135,33), (Tree1x2))
    pygame.draw.lines(screen,(0,0,0), (False), (Tree1x2))
    pygame.draw.polygon(screen, (139,69,19), (Tree1x3))
    pygame.draw.lines(screen,(0,0,0), (False), (Tree1x3))

    n = 0
    while n < 20:
        n += 1  
        pygame.draw.polygon(screen, (36,135,33), (Tree1x1))
        pygame.draw.lines(screen,(0,0,0), (False), (Tree1x1))
        pygame.draw.polygon(screen, (36,135,33), (Tree1x2))
        pygame.draw.lines(screen,(0,0,0), (False), (Tree1x2))
        pygame.draw.polygon(screen, (139,69,19), (Tree1x3))
        pygame.draw.lines(screen,(0,0,0), (False), (Tree1x3))

        Tree1x1x1 += 15
        Tree1x1x2 += 15
        Tree1x1x3 += 15
        Tree1x2x1 += 15
        Tree1x2x2 += 15
        Tree1x2x3 += 15
        Tree1x3x1 += 15
        Tree1x3x2 += 15
        Tree1x3x3 += 15
        Tree1x3x4 += 15

        Tree1x1 = (
            (Tree1x1x1, Tree1x1y1),
            (Tree1x1x2, Tree1x1y2),
            (Tree1x1x3, Tree1x1y3),
        )
        Tree1x2 = (
            (Tree1x2x1, Tree1x2y1),
            (Tree1x2x2, Tree1x2y2),
            (Tree1x2x3, Tree1x2y3),
        )
        Tree1x3 = (
            (Tree1x3x1, Tree1x3y1),
            (Tree1x3x2, Tree1x3y2),
            (Tree1x3x3, Tree1x3y3),
            (Tree1x3x4, Tree1x3y4),
        )

    #bubble
    frame += 1
    
    if frame % 100 == 0:
        pygame.draw.circle(screen, (255,255,255), (3, 467), (4))
        pygame.draw.circle(screen, (255,255,255), (20, 466), (4))
        pygame.draw.circle(screen, (255,255,255), (23, 450), (4))
        pygame.draw.circle(screen, (255,255,255), (40, 452), (4))
        pygame.draw.circle(screen, (255,255,255), (49, 467), (4))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()   
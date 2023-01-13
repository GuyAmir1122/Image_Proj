import pygame

max_x = 1000
max_y = 1000
location_x = 0
location_y = 0
while not FINISH:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if location_x > 0:
                    location_x -= 1
            if event.key == pygame.K_RIGHT:
                if location_x < max_x:
                    location_x += 1
            if event.key == pygame.K_UP:
                if location_y > 0:
                    location_y -= 1
            if event.key == pygame.K_DOWN:
                if location_y < max_y:
                    location_y += 1
import pygame
import sys
from button import ImageButton
import os
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 960, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nuclear Dawn")

# Загрузка ресурсов
menu_background = pygame.transform.smoothscale(pygame.image.load(os.path.join("resources/image/background/menu.jpg")), (WIDTH, HEIGHT))

# Шрифты
title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)

# Настройки по умолчанию
settings = {
    "music_volume": 0.5,
    "sound_volume": 0.5,
    "fullscreen": False
}

# Загрузка и воспроизведение музыки меню
pygame.mixer.music.load("resources/music/menu.mp3")
pygame.mixer.music.set_volume(settings["music_volume"])
pygame.mixer.music.play(-1)  # -1 означает бесконечный цикл

buttons_menu = [
        ImageButton(WIDTH//2 - 100, 150, 200, 50, "Новая игра", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 100, 220, 200, 50, "Сохранения", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 100, 290, 200, 50, "Настройки", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 100, 360, 200, 50, "Выход", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
    ]

buttons_setting = [
        ImageButton(WIDTH//2 - 100, 400, 200, 50, "Назад", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 + 120, 200, 40, 40, "+", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 160, 200, 40, 40, "-", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 + 120, 280, 40, 40, "+", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 160, 280, 40, 40, "-", "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
        ImageButton(WIDTH//2 - 100, 340, 200, 50, "Полный экран: ВЫКЛ" if not settings["fullscreen"] else "Полный экран: ВКЛ", 
                   "resources/image/button/button.png", "resources/image/button/button_hover.png", "resources/music/click_button.mp3"),
    ]

def main():
    running = True
    
    while running:
        screen.blit(menu_background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = title_font.render("Меню", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH//2, 100))
        screen.blit(title_text, title_rect)

        for button in buttons_menu:
            button.check_hover(mouse_pos)
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == buttons_menu[0]:
                new_game()
            if event.type == pygame.USEREVENT and event.button == buttons_menu[1]:
                save()
            if event.type == pygame.USEREVENT and event.button == buttons_menu[2]:
                settings_menu()
            if event.type == pygame.USEREVENT and event.button == buttons_menu[3]:
                running = False
                pygame.quit()
                sys.exit()

            for button in buttons_menu:
                button.handle_event(event)

        pygame.display.flip()

def new_game():
    pygame.mixer.music.stop()
    pass

def save():
    pass

def settings_menu():
    running = True
    
    while running:
        screen.blit(menu_background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = title_font.render("Настройки", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH//2, 100))
        screen.blit(title_text, title_rect)

        music_text = button_font.render(f"Громкость музыки: {int(settings['music_volume'] * 100)}%", True, (255, 255, 255))
        screen.blit(music_text, (WIDTH//2 - 150, 170))
        
        sound_text = button_font.render(f"Громкость звуков: {int(settings['sound_volume'] * 100)}%", True, (255, 255, 255))
        screen.blit(sound_text, (WIDTH//2 - 150, 250))

        buttons_setting[5].text = "Полный экран: ВЫКЛ" if not settings["fullscreen"] else "Полный экран: ВКЛ"

        for button in buttons_setting:
            button.check_hover(mouse_pos)
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == buttons_setting[0]:
                running = False
            elif event.type == pygame.USEREVENT and event.button == buttons_setting[1]:
                settings["music_volume"] = min(1.0, settings["music_volume"] + 0.1)
                pygame.mixer.music.set_volume(settings["music_volume"])
            elif event.type == pygame.USEREVENT and event.button == buttons_setting[2]:
                settings["music_volume"] = max(0.0, settings["music_volume"] - 0.1)
                pygame.mixer.music.set_volume(settings["music_volume"])
            elif event.type == pygame.USEREVENT and event.button == buttons_setting[3]:
                settings["sound_volume"] = min(1.0, settings["sound_volume"] + 0.1)
            elif event.type == pygame.USEREVENT and event.button == buttons_setting[4]:
                settings["sound_volume"] = max(0.0, settings["sound_volume"] - 0.1)
            elif event.type == pygame.USEREVENT and event.button == buttons_setting[5]:
                settings["fullscreen"] = not settings["fullscreen"]
                if settings["fullscreen"]:
                    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode((WIDTH, HEIGHT))

            for button in buttons_setting:
                button.handle_event(event)

        pygame.display.flip()

if __name__ == "__main__":
    main()

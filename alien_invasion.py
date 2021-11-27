#!/usr/bin/python3
# -*- coding: UTF-8 -*-    
# Author:liweixin
# FileName:alien_invasion
# DateTime:2021/11/24 11:03
# SoftWare: PyCharm
import pygame
# import sys # 因为导入了game_functions，这里不再需要导入sys了
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建屏幕
    pygame.display.set_caption("Alien Invasion")  # 设置屏幕名称
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例  # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    """创建一群外星人"""
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置背景色
    bg_color = ai_settings.bg_color

    # 开始游戏循环
    while True:
        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        """替换为函数来实现"""
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 调用函数实现屏幕的监控键盘和鼠标事件
        if stats.game_active:
            ship.update()  # 上面捕捉键盘事件，同时调用这个函数实现飞船的移动
            # bullets.update()

            """替换为函数来实现"""
            # 删除已消失的子弹
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)  # bullets移除产生并跑出屏幕的子弹
            # print(len(bullets))
            # # 每次循环时都绘制屏幕
            # screen.fill(bg_color)
            # ship.blitme()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,  screen, stats, sb, ship, aliens, bullets)
        """替换为函数来实现"""
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 调用函数实现屏幕更新

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    run_game()

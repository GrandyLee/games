#!/usr/bin/python3
# -*- coding: UTF-8 -*-    
# Author:liweixin
# FileName:bullet
# DateTime:2021/11/24 16:17
# SoftWare: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船所发生的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        # super(Bullet, self).__init__()  # python2.7语法
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    pass

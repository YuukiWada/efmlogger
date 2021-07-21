# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import serial
import sys
import time
import datetime
import RPi.GPIO as GPIO
from time import sleep
from matplotlib.font_manager import FontProperties#日本語化に必要
from mcp3208_01 import readadc#mcp3208_01.pyをインポート
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# ピンの名前を変数として定義
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
# SPI通信用の入出力を定義
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)
font_path = '/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf'#日本語化
font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
def main():
    ads0 = [0]*100              # ch0格納
    ads1 = [0]*100              # ch1格納
    t = np.arange(0,100,1)
    plt.ion()
    pygame.init()                # Pygameを初期化
    screen = pygame.display.set_mode((300, 100))   # 画面作成(横300×100)
    pygame.display.set_caption("傾斜角度")         # タイトルバー
    font = pygame.font.Font(None, 50)              # 文字の設定
    while True:
        screen.fill((0,0,0))            # 画面のクリア
        result0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)  # ch0のデータ
        result1 = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)  # ch1のデータ
        ad0 = str(result0) # ch0を文字列にする
        ad1 = str(result1) # ch1を文字列にする
        text = font.render(ad0 + "," + ad1 + "", False, (255,255,255))    # 表示する文字の設定
        screen.blit(text, (10, 10))     # レンダ，表示位置
        pygame.display.flip()           # 画面を更新して、変更を反映
        # 温度データのリスト更新
        ads0.pop(99)
        ads1.pop(99)
        ads0.insert(0,float(ad0)) # 文字列にしたデータを少数を含む数値に変換
        ads1.insert(0,float(ad1))
        # グラフ表示設定
        line1, = plt.plot(t*2.43+1.215, ads0, 'b-',label="ch0") # X軸を2秒になるように調整、Y軸更新
        line1.set_ydata(ads0)
        line2, = plt.plot(t*2.43+1.215, ads1, 'r-',label="ch1") # X軸を2秒になるように調整、Y軸更新
        line2.set_ydata(ads1)
        plt.title("Real-time ch0　ch1")
        plt.xlabel("Time [s]")
        plt.ylabel("入力")
        plt.legend()
        plt.grid()
        plt.xlim([1,200])
        plt.ylim([0,4095])
        plt.draw()
        plt.clf()
        for event in pygame.event.get():
            # 終了ボタンが押されたら終了処理
            if event.type == QUIT:
                pygame.quit()
                plt.close()
                sys.exit()
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:35:51 2019

@author: Administrator
"""

#import time

def jisuanDanli(benjin, lilv, tianshu):
    shouyiDanli = benjin * lilvDanli / 100 * tianshu / 365
    return shouyiDanli

def jisuanFuli(benjin, lilv, tianshu):
    shouyiFuli = 0
    for i in range(tianshu):
        yitianShouyi = benjin * lilvFuli / 100 / 365
        benjin += yitianShouyi
        shouyiFuli += yitianShouyi
    return shouyiFuli


if __name__ == '__main__':
    benjin = float(input('请输入本金： '))
    lilvDanli = float(input('请输入单利年利率： '))
    lilvFuli = float(input('请输入复利年利率： '))
    tianshu = int(input('请输入天数： '))
    shouyiDanli = jisuanDanli(benjin, lilvDanli, tianshu)
    shouyiFuli = jisuanFuli(benjin, lilvFuli, tianshu)
    
    print('\n单利总收益为：%.3f\n复利总收益为：%.3f'%(shouyiDanli, shouyiFuli))
    
    if shouyiDanli > shouyiFuli:
        print('\n建议投资单利，利率%.2f%%\n'%(lilvDanli))
#        time.sleep(5)
        lilvFuliPie = lilvFuli
#        print(lilvFuliPie)
        while True: 
            lilvFuli += 0.1
            shouyiFuli = jisuanFuli(benjin, lilvFuli, tianshu)
            if shouyiFuli > shouyiDanli:
                print('复利利率至少达到 %.2f%% 方可与单利持平，此时收益为： %.2f'%(lilvFuli, shouyiFuli))
                break
        while True:
            lilvFuli = lilvFuliPie
            tianshu += 1
            if tianshu > 3650:
                print('10年也赶不上了。')
                break
            shouyiDanli = jisuanDanli(benjin, lilvDanli, tianshu)
            shouyiFuli = jisuanFuli(benjin, lilvFuli, tianshu)
            if shouyiFuli >= shouyiDanli:
                if tianshu > 365:
                    nianshu = tianshu // 365
                    yuxiaTianshu = tianshu % 365
                    if yuxiaTianshu == 0:
                        print('或者复利天数至少达到 %d 整年方可与单利持平，此时收益为： \n单利：%.2f\t复利：%.2f'%(nianshu, shouyiDanli, shouyiFuli))
                    else:
                        print('或者复利天数至少达到 %d 年零 %d 天方可与单利持平，此时收益为： \n单利：%.2f\t复利：%.2f'%(nianshu, yuxiaTianshu, shouyiDanli, shouyiFuli))
                else:
                    print('或者复利天数至少达到 %d 天方可与单利持平，此时收益为： \n单利：%.2f\t复利：%.2f'%(tianshu, shouyiDanli, shouyiFuli))
                break
            
    elif shouyiDanli < shouyiFuli:
        print('\n建议投资复利，利率%.2f%%\n'%(lilvFuli)) 
#        time.sleep(5)
        while True:
            lilvDanli += 0.1
            shouyiDanli = jisuanDanli(benjin, lilvFuli, tianshu)
            if shouyiDanli > shouyiFuli:
                print('单利利率至少达到 %.2f%% 方可与复利持平，此时收益为： %.2f'%(lilvDanli, shouyiDanli))
                break
    else:
        print('在当前投资天数情况下，二者收益都一样。\n若投资多一点天数，则复利收益更多，利滚利滚利滚利！')
        print('若投资天数少于当前天数，则单利收益更高。')
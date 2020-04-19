#!/usr/bin/python3
#-*- encoding: utf-8 -*-

# そのうち機能追加予定
import argparse

parser = argparse.ArgumentParser(description='''
YAMAHA L2TP tunnel config command generator.
''')

args = parser.parse_args()

transport = ''
with open('./conf.txt', 'w') as f:
    for i in range(1, 101, 1):
        f.write('tunnel select ' + str(i) + '\n')
        f.write('tunnel capsulation l2tp\n')
        f.write('ipsec tunnel ' + str(i) + '\n')
        f.write(' ipsec sa policy ' + str(i) + ' ' + str(i) + ' esp 3es-cbc shs-hmac\n')
        f.write(' ipsec ike keepalive log ' + str(i) + ' off\n')
        f.write(' ipsec ike keepalive use ' + str(i) + ' off\n')
        f.write(' ipsec ike nat-traversal ' + str(i) + ' on\n')
        f.write(' ipsec ike pre-shared-key ' + str(i) + ' text key-phrase\n')
        f.write(' ipsec ike remote address ' + str(i) + ' any\n')
        f.write('l2tp tunnel auth off\n')
        f.write('l2tp tunnel disconnect time off\n')
        f.write('ip tunnel tcp mss limit auto\n')
        f.write('tunnel enable ' + str(i) + '\n')
        transport += 'ipsec transport ' + str(i) + ' ' + str(i) + ' udp 1701\n'
    f.write(transport)

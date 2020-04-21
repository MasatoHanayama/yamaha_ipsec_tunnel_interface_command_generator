#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='''
YAMAHA L2TP tunnel config command generator.
''')

parser.add_argument('-p', '--pre_shared_key', help='Pre-Shared-Key.', required=True)
parser.add_argument('-c', '--count_generate_tunnel', type=int, help='Count of generate tunnel.', required=True)
parser.add_argument('-ca', '--cert', default="SHA", choices=['MD5', 'SHA', 'SHA256'], help='Optional, Certification algorithm. Input any of "MD5", "SHA", "SHA256".')
parser.add_argument('-ea', '--encrypt', default="3DES", choices=['DES', '3DES', 'AES', 'AES256'], help='Optional, Encrypt algorithm. Input any of "DES", "3DES", "AES", "AES256".')

args = parser.parse_args()

limit = int(args.count_generate_tunnel)
limit += 1

if args.cert == 'MD5':
    cert = 'md5-hmac'
elif args.cert == 'SHA':
    cert = 'sha-hmac'
elif args.cert == 'SHA256':
    cert = 'sha256-hmac'

if args.encrypt == 'DES':
    encrypt = 'des-cbc'
elif args.encrypt == '3DES':
    encrypt = '3des-cbc'
elif args.encrypt == 'AES':
    encrypt = 'aes-cbc'
elif args.encrypt == 'AES256':
    encrypt = 'aes256-cbc'

transport = ''
with open('./conf.txt', 'w') as f:
    for i in range(1, limit, 1):
        f.write('tunnel select ' + str(i) + '\n')
        f.write('tunnel capsulation l2tp\n')
        f.write('ipsec tunnel ' + str(i) + '\n')
        f.write(' ipsec sa policy ' + str(i) + ' ' + str(i) + ' esp ' + encrypt + ' ' + cert + '\n')
        f.write(' ipsec ike keepalive log ' + str(i) + ' off\n')
        f.write(' ipsec ike keepalive use ' + str(i) + ' off\n')
        f.write(' ipsec ike nat-traversal ' + str(i) + ' on\n')
        f.write(' ipsec ike pre-shared-key ' + str(i) + ' text ' + args.pre_shared_key + '\n')
        f.write(' ipsec ike remote address ' + str(i) + ' any\n')
        f.write('l2tp tunnel auth off\n')
        f.write('l2tp tunnel disconnect time off\n')
        f.write('ip tunnel tcp mss limit auto\n')
        f.write('tunnel enable ' + str(i) + '\n')
        transport += 'ipsec transport ' + str(i) + ' ' + str(i) + ' udp 1701\n'
    f.write(transport)

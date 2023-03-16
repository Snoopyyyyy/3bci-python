import platform
import json
from flask import Flask
from flask import render_template
from cpuinfo import get_cpu_info 
import os
import socket

class Machine:
    # constructor where i get all system information
    def __init__(self):
        cpu_data = get_cpu_info()

        self.type = platform.machine()
        self.name = platform.node()
        self.system = platform.system()
        self.release = platform.release()
        self.cpu_version = cpu_data["cpuinfo_version_string"]
        self.cpu_bits = cpu_data["bits"]
        self.cpu_frequence = cpu_data["hz_advertised_friendly"]
        self.cpu_brand = cpu_data["brand_raw"]

    # return the instance as a dictonary 
    def getDico(self):
        return {
            'Systeme': self.system,
            'Release': self.release,
            'Type': self.type,
            'name': self.name,
            'Version du CPU': self.cpu_version,
            'Bits du CPU': self.cpu_bits,
            'Marque du CPU': self.cpu_brand,
            'Frequence du CPU': self.cpu_frequence
        }

    # start flask
    def start(self):
        app = Flask(__name__)

        @app.route("/")
        def MyMachine():
            return render_template("index.html", maMachine = self.getDico())
        
        app.run()

tmp = Machine()
tmp.start()
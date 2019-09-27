import subprocess

interface =input("Interface > ")
new_mac = input("New Mac > ")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +  " up ", shell=True)


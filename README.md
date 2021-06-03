# Data-Secuirty-and-Privacy
Hex 3 - 2021 - Data Security and Privacy Assessment 3

# Welcome to Michael Bishop's Recon Toolkit

![Homescreen](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Description.png)

## Description

##### Michael Bishop's Recon Toolkit is coded via Python. It contains multiple options for entry level recon on a host network. I have developed this tool to be used inside workplaces for recon testing and entry level cybersecurity users. 

---

## What does the tool do?

##### This tool currently has three options to use. 
##### 1. Find Devices on Current Subnet
##### 2. Scan Open Ports on Current Device
##### 3. Scan Open Ports on another device

##### Option 1. Allows you to discover devices that are currently on your subnet that you might not be aware about. Optimal utilisation will allow both the hostname and the IP address to appear. 
###### Please note: Certain enviroment will not resolve the hostname but the IP address will be available still 

##### Option 2. Allows you to view all the open ports on your current device. 
###### Please note: Ensure your loopback adapter is either disabled and set as secondary priority for network connections. Due to the tool using the host IP, it will grab the 127 address if your loopback adapter is first priority.
###### Please note: Microsoft Defender and other AVs may prevent the tool discovering all open ports

##### Option 3. ALlows you to view all open ports on a target host
###### Please note: Ensure your loopback adapter is either disabled and set as secondary priority for network connections. Due to the tool using the host IP, it will grab the 127 address if your loopback adapter is first priority.
###### Please note: Microsoft Defender and other AVs may prevent the tool discovering all open ports

---

## What to check before running the tool

#### Ensure you have python installed on your device 
> Use the following link to the python download page - https://www.python.org/downloads/

#### Ensure you install the requirements txt before using the tool to ensure all modules are installed
> Use the following command - **pip install r requirements.txt** (Please note you will need to be in the current directory where the requirements txt is stored on your device)
#### Once you have installed the requirements txt, proceed to launch the Data Security and Privacy.py file
> Use the following command - **python3 Data and Security and Privacy.py** (Please note you will need to be in the current directory where the .py file is stored on your device)

---

## How to use the tool

#### Once you have launched the python file, you will see three options.
![Options](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Options.png)

#### To select options, you will type the corresponding option number
##### For option 1, you will type "1"
##### For option 2, you will type "2"
##### For option 3, you will type "3"
##### To quit the tool, you will type "Quit"
> Any other input will not work and you will recieve the following message
![OptionNotFound](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/NotFound.png)

---

# Error Code Fixes
---

## Requirement.txt Error
#### If you see a message when you are using the requirements.txt, please ensure that;
> You have updated your pip - **pip install --upgrade pip**
> You are using sudo / admin mode in the cmd / terminal
#### If this is still not working for you, you will need to install the following packages
> **pip install pyfiglet

---

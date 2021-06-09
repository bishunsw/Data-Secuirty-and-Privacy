# Data-Security-and-Privacy
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
##### 4. Choose MIN and MAX ports to scan on another device for open ports

##### Option 1. Allows you to discover devices that are currently on your subnet that you might not be aware about. Optimal utilisation will allow both the hostname and the IP address to appear. 
###### Please note: Certain environment will not resolve the hostname but the IP address will be available still 

##### Option 2. Allows you to view all the open ports on your current device. 
###### Please note: Ensure your loopback adapter is either disabled or set as secondary priority for network connections. Due to the tool using the host IP, it will grab the 127 address if your loopback adapter is first priority.
###### Please note: Microsoft Defender and other AVs may prevent the tool discovering all open ports

##### Option 3. Allows you to view all open ports on a target host
###### Please note: Ensure your loopback adapter is either disabled or set as secondary priority for network connections. Due to the tool using the host IP, it will grab the 127 address if your loopback adapter is first priority.
###### Please note: Microsoft Defender and other AVs may prevent the tool discovering all open ports

##### Option 4. Allows you to select the minimum and maximum port numbers you would like to scan on another host to verify what ports are open
###### Please note: Ensure your loopback adapter is either disabled or set as secondary priority for network connections. Due to the tool using the host IP, it will grab the 127 address if your loopback adapter is first priority.
###### Please note: Microsoft Defender and other AVs may prevent the tool discovering all open ports
###### Please note: The program will close if you attempt to enter a value that is not a number in the input fields of the min and max port option
---

## What to check before running the tool

#### Ensure you have python installed on your device 
> Use the following link to the python download page - https://www.python.org/downloads/

#### Ensure you install the requirements txt before using the tool to ensure all modules are installed
> Use the following command - **pip install r requirements.txt** (Please note you will need to be in the current directory where the requirements txt is stored on your device)
#### Once you have installed the requirements txt, proceed to launch the Data Security and Privacy.py file
> Use the following command - **python3 Data and Security and Privacy.py** (Please note you will need to be in the current directory where the .py file is stored on your device)

---

# How to use the tool

#### Once you have launched the python file, you will see three options.
![Options](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Options.png)

#### To select options, you will type the corresponding option number
##### For option 1, you will type "1" - You won't need to enter anything
##### For option 2, you will type "2" - You won't need to enter anything
##### For option 3, you will type "3" - You will need to enter in an IP address of another device you would like to scan
##### For option 4, you will type "4" - You will need to enter a min, max port number and IP address of another device you would like to scan
##### To quit the tool, you will type "Quit"
> Any other input will not work and you will receive the following message
![OptionNotFound](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/NotFound.png)

---

# Test Inputs and Outputs

### Option 1 Test Output
![Option1Output](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/OptionTestOutput.png)
##### As you can see above, this is the test output of option 1 on my current network.
##### Please note: Some information is redacted but the boxes detail what is hidden underneath

### Option 2 Test Output
![Option2Output](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Option2TestOutput.png)
##### As you can see above, this is the test output of option 2 on my current device.
##### Please note: Some information is redacted but the boxes detail what is hidden underneath. There is no results as I have filtered most of my ports for security reasons

### Option 3 Test Input
![Option3Input](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Option3TestInput.png)
##### As you can see above, this is the test input of option 3 targeting another device on my network.
##### Please note: Some information is redacted but the boxes detail what is hidden underneath.

### Option 3 Test Output
![Option3Output](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Option3TestOutput.png)
##### As you can see above, this is the test output of option 3's (test input above) targeting another device on my network.
##### Please note: Some information is redacted but the boxes detail what is hidden underneath.

### Option 4 Test Inputs **Ports**
![Option4Input](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Option4TestInput.png)
##### As you can see above, this is the test inputs of option 4's for the min and max ports.
##### Please note: Inputs are sanitized to prevent inputs not being numbers and max being smaller than the min

### Option 4 Test Inputs **IP**
![Option4InputIP](https://github.com/bishunsw/Data-Secuirty-and-Privacy/blob/main/Readme%20-%20Images/Option4TestInputIP.png)
##### As you can see above, this is the test inputs of option 4's for the IP address.
##### Please note: Inputs are sanitized to prevent inputs having text added before the IP address or after an IP address

---

# Error Code Fixes
---

## Requirement.txt Error
#### If you see a message when you are using the requirements.txt, please ensure that;
> You have updated your pip - **pip install --upgrade pip**
> You are using sudo / admin mode in the cmd / terminal
#### If this is still not working for you, you will need to install the following packages
> **pip install pyfiglet**

---

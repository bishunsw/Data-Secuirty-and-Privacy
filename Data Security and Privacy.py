import os                                                                       #Used to import the OS module to allow for OS specific commands like "ping" to be used                                                              
import sys                                                                      #Used to import the Sys module to allow for the terminal shell to exit functions running in the terminal
import socket                                                                   #Used to import the Socket module to allow for the collection of IP and hostnames inside this tool
import pyfiglet                                                                 #Used to import the pyfiglet module to allow for the ASCII banner within this tool to display the Michael Bishop banner
import re                                                                       #Used to import the re module to allow for regex checking function within this tool

def clean():                                                                    #Clean Function that allows the tool to reference the function of clearing the terminal results to minimise result clogging the terminal
    os.system('clear')                                                          #Using the sys module, this clears the python terminal so everything is removed including results

def scanall():                                                                  #ScanAll Function that allows the tool to reference the function for scanning and returning all the hosts on the subnet of the device running this tool
    devices = []                                                                #This array is used to store the devices that have resolved hostnames for later output
    unknown = []                                                                #This array is used to store the devices that their hostname was unable to be resolved for later output
    for device in os.popen('arp -a'):                                           #This for loop creates a shell pipe to run the arp -a command for both unix and linux system terminals to allow address resolution protocol
        if device[0] == "?":                                                    #This if statement checks the results of the arp command in the line above to find the devices where their hostname was not resolved
            unknown.append(device)                                              #This appends the unknown hosts to the array called "Unknown"
        else:                                                                   #This else statement is for the hostname that were able to be resolved via the arp command
            devices.append(device)                                              #This appends the known hostnames to the devices array
    final_list = '\n'.join(devices)                                             #This final list creates an empty line (enter value) between each value in the known device and then stores it inside another array. 
    unknown_final_list = '\n'.join(unknown)                                     #This unknown final list array is used to create an empty line between the values of the unknown devices array into this array for a list view
    print("_" * 70)                                                             #This creates 70 underscore symbols to tweak the result view in the terminal
    print ("############## Discoverable Devices Found ##############")          #This display a seperator text to show what discoverabled (resolved hostname) devices found
    print("-" * 70)                                                             #This creates 70 dash symbols to tweak the result view in the terminal
    print (final_list)                                                          #This prints the list view of the known devices inside the terminal
    print ("Discoverable Devices count is - ", len(devices))                    #This prints a count of the known devices found using an int number
    print("-" * 70)                                                             #This creates 70 dash symbols to tweak the result view in the terminal
    print ("############## Unknown Devices Found ##############")               #This display a seperator text to show what undiscoverabled (unresolved hostname) devices found
    print("_" * 70)                                                             #This creates 70 underscore symbols to tweak the result view in the terminal
    print (unknown_final_list)                                                  #This prints the list view of the unknown devices inside the terminal

def portscanner():
    host = socket.gethostname()
    ips = socket.gethostbyname(host)
    target = str(ips)

    print("-" * 35)
    print("Scanning Your Device: IP -  " + str(target))
    print("-" * 35)
    print("-" * 35)
    print("If you would like to cancel the scan, please use CTRL + C, scanning may take some time")
    print("-" * 35)
    print("*" * 80)
    print("                                 Results")
    print("*" * 80)

    try:
        for port in range(1,6000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = s.connect_ex((str(target),port))
            if result == 0:
                print ("Port {} is open".format(port))
            s.close
    except KeyboardInterrupt:
        print ("Program Exitting")
        sys.exit()
    except socket.error:
        print("Not responding")
        sys.exit()
    except socket.gaierror:
        print("Hostname cannot be resolved")
        sys.exit()

def portscanner2():
    ips = input ("What is the IP of the device you would like to scan? - ")
    target = str(ips)
    host_check = False

    try:
        socket.inet_aton(target)
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"           #Idea came from this following link https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/ 
        if (re.search(regex, target)):
            print("Initial IP Address Check Complete - Please wait while we check the host")
            ping_test = os.system("ping -c 1 " + target)                                                                        #Idea came from this following link https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python 
            if ping_test != 0:
                print("*" * 80)
                print("            Host not found - Please check host IP address again")
                print("*" * 80)
                portscanner2()
            else:
                print("Host found - Starting Port Scan Now")
        else:
            print("IYou have entered a value that is not an IP Address - Format ###.###.###.###")
            portscanner2()
    except socket.error:
        print("You have entered a value that is not an IP Address - Format ###.###.###.###")
        portscanner2()

    print("-" * 35)
    print("Scanning Device: IP -  " + str(target))
    print("-" * 35)
    print("-" * 35)
    print("If you would like to cancel the scan, please use CTRL + C, scanning may take some time")
    print("-" * 35)
    print("*" * 80)
    print("                                 Results")
    print("*" * 80)

    try:
        for port in range(1,6000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = s.connect_ex((str(target),port))
            if result == 0:
                print ("Port {} is open".format(port))
            s.close
    except socket.gaierror:
        print("Hostname cannot be resolved")
        sys.exit()
    except KeyboardInterrupt:
        print ("Program Exitting")
        sys.exit()
    except socket.error:
        print("Not responding")
        sys.exit()

ascii_banner = pyfiglet.figlet_format("Welcome to Michael Bishop's Recon Toolkit")
print(ascii_banner)

def options():
    print("-" * 80)
    print("Option 1. Scan for all network devices on your subnet")
    print("-" * 80)
    print("Option 2. Scan Open Ports on your device")
    print("-" * 80)
    print("Option 3. Scan Open Ports on another device")
    print("-" * 80)
    print("IF YOU WOULD LIKE TO LEAVE THIS TOOL - PLEASE TYPE --> 'Quit'")
    print("-" * 80)

options()
option = input ("What option would you like? (Please type the option number - Like '1') - ")


while True:
    if option == "1":
        clean()
        print("*" * 80)
        print("                               Results Loading")
        print("*" * 80)
        clean()
        scanall()
        print("-" * 80)
        retry = input ("Would you like to see the options agian? (Please type Y or N) - ")
        if retry == "Y":
            options()  
            option = input ("What option would you like? (Please type the option number - Like '1') - ")
        else:
            break
    elif option == "2":
        clean()
        portscanner()
        print("-" * 80)
        print("-" * 80)
        options()
        option = input ("What option would you like? (Please type the option number - Like '1') - ")
    elif option == "3":
        clean()
        portscanner2()
        print("-" * 80)
        print("-" * 80)
        options()
    elif option == "Quit":
        break
    else:
        clean()
        print("*" * 80)
        print("       You enter in an option that is not available - Please try again")
        print("*" * 80)
        options()
        option = input ("What option would you like? (Please type the option number - Like '1') - ")

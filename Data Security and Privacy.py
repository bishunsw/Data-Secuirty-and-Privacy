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

def portscanner():                                                              #PortScanner function that allows this tool to check what ports are open on the current device and returning the output in the terminal
    host = socket.gethostname()                                                 #This creates a variable that uses the socket module to grab the current machine's hostname
    ips = socket.gethostbyname(host)                                            #This creates a variable that uses the variable above to translate the hostname into an IP address
    target = str(ips)                                                           #This creates a variable based on the IP address above and ensures that it is changed to a string

    print("-" * 35)                                                             #This creates 35 dash symbols to tweak the result view in the terminal
    print("Scanning Your Device: IP -  " + str(target))
    print("-" * 35)                                                             #This creates 35 dash symbols to tweak the result view in the terminal
    print("-" * 35)                                                             #This creates 35 dash symbols to tweak the result view in the terminal
    print("If you would like to cancel the scan, please use CTRL + C, scanning may take some time")       #This creates the current message to appear in the terminal to tell the user how to quit the scanning if it takes too long
    print("-" * 35)                                                             #This creates 35 dash symbols to tweak the result view in the terminal
    print("*" * 80)                                                             #This creates 80 * symbols to tweak the result view in the terminal
    print("                                 Results")                           #This creates the following text to appear in the terminal to allow the user to know what results were found below
    print("*" * 80)                                                             #This creates 80 * symbols to tweak the result view in the terminal

    try:                                                                        #This try function is here to ensure that the port scanner loop continues until an exception is activated further onwards
        for port in range(1,6000):                                              #This port loops works to increase ports value starting from 1 to 6000 as the port number to be tested below
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               #This makes s the variable that will use the socket module to create a stream via IPv4 to tcp for the creation of the requests of the port scanner   -Reference -  https://docs.python.org/3/howto/sockets.html
            socket.setdefaulttimeout(0.1)                                       #This sets the socket timeout to 0.1 seconds, since we are scanning up to 6000 ports, we don't want the ports that are not open to hold up this tool
            result = s.connect_ex((str(target),port))                           #This creates another variable name results that stores the result when the program takes the target variable (which is the IP address of the host) and the port number and creates a socket packet that is sent to the host
            if result == 0:                                                     #If the result returns a 0 value, this means the port is open on the hostmachine    
                print ("Port {} is open".format(port))                          #If the result above returns 0, this prints the following statement including the port that was found to be open
            s.close                                                             #This closes the socket stream once the ports have all been checked
    except KeyboardInterrupt:                                                   #This check to see if the user types anything             
        print ("Program Exitting")                                              #This prints the following statement in the terminal
        sys.exit()                                                              #The loop will close if the user types anything into the terminal or presses any keys on their device
    except socket.error:                                                        #If the socket function has an error such as the socket stream recieving back a misc response, the loop will be exited    
        print("Not responding")                                                 #This prints the following statement within the terminal
        sys.exit()                                                              #This will exit the following loop if the socket has an error occur
    except socket.gaierror:                                                     #This except function will be triggered if the host is unable to respond to the port scan - if the host drops halfway through the scan
        print("Hostname cannot be resolved")                                    #This prints the following statement within the terminal
        sys.exit()                                                              #This will exit the following loop if the host can no longer be contacted by the loop socket stream

def portscanner2():
    ips = input ("What is the IP of the device you would like to scan? - ")
    target = str(ips)
    host_check = False

    try:
        socket.inet_aton(target)
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"           #Idea came from this following link https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/ 
        if (re.search(regex, target)):
            print("*" * 80)
            print("Initial IP Address Check Complete - Please wait while we check the host")
            print("*" * 80)
            ping_test = os.system("ping -c 1 " + target)                                                                        #Idea came from this following link https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python 
            if ping_test != 0:
                print("*" * 80)
                print("            Host not found - Please check host IP address again")
                print("*" * 80)
                portscanner2()
            else:
                print("*" * 80)
                print("Host found - Starting Port Scan Now")
                print("*" * 80)
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

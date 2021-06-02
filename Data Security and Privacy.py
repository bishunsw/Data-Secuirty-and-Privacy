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

def portscanner2():                                                             #This function is very similar to the portscanner function above but allows for the user to select their own target host
    ips = input ("What is the IP of the device you would like to scan? - ")     #This variable stores the input of the user that contains the IP address of the host they are wanting to scan
    target = str(ips)                                                           #This variable converts the variable that is storing the input of the user into a string
    host_check = False                                                          #This variable is created to be used later in the code to check the host is valid or not

    try:                                                                        #This try function is here to ensure that the port scanner loop continues until an exception is activated further onwards
        socket.inet_aton(target)                                                #This attempts converting the IP Address into a dotted-quad string, this will fail if the user try to input a bad input instead of a IP address at the front of the input
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"           #Idea came from this following link https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/ 
        if (re.search(regex, target)):                                          #This check the entire string including the end of the input to ensure the user types an IP address instead of bad code for the input
            print("*" * 80)                                                     #This creates 80 * symbols to tweak the result view in the terminal
            print("Initial IP Address Check Complete - Please wait while we check the host")           #This prints the following statement to the terminal to let the user know that they inputted a correct IP address notation for the input
            print("*" * 80)                                                     #This creates 80 * symbols to tweak the result view in the terminal
            ping_test = os.system("ping -c 1 " + target)                        #Idea came from this following link https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python - Since this code runs anything for the target variable, i needed to ensure that user could not inject bad code for this line
            if ping_test != 0:                                                  #If the ping test fails to ping the target IP, this will mean the user has inputted an IP address where the host cannot be contacted
                print("*" * 80)                                                 #This creates 80 * symbols to tweak the result view in the terminal
                print("            Host not found - Please check host IP address")                #This prints the following statement to the terminal to let the user know that the host could not be resolved
                print("*" * 80)                                                 #This creates 80 * symbols to tweak the result view in the terminal
                portscanner2()                                                  #This returns back to the function again so the user can try another host to test
            else:                                                               #This else statement is used when the ping test works
                print("*" * 80)                                                 #This creates 80 * symbols to tweak the result view in the terminal                                        
                print("Host found - Starting Port Scan Now")                    #This prints the following statement in the terminal to let the user know that the host was found
                print("*" * 80)                                                 #This creates 80 * symbols to tweak the result view in the terminal
        else:                                                                   #This else statment is used when the ip address entered by the user does not use IP notation
            print("IYou have entered a value that is not an IP Address - Format ###.###.###.###")       #This prints the following statement in the terminal to let the user know that they did not enter the correct ip address formatting
            portscanner2()                                                      #This loops back to the start of this function to prompt the user for an ip address
    except socket.error:                                                        #This exception is here, just in case the two function above to not determine the ip address as not an ip address - Triple layer input sanitisation
        print("You have entered a value that is not an IP Address - Format ###.###.###.###")            #This prints the following statement in the terminal to let the user know that they did not input the correct ip address notation.
        portscanner2()                                                          #This loops back to the start of this function to prompt the user for an ip address

    print("-" * 35)                                                             #This prints a dash symbol 35 times inside the terminal to tweak the output for user experience
    print("Scanning Device: IP -  " + str(target))
    print("-" * 35)                                                             #This prints a dash symbol 35 times inside the terminal to tweak the output for user experience
    print("-" * 35)                                                             #This prints a dash symbol 35 times inside the terminal to tweak the output for user experience
    print("If you would like to cancel the scan, please use CTRL + C, scanning may take some time")     #This prints the following statement inside the terminal to allow the user to know what device IP is getting scanned and how to exit the tool if required.
    print("-" * 35)                                                             #This prints a dash symbol 35 times inside the terminal to tweak the output for user experience
    print("*" * 80)                                                             #This creates 80 * symbols to tweak the result view in the terminal
    print("                                 Results")                           #This prints the following statement to allow the user to know the results of the port scanner function
    print("*" * 80)                                                             #This creates 80 * symbols to tweak the result view in the terminal

    try:                                                                        #This try function is here to ensure that the port scanner loop continues until an exception is activated further onwards  
        for port in range(1,6000):                                              #This port loops works to increase ports value starting from 1 to 6000 as the port number to be tested below
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               #This makes s the variable that will use the socket module to create a stream via IPv4 to tcp for the creation of the requests of the port scanner   -Reference -  https://docs.python.org/3/howto/sockets.html
            socket.setdefaulttimeout(0.1)                                       #This sets the socket timeout to 0.1 seconds, since we are scanning up to 6000 ports, we don't want the ports that are not open to hold up this tool

            result = s.connect_ex((str(target),port))                           #This creates another variable name results that stores the result when the program takes the target variable (which is the IP address of the host) and the port number and creates a socket packet that is sent to the host
            if result == 0:                                                     #If the result returns a 0 value, this means the port is open on the hostmachine
                print ("Port {} is open".format(port))                          #If the result above returns 0, this prints the following statement including the port that was found to be open
            s.close                                                             #This closes the socket stream once the ports have all been checked
    except socket.gaierror:                                                     #This except function will be triggered if the host is unable to respond to the port scan - if the host drops halfway through the scan
        print("Hostname cannot be resolved")                                    #This prints the following statement within the terminal
        sys.exit()                                                              #This will exit the following loop if the host can no longer be contacted by the loop socket stream
    except KeyboardInterrupt:                                                   #This check to see if the user types anything             
        print ("Program Exitting")                                              #This prints the following statement in the terminal
        sys.exit()                                                              #The loop will close if the user types anything into the terminal or presses any keys on their device
    except socket.error:                                                        #If the socket function has an error such as the socket stream recieving back a misc response, the loop will be exited    
        print("Not responding")                                                 #This prints the following statement within the terminal
        sys.exit()                                                              #This will exit the following loop if the socket has an error occur

ascii_banner = pyfiglet.figlet_format("Welcome to Michael Bishop's Recon Toolkit")       #This uses the pyfiglet module to create the banner for the tool for visual aid
print(ascii_banner)                                                             #This prints the banner variable above

def options():                                                                  #This is the main option view so that the options can be called whenever instead of having to print the options everytime
    print("-" * 80)                                                             #This creates 80 dash symbols to tweak the result view in the terminal
    print("Option 1. Scan for all network devices on your subnet")              #This prints the following statement inside the terminal
    print("-" * 80)                                                             #This creates 80 dash symbols to tweak the result view in the terminal
    print("Option 2. Scan Open Ports on your device")                           #This prints the following statement inside the terminal
    print("-" * 80)                                                             #This creates 80 dash symbols to tweak the result view in the terminal
    print("Option 3. Scan Open Ports on another device")                        #This prints the following statement inside the terminal
    print("-" * 80)                                                             #This creates 80 dash symbols to tweak the result view in the terminal
    print("IF YOU WOULD LIKE TO LEAVE THIS TOOL - PLEASE TYPE --> 'Quit'")      #This prints the following statement inside the terminal
    print("-" * 80)                                                             #This creates 80 dash symbols to tweak the result view in the terminal

options()                                                                       #This calls the option function which displays all the options in this tool
option = input ("What option would you like? (Please type the option number - Like '1') - ")        #This prompts the user to select an option via their input in the terminal


while True:                                                                     #This is forever loop unless the user types "Quit" in the terminal
    if option == "1":                                                           #This checks if the uses types 1 which selects the scanall function to find all devices on the same subnet
        clean()                                                                 #This calls the clean function that "cleans" the terminal of all previous messages so that the terminal is empty
        print("*" * 80)                                                         #This creates 80 * symbols to tweak the result view in the terminal
        print("                               Results")                         #This prints the following statement inside the terminal
        print("*" * 80)                                                         #This creates 80 * symbols to tweak the result view in the terminal                                                        
        scanall()                                                               #This calls the scanall function to start the function to return the arp result
        print("-" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        retry = input ("Would you like to see the options agian? (Please type Y or N) - ")                          #This prompts the user to input whether or not the user wants to see the options again to run the tool again
        if retry == "Y":                                                        #This checks if the user types "Y" to view the options again
            options()                                                           #This calls the option function which displays all the options in this tool
            option = input ("What option would you like? (Please type the option number - Like '1') - ")            #This prompts the user to select an option via their input in the terminal
        else:                                                                   #This checks if the user doesn't type "Y" in the terminal
            break                                                               #This will close the tool
    elif option == "2":                                                         #This will check if the user inputs "2" in the terminal for the port scanner option to check their own device
        clean()                                                                 #This calls the clean function that "cleans" the terminal of all previous messages so that the terminal is empty
        portscanner()                                                           #This calls the portscanner function to start the port scan socket loop to test each port on the user's device
        print("-" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        print("-" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        options()                                                               #This calls the option function which displays all the options in this tool
        option = input ("What option would you like? (Please type the option number - Like '1') - ")                #This prompts the user to select an option via their input in the terminal
    elif option == "3":                                                         #This checks if the user has typed "3" in the terminal to select the port scanner 2 option
        clean()                                                                 #This calls the clean function that "cleans" the terminal of all previous messages so that the terminal is empty
        portscanner2()                                                          #This calls the port scanner 2 function to start the port scan socket loop to test another host of the user's choosing for open ports
        print("-" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        print("-" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        options()                                                               #This calls the option function which displays all the options in this tool
    elif option == "Quit":                                                      #This check if the user has typed "Quit" into the terminal
        break                                                                   #This exits the tool
    else:                                                                       #This checks if all the other previous if statements were not triggered meaning that the user did not type a correct option in the terminal
        clean()                                                                 #This calls the clean function that "cleans" the terminal of all previous messages so that the terminal is empty
        print("*" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        print("       You enter in an option that is not available - Please try again")                              #This prints the following statement to let the user know they select an option that isn't available
        print("*" * 80)                                                         #This creates 80 dash symbols to tweak the result view in the terminal
        options()                                                               #This calls the option function which displays all the options in this tool
        option = input ("What option would you like? (Please type the option number - Like '1') - ")                #This prompts the user to select an option via their input in the terminal

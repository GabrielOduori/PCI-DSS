"""
This code generates systems files and configurations 
required to conduct a PCI DSS analys and audit.
    
"""
    
# CREATE WORKING DIRECTORIES

"""
01. Requirement_01
02. Requirement_02
03. Requirement_03
04. Requirement_04
05. Requirement_05
06. Requirement_06
07. Requirement_07
08. Requirement_08
09. Requirement_09
10. Requirement_10
11. Requirement_11
12. Requirement_12
"""



import platform

get_OS = platform.system()
np = platform.architecture()
nx = platform.machine()
ny = platform.mac_ver()
nn = platform.java_ver()
no = platform.version()
# print(get_OS)
print(nx)
# print(nx)
# print(ny)
# print(nn)
# print(no)

print( get_OS + " Version " + no )




            
# If OS ia windows:
# ren windows filse

# Requirement 01
# Requirement 1: Install and maintain a firewall configuration to protect cardholder data
    
    
    
# Requirement 2: Do not use vendor-supplied defaults for system passwords and other security parameters
# Check default usernames and password




# Requirement 3: Protect stored cardholder data




# Requirement 4: Requirement 4: Encrypt transmission of cardholder data across open, public networks


# Requirement 5: Use and regularly update anti-virus software or programs



# Requirement 6: Develop and maintain secure systems and applications
"""

WHAT TO LOOK OUT FOR:

The current version of the OS as well as latest pathches that are at lease 3 months old.

TESING PROCEDURE:
Check if the OS is still supported and patches are available or if it has
reached end of life and no more support is being provided.


"""




# Requirement 7: Restrict access to cardholder data by business need to know




# Requirement 8: Assign a unique ID to each person with computer access




# Requirement 9: Restrict physical access to cardholder data



# Requirement 10: Track and monitor all access to network resources and cardholder data



# Requirement 11: Regularly test security systems and processes




#Requirement 12: Maintain a policy that addresses information security for all personnel
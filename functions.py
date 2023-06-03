import random

def createRandomBinary():
    random_binary = ''
    for i in range(8):
        bit = random.randint(0,1)
        random_binary += str(bit)
    return random_binary
    #return String
    #DONE
####################################################
def fixBinary(given_num):
    if len(given_num) < 8: 
        difference = 8 - len(given_num)
        for i in range(difference):
            given_num = ''.join(('0',given_num))
        return(given_num)
    if len(given_num) > 8:
        given_num = given_num[-8:]
        return(given_num)
####################################################
def binaryToDecimal(binary_num):
    translated_binary = 0
    #binaryNum = binaryNum[::-1]
    start = 7
    for i in range(len(binary_num)):
        translated_binary += (2 ** start) * int(binary_num[i])
        start -= 1
    return translated_binary
####################################################
def generate_random_ip_address( ipclasslist):
    ips = []
    for i in ipclasslist: 
        if i == 'A':
            first_octet = random.randint(1, 126)
        elif i == 'B':
            first_octet = random.randint(128, 191)
        elif i == 'C':
            first_octet = random.randint(192, 223)
        elif i == 'D':
            first_octet = random.randint(224, 239)
        elif i == 'E':
            first_octet = random.randint(240, 255)
        ips.append(f"{first_octet}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")
    return ips
####################################################


def calculate_network_info():
    
    
    # Generate random IP address
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))

    # Generate random CIDR prefix between 24 and 30
    cidr_prefix = random.randint(24, 30)

    # Construct the CIDR notation
    cidr_notation = ip_address + "/" + str(cidr_prefix)

    # Calculate the subnet mask
    subnet_mask = calculate_subnet_mask(cidr_prefix)

    # Calculate the network address
    network_address = calculate_network_address(ip_address, subnet_mask)

    # Calculate the broadcast address
    broadcast_address = calculate_broadcast_address(ip_address, subnet_mask)

    # Calculate the total number of hosts in the network
    total_hosts = calculate_total_hosts(cidr_prefix)

    # Calculate the valid host range
    valid_host_range = calculate_valid_host_range(network_address, broadcast_address)
    
    
    dictionary = {}
    dictionary['cider'] = cidr_notation
    dictionary['subnetMask'] = subnet_mask
    dictionary['networkAddress'] = network_address
    dictionary['broadcastAddress'] = broadcast_address
    dictionary['totalhosts'] = total_hosts
        
    
    return dictionary   

    # Print the results
    # print("IP Address: ", ip_address)
    # print("CIDR Notation: ", cidr_notation)
    # print("Subnet Mask: ", subnet_mask)
    # print("Network Address: ", network_address)
    # print("Broadcast Address: ", broadcast_address)
    # print("Total Number of Hosts: ", total_hosts)
    # print("Valid Host Range: ", valid_host_range)


def calculate_subnet_mask(cidr_prefix):
    # Calculate the subnet mask by converting the CIDR prefix to binary
    subnet_mask = ""
    for i in range(4):
        if cidr_prefix >= 8:
            subnet_mask += "255"
            cidr_prefix -= 8
        else:
            subnet_mask += str(256 - (2 ** (8 - cidr_prefix)))
            cidr_prefix = 0
        if i < 3:
            subnet_mask += "."
    return subnet_mask


def calculate_network_address(ip_address, subnet_mask):
    # Perform bitwise AND operation between the IP address and subnet mask
    ip_parts = ip_address.split(".")
    subnet_parts = subnet_mask.split(".")
    network_parts = []
    for i in range(4):
        network_parts.append(str(int(ip_parts[i]) & int(subnet_parts[i])))
    network_address = ".".join(network_parts)
    return network_address


def calculate_broadcast_address(ip_address, subnet_mask):
    # Perform bitwise OR operation between the IP address and inverted subnet mask
    ip_parts = ip_address.split(".")
    subnet_parts = subnet_mask.split(".")
    broadcast_parts = []
    for i in range(4):
        broadcast_parts.append(str(int(ip_parts[i]) | (255 - int(subnet_parts[i]))))
    broadcast_address = ".".join(broadcast_parts)
    return broadcast_address


def calculate_total_hosts(cidr_prefix): 
    # Calculate the total number of hosts in the network
    total_hosts = 2 ** (32 - cidr_prefix) - 2
    return total_hosts


def calculate_valid_host_range(network_address, broadcast_address):
    # Calculate the valid host range by excluding the network and broadcast addresses
    valid_host_range = network_address + " to " + broadcast_address
    return valid_host_range

# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

# Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

# However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

# Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

# Note: You may assume there is no extra space or special characters in the input string.

# Example 1:
# Input: "172.16.254.1"

# Output: "IPv4"

# Explanation: This is a valid IPv4 address, return "IPv4".
# Example 2:
# Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

# Output: "IPv6"

# Explanation: This is a valid IPv6 address, return "IPv6".
# Example 3:
# Input: "256.256.256.256"

# Output: "Neither"

# Explanation: This is neither a IPv4 address nor a IPv6 address.


class Solution:
    def validIPAddress(self, IP: str) -> str:
        is_ip4 = True
        is_ip6 = True
        num_segments = 1
        segment_start = 0
        
        i = 0
        while i < len(IP) and (is_ip4 or is_ip6):
            if IP[i] == '.' or IP[i] == ':':
                if i - segment_start == 0:
                    is_ip4 = False
                    is_ip6 = False
                    break
                
                if IP[i] == '.':
                    is_ip6 = False
                    if is_ip4:                        
                        num_segments += 1
                        segment_start = i + 1                               
                else:
                    is_ip4 = False
                    if is_ip6:
                        num_segments += 1
                        segment_start = i + 1
                    
            elif '0' <= IP[i] <= '9' or 'a' <= IP[i] <= 'f' or 'A' <= IP[i] <= 'F':                                    
                if i - segment_start >= 4:
                    is_ip6 = False
                    
                if 'a' <= IP[i] <= 'f' or 'A' <= IP[i] <= 'F':
                    is_ip4 = False
                elif is_ip4:
                    if i - segment_start == 1 and IP[segment_start] == '0':
                        is_ip4 = False
                        
                    if i - segment_start == 2:
                        is_ip4 = 0 <= int(IP[segment_start:i+1]) <= 255
                        
                    if i - segment_start >= 3:
                        is_ip4 = False
                                                                
            else:
                is_ip4 = False
                is_ip6 = False
                break
                
            i += 1
                
        if is_ip4 and num_segments == 4 and segment_start < len(IP):
            return 'IPv4'
        elif is_ip6 and num_segments == 8 and segment_start < len(IP):
            return 'IPv6'
        else:
            return 'Neither'
                
import socket
import sys
from datetime import datetime

Green = '\033[32m'
end = '\033[0m'

print(Green + r'''
                                                                                                          
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                ...                                                 
                                                -.+=                                                
                                                .=-.                                                
                                                .-=                                                 
                                                :.:.                                                
                                                ::::                                                
                                                :.:.                                                
                                         .=*DVPORTSCANNER*=.                                         
                                         .-.    :-:.   .:-.                                         
                                             ..-=::                                                 
                                             .=.- .:                                                
                                             ..=-:.-                                                
                                            .:-=-:.-                                                
                                               .-:.-.                                               
                                                -:.+:                                               
                                                -:.+--.                                             
                                                -:.-:-.                                             
                                                -..-.::                                             
                                                -..-=.                                              
                                                -:+-:.                                              
                                               -+:::                                                
                                               =*..:                                                
                                             .:-=.:.                                                
                                               .-.:.                                                
                                                -.::..                                              
                                                -.:.-.                                              
                                                -.:.-.                                              
                                                ::=-==.                                             
                                                ==-:                                                
                                                .::                                                 
                                                                                                    
                                           --BY DADDY V
                                                                                                    ''' + end)


TARGET_HOST = input('Enter Target Website: ')


PORTS_TO_SCAN = [21, 22, 80, 443, 8080, 4444]

print("-" * 50)
print(f"Scanning target: {TARGET_HOST}")
print("-" * 50)

try:
    for port in PORTS_TO_SCAN:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        s.settimeout(1.0)
        
        result = s.connect_ex((TARGET_HOST, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
            
        s.close()

except KeyboardInterrupt:
    print("\nExiting script (Ctrl+C detected).")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()

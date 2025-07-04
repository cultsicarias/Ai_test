import socket as s
import geocoder

def ip_loc()
    my_hostname = s.gethostname()
    print('Your Hostname is: ' + my_hostname)
    my_ip = s.gethostbyname(my_hostname)
    ip = geocoder.ip(my_ip)
    city=ip.city

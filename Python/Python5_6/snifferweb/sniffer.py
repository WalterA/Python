from scapy.all import *
from scapy.layers.inet import IP ,TCP 
from scapy.layers.http import HTTPRequest 
import csv
from datetime import datetime

iPkt = 0
load_layer('ls')
with open('packets.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data', 'IP Sorgente', 'IP Destinazione', 'Porta Sorgente', 'Porta Destinazione','Host'])
    
    def process_pkt(pkt):
        global iPkt
        
        iPkt += 1
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
        #tcp = pkt[TCP].show()
        
        if pkt.haslayer(HTTPRequest):
            host = pkt[HTTPRequest].Host
            #host = pkt[HTTPRequest].Host.decode() 
        else:
            host = "Unkonwn"
        print(f"Ho ricevuto un pacchetto {iPkt} IP: {pkt[IP]} da {ip_src} a {ip_dst} (sport: {sport}, dport: {dport},Host {host}")
        writer.writerow([data, ip_src, ip_dst, sport, dport,host])
        

    # Avvia lo sniffing dei pacchetti
    sniff(iface="eth0", filter="tcp", prn=process_pkt)
    """    
    if (pkt.haslayer(tcp)):
        print(pkt[tcp].show())
    """
    
    """FATTA DAL PROF
    def process_pkt(pkt):
    global iPkt
    with open('packets.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        iPkt += 1
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([data, "Ricevuto pkt",packet[IP].src  ])
    
    def proce_pa1(packet):
        if packet.haslayer(TLS):
            print("TLS packet")
            print(packt[TLS].show())
"""
#part2
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.tls.record import TLS    
from scapy.layers.http import HTTPRequest
from datetime import datetime
import csv
import os

def get_tls_sni(pkt):    #NUOVA FUNZIONE TO GET THE TLS
    try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
    except (IndexError, AttributeError):
        return ""


def process_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]:
            
            #Atributi info csv
            data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip_src = pkt[IP].src
            ip_dst = pkt[IP].dst
            tcp_src = pkt[TCP].sport
            tcp_dst = pkt[TCP].dport
            
            #Verifica l'host in caso di protocollo HTTP, altrimenti " "
            host = ""
            if HTTPRequest in pkt:
                if pkt[HTTPRequest].Host:
                    host = pkt[HTTPRequest].Host.decode()
            elif TLS in pkt:
                host = get_tls_sni(pkt)
            
            
            if 443 in [tcp_src, tcp_dst]:
                protocol = "HTTPS" 
            else:
                protocol = "HTTP"
                
            
                                                                    #(se il file già esiste integra i nuovi info)
            with open('connessioni.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if host != '':
                    writer.writerow([data_ora, ip_src, ip_dst, tcp_src, tcp_dst, host, protocol])

# Crea il file CSV con l'intestazione
with open('connessioni.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["data-ora", "ip_src", "ip_dst", "tcp_src", "tcp_dst", "host", "protocol"])

# Avvia lo sniffing
sniff(filter="tcp and (port 80 or port 443)", prn=process_pkt)
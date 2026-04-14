# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor

def main():
    filename = input("Nombre del archivo: ")
    
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            
            monitor = temp_monitor.init(n)
            
            for _ in range(n):
                line = file.readline().strip()
                if line:
                    temp = float(line)
                    temp_monitor.add_reading(monitor, temp)
            
            print(temp_monitor.longest_rising_streak(monitor))
            
    except FileNotFoundError:
        print("Error: El archivo no existe.")

if __name__ == "__main__":
    main()


import os
import time


def animacion():
    print("--- 3. Animation ---")
    input("Presiona ENTER para iniciar...")
    
    frames = [
        "   ( ^_^ )   ",
        "   (/-_-/)   ",
        "   ( ^_^ )   ",
        "   (\\-_-\\)   "
    ]
    
    for _ in range(3):
        for frame in frames:
            comando = "cls" if os.name == "nt" else "clear"
            os.system(comando)
            print("\n" * 5)
            print(frame)
            time.sleep(0.4) 
           
if __name__ == "__main__":
    animacion()

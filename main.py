import os

if __name__ == '__main__':
    print("Welcome to Robo speaker 1.1. Created by Durgesh")
    while True:
        sentence = input("Enter what do you want me to speak: ")
        command = f"say {sentence}"
        if sentence == "bye":
            os.system(command)
            break
        elif sentence.find("bye") != -1:
            os.system(command)
            break
        os.system(command)

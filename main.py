import time
import subprocess

def send_notfy(title: str, text: str):
    subprocess.call(["notify-send", title, text])

def main():
    remind_text = input("What should I remind you about?: ")
    remind_time = int(input("How often should I remind you?: "))
    while True:
        send_notfy("Notify", remind_text)
        time.sleep(remind_time*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
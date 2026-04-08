import os
import time
import json
import subprocess

def send_notfy(title: str, text: str):
    subprocess.call(["notify-send", title, text])

def load_config():
    if not os.path.exists("config.json"):
        with open("config.json", "w", encoding="utf-8") as f:
            config_body = {"interval": 5, "message": "Drink some water"}
            f.write(json.dumps(config_body))
            
    with open("config.json", "r", encoding="utf-8") as f:
        f = json.load(f)

    return f

def main():
    f = load_config()

    remind_time = f["interval"] * 60
    remind_message = f["message"]

    while True:
        send_notfy("Notify", remind_message)
        time.sleep(remind_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
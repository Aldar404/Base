import schedule


def greeting():
    print("good morning")


def do_greeting():
    schedule.every().day.at("14:13").do(greeting)
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    do_greeting()
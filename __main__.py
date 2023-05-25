import colorama
from application import Application

def main():
    colorama.init(autoreset=True)
    app = Application()
    app.launch()

if __name__ == "__main__":
    main()

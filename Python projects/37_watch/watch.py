import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try: 
        match = re.search(r"^.+src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+).+$", s) 
        url = match.group(1)
        return f"https://youtu.be/{url}"
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
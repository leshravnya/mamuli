import sys


def display_time(seconds):
    """
    Displays the seconds in days, hours, minutes and seconds
    """
    mins, seconds = divmod(seconds, 60)
    seconds = round(seconds, 2)
    mins = int(mins)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)

    display_zip = zip((days, hours, mins, seconds), "days hrs mins secs".split())
    return " ".join(map(lambda x: f"{x[0]}{x[1]}", filter(lambda x: x[0], display_zip)))


if __name__ == "__main__":
    print(display_time(float(sys.argv[1])))

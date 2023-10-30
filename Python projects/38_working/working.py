import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"^([^:]+):?(.+)? (AM|PM) to ([^:]+):?(.+)? (AM|PM)$", s)
        startHour, startMinutes, startMeridiem = match.group(1), match.group(2), match.group(3),
        finishHour, finishMinutes, finishMeridiem =  match.group(4), match.group(5), match.group(6)

        startTime = general_time(startMeridiem, startHour, startMinutes)
        finishTime = general_time(finishMeridiem, finishHour, finishMinutes)
        return f"{startTime} to {finishTime}"
    except:
        raise ValueError("ValueError has occured")

    

def general_time(meridiem, hours, minutes):
    hours = int(hours) % 12

    if minutes == None:
        minutes = "00"
    elif int(minutes) >= 60:
        raise ValueError
    
    if meridiem == "AM":
        time = f"{hours:02d}:{minutes}"
        return time
    elif meridiem == "PM":
        time = f"{(hours+12):02d}:{minutes}"
        return time


if __name__ == "__main__":
    main()
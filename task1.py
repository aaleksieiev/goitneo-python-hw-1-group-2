from datetime import datetime, timedelta
from collections import defaultdict
from colorama import Fore, Style


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days=days_ahead)


def get_birthdays_per_week(users):

    result = defaultdict(list)

    today = datetime.today().date()

    upcoming_monday = next_weekday(today, 0)
    weekend_befor_upcoming_monday = upcoming_monday - timedelta(days=2)
    upcoming_friday = next_weekday(upcoming_monday, 4)

    days_when_to_congratulate = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
    }

    for user in users:
        this_year_user_birthday = user["birthday"].replace(
            minute=0, hour=0, second=0, year=today.year
        ).date()

        if this_year_user_birthday > upcoming_friday:
            continue

        if this_year_user_birthday < weekend_befor_upcoming_monday:
            continue

        if this_year_user_birthday < upcoming_monday:
            result[days_when_to_congratulate[1]].append(user["name"])
            continue

        result[days_when_to_congratulate[this_year_user_birthday.isoweekday()]].append(
            user["name"])

    for week_name in result.keys():
        names = ", ".join(result[week_name])
        print(f"{Fore.BLUE}{week_name}: {Fore.WHITE}{names}")


if __name__ == "__main__":
    users = [
        {"name": "Testcase4 upcoming", "birthday": datetime(2003, 3, 10)},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Ann Man", "birthday": datetime(1984, 1, 15)},
        {"name": "Testcase upcoming", "birthday": datetime(1988, 3, 13)},
        {"name": "Testcase2 upcoming", "birthday": datetime(1977, 3, 13)},
        {"name": "My Granny", "birthday": datetime(1944, 3, 23)},
        {"name": "John Dou", "birthday": datetime(2010, 4, 15)},
        {"name": "Testcase3 upcoming", "birthday": datetime(2001, 3, 15)},
        {"name": "Testcase5 upcoming", "birthday": datetime(2001, 1, 15)},
    ]

    get_birthdays_per_week(users)

def add_time(start, duration, day=""):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    extra_days = 0

    class time:
        hours = ""
        minutes = ""
        day_night = ""

        def __init__(self, hours, minutes, day_night):
            self.hours = hours
            self.minutes = minutes
            self.day_night = day_night

        def sum_time(self, time2):
            result_day_night = self.day_night
            sum_minutes = int(float(self.minutes)) + int(float(time2.minutes))
            extra_hours = sum_minutes // 60
            global extra_days

            extra_days = ((int(first_time.hours) + int(second_time.hours) + extra_hours) // 24)


            if sum_minutes > 60:
                extra_hours = sum_minutes // 60
                sum_minutes = sum_minutes % 60
            if sum_minutes < 10:
                sum_minutes_str = "0" + str(sum_minutes)
            else:
                sum_minutes_str = str(sum_minutes)

            sum_hours = ((int(self.hours) + int(time2.hours) + extra_hours)) % 24

            if sum_hours >= 12:

                sum_hours = sum_hours - 12
                if self.day_night == "PM":
                    result_day_night = "AM"
                    extra_days = extra_days + 1

                if sum_hours == 0:
                    sum_hours = 12
                if self.day_night == "AM":
                    result_day_night = "PM"

            result_time = time(str(sum_hours), sum_minutes_str, (result_day_night))
            resultat = []
            resultat.append(result_time)

            resultat.append(extra_days)
            return resultat

        def output_time(self):
            result = self.hours + ":" + self.minutes + " " + self.day_night
            return result

    components_start = start.split()
    hours_minutes = components_start[0].split(':')

    hours_start = hours_minutes[0]
    if int(float(hours_minutes[1])) < 10:
        minutes_start = hours_minutes[1][1:2]

    else:
        minutes_start = hours_minutes[1]

    am_pm_start = components_start[1]

    first_time = time(hours_start, minutes_start, am_pm_start)

    components_duration = duration.split()
    hours_duration = components_duration[0].split(":")[0]
    if int(float(components_duration[0].split(":")[1])) < 10:
        minutes_duration = components_duration[0].split(":")[1]


    else:
        minutes_duration = components_duration[0].split(":")[1]

    second_time = time(hours_duration, minutes_duration, "")

    result_time = first_time.sum_time(second_time)[0]
    extra_days = first_time.sum_time(second_time)[1]

    result_day = ""

    if day != "":
        index_of_day = days.index(day.lower().capitalize())
        new_index = (index_of_day + extra_days) % 7
        result_day = days[new_index]

    number_of_dayss = ""
    if extra_days == 1:
        number_of_dayss = " (next day)"
    elif extra_days >= 2:
        number_of_dayss = " (" + str(extra_days) + " days later)"

    str1 = result_time.output_time()

    if day != "":
        return str1 + ", " + result_day + number_of_dayss

    new_time = str1 + number_of_dayss

    return new_time

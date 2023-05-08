"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is
expressed as a combination of years, days, hours, minutes and seconds.
It is much easier to understand with an example:
* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.
Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.
A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
correct, but 1 year and 1 second is.
Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but
it should be just 1 minute.
A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1
minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid
more significant unit of time.
"""
def format_duration(seconds):
    y,d,h,m,s = 0,0,0,0,0
    if seconds == 0:
        return "now"
    res = ""
    y = int(seconds/31536000)
    if y >= 1:
        seconds = ((seconds/31536000) - int(seconds/31536000))*31536000
        if y > 1:
            res += str(y) + " " + "years"
        elif y == 1:
            res += str(y) + " " + "year"
        if seconds > 0:
            res += ", "
    else:
        res += ""
    d = int(seconds/86400)
    if d >= 1:
        seconds = ((seconds/86400) - int(seconds/86400))*86400
        if d > 1:
            res += str(d) + " " + "days"
        elif d == 1:
            res += str(d) + " " + "day"
        if seconds > 0:
            res += ", "
    else:
        res += ""
    h = int(seconds/3600)
    if h >= 1:
        seconds = ((seconds/3600) - int(seconds/3600))*3600
        if h > 1:
            res += str(h) + " " + "hours"
        elif h == 1:
            res += str(h) + " " + "hour"
        if seconds > 0:
            res += ", "
    else:
        res += ""
    m = int(seconds/60)
    if m >= 1:
        seconds = ((seconds /60) - int(seconds / 60))*60
        print(seconds)
        if m > 1:
            res += str(m) + " " + "minutes"
        elif m == 1:
            res += str(m) + " " + "minute"
        if seconds > 0:
            res += " and "
    else:
        res += ""
    s = int(seconds)
    if s > 1:
        res += str(s)+" "+"seconds"
    elif s == 1:
        res += str(s)+" "+"second"

    print(res)

seconds = 3662151515151
res = format_duration(seconds)
print(res)


# words = ["year", "day", "hour", "minute", "second"]
#
#     if not seconds:
#         return "now"
#     else:
#         m, s = divmod(seconds, 60)
#         h, m = divmod(m, 60)
#         d, h = divmod(h, 24)
#         y, d = divmod(d, 365)
#
#         time = [y, d, h, m, s]
#
#         duration = []
#
#         for x, i in enumerate(time):
#             if i == 1:
#                 duration.append(f"{i} {words[x]}")
#             elif i > 1:
#                 duration.append(f"{i} {words[x]}s")
#
#         if len(duration) == 1:
#             return duration[0]
#         elif len(duration) == 2:
#             return f"{duration[0]} and {duration[1]}"
#         else:
#             return ", ".join(duration[:-1]) + " and " + duration[-1]
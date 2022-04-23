from datetime import date


def getFileNamePart():
    req_date = date.today()
    x = req_date.day
    y = req_date.strftime("%b")
    z = req_date.year
    formatted_date = str(x - 1) + "-" + y + "-" + str(z)
    return formatted_date
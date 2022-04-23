import requests

from utils.utils import getFileNamePart


def first_function():
    formatted_date = getFileNamePart()
    params = {'frmdt': formatted_date}
    resp = requests.get("https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx",params=params)
    response_text = resp.text
    filtered_response = "".join(c for c in response_text if ord(c) < 128)
    with open('/Users/karanprinja/Documents/sample' + formatted_date + '.txt', 'w') as json_file:
        for lines in filtered_response:
            json_file.writelines(str(lines))
first_function()
from practice.utils.reader import get_file_contents
from practice.utils.constant import MappingIndexF2
from datetime import datetime

file_contents = get_file_contents()

for file_content in file_contents:
    date = file_content[MappingIndexF2.DATE]
    events = file_content[MappingIndexF2.EVENTS]

    if events == "Thunderstorm":

        date_str = str(date)

        date_to_names = datetime.strptime(date_str, "%Y-%m-%d")
        day_name = date_to_names.strftime("%A")

        print(f"{date_str} of weather is Thunderstorm and day is {day_name}")

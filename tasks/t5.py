from practice.utils.reader import get_file_contents
from practice.utils.constant import MappingIndexF2

file_contents = get_file_contents()

for file_content in file_contents:
    date = file_content[MappingIndexF2.DATE]
    events = file_content[MappingIndexF2.EVENTS]

    if events in ["Rain",  "Snow",  "Rain-Snow"]:

        print(f"{events} of the date {date}")

from practice.utils.reader import get_file_contents
from practice.utils.constant import MappingIndexF1

file_contents = get_file_contents()

for file_content in file_contents:
    date = file_content[MappingIndexF1.DATE]
    max_temperature = float(file_content[MappingIndexF1.MAXIMUM_TEMPERATURE])
    min_temperature = float(file_content[MappingIndexF1.MINIMUM_TEMPERATURE])

    difference = max_temperature - min_temperature

    print(f"{date}, Maximum-Temp is {max_temperature} AND Minimum-Temp is {min_temperature} Differance, {difference}")

import json
import xml.etree.ElementTree as ET


def json_parser(json_string):
    data = json.loads(json_string)
    return data



def xml_parser(xml_string):
    root_element = ET.fromstring(xml_string)
    return root_element


json_string1 ='{"Age": "20", "Name": "Evan", "Employed": true}'
print(json_parser(json_string1))
print(type(json_parser(json_string1)))

xml_string1 = """
<root>
    <person>
        <name>Ivan</name>
        <age>50</age>
    </person>
</root>
"""

result = xml_parser(xml_string1)
print(result)
print(type(result))

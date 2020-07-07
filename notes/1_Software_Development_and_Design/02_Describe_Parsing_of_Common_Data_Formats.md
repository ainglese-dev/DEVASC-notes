# Describe Parsing of Common Data Formats

## JSON

Use the built-in `json` module

### JSON to Python Objects
- `json.load()`: Deserialize a JSON document from a file to python structures
- `json.loads()`: Deserialize a JSON document from a string to python structures

### Python Objects to JSON
- `json.dump()`: Serialize python structures to a JSON document in a file
- `json.dumps()`: Serialize python structures to a JSON document in a string

## XML

### XML to Python Objects

#### ElementTree

```
import xml.etree.ElementTree as ET

# Import the contents of the file 'example.xml' and store as a string
raw_xml = open("example.xml", "r")

#Parse the data into an ElementTree object
xml_etree = ET.parse(raw_xml)

# Grab the 'root' Element object from the ElementTree
root = xml_etree.getroot()

# Iterate through each child of the root Element
for ele in root:
    # Print the stringified version of the element
    print(ET.tostring(ele))
    print("")

    # Print the 'Id' attribute of the Element object
    print(e.get("Id"))
```

#### lxml

```
#!/usr/bin/env python

from lxml import etree as ET

xml_etree = ET.parse(raw_xml)

## The rest should look pretty familiar
```

#### xmltodict

Must be installed before it's usable:

```
# pip install xmltodict
```

```
#!/usr/bin/env python
import xmltodict

# Import the contents of th efile 'example.xml' and store as a string
raw_xml = open("example.xml", "r")

# Parse XML into an OrderedDict object
not_xml = xmltodict.parse(raw_xml.read())

for ele in not_xml:
    print(ele)
```

### Python Objects to JSON

#### xmltodict

Offers an 'unparse' method to convert a dict to xml:

```
#!/usr/bin/env python

import xmltodict

not_xml = {"root": {"sub1": "value1", "sub2": "value2"}}

totes_xml = xmltodict.unparse(not_xml)

print(totes_xml)
```

#### dicttoxml

Third-party module needs to be installed:

```
# pip install dicttoxml
```

##### Dict to XML

```
#!/usr/bin/env python
from dicttoxml import dicttoxml

xml = dicttoxml(somedict)
```

##### JSON to XML

```
#!/usr/bin/env python

import json
from dicttoxml import dicttoxml

obj = json.loads(json_api_resp)

xml = dicttoxml(obj)
```


## YAML

The third-party `PyYAML` package must be installed:

```
# pip install PyYAML
```

```
#!/usr/bin/env python

import yaml

yaml.safe_load(yaml_string)
```

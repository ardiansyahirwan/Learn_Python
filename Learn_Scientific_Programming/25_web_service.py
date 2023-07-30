import xml.etree.ElementTree as ET
import xmlschema

# XML data as a string
xml_data = '''
<root>
    <person>
        <name>John</name>
        <age>30</age>
    </person>
    <person>
        <name>Jane</name>
        <age>25</age>
    </person>
</root>
'''

# XML Schema as a string
xml_schema = '''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:element name="root">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="person" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="name" type="xs:string"/>
              <xs:element name="age" type="xs:int"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
'''

# Parse XML data into an ElementTree object
xml_tree = ET.ElementTree(ET.fromstring(xml_data))

# Create an XMLSchema object with the XML Schema
schema = xmlschema.XMLSchema(xml_schema)

# Validate XML data against the XML Schema
is_valid = schema.is_valid(xml_tree)

# Output validation result
if is_valid:
    print("XML data is valid according to the XML Schema.")
else:
    print("XML data is NOT valid according to the XML Schema.")
    print("Validation errors:")
    for error in schema.errors:
        print(error)

import xml.etree.ElementTree as ET
tree = ET.parse('MKB308 2.4.xml')

root = tree.getroot()

i = 0
element_count = len(root)

cSql = "insert into mkb_bot.mkb_10(id, id_parent, mkb_code, mkb_name, rec_code, addl_code) values({}, {}, {}, {}, {}, {});\n"

def toSqlValue(s):
    s = s.strip()
    if s == '':
        return 'null'
    else:
        return "'{}'".format(s.replace("'", "''"))

def toSqlIntVelue(s):
    s = s.strip()
    if s == '':
        return 'null'
    else:
        return s

f = open('out.sql', 'w')

f.write('delete from mkb_bot.mkb_10;\n\n')

while i < element_count:
    mkb_code = toSqlValue(root[i].text)
    rec_code = toSqlValue(root[i + 1].text)
    addl_code = toSqlValue(root[i + 2].text)
    mkb_name = toSqlValue(root[i + 3].text)
    id = root[i + 4].text
    id_parent = toSqlIntVelue(root[i + 5].text)

    f.write(cSql.format(id, id_parent, mkb_code, mkb_name, rec_code, addl_code))

    i += 6

f.close()

u"""Parse html to readable table"""
import re
import xml as etree


def getMarksTable(document):
    table_pattern = "<table [^$]* id=\"ctl00_ctl00_ContentPlaceHolder_RightContentPlaceHolder_dgDane\">[^$]*</table>"
    document = re.findall(table_pattern, document)
    return document[0]


def creteGradeList(dcm):
    document = getMarksTable(dcm)
    words = document.split('&nbsp;')
    document = ' '.join(words)

    tree = etree.fromstring(document)
    result = []

    for row in tree:
        tmp = row.getchildren()
        tmp_list = []

        for cell in tmp:
            tmp_list.append(cell.text)
        result.append(tmp_list)

    return result


def saveTableToFile(table, filename="oceny.txt"):
    file = open(filename, 'w')
    for row in table:
        try:
            file.write("    ".join(row))
        except TypeError:
            pass
        # print i, # python2.x
        file.write("\n")

    file.close()


if __name__ == "__main__":
    f = open('test.html')
    doc = f.read()
    f.close()
    res = creteGradeList(doc)

    for row in res:
        for i in row:
            print(i, end=" ")
            # print i, # python2.x
        print("\n")

    saveTableToFile(res)

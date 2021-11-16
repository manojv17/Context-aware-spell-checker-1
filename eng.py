from gingerit.gingerit import GingerIt #Gingerit is used to ease the file collection of dictionaries and to compare the data to the database.

def ginger(data):
      result = GingerIt().parse(data)
      return result #method to compare the text to the database and lets the miss spelt words.

if __name__ == '__main__':

    with open('tests.tsv',  encoding="utf8") as f:
        row_list = []
        for row in f:
            stripped = row.strip()
            row_list = stripped.split()
            data = row_list[0]
            w = ginger(data)
            if w!= row_list[1]:
                print('Test case failed. Expected', row_list[1], 'when spell checking',row_list[0], 'but got',w)
            else:
                print('Test case passed')

    f.close()
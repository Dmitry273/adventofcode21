class Table:
    def __init__(self, rows):
        self.rows = rows

data = [i.strip() for i in open('Day4/d4.txt', 'r')]
nums = data[0].split(',')
tables = []

for j in range((len(data)-1)//6):
    table_rows = []
    cols = [[],[],[],[],[]]
    for i in range(5):
        row = data[2+6*j+i].split()
        table_rows.append(row)
        for k, num in enumerate(row):
            cols[k].append(num)
    table_rows = table_rows + cols
        
    tables.append(Table(table_rows))

for i in range(len(nums)):
    sett = set(nums[:i])
    for table in tables:
        for row in table.rows:
            if set(row).issubset(sett):
                final = nums[i-1]
                winner = table
                allnums = sett
                break
        else:
            continue
        break
    else:
        continue
    break

winner_nums = set()
for row in winner.rows:
    winner_nums |= set(row)

print(sum([int(i) for i in winner_nums.difference(allnums)])*int(final))

import csv

# Open raw csv file in read mode
raw_data = open('rock.csv', 'rb')  # python 3: rU

# Instantiate DictReader with our raw data
reader = csv.DictReader(raw_data)

rows = [row for row in reader]


def is_valid_year(candidate):
    """
    Returns boolean value.
    """
    try:
        int(candidate)
    except ValueError:
        return False
    else:
        return int(candidate) > 1900


print "There were {} songs released in 1981".format(
    len([row for row in rows if row['Release Year'] == '1981'])
)

print "There were {} songs released before 1984".format(
    len([row for row in rows
        if is_valid_year(row['Release Year'])
        and int(row['Release Year']) < 1984])
    )

print "The earliest release year is {}".format(
    min([int(row['Release Year'])
        for row in rows
        if is_valid_year(row['Release Year'])])
)

sorted_by_playcount = sorted(
    rows,
    key=lambda row: int(row['PlayCount']),
    reverse=True
)
print "The top 20 songs by play count are:"

title_and_playcount = [
    (row['PlayCount'], row['Song Clean'])
    for row in sorted_by_playcount[:20]
]

for data in title_and_playcount:
    print data


import ipdb; ipdb.set_trace();
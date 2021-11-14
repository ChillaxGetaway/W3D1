places = [' ','Argentina','','San Diego','','Boston','','Ney York','']

f= lambda x:x if x.strip() else None
filtered_places = list(filter(f, places))
print(filtered_places)



#2

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
sorted_authors = sorted(authors, key=lambda n:n.split() [-1]. lower())
print (sorted_authors)





#3
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

f_places = list(map(lambda d: (d[0], d[1]*(9/5)+32), places))
print (f_places)
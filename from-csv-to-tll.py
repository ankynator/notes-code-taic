# import the CSV module for dealing with CSV files
import csv

# create a 'reader' variable, which allows us to play with the contents of the CSV file
# in order to do that, we create the ifile variable, open the CSV file into that, then pass its' contents into the reader variable.
ifile = open('./casos_covid.csv', 'rt')
reader = csv.reader(ifile)


# create a new variable called 'outfile' (could be any name), which we'll use to create a new file that we'll pass our TTL into.
outfile = open('./casos_covid_v1.ttl', 'a')

# header
outfile.write('@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n')
outfile.write('@prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> .\n')
outfile.write('@prefix dc: <http://purl.org/dc/elements/1.1/> .\n')
outfile.write('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n')


# get python to loop through each row in the CSV, and ignore the first row.
rownum = 0
for row in reader:
    if rownum == 0:
        pass
    else:  # if it's not the first row, place the contents of the row into the 'c' variable, then create a 'd' variable with the stuff we want in the file.
        c = row

        d = 'dataFromRegion:' + c[1] + '\n' \
            'rdf:type bsbm:Region ; \n' \
            'bsbm: PCR(+) ' + '"' + c[2] + '"' + '^^xsd:Integer ;\n' \
            'bsbm: PruebaRapida(+) ' + '"' + c[3] + '"' + '^^xsd:Integer ;\n' \
            'bsbm: PruebaAntigeno(+) ' + '"' + c[4] + '"' + '^^xsd:Integer ;\n' \
            'bsbm: TotalCasos(+) ' + '"' + c[5] + '"' + '^^xsd:Integer ;\n' \
            'bsbm: Fallecidos ' + '"' + c[6] + '"' + '^^xsd:Integer ;\n' \


        outfile.write(d)  # now write the d variable into the file
    rownum += 1  # advance the row number so we can loop through again with the next row

# finish off by closing the two files we created

outfile.close()
ifile.close()

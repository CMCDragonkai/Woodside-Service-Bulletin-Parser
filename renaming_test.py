#!/usr/bin/env python2
import os, sys, csv

# all paths are absolute and start with root `/`
renaming_rules_csv_path = '/path/to/Titles.csv'
bulletin_directory_path = '/path/to/bulletins/directory/'

with open(renaming_rules_csv_path, 'rU') as csv_file:
    
    csv_table = csv.reader(csv_file, delimiter = ',')

    for csv_row in csv_table:

        oldPath = os.path.join(bulletin_directory_path, csv_row[0])

        if os.path.exists(oldPath):

            newPath = os.path.join(bulletin_directory_path, csv_row[1])
            os.rename(oldPath, newPath)
            print >> sys.stdout, "Renamed '%s' to '%s'!" % (oldPath, newPath)

        else:

            print >> sys.stderr, "File '%s' not found!" % oldPath
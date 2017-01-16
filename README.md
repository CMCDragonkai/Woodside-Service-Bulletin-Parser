Woodside Service Bulletin Parser
================================

Note that all directories will be scanned recursively.

If you have mutated the CSV output, save the files elsewhere, so they won't be overwritten with automated runs of the below commands.

```sh
# phase 1, parse compliance reports
extract-compliance-data './directory/to/compliance-reports' './path/to/compliance.csv' >./compliance-parsed.txt 2>./compliance-unparsed.txt

# look at compliance-unparsed.txt to examine which compliance report files you need to parse manually
# it's possible that some compliance report files have their table titles on page X and their table data on page X+1
# this will trip up the parser

# phase 2, parse bulletins
extract-bulletin-data './directory/to/bulletins' './path/to/bulletins.csv' >./bulletins-parsed.txt 2>./bulletins-unparsed.txt

# look at bulletins-unparsed.txt to examine which bulletin files you need to parse manually

# phase 3, cross-reference the 2 CSV files and combine
# needs python csvkit csvsql
# ensure both CSV files are UTF-8 encoded
# detect encoding with `file -bi ./file.csv`

./combine-bulletin-compliance './path/to/compliance.csv' './path/to/bulletins.csv' './path/to/combined.csv'
```

######################################################
### Extracts simple dates  from a txt file         ###
### Author: Marco Fonseca                          ###
### Last update: 2016/02/09 15:37:51               ### 
######################################################


import sys     
text_file=sys.argv[1] #this is to read the file direct from the command line

import re 

regex1 = r'((the|The)\s\d{1,2}[(st|nd|rd|th)?\s(of)\s[a-zA-Z]+(,\s?\d{4})?)' #matches patterns such as the 21st of december. Markers of ordinal numbers and year are optional. 
regex2 = r'(\d+/\d+/\d+)' #matches patterns such as XX/XX/XXXX
regex3 =r'((January|Jan.)|(February|Feb.)|(March|Mar.)|(April|Ap.|Apr.|)|May|(June|Jun.)|(July|Jul.)|(August|Aug.)|(September|Sep.)|(November|Nov.)|(December|Dec.)|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday)(\s(the))?\s\d{1,2}(st|nd|rd|th)?(,\s?\d{4})?'

regex3 =r'(January|February|March|April|May|June|July|August|September|November|December|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday)(\s(the))?\s\d{1,2}(st|nd|rd|th)?(,\s?\d{4})?'


#matches patterns such as "Month/Day of the week the 1st, 2012". 'The' and year are optional.
regex4= r'((New Year\'s|Martin Luther King|George Washington\’s Birthday|Memorial|Independence|Columbus|Labor|Veterans|Thanksgiving|Christmas)(\sDay)?)' #matches national holidays
regex5= r'(January|February|March|April|May|June|July|August|September|November|December)' #matches individual months 
regex6= r'((Sunday|Monday|Tuesday|Thursday|Friday|Saturday)(\safternoon|\smorning|\sevening|\snight)?)'#matches individuals days of the weeks plus optional "night, afternoon"

#regex6 = r'(Sunday|Monday|Tuesday|Thursday|Friday|Saturday)' #matches individuals days of the weeks
regex = re.compile('('+regex1+'|'+regex2+'|'+regex3+'|'+regex4+'|'+regex5+'|'+regex6+')') #compiles all the regexes

news = open(text_file) 
for line in news:
    dates = regex.findall(line) #looks for the regexes 
    for i in dates:
        print(i[0])#prints only the first tuple because I was getting unnecessary information
        i[0].write("output.txt")


#print [i[0]]



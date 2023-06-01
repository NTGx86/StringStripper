'''
Title:             StringStripper
Verison:           1.2
Author:            NTGx86
Last Modified:     June 1 2023


Short Description: 

This script filters the output from Strings.exe (Forensics/Malware Analysis tool). Attempting to remove the vast
majority of strings that will not likely be relevant to a malware analyst. 

Detailed Description: 

For those familiar with Strings.exe you're surely aware that more often than not the number of lines outputted
can be more than anyone wants to manual sift through. Hence, I've created this tool. As of now it first searches 
for strings or lines that contain possible file extensions or urls and then it searches for any other 
possible relevant strings of either a shorter length or a longer length. Then lastly includes strings that are
over 15 chars in length, as there's a higher chance they may be relevant to a malware analyst. 

Future Plans:

1) Change the functionality so it can work from the command-line.
2) Continue to test the script against real live malware and refine the filtering parameters. 

Final Notes: 

This script just like many other on my GitHub page are tools that I delevoped as projects
in response to my cybersecurity engineering coursework at the University of Arizona. With that in mind, much 
of the functionality is not exactly novel or groundbreaking, but simply a method for me to apply my skills and 
have fun with python. 
'''

import re
import argparse                     # Command Line Argument Parsing

# Print starting message to console
print('Script Starting\n')

# keeping track of all specifically initial lines
additionalLineCount = 0
allOtherCount = 0

# creating an empty set to store all strings
strings = set()

try: 
    # Open file named "strings.txt" in read mode and read in all lines
    # Sort the lines by length in reverse order (longest first)
    with open('strings.txt', 'r') as file:
        # lines is all the strings pulled from a file
        lines = sorted(file.readlines(), key=len, reverse=True)
    
    print('Processing File: strings.txt\n')
        
    # Open "final_lines.txt" in write mode
    # check for any mathces and write them to the file (basically what you might grep for) 
    with open('final_lines.txt', 'w') as f:
        ''' WRITING LINES THAT CONTAIN ANY POSSIBLE FILE EXTENSIONS OR URLs '''
        f.write('='*75)
        f.write('\nWRITING LINES THAT CONTAIN ANY POSSIBLE FILE EXTENSIONS OR URLs\n')
        f.write('='*75)  
        f.write('\n')        
        for line in lines:
            possibleFileExtMatch = re.findall(r'\.\w{3}', line)
            if possibleFileExtMatch:
                f.write(line)
                strings.add(line)
                additionalLineCount += 1
        f.write('\n') 
        f.write('='*75) 
        f.write('\n')      
 
    ''' Start of Regex madness created with the help of ChatGPT (will refine at some point)  '''
    # Define a list comprehension to filter the input 'lines' list.
    # The filtered list 'valid_lines' only includes lines that:
    # 1) Are 4 characters or longer (after leading and trailing whitespace is removed).
    # 2) Do not contain three consecutive non-alphanumeric characters.
    valid_lines = [
        line.strip() for line in lines 
        if len(line.strip()) >= 4 and not re.search(r'[^\w\d]{3}', line)
    ]
    
    # Define a second list comprehension to further filter 'valid_lines'.
    # The resulting list 'short_lines' only includes lines that:
    # 1) Are shorter than 6 characters.
    # 2) Do not contain at least two consecutive characters from the set '%=+;"@#$][}{'. 
    short_lines = [
        line for line in valid_lines 
        if len(line) < 6 and not re.search(r'[%=+;"@#$\]\[\}\{]{2,}', line)
    ]
    
    # Define a third list comprehension to further filter 'valid_lines'.
    # The resulting list 'long_lines' only includes lines that:
    # 1) Are 7 characters or longer.
    # 2) Do not contain at least three consecutive characters from the set '%=+;"@#$][}{'. 
    long_lines = [
        line for line in valid_lines 
        if len(line) >= 7 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line)
    ]

    ''' Open "final_lines.txt" in append mode '''
    with open('final_lines.txt', 'a') as f:
        f.write('WRITING SHORT & LONG STRIPPED LINES\n')
        f.write('='*75)
        f.write('\n') 
        
        ''' long lines  '''
        for line in long_lines:
            if (line not in strings):
                # Write each non-duplicate long line to the file
                f.write(line + '\n')
                strings.add(line)
                allOtherCount += 1 
                
        ''' short lines  '''
        for line in short_lines:
            if (line not in strings):
                # Write each non-duplicate short line to the file
                f.write(line + '\n')
                strings.add(line)
                allOtherCount += 1 

        f.write('\n')
        f.write('='*75)
        f.write('\nWRITING ALL REALLY LONG UNALTERED LINES (>15 IN LENGTH).\n')
        f.write('='*75)  
        f.write('\n') 
        
        ''' really long lines  '''
        for line in lines:
            # write all longest lines not already written
            if (line not in strings) and (len(line) > 15):
                f.write(line)
                strings.add(line)
                allOtherCount += 1             
        f.write('\n')
        f.write('='*75)
        f.write('\nALL STRIPPED LINES PRINTED. SCRIPT COMPLETE.\n')
        f.write('='*75)      
    
    ''' Script complete printing results to screen '''    
    print("Number of lines in file before filtering: ", len(lines))
    print("Number of lines after filtering:          ", len(strings))
    
    print('\nOutput File Created: final_lines.txt')
    
    print('\nScript Complete')

except Exception as error:
    print(f"An error occurred: {error}\n")
    print('Script Exiting\n')

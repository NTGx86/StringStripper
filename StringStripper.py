'''
Title:             StringStripper
Verison:           1.0
Author:            NTGx86
Last Modified:     May 22 2023

Detailed Description:

For those familiar with Strings.exe you're surely aware that more often than not the number of lines outputted
can be more than anyone wants to manual sift through. Hence, while learning malware analysis at the
University of Arizona I created a python script to filter out many of the lines that aren't relative to 
a malware analyst. 

Future Plans:

1) Adjusting it to do the equilivalent of grep for ".exe", "www.", ".com", etc.
2) Change the functionality so it can work from the command-line.

Final Notes: 

This script just like many other on my GitHub page are tools that I delevoped as projects
in response to my cybersecurity engineering coursework at the University of Arizona. With that in mind, many 
of the functionality is not exactly novel or groundbreaking, but simply a method for me to apply my skills and have 
fun with python. 
'''

import re
import argparse                     # Command Line Argument Parsing

# Print starting message to console
print('Script Starting\n')

try: 
    # Open file named "strings.txt" in read mode and read in all lines
    # Sort the lines by length in reverse order (longest first)
    with open('strings.txt', 'r') as file:
        # lines is all the strings pulled from a file
        lines = sorted(file.readlines(), key=len, reverse=True)
    
    print('Processing File: strings.txt\n')   
        
    
    # Filter out invalid lines based on these criteria:
    # - Line length must at least 4 characters
    # - Line must not contain 3 or more consecutive non-alphanumeric characters
    valid_lines = [line for line in lines if len(line.rstrip()) >= 4 and not re.search(r'[^\w\d]{3}', line)]

    # Filter out lines that contain 2 or more occurrences (consecutive or non-consecutive) 
    # of the specified special characters using a regular expression with a positive lookahead assertion 
    # to check for the presence of the characters, followed by the same characters again.
    final_lines = [line for line in valid_lines if not re.search(r'[%=+;"@#$\]\[\}\{]{2,}', line)]
    

    # the lines below perform additional filtering based on number of special chars and length of the string
    final_lines2 = [line for line in final_lines if not (len(line.strip()) == 5 and not re.search(r'[%=+;"@#$\]\[\}\{]{2,}', line))]

    final_lines3 = [line for line in final_lines2 if not (len(line.strip()) == 6 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]

    final_lines4 = [line for line in final_lines3 if not (len(line.strip()) == 7 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]

    final_lines5 = [line for line in final_lines4 if not (len(line.strip()) == 8 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]

    final_lines6 = [line for line in final_lines5 if not (len(line.strip()) == 9 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]

    final_lines7 = [line for line in final_lines6 if not (len(line.strip()) == 10 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]
            
    final_lines8 = [line for line in final_lines7 if not (len(line.strip()) == 11 and not re.search(r'[%=+;"@#$\]\[\}\{]{3,}', line))]

    # Open a new file named "final_lines.txt" in write mode
    # Write each line in final_lines8 to the new file
    with open('final_lines.txt', 'w') as f:
        for line in final_lines8:
            f.write(line)

    # Count the number of lines in final_lines8 and print the count to the console
    print("Number of lines in file before filtering: ", len(lines))

    # print the number of lines for the filtered results
    print("Number of lines after filtering:          ", len(final_lines8))

    print('\nOutput File Created: final_lines.txt')

    # Print completion message to console
    print('\nScript Complete')

except Exception as error:
    print(f"An error occurred: {error}\n")
    print('Script Exiting\n')
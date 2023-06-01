# StringStripper
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
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    infile = open('c:/Users/Cory/Documents/_Code/Python_EssentialTraining/Exercise Files/Chap12/lines.txt', 'rt')
    outfile = open('c:/Users/Cory/Documents/_Code/Python_EssentialTraining/Exercise Files/Chap12/lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile) # using print I can change the line endings on the fly
        #could also use this
        # outfile.writelines(line)
        print('.', end='', flush=True) # end='' Prevents a new line, flush=True cleaning the output buffer for some OS's
    outfile.close() # closing the output file to prevent data loss
    print('\ndone.')

if __name__ == '__main__': main()

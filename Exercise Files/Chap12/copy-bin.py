#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# copies a Binary File

def main():
    infile = open('c:/Users/Cory/Documents/_Code/Python_EssentialTraining/Exercise Files/Chap12/berlin.jpg', 'rb')
    outfile = open('c:/Users/Cory/Documents/_Code/Python_EssentialTraining/Exercise Files/Chap12/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # Don't want to read the entire file 10,000Bytes / 10kb is pretty small, need to know how much system ram you have
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

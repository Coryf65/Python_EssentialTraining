#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:

    sound = 'Quaaaack!'
    walking = 'Walk like a Duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        # calling self gives us access into the Properties
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()

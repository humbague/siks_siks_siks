import os
import random
import numpy as np


class CollectLyrics(object):
    def __init__(self, albums):
        self.albums = albums

    def read_lyrics(self):
        albums = self.albums
        """Read lyrics for a specified number of albums"""
        # list to collect lyrics
        lrcs = []

        # the length of the cong
        lensong = []

        for alb in albums:
            # go to the directory
            os.chdir(alb)
            # find the number of songs
            song = os.listdir(os.getcwd())

            alrc = []
            for isng in song:
                tlrc = []
                f = open(isng, 'r')
                for row in f:
                    tlrc.append(f.readline())
                f.close()
                alrc.append(tlrc)
                if len(tlrc) > 1:
                    lensong.append(len(tlrc))

            os.chdir('../')
            lrcs.append(alrc)

        return lrcs


    def write_database(self,lrcs):
        """Create a database with all of the song lines"""

        # allocate list
        lns = []

        for i in range(len(lrcs)):
            # album level
            for j in range(len(lrcs[i])):
                # song level
                for k in range(1,len(lrcs[i][j])):
                    lns.append(lrcs[i][j][k])

        # create database
        f = open('KISS_LINES','w')

        for iln in lns:
            f.write(iln)

        f.close()

        return 1

    def add_to_database(self, lyrcs):
        """Create a database with all of the song lines"""

        # allocate list
        lns = []

        for i in range(len(lyrcs)):
            # album level
            for j in range(len(lyrcs[i])):
                # song level
                for k in range(1, len(lyrcs[i][j])):
                    lns.append(lyrcs[i][j][k])

        # create database
        f = open('KISS_LINES', 'a')

        for iln in lns:
            f.write(iln)

        f.close()

        return 1

    def read_database(self):
        """Read the KISS_LINES database"""
        # open the database
        f = open('KISS_LINES','r')
        # make a list which will contain lines
        tlc = []
        for row in f:
            tlc.append(f.readline())
        f.close()

        return tlc

    def create_song(self, lnmn, lnmx):
        """
        Create a song from the databse KISS_LINES
        lnmn: minimum number of lines
        lnmx: maximum number of lines
        """
        # decide on the length of the song
        nlng = random.randint(lnmn, lnmx)

        # load the database
        lns = self.read_database()

        # randomly pick nlng lines
        rsong = []
        for i in range(nlng):
            j = random.randint(0,len(lns)-1)
            rsong.append(lns[j])

        return rsong

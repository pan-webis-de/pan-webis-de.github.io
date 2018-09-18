#!/usr/bin/env python

"""Random baseline for the PAN19 hyperpartisan news detection task"""

from __future__ import division

import os
import getopt
import sys
import xml.sax
import random

random.seed(42)
runOutputFileName = "prediction.txt"


def parse_options():
    """Parses the command line options."""
    try:
        long_options = ["inputDataset=", "outputDir="]
        opts, _ = getopt.getopt(sys.argv[1:], "d:o:", long_options)
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    inputDataset = "undefined"
    outputDir = "undefined"

    for opt, arg in opts:
        if opt in ("-d", "--inputDataset"):
            inputDataset = arg
        elif opt in ("-o", "--outputDir"):
            outputDir = arg
        else:
            assert False, "Unknown option."
    if inputDataset == "undefined":
        sys.exit("Input dataset is undefined. Use option -d or --inputDataset.")
    elif not os.path.exists(inputDataset):
        sys.exit("The input dataset folder does not exist (%s)." % inputDataset)

    if outputDir == "undefined":
        sys.exit("Output path undefined. Use option -o or --outputDir.")
    elif not os.path.exists(outputDir):
        os.mkdir(outputDir)

    return (inputDataset, outputDir)


########## SAX ##########

class HyperpartisanNewsRandomPredictor(xml.sax.ContentHandler):
    def __init__(self, outFile):
        xml.sax.ContentHandler.__init__(self)
        self.outFile = outFile

    def startElement(self, name, attrs):
        if name == "article":
            articleId = attrs.getValue("id")
            prediction = random.choice(["true", "false"])
            confidence = random.random()
            self.outFile.write(articleId + " " + prediction + " " + str(confidence) + "\n")


########## MAIN ##########


def main(inputDataset, outputDir):
    """Main method of this module."""

    with open(outputDir + "/" + runOutputFileName, 'w') as outFile:
        for file in os.listdir(inputDataset):
	    if file.endswith(".xml"):
	        with open(inputDataset + "/" + file) as inputRunFile:
	            xml.sax.parse(inputRunFile, HyperpartisanNewsRandomPredictor(outFile))


    print("The predictions have been written to the output folder.")


if __name__ == '__main__':
    main(*parse_options())


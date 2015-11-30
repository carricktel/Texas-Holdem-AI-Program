#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carricktel
#
# Created:     24/10/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Out:

    def __init__(self):
        self.output = ""


    def append_output(self,string):
        self.output += str(string) + "\n"

    def return_output(self):
        return self.output


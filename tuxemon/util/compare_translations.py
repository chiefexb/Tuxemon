#!/usr/bin/python
# -*- coding: utf-8 -*
# Compare Translations Utility
# Copyright (C) 2016, Alex Pricker <alex.pricker@gmail.com>
# https://github.com/chiefexb/Tuxemon
# This file is part of Compare Translations Utility.
#
# Compare Translations Utility is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Compare Translations Utility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sprite Splitter.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# Alex Pricker <alex.pricker@gmail.com>
# https://github.com/chiefexb/Tuxemon
# compare_translations.py is utiliy that provide compare original locale "en_US" with another locale
# and update it. Usefull tools for localization.
#
# Usage:
# ./compare_translations.py <locale_name> 
#
#

# Check to see 
import json
import sys
import os
def main():
    if len(sys.argv) <2:
       print "Copyright (C) 2016, Alex Pricker <alex.pricker@gmail.com>  https://github.com/chiefexb/Tuxemon"
       print "Usage : ./compare_translation.pu <Your.Locale> [update]"
       print 'update-option update your locale file'
       sys.exit(2)
    f=file ("../resources/db/locale/en_US.json")
    mylocale=sys.argv[1]
    orig=json.load(f)
    f.close()
    #print orig.keys(),len(orig.keys())
    if os.path.isfile("../resources/db/locale/"+mylocale+".json" ):
        f=file ("../resources/db/locale/"+mylocale+".json")
        loc=json.load(f)
        f.close()
        #print loc
        difflist=list(set (orig.keys())-set(loc.keys()) )
        if len(difflist)>0:
            print "Find new "+str(len(difflist)) +"strings to tranlate."
    else:
      print "no file"+"../resources/db/locale/"+mylocale+".json"
      print "type for create new locale file for translation: "
      print "./compare_tranlation.py "+mylocale+" update"  
if __name__ == "__main__":
    main()

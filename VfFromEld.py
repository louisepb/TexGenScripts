# =============================================================================
# Script to calculate average yarn volume fraction from .eld file output by
# TexGen Abaqus export
# Copyright (C) 2016 Mikhail Matveev, Louise Brown

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# =============================================================================

# Count fibre volume fraction
import sys, getopt

def main():
    # Get filename
    try:
        opts, args = getopt.getopt(sys.argv[1:], "")
        Filename = args
        assert(len(Filename) == 1)
    except:
        print 'Usage: python VfFromEld.py <Filename>'
        return
    
    file = open( Filename[0] )
    vf = 0.0
    maxvf = 0.0
    count = 0.0
    # Read the file line by line
    for line in file:
        data = line.split(',')
        # Data lines have six elements
        if (len(data) == 6 ):
            # Volume fraction data is 5th field
            ElementVf = float(data[4].split(',')[0])
            vf = vf + ElementVf
            # Find element with maximum volume fraction
            if (ElementVf > maxvf):
                maxvf = ElementVf
            if (ElementVf > 0.0):
                count = count + 1.0

    file.close()
    print 'Sum of volume fractions = ' + str(vf)
    if (count > 0.0):
        print 'Average volume fraction = ' + str(vf/count)
    print 'Maximum volume fraction = ' + str(maxvf)

if __name__ == '__main__':
    main()

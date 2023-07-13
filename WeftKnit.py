# =============================================================================
# TexGen: Geometric textile modeller.
# Copyright (C) 2006 Martin Sherburn

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

# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *

# Create a textile
Textile = CTextile()

# Create a yarn
Yarn = CYarn()

# Define some constants
r = 1
sx = r*2.5
sy = r*10
ly = 0.75*(sx+r)

# Add nodes to the yarns to describe the yarn path
Yarn.AddNode(CNode(XYZ(0, 0, r)))
Yarn.AddNode(CNode(XYZ(sx+r, ly, 0)))
Yarn.AddNode(CNode(XYZ(sx, ly+0.5*sy, -r)))
Yarn.AddNode(CNode(XYZ(sx-r, ly+sy, 0)))
Yarn.AddNode(CNode(XYZ(2*sx, 2*ly+sy, r)))
Yarn.AddNode(CNode(XYZ(3*sx+r, ly+sy, 0)))
Yarn.AddNode(CNode(XYZ(3*sx, ly+0.5*sy, -r)))
Yarn.AddNode(CNode(XYZ(3*sx-r, ly, 0)))
Yarn.AddNode(CNode(XYZ(4*sx, 0, r)))

# Assign a constant circular cross-section
Section = CSectionEllipse(2*r, 2*r)
Yarn.AssignSection(CYarnSectionConstant(Section))

# Create repeats
Yarn.AddRepeat(XYZ(4*sx, 0, 0))
Yarn.AddRepeat(XYZ(0, 2*sy, 0))

# Set the resolution of the surface mesh created
Yarn.SetResolution(20)

# Add the yarn to the textile
Textile.AddYarn(Yarn)

# Translate the yarn and add it to the textile
# Note that this could be part of the repeat vectors but it is done like 
# this to give the yarns different colours
Yarn.Translate(XYZ(0, sy, 0))
Textile.AddYarn(Yarn)

# Create a domain and assign it to the textile
Textile.AssignDomain(CDomainPlanes(XYZ(0, -ly, -2*r), XYZ(4*(r*sx), 4*sy-ly, 2*r)))

# Add the textile
AddTextile("weftknit", Textile)
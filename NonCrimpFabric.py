# =============================================================================
# TexGen: Geometric textile modeller.
# Copyright (C) 2015 Louise Brown

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

# Create a textile
Textile = CTextile()

# Create a python list containing 2 inlay yarns
Yarns = [CYarn(), CYarn()]

# Define some constants
w = 0.95
s = 1
h = 0.2

# Add nodes to the yarns to describe the yarn path
Yarns[0].AddNode(CNode(XYZ(0, 0, 0)))
Yarns[0].AddNode(CNode(XYZ(0, s, 0)))

Yarns[1].AddNode(CNode(XYZ(0, 0, h)))
Yarns[1].AddNode(CNode(XYZ(s, 0, h)))

# Loop over all the yarns in the list
for Yarn in Yarns:
	# Assign a power ellipse to the inlay yarns
	InlaySection = CSectionPowerEllipse(w, h, 0.5)
	Yarn.AssignSection(CYarnSectionConstant(InlaySection))
	#Add repeats
	Yarn.AddRepeat(XYZ(s, 0, 0))
	Yarn.AddRepeat(XYZ(0, s, 0))
	# Set the interpolation function
	Yarn.AssignInterpolation(CInterpolationCubic())
	# set the resolution of the surface mesh created
	Yarn.SetResolution(40)
	# Add the yarn to our textile
	Textile.AddYarn(Yarn)
	
# Define some more constants for the stitching
a = 0.05
r = 0.025
u = 1.5*h+r
d = -0.5*h-r

# Create a stitch yarn
StitchYarn = CYarn()

# Create stitch yarn path. This path is quite complex and has been 
# created with a fair amount of tweaking. Note that the tangents
# at the nodes have been specified for further control on the path.
StitchYarn.AddNode(CNode(XYZ(2*a, a, u), XYZ(1, 1, 0)))
StitchYarn.AddNode(CNode(XYZ(s+a, s-a, u), XYZ(1, 1, 0)))

StitchYarn.AddNode(CNode(XYZ(s+a, s, d), XYZ(0, 1, 0)))
StitchYarn.AddNode(CNode(XYZ(s+2*a, 2*s-a, d+a), XYZ(0, 1, 0)))

StitchYarn.AddNode(CNode(XYZ(s+a, 2*s, d+a), XYZ(-1, 0, 0)))
StitchYarn.AddNode(CNode(XYZ(s-a, 2*s, d+a), XYZ(-1, 0, 0)))

StitchYarn.AddNode(CNode(XYZ(s+a, 2*s, d+a), XYZ(0, -1, 0)))
StitchYarn.AddNode(CNode(XYZ(s-a, s, d), XYZ(0, -1, 0)))

StitchYarn.AddNode(CNode(XYZ(s-2*a, s+a, u), XYZ(-1, 1, 0)))
StitchYarn.AddNode(CNode(XYZ(-a, 2*s-a, u), XYZ(-1, 1, 0)))
	
StitchYarn.AddNode(CNode(XYZ(-a, 2*s, d), XYZ(0, 1, 0)))
StitchYarn.AddNode(CNode(XYZ(-2*a, 3*s-a, d), XYZ(0, 1, 0)))

StitchYarn.AddNode(CNode(XYZ(-a, 3*s, d+a), XYZ(1, 0, 0)))
StitchYarn.AddNode(CNode(XYZ(a, 3*s, d+a), XYZ(1, 0, 0)))

StitchYarn.AddNode(CNode(XYZ(2*a, 3*s-a, d), XYZ(0, -1, 0)))
StitchYarn.AddNode(CNode(XYZ(a, 2*s, d), XYZ(0, -1, 0)))

StitchYarn.AddNode(CNode(XYZ(2*a, 2*s+a, u), XYZ(1, 1, 0)))

# Add the repeat vectors for the stitching
StitchYarn.AddRepeat(XYZ(1, 0, 0))
StitchYarn.AddRepeat(XYZ(0, 2, 0))

# Assign a circular section to the stitch yarns
StitchSection = CSectionEllipse(2*r, 2*r)
StitchYarn.AssignSection(CYarnSectionConstant(StitchSection))
# Set the interpolation functin to Bezier so that 
# the yarn tangents specified above are respected
StitchYarn.AssignInterpolation(CInterpolationBezier())
# Set a lower surface mesh resolution than for the inlays.
# The stitching is so thin that a high resolution is not needed
StitchYarn.SetResolution(8)
# Translate the stitch yarn so that it falls between the inlay yarns
StitchYarn.Translate(XYZ(0.5*s, 0.5*s+r, 0))
# Add the yarn to the textile
Textile.AddYarn(StitchYarn)

# Create a domain and assign it to the textile
Textile.AssignDomain(CDomainPlanes(XYZ(0, 0, -1), XYZ(4*s, 4*s, 1)))

# Add the textile
AddTextile("NonCrimpFabric", Textile)
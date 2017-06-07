# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 09:50:00 2017

@author: epzlpb
=============================================================================
Copyright (C) 2017 Louise Brown

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
=============================================================================
"""
# Script to remove small intersections between yarns in a textile
# This uses the interference detection implemented in TexGen and then makes
# adjustments to both yarns. Yarn area will be reduced in this process and
# may not be a true representation of the yarn behaviour.  It was intended to 
# remove very small intersections which prevented the model from running in
# FE solvers.

# Get existing textile. May need to add name as parameter if more than one textile created
textile = GetTextile()

# Create vector of CMesh and resize to number of yarns in textile
YarnMeshes = MeshVector()
NumYarns = textile.GetNumYarns()
YarnMeshes.resize(NumYarns)

# May need to adjust tolerance depending on model
Tol = 1e-6

# Create a volume mesh for each yarn, clipped to domain and add to mesh vector
Domain = textile.GetDomain()
for i in range(NumYarns):
    yarn = textile.GetYarn(i)
    yarn.AddVolumeToMesh(YarnMeshes[i], Domain)
  
# Initialise class which does the interference adjustment  
AdjustMesh = CAdjustMeshInterference()

# Mesh is only adjusted if interference is less than one volume mesh element deep
if ( AdjustMesh.AdjustMesh(textile, YarnMeshes, Tol) == False ):
    print("Unable to adjust mesh: intersection depths too large")
else:
    AdjustMesh.AdjustSectionMeshes(textile, YarnMeshes)
    
    
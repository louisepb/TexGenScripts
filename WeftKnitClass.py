# =============================================================================
# TexGen: Geometric textile modeller.
# Copyright (C) 2024 Louise Brown

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

# Create a weft knit textile with 2 wales and courses, wale height 1, loop height 1.2 and yarn thickness 0.15
# The fifth parameter indicates whether to refine the textile to avoid intersections
WeftKnit = CTextileWeftKnit(2, 2, 1, 1.2, 1, 0.15);

numSectionPoints = 30
numSlaveNodes = 60
WeftKnit.SetResolution( numSectionPoints, numSlaveNodes )

# Setup a domain
WeftKnit.AssignDefaultDomain()

# Select knit model (only one available currently)
WeftKnit.SetLoopModel(RAVANDI_2021)

# Add the textile
AddTextile(WeftKnit)
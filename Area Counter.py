import ezdxf
from ezdxf import math
import math as m
# import tkinter.messagebox
# from tkinter.filedialog import askopenfilename
#
# tkinter.messagebox.showinfo('Land Info Extraction: Introduction', 'Convert Land Type block to Pandas Dataframe')
#
# docPath = askopenfilename(title='Select DXF File with "Land Type" Blocks ------------------(MIN 2  BLOCKS!!)')
# doc = ezdxf.readfile(docPath)

doc = ezdxf.new()
msp = doc.modelspace()

Barrier_vertices=(math.Vec2(836961.3903, 822327.538),math.Vec2(836964.055, 822326.678),math.Vec2(836962.6729, 822322.3955),math.Vec2(836965.2234, 822321.5724),math.Vec2(836964.2167, 822318.5611),math.Vec2(836966.4838, 822317.7611),math.Vec2(836966.8571, 822318.9829),math.Vec2(836969.6736, 822318.0399),math.Vec2(836969.8179, 822318.4872),math.Vec2(836972.1597, 822317.8313),math.Vec2(836970.7791, 822313.5536),math.Vec2(836973.0965, 822312.8057),math.Vec2(836974.3961, 822317.1096),math.Vec2(836976.6509, 822316.2821),math.Vec2(836976.5563, 822315.7609),math.Vec2(836979.4184, 822315.0894),math.Vec2(836978.9801, 822313.7966),math.Vec2(836981.4735, 822312.9919),math.Vec2(836980.7825, 822310.8506),math.Vec2(836982.3051, 822310.3592),math.Vec2(836981.6156, 822308.0599),math.Vec2(836983.0201, 822307.5278),math.Vec2(836983.4193, 822308.7647),math.Vec2(836985.3597, 822310.6288),math.Vec2(836983.7491, 822312.3055),math.Vec2(836985.6905, 822314.0664),math.Vec2(836984.9426, 822314.845),math.Vec2(836987.0351, 822316.925),math.Vec2(836986.7095, 822317.2639),math.Vec2(836988.3961, 822319.0159),math.Vec2(836991.4488, 822315.7154),math.Vec2(836992.5426, 822316.8285),math.Vec2(836996.4498, 822312.7612),math.Vec2(836995.3861, 822311.7393),math.Vec2(836998.4689, 822308.5301),math.Vec2(836996.7788, 822306.7818),math.Vec2(836996.4532, 822307.1208),math.Vec2(836992.3498, 822303.1789),math.Vec2(836992.5256, 822302.9526),math.Vec2(836990.8606, 822301.2215),math.Vec2(836987.7777, 822304.4305),math.Vec2(836986.7862, 822303.4781),math.Vec2(836985.6435, 822304.6677),math.Vec2(836985.1202, 822303.0462),math.Vec2(836983.8116, 822303.4685),math.Vec2(836982.3758, 822299.0195),math.Vec2(836980.1165, 822299.7647),math.Vec2(836980.3045, 822300.611),math.Vec2(836977.5055, 822301.5107),math.Vec2(836977.6591, 822301.9865),math.Vec2(836975.4227, 822302.7082),math.Vec2(836975.2, 822302.0183),math.Vec2(836972.4021, 822302.9212),math.Vec2(836972.2255, 822302.374),math.Vec2(836969.8844, 822303.1295),math.Vec2(836971.2972, 822307.5072),math.Vec2(836969.0608, 822308.229),math.Vec2(836967.625, 822303.7799),math.Vec2(836965.3069, 822304.6068),math.Vec2(836965.5406, 822305.5591),math.Vec2(836962.8093, 822306.4405),math.Vec2(836963.8075, 822309.5334),math.Vec2(836961.3332, 822310.332),math.Vec2(836962.0294, 822312.4894),math.Vec2(836957.0522, 822314.0957),math.Vec2(836961.3903, 822327.538))
#
# Boundary = ezdxf.math.area(Barrier_vertices)
# #
# Boundary_path= ezdxf.path.from_vertices(Barrier_vertices)
#
# Boundary_polyline= ezdxf.path.render_polylines2d(msp, Boundary_path, *, distance: float = 0.01, segments: int = 4, extrusion: Vertex = (0, 0, 1), dxfattribs: Dict = None) → EntityQuery
#


# check items in a bounding box https://github.com/mozman/ezdxf/discussions/600

Boundary_hull=ezdxf.math.convex_hull_2d(Barrier_vertices)

msp.add_polyline2d(Boundary_hull)


import sys
import ezdxf
import matplotlib.pyplot as plt
from ezdxf import recover
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

import os
import sys
import pandas as pd
import numpy as np
from descartes import PolygonPatch
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.getcwd()))
import alphashape


fig, ax = plt.subplots()
ax.scatter(*zip(*Barrier_vertices))
plt.show()

alpha_shape = alphashape.alphashape(Barrier_vertices, 0.1)
alpha_shape



fig, ax = plt.subplots()
ax.scatter(*zip(*Barrier_vertices))
ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
plt.show()

alpha_shape = alphashape.alphashape(Barrier_vertices,5)
alpha_shape


fig, ax = plt.subplots()
ax.scatter(*zip(*Barrier_vertices))
ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
plt.show()

alpha_shape = alphashape.alphashape(Barrier_vertices,1)
alpha_shape


fig, ax = plt.subplots()
ax.scatter(*zip(*Barrier_vertices))
ax.add_patch(PolygonPatch(alpha_shape, alpha=5))
plt.show()




# # Safe loading procedure (requires ezdxf v0.14):
# try:
#     doc, auditor = recover.readfile(doc)
# except IOError:
#     print(f'Not a DXF file or a generic I/O error.')
#     sys.exit(1)
# except ezdxf.DXFStructureError:
#     print(f'Invalid or corrupted DXF file.')
#     sys.exit(2)

# The auditor.errors attribute stores severe errors,
# which may raise exceptions when rendering.
# if not auditor.has_errors:
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ctx = RenderContext(doc)
out = MatplotlibBackend(ax)
Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
fig.savefig('your.png', dpi=1200)
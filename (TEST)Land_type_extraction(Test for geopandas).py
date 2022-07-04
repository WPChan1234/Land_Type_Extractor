import collections
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
import geopandas as gpd

import ezdxf

tkinter.messagebox.showinfo('Land Info Extraction: Introduction', 'Convert Land Type block to Pandas Dataframe')

docPath = askopenfilename(title='Select DXF File with "Land Type" Blocks ------------------(MIN 2  BLOCKS!!)')
doc = ezdxf.readfile(docPath)


msp = doc.modelspace()
List = []
Source_List = []
SourceFile = []
ListFile = ["Source_ID, Room, Tower, Unit, Window"]

SourceFile.append("TEXT \nREC \n")



# # Source ID duplicacy check#
#
# for insert in msp.query('INSERT'):
#
#     List = [(attrib.dxf.tag, attrib.dxf.text) for attrib in insert.attribs]
#     if any("SOURCE_ID" in s for s in List):  ### Filter applied to search Source blocks only ###
#         Source_ID = List[0][1]
#         Source_List.append(Source_ID)
#
# Duplicated_Source = [item for item, count in collections.Counter(Source_List).items() if count > 1]
#
# tkinter.messagebox.showinfo("Source Duplicate Check", "Duplicated Source "
#                                                    "(Gd to go if no duplicated Source) = " + str(Duplicated_Source))

# Rec file formation#
Land=[]
for insert in msp.query('INSERT'):

    List = [(attrib.dxf.tag, attrib.dxf.text) for attrib in insert.attribs]
    if any("BOX_AREA" in s for s in List):
        ### Filter applied to search Source blocks only ###
        print(List)
        if ('BOX_AREA', '########') not in List:
            BoxID=str(insert)
            Area = str(List[0][1]).partition('sqm')[0]

            OPXY = List[1][1].replace('"', '')
            OPX = round(float(OPXY.split(",")[0]), 1)
            OPY = round(float(OPXY.split(",")[1]), 1)
            Land_Type = str(List[2][1])
            Box_width=round(0.5*(float(Area))**0.5,1)
            Left_bound=OPX-Box_width
            Right_bound=OPX+Box_width
            Bottom_bound=OPY-Box_width
            Upper_bound=OPY+Box_width


            Current_Land = {"BoxID": BoxID,
                            "Land Type": Land_Type,
                            "Area": Area,
                            "Center": [OPX,OPY],
                            "Boundary": [(Left_bound,Bottom_bound),(Left_bound,Upper_bound),(Right_bound,Upper_bound),(Right_bound,Bottom_bound)]

                           }
            Land.append(Current_Land)

Df_Land = pd.DataFrame(Land)
print(Df_Land)
Df_Land.to_excel("Land list.xlsx")

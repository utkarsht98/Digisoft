import pydicom
from pydicom.tag import Tag
import time as t
start_time = t.time()
ttfm_data = pydicom.read_file("ttfm.dcm")#Readind '.dcm' files using pydicom module
print("ttfm data:\n")
for element in ttfm_data:
    tx = Tag(element.tag)
    print(tx)
    with open('output_ttfm.txt' ,'a') as file:#writing the DICOM tags
        file.write(str(tx)+'\n')
print("\n")
bmode_data = pydicom.read_file("bmode.dcm")
print("bmode data:\n")
for element in bmode_data:
    ty = Tag(element.tag)
    print(ty)
    with open('output_bmode.txt' ,'a') as file:
        file.write(str(ty)+'\n')
tot_time = t.time() - start_time
print("\n")
print("Total time taken: ",tot_time)


import sys               
sys.path.insert(0, '/home/peter/math/codes/CoordGeo') 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *

from triangle.funcs import *
from conics.funcs import circ_gen

import subprocess
import shlex

A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])
H = np.array([-0.15, -2.15])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Generating the incircle
[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)
x_IH = line_gen(I,H)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],linestyle='dotted',label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],linestyle='dotted',label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],linestyle='dotted',label='$CA$')
plt.plot(x_IH[0,:],x_IH[1,:],label='$r$')


#Plotting the circumcircle
plt.plot(x_icirc[0,:],x_icirc[1,:],label='$incircle$')

#Labeling the coordinates
#tri_coords = np.vstack((A,B,C,O,I)).T
#np.block([[A1,A2,B1,B2]])
A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
I = I.reshape(-1,1)
H = H.reshape(-1,1)
tri_coords = np.block([[A,B,C,I,H]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I','H']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('tri_sss.pdf')
plt.savefig('fig_1.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
# image = mpimg.imread('tri_sss.png')
# plt.imshow(image)
plt.show()






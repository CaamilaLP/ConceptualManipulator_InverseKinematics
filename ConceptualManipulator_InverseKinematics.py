import numpy as np
import math

#Datos constructivos del manipulador
a1=34 #Length of a1 link in mm
a2=60 #Length of a2 link in mm
a3=34 #Length of a3 link in mm
a4=60 #Length of a4 link in mm

#Posición deseada (Max = a2+a4)
x0_2 = 70
y0_2 = 30


T1=30 #Theta 1 angle in degrees
T2=50 #Theta 2 angle in degrees

T1=(T1/180.0)*np.pi #Theta 1 in radians
T2=(T2/180.0)*np.pi #Theta 2 in radians

r1 = math.sqrt(x0_2*2 + y0_2*2)
print(r1)

phi1 = np.arccos((a4**2-a2**2-r1**2)/(-2*a2*r1))
print(phi1)

phi2 = np.arctan(y0_2/x0_2)
print(phi2)

theta1 = phi2-phi1
print(theta1)

phi3 = np.arcsin(r1*np.sin(phi1)/a4)
print(phi3)

theta2 = np.pi - phi3 #np.pi radians = 180 degrees
print(theta2)

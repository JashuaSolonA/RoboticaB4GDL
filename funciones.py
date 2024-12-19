from math import atan, sqrt, cos, pi, sin

def angulos(X,Y,Z,c):
    L1=0.046; 
    L2=0.2; 
    L3=0.2; 
    L4=0.154;

    #q1
    q1 = atan(Y/X)

    M = sqrt(X**2+Y**2)
    Lx = L4 * cos(c*pi/180)
    Lz = L4 * sin(c*pi/180)
    X1=M-Lx
    Z1=Z-Lz-L1
    h = sqrt(X1**2+Z1**2)

    #q3
    cosq3 = (h**2 - L2**2 - L3 **2)/(2*L2*L3)
    #q3=atan(sqrt(1-cosq3.^2)/cosq3) ##Codo abajo
    q3 = atan(-sqrt(1-cosq3**2)/cosq3) #Codo arriba

    #Variable q2
    beta = atan(Z1/X1)
    cosphi = (h**2 + L2**2 - L3**2)/(2*h*L2)
    # #phi=atan(sqrt(1-cosphi.^2)/cosphi) #Codo abajo
    phi = atan(-sqrt(1-cosphi**2)/cosphi) #Codo arriba
    q2 = beta - phi
    
    #q4
    q4 = c*pi/180-q2-q3

    q1_deg = round(q1*180/pi)
    q2_deg = round(q2*180/pi)
    q3_deg = round(q3*180/pi)
    q4_deg = round(q4*180/pi)

    if q1_deg > 180 or q1_deg < 0:
        q1_deg = 0
        print("q1 fuera de rango, Singularidad")
    if q2_deg > 180 or q2_deg < 0:
        q2_deg = 0
        print("q2 fuera de rango, Singularidad")
    if q3_deg > 180 or q3_deg < 0:
        q3_deg = 0
        print("q3 fuera de rango, Singularidad")
    if q4_deg > 180 or q4_deg < 0:
        q4_deg = 0
        print("q4 fuera de rango, Singularidad")

    #Salida
    return q1_deg,q2_deg,q3_deg,q4_deg

angulo1,angulo2,angulo3,angulo4 = angulos(0.2,0.2,0.2,0)
print(angulo1,angulo2,angulo3,angulo4)

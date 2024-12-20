function datos = trayectoria()

a=0.05;
b=320; %factor de reducción
T=32; %periodo
c=2*pi/T; %frecuencia angular

tiempo_max=128;

 t = linspace(0,tiempo_max+1,tiempo_max+1)

centrox=0.1;
centroy=0.1;

for i=1:(tiempo_max+1)
    if i<=(tiempo_max/2+1)
        x(i) = (i-1)/b+centrox;
        y(i) = a*sin(c*(i-1))+centroy;
    else 
        x(i) =(tiempo_max-(i-1))/b+centrox;
        y(i) = -a*sin(c*(tiempo_max-(i-1)))+centroy;
    end
end

for i =1:(tiempo_max+1)
    z(i) = 0.1;
end
x=x.';
y=y.';
z=z.';

datos = [x,y,z];
plot3(x,y,z)
rotate3d

end
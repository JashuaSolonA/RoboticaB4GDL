%PLANIFICACIÓN DE TRAYECTORIA DE ROBOT 3GDL (GENERADOR DE TRAYECTORIA)
%INGENIERÍA MECATRÓNICA UNT
%ROBÓTICA
%Elaborado by Josmell Alva Alcántara.
% script para exportar txt con las variables articularles(sexagesimales)
% la funcion de este es:  cinematInversa3GDL
%...........................................................................
clc, close all, clear all
clc, close all;
%P=xlsread('TRAYECTORIA_v3.xlsx'); %% Insertamos la tabla de las coordenadas como una matriz con Excel
P=trayectoria(); %% Insertamos la tabla de las coordenadas como una matriz con función
% j=1:1:334;  %con el P2
j=1:1:129;  % se crea un vector de 1 a 74 con paso 1 
    X(j)=P(j,1); %% primera columna de P almacenamos en X 
    Y(j)=P(j,2); %% segunda columna de P almacenamos en Y
    Z(j)=P(j,3); %% tercera columna de P almacenamos en Z
    % o tambien:  X=P(:,1)';  Y=P(:,2)';  Z=P(:,3)';    
% longitud de los eslabones
L1=0.046; %metro
L2=0.2; %metro
L3=0.354; %metro

%%CINEMÁTICA INVERSA
for i=1:129
    [q1_0(i),q2_0(i),q3_0(i)]=CInvRobotEcografo(X(i),Y(i),Z(i));
end

q1 = q1_0.'*180./pi;
q2 = q2_0.'*180./pi;
q3 = q3_0.'*180./pi;

j=1:1:129;
datos=[q1(),q2(),q3()]
figure(1)
plot(X(j),Y(j),'-ro')
grid on;
title('TRAYECTORIA');

figure(2)
subplot(1,3,1)
plot(j,q1,'b')
grid on;
title('Motor_1');
xlabel('tiempo(seg)');
ylabel('angulo(grados°)');
subplot(1,3,2)
plot(j,q2,'r')
grid on;
title('Motor_2');
xlabel('tiempo(seg)');
ylabel('angulo(grados°)');
subplot(1,3,3)
grid on;
plot(j,q3,'m')
title('Motor_3');
xlabel('tiempo(seg)');
ylabel('angulo(grados°)');
grid on;

% GUARDAR DATOS:
xlswrite('angulo_robotEcografo.csv', [datos],'Hoja1');
k=j';
for j=1:129
    q1_final(j,:)=[k(j) q1(j)];
    q2_final(j,:)=[k(j) q2(j)];
    q3_final(j,:)=[k(j) q3(j)];
end
dlmwrite('articulacionq1.txt',q1_final)
dlmwrite('articulacionq2.txt',q2_final)
dlmwrite('articulacionq3.txt',q3_final)

%}
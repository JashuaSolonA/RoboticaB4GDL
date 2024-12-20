%Cinemática Inversa de Robot Ecógrafo
%c=1, Codo arriba; c=0, Codo abajo

function [q1,q2,q3]=CInvRobotEcografo(X,Y,Z)
    L1=0.046; %metro
    L2=0.2; %metro
    L3=0.354; %metro
        
    r1=sqrt(X.^2+Y.^2);
    r1_2=r1.^2;
    r2=sqrt(r1_2+(Z-L1).^2);
    r2_2=r2.^2;

    %Variable q1
    q1=atan(Y./X);

    %Variable q3
    q3=acos((r2_2-L2^2-L3^2)./(2*L2*L3));

    %Variable q2
    beta=atan((Z-L1)./r1);
    phi=acos((r2_2+L2^2-L3^2)/(2*L2*r2));

    q2=pi./2-beta-phi;

end

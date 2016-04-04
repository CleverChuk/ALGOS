function [ y ] = interpo( x, y,xk )
%Interpolates to find the value of y at xk
%   
y = interp1(x,y,xk);


end


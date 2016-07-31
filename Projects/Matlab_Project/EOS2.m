%AUTHOR: UME-UGWA CHUKWUBUIKEM
function  [Itable, Vtable] = EOS2( Pressure, Temperature, mass,L, D, K, pA, cT, cP, mW )
% Uses different equation of states to calculate volumetric flow rate, molar 
% volume flow rate, and other variables given temperature, pressure and mass flow rate
% Constants are define within the function and other system variables such
% as length, diameter etc
%  

%INITIALIZE VARIABLES
    P = Pressure; % Pressure in (atm)
    T = Temperature; % Temperature in (K)
    m = mass; % Mass flow rate in (kg/s)
   % L = L; % Length of the pipe in (ft)
   % D = D; % Diameter of the pipe in (inch)
    f = K; % Given constant for energy density calculation
    R = 0.08206; % Universal gas constant in (atm*l/mol*k)
    Mw = mW; % molecular weight of SO2 in (kg/kmol)
    
    % mole calculation for SO2
        n = (m/Mw)*1000; % molar flow rate of SO2 in (mol/s) given the mass flow rate
        
    % Converts length and diameter to meters
%         L = L/3.2808; % Length in (m)
%         D = D/39.37; % Diameter in (m)
    
    % Calculates area
        A = pi*((D^2)/4); % Cross-sectional area in (m^2)
    
    
        
    function [Itable] = idealGas()
        % Computes volumtric flow rate, molar volume and other required variables
        % using the ideal gas EOS
        % Open file for writting
            pid = fopen('Computed_Data.txt', 'w');
            
            Vflow_I = (n*R.*T)./P; % Volumeric flow rate in (L/s)
            
            Vhat_I = Vflow_I./n; % Molar Volume in (L/mol)
            
            velocity_I = (Vflow_I/1000)./A; % Velocity of gas in (m/s)
            
            density_I = m./Vflow_I; % Density of gas in (kg/L) equivalent to (gm/cc)
            
            uLoss_I = 4*f*(L/D)*0.5*(density_I*1000).*velocity_I.^2; % Loss estimate in (Pa*m)
          
        % DATA TABLE CREATION
            idealTable = [Vhat_I; Vflow_I; velocity_I; density_I; uLoss_I;T]; 
            Itable = Vhat_I;
            fprintf(pid,'                          Ideal Table\r\n\n');           
            fprintf(pid,'Vhat(L/mol)  Vdot(L/s)   Velocity(m/s)   Density(kg/L)    Energy density(j/m/m/m)  Temp(K)\r\n');
            fprintf(pid,'%4.4g %14.4g %14.4g %14.4g %18.4g %18.4g\r\n', idealTable);
            fprintf(pid,'\r\n\n');
            fclose(pid);

    end

    function [Vtable] = virialTrunc()
        %Uses the virial truncated EOS to calculate for the requested system
        %variables
        % Open file for appending
            pid = fopen('Computed_Data.txt', 'a');
            
        % Estimation of virial two body interaction constant

            w = pA; % pitzer acentric factor for SO2
            Tc = cT; % critical temperature (K)
            Pc = cP; % critical pressusre (atm)

            Pr = P / Pc; % Reduced pressure to find z from the chart
            Tr = T / Tc; % Reduced temperature to find z from the chart

            Bo = 0.083 - (0.422 ./ (Tr.^1.6)); % calculates Bo for estimation of B
            B1 = 0.139 - (0.172 ./ (Tr.^4.2)); % calculates B1 for estimation of B

            B = ((R * Tc) / Pc) * (Bo + w * B1); % Calculates virial 2body constant

            % Vhat CALCULATION                   
             '(P/RT)*Vhat^2 - Vhat - B = 0'; % Derived quadratic equation from virial truncated EOS

             Vhat_V = rand(1,numel(T));
             
             try

                 for i = 1:numel(T)

                     a = P/(R*T(i)); % Coefficient of Vhat^2 from the quadratic
                     b = -1;  % Coefficient of Vhat from the quadratic
                     c = -1*B(i);  % Virial two body interaction constant from the quadratic
                     k1 = [a b c]; % Array of coefficients of vhat and constant B at the given temperature
                     r = roots(k1); % Finds the roots of the quadratic at the given temperature
                     Vhat_V(i) = r(1);
                                      
                                       
                 end
                 
             catch
                 error = fopen('Error.txt', 'w');
                 fprintf(error,'Please make sure you input comma or space separated temp values');
                 fclose(error);
             end


                Vflow_V = Vhat_V*n; % Volumetric flow rate in (L/s)

                velocity_V = (Vflow_V/1000)/A; % velocity in (m/s)

                density_V = m./Vflow_V; % Density in (kg/L) equivalent to (gm/cc)

                uLoss_V = 4*f*(L/D)*.5*(density_V*1000).*velocity_V.^2; % Loss estimate in (j/m^3)

                % DATA TABLE CREATION
                    VirialTable = [Vhat_V; Vflow_V; velocity_V; density_V; uLoss_V; T];
                    fprintf(pid,'                           Virial Table\r\n\n');    
                    
                    fprintf(pid,'Vhat(L/mol)    Vdot(L/s)    Velocity(m/s)    Density(kg/L)    Energy density(j/m/m/m)  Temp(K)\r\n');
                    
                    fprintf(pid,'%4.4g %14.4g %16.4g %16.4g %20.4g %16.4g\r\n', VirialTable);    
                    
                    Vtable = Vhat_V;
                    fclose(pid);

    end
    [Itable] = idealGas; % Calls the ideal gas EOS function to calculate the required variables
    [Vtable] = virialTrunc; % Calls the virial truncated EOS function to calculate the required variables        
%     figure
%     plot(T,Itable)
%     hold on
%     plot(T,Vtable)
%     title('Comparison between Ideal and Virial EOS')
%     ylabel('Molar Volume (L/mol)')
%     xlabel('Temperature (K)')
%     legend('Ideal','Virial','BestOutside')

end





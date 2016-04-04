function [ Data ] = data_extractor( strg )
%Takes a string args and parses it to retrieve the correct data from data
%table
% tailed explanation goes here
data = importdata('Project_Data.xlsx');
names = data.textdata;
names = names([2:end],1);
data = data.data;

for i = 1:length(names)
    if strcmpi(names(i),strg)
        Data = data(i,1:end);
        break
    end
end   


end


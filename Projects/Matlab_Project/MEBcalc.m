function varargout = MEBcalc(varargin)
% MEBCALC MATLAB code for MEBcalc.fig
%      MEBCALC, by itself, creates a new MEBCALC or raises the existing
%      singleton*.
%
%      H = MEBCALC returns the handle to a new MEBCALC or the handle to
%      the existing singleton*.
%
%      MEBCALC('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MEBCALC.M with the given input arguments.
%
%      MEBCALC('Property','Value',...) creates a new MEBCALC or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before MEBcalc_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to MEBcalc_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help MEBcalc

% Last Modified by GUIDE v2.5 24-Nov-2015 23:10:50

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @MEBcalc_OpeningFcn, ...
                   'gui_OutputFcn',  @MEBcalc_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before MEBcalc is made visible.
function MEBcalc_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to MEBcalc (see VARARGIN)

% Choose default command line output for MEBcalc
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes MEBcalc wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = MEBcalc_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in Compute.
function Compute_Callback(hObject, eventdata, handles)
% hObject    handle to Compute (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% THESE BLOCKS OF CODES HANDLES DATA EXTRACTION
% CALLS TO FUNCTIONS
 handles.data = data_extractor(handles.comp);
 pa_factor = handles.data(1,1);
 mw = handles.data(1,2);
 ctemp = handles.data(1,3);
 cpress = handles.data(1,4);
 L = handles.lendata(1,1);
 D = handles.lendata(1,2);
 K = handles.lendata(1,3);
 
[Itable, Vtable] = EOS2(handles.press,handles.temp,handles.mass,L,D,K,pa_factor,ctemp,cpress,mw);


 guidata(hObject,handles);



function temp_text_Callback(hObject, eventdata, handles)
% hObject    handle to temp_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% FOR LOOP STRUCTURE TO CHECK WHETHER THE TEMPERATURE DATA
% IS COMMA SEPARATED OR SPACE SEPARATED
x = 0;
for i = get(hObject, 'String')
            
    if i == ','
        temparray = strsplit(get(hObject, 'String'),',');
        x = x + 1;
        break
    elseif i == ' '
            temparray = strsplit(get(hObject, 'String'),' ');
            x = x + 1;
            break   
    end

end

if x == 0
      temparray(1) = str2double(get(hObject, 'String'));
end

% THIS BLOCK OF CODE CHECKS THE NUMBER OF TEMPERATURE DATA ENTERED
% AND PUT THEM INTO AN ARRAY OF CORREPONDING SIZE
if length(temparray) == 1
    if isa(temparray(1,1),'double') == 0
        temp1 = str2double(temparray(1,1));
        tempA = [temp1];
    else
        tempA = [temparray(1,1)];
    end

else
    tempA = rand(1,numel(temparray));
    for i = 1:numel(temparray)
        tempA(i) = str2double(temparray(i));
    end
        
end


handles.temp = tempA; % Saves data to GUI structure
guidata(hObject, handles); % saves data into the GUI data stack
% Hints: get(hObject,'String') returns contents of temp_text as text
%        str2double(get(hObject,'String')) returns contents of temp_text as a double


% --- Executes during object creation, after setting all properties.
function temp_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to temp_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function pressure_text_Callback(hObject, eventdata, handles)
% hObject    handle to pressure_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.press = str2double(get(hObject, 'String')); %gets the pressure
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of pressure_text as text
%        str2double(get(hObject,'String')) returns contents of pressure_text as a double


% --- Executes during object creation, after setting all properties.
function pressure_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pressure_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Mass_flow_text_Callback(hObject, eventdata, handles)
% hObject    handle to Mass_flow_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.mass = str2double(get(hObject, 'String')); % Gets mass data
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of Mass_flow_text as text
%        str2double(get(hObject,'String')) returns contents of Mass_flow_text as a double


% --- Executes during object creation, after setting all properties.
function Mass_flow_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Mass_flow_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function comp_text_Callback(hObject, eventdata, handles)
% hObject    handle to comp_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.comp = get(hObject,'String'); % gets compound name
guidata(hObject, handles); % 
% Hints: get(hObject,'String') returns contents of comp_text as text
%        str2double(get(hObject,'String')) returns contents of comp_text as a double


% --- Executes during object creation, after setting all properties.
function comp_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to comp_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function length_text_Callback(hObject, eventdata, handles)
% hObject    handle to length_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Array parsing
% This block of code gets, and parses data from the text box
lendata = strsplit(get(hObject, 'String'),',');
L = str2double(lendata(1,1));
D = str2double(lendata(1,2));
K = str2double(lendata(1,3));
lendata = [L D K];
handles.lendata = lendata;
guidata(hObject, handles);

% Hints: get(hObject,'String') returns contents of length_text as text
%        str2double(get(hObject,'String')) returns contents of length_text as a double


% --- Executes during object creation, after setting all properties.
function length_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to length_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function x_Callback(hObject, eventdata, handles)
% hObject    handle to x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.interpdataXk = str2double(get(hObject, 'String'));
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of x as text
%        str2double(get(hObject,'String')) returns contents of x as a double


% --- Executes during object creation, after setting all properties.
function x_CreateFcn(hObject, eventdata, handles)
% hObject    handle to x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function x1_Callback(hObject, eventdata, handles)
% hObject    handle to x1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.interpdataX(1) = str2double(get(hObject, 'String'));
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of x1 as text
%        str2double(get(hObject,'String')) returns contents of x1 as a double


% --- Executes during object creation, after setting all properties.
function x1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to x1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function x2_Callback(hObject, eventdata, handles)
% hObject    handle to x2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.interpdataX(2) = str2double(get(hObject, 'String'));
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of x2 as text
%        str2double(get(hObject,'String')) returns contents of x2 as a double


% --- Executes during object creation, after setting all properties.
function x2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to x2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function y1_Callback(hObject, eventdata, handles)
% hObject    handle to y1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.interpdataY(1) = str2double(get(hObject, 'String'));
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of y1 as text
%        str2double(get(hObject,'String')) returns contents of y1 as a double


% --- Executes during object creation, after setting all properties.
function y1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to y1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function y2_Callback(hObject, eventdata, handles)
% hObject    handle to y2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.interpdataY(2) = str2double(get(hObject, 'String'));
guidata(hObject, handles);

% Hints: get(hObject,'String') returns contents of y2 as text
%        str2double(get(hObject,'String')) returns contents of y2 as a double


% --- Executes during object creation, after setting all properties.
function y2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to y2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function y_text_Callback(hObject, eventdata, handles)
% hObject    handle to y_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% y = handles.y;

% Hints: get(hObject,'String') returns contents of y_text as text
%        str2double(get(hObject,'String')) returns contents of y_text as a double


% --- Executes during object creation, after setting all properties.
function y_text_CreateFcn(hObject, eventdata, handles)
% hObject    handle to y_text (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in interpolator.
function interpolator_Callback(hObject, eventdata, handles)
% hObject    handle to interpolator (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x = handles.interpdataX;
y = handles.interpdataY;
xk = handles.interpdataXk;

y = interpo(x,y,xk);
y = num2str(y);
set(handles.Ytext,'String', y);

guidata(hObject, handles);

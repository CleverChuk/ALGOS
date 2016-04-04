#!/usr/bin/env python3
try:
	import sys, os, time, threading as t;
	import re, datetime as dt, pickle;
	import tkinter as tk;	
	from tkinter import ttk	
	from PIL import Image; from PIL import ImageTk;
	from tkinter import messagebox;
	from tkinter import filedialog;

except:
	pass;
try:
	import sys;
	import re, datetime as dt, pickle;
	import Tkinter as tk;	
	from Tkinter import ttk;    
	from PIL import Image; from PIL import ImageTk;
	#from Tkinter import tkMessageBox as messagebox;

except:
	pass;




class TradingPlan(tk.Tk):

	def __init__(self, *arg, **kwargs):
		tk.Tk.__init__(self, *arg, **kwargs);
		#tk.Tk.iconbitmap(self, default = 'icon.ico')
		global overwrite_var;
		overwrite_var = True;

		self.resizable(1, 1);
		self.update();
		self.geometry(self.geometry());
		#self.event_generate('Ctrl + S', func = self.saveFile)
		self.bind('<Control-W>', self.close);
		self.bind('<Control-w>', self.close);

		# undo_photo = ImageTk.PhotoImage(Image.open('Undo-50.png'));
		# redo_photo = ImageTk.PhotoImage(Image.open('Redo-50.png'));
		# copy_photo = ImageTk.PhotoImage(Image.open('Copy-50.png'));
		# cut_photo = ImageTk.PhotoImage(Image.open('cut.ico'));
		# paste_photo = ImageTk.PhotoImage(Image.open('Cut-50.png'));

	
		

		self.menuBar = tk.Menu(self);
		self.theme = tk.Menu(self, tearoff = False);

		self.menu = tk.Menu(self.menuBar, tearoff = 0);						
		self.menu.add_cascade(label = 'Themes', menu = self.theme);			

		self.theme.add_radiobutton(label = 'Default', command = self.default_theme);
		self.theme.add_radiobutton(label = 'Forex', command = self.forex_theme);
		self.theme.add_radiobutton(label = 'Stock', command = self.stock_theme);
		self.menu.add_command(label = 'New', command = self.new)
		#self.theme.add_separator();
		self.menu.add_command(label = 'Save', image = None, command = self.saveFile);
		#self.theme.add_command(label = 'Save as', image = None, command = self.saveFile_as);
		self.menu.add_command(label = 'Clear All', image = None, command = self.clear_all); #, accelerator = 'Ctrl + D'
		self.menu.add_command(label = 'Exit', accelerator = 'Ctrl+W', image = None, command = self.close);	
		

		self.menu.add_separator();
		self.menuBar.add_cascade(label = 'App', menu = self.menu);
		
		


		self.editMenu = tk.Menu(self.menuBar, tearoff = 0);
		self.editMenu.add_command(label = 'Undo', accelerator = 'Ctrl+Z', compound = tk.LEFT, image = None, command = self.undo);
		self.editMenu.add_command(label = 'Redo', accelerator = 'Ctrl+Shift+Z', compound = tk.LEFT, image = None, command = self.redo);
		self.editMenu.add_command(label = 'Copy', accelerator = 'Ctrl+C', compound = tk.LEFT, image = None, command = self.copy);
		self.editMenu.add_command(label = 'Cut', accelerator = 'Ctrl+X', compound = tk.LEFT, image = None, command = self.cut);
		self.editMenu.add_command(label = 'Paste', accelerator = 'Ctrl+V', compound = tk.LEFT, image = None, command = self.paste);
		self.editMenu.add_command(label = 'Select All', accelerator = 'Ctrl+A', compound = tk.LEFT, image = None, command = self.select_all);
		self.editMenu.add_command(label = 'Update', command = self.file_update);
		# self.editMenu.undo_photo = undo_photo;
		# self.editMenu.redo_photo = redo_photo;
		# self.editMenu.copy_photo = copy_photo;
		# self.editMenu.cut_photo = cut_photo; image = undo_photo, image = redo_photo,image = copy_photo,

		self.editMenu.add_separator();
		self.menuBar.add_cascade(label = 'Edit', menu = self.editMenu);
		self.config(menu = self.menuBar);


		self.help = tk.Menu(self.menuBar, tearoff = 0);
		self.help.add_command(label = 'About', command = self.aboutApp);		
		self.menuBar.add_cascade(label = 'Help', menu = self.help);
		

		self.container = ttk.Frame(self);
		self.container.pack(side = 'top', fill = 'both', expand = 1);
		self.container.grid_rowconfigure(0, weight = 1);
		self.container.grid_columnconfigure(0, weight =1);
		
		#self.container.bind('Button-3', self.pop);

		self.frames = {};

		for P in (Home_Page, App_Page):

			self.frame = P(self.container, self);
			self.frames[P] = self.frame;
			self.frame.grid(row=0, column=0, sticky ='NSEW');
			

		self.next_page(Home_Page);
		self.after(2000, lambda:self.next_page(App_Page));

		
	def close(self, event = None):
		if messagebox.askokcancel("Exit", 'Are you sure?'):
			self.quit();

	
	def next_page(self, cont):

		self.frame = self.frames[cont];
		self.frame.lift();
	
	def default_theme(self)	:
		page_label.config(bg = '#00DD88');
		date_label.config(bg = 'Orange', font = ('courier', 14, 'italic'));
		pair_label.config(bg = 'Orange', font = ('courier', 14, 'italic'));
		strategy_label.config(bg = 'Orange', font = ('courier', 14, 'italic'));
		notes_label.config(bg = 'Orange', font = ('courier', 14, 'italic'));
		text.config( font = ('courier', 12), bg = 'white', fg = 'black');
		pair_entry.config( font = ('courier', 12), bg = 'white', fg = 'black');
		strategy_entry.config( font = ('courier', 12), bg = 'white', fg = 'black');
		date_entry.config( font = ('courier', 12), bg = 'white', fg = 'black');
		cont.config(bg = 'Orange')
#Page Title get squashed when theme is changed;
#Troubleshoot and fix;

	def forex_theme(self):
		page_label.config( bg = '#915C83', fg = '#000000', font = ('courier', 20, 'italic'));
		date_label.config(bg = 'purple', font = ('courier', 14, 'bold', 'italic'));
		pair_label.config(bg = 'purple', font = ('courier', 14, 'bold', 'italic'));
		strategy_label.config(bg = 'purple', font = ('courier', 14, 'bold', 'italic'));
		notes_label.config(bg = 'purple', font = ('courier', 14, 'bold', 'italic'));
		text.config(font = ('helvatica',12, 'italic'), fg = '#339944', bg = 'black');
		pair_entry.config(font = ('helvatica',12, 'italic'), fg = '#339944', bg = 'black');
		strategy_entry.config(font = ('helvatica',12, 'italic'), fg = '#339944', bg = 'black');
		date_entry.config(font = ('helvatica',12, 'italic'), fg = '#339944', bg = 'black');
		cont.config(bg = 'purple');


	def stock_theme(self):
		page_label.config(bg = 'aqua');
		date_label.config(bg = 'blue', font = ('courier', 14, 'bold', 'italic'));
		pair_label.config(bg = 'blue', font = ('courier', 14, 'bold', 'italic'));
		strategy_label.config(bg = 'blue', font = ('courier', 14, 'bold', 'italic'));
		notes_label.config(bg = 'blue', font = ('courier', 14, 'bold', 'italic'));
		text.config(font = ('times new roman',12, 'italic'), fg = '#33AAFF', bg = '#662200');
		pair_entry.config(font = ('times new roman',12, 'italic'), fg = '#33AAFF', bg = '#662200');
		strategy_entry.config(font = ('times new roman',12, 'italic'), fg = '#33AAFF', bg = '#662200');
		date_entry.config(font = ('times new roman',12, 'italic'), fg = '#33AAFF', bg = '#662200');
		cont.config(bg = 'blue');
	
	global overwrite_var;
		
	
	def saveFile(self):
		'''Handles data Creation and Overwrite'''		
		global date_file;
		global note_file;
		global strategy_file;		
		global numStor;
		global overwrite_var;
		global num;

		num = [1];	
		
		
		data_dict = {'Date':date_entryVar.get(), 'Pair':pair_entryVar.get(), 'Strategy':strategy_entryVar.get(), 'Notes':text.get(1.0, tk.END)};
		
		#print(os.getcwd())
		if os.path.exists('Tjournal_data') == False:
			overwrite_var = False			
			os.makedirs('Tjournal_data');
			os.chdir('Tjournal_data');
			n = num[0]
			n = str(n);
			
			pickle_data = open('pickle_data'+n+'.pickle', 'wb');
			pickle.dump(data_dict, pickle_data);
			pickle_data.close(); n = int(n); n+=1;			
			num[0] = n
			

			num_pickle = open('num.pickle', 'wb');
			pickle.dump(num, num_pickle);
			num_pickle.close();			
			os.chdir('..');
			
		else:
			#print(os.getcwd())
			if overwrite_var == True:
				overwrite_var = False;			
				os.chdir('Tjournal_data');
				
				
				num_out = open('num.pickle', 'rb');
				num_data = pickle.load(num_out);					
				n = num_data;
				n = n[0];					
				n = str(n);

				if os.path.exists('pickle_data'+n+'.pickle') == False:				
					pickle_data = open('pickle_data'+n+'.pickle', 'wb');
					pickle.dump(data_dict, pickle_data);
					pickle_data.close(); n = int(n); n+=1;
					
					num[0] = n
										
					num_pickle = open('num.pickle', 'wb');
					pickle.dump(num, num_pickle);
					num_pickle.close();					
					os.chdir('..');					

			else:
				#print(os.getcwd())
				n = num[0];
				n = str(n);
				os.chdir('Tjournal_data');
				pickle_data = open('pickle_data'+n+'.pickle', 'wb');
				pickle.dump(data_dict, pickle_data);
				pickle_data.close();
				os.chdir('..');

	def file_update(self):
		global List;
		n = List[0];
		n = str(n-1);

		data_dict = {'Date':date_entryVar.get(), 'Pair':pair_entryVar.get(), 'Strategy':strategy_entryVar.get(), 'Notes':text.get(1.0, tk.END)};		

		if os.path.exists('Tjournal_data') == True:
			os.chdir('Tjournal_data');
			try:

				if os.path.exists('pickle_data'+n+'.pickle') == True:	
						#print(n);
						pickle_data = open('pickle_data'+n+'.pickle', 'wb');
						pickle.dump(data_dict, pickle_data);
						pickle_data.close();
						os.chdir('..')
				
				else:
					os.chdir('..');
			except:				
				pass;

	
	def saveFile_as(self):

		date_file = ('Date:'+date_entryVar.get()+'\n\n');
		strategy_file = ('Strategy:'+strategy_entryVar.get()+'\n\n');
		note_file = ('Notes:'+text.get(1.0, tk.END));

		filename = filedialog.asksaveasfilename(defaultextension=".txt", parent = self, title = 'Save as');
		if filename:
			filename = open(filename, 'w');
			filename.write(date_file);
			filename.write(strategy_file);
			filename.write(note_file);
			filename.close()

	def clear_all(self):
		text.delete(1.0, tk.END);
		date_entry.delete(0, tk.END);
		pair_entry.delete(0, tk.END);
		strategy_entry.delete(0, tk.END);
		pair_entry.focus_set();
		self.reset();
			
	def new(self):		
		global overwrite_var;
		overwrite_var = True;
		text.delete(1.0, tk.END);
		date_entry.delete(0, tk.END);
		pair_entry.delete(0, tk.END);
		strategy_entry.delete(0, tk.END);
		pair_entry.focus_set();
		self.reset();		
		
			
	def reset(self):
		date = dt.datetime.now().strftime("%Y-%m-%d %H:%M");
		date_entryVar.set(date);		


	def undo(self):
		text.edit_undo();

	
	def redo(self):		
		try:
			text.edit_redo();		
		except:
			pass;

	def copy(self):
		text.event_generate('<<Copy>>');

	def cut(self):
		text.event_generate('<<Cut>>');	

	def paste(self):
		text.event_generate('<<Paste>>');

	def select_all(self):
 		text.tag_add('sel', '1.0', 'end');
		

	def aboutApp(self):
		messagebox.showinfo(title = 'About', message = '''This app is designed for the trader/investor who wants to get better by tracking his/her decision making on trades/investments by using a digital Journal that makes keeping a journal a breeze. It has basic functionalities such as viewing previous journal entries, updating those entries and many more!''');
		

	#text.bind('<Control-A>', select_all)
	#text.bind('<Control-a>', select_all)
	
	
	
class Home_Page(tk.Frame):

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent);
                self.config(bg = '#33AA66')

                self.grid_columnconfigure(0, weight = 1);
                self.grid_rowconfigure(0, weight = 1);
                self.update();

                # self.button = ttk.Button(self, text = 'Next', command = lambda: controller.next_page(App_Page));
                # self.button.grid(row = 1, column = 0, pady = 2, padx = 2);

                #self.showImg();	
                #self.after(10, self.animate);
                # self.after(500, self.animate_1);
                # self.after(1420, self.animate_2);
                # self.after(3000, self.animate_3);
                # self.after(4000, self.animate_4);
                # self.after(6000, self.animate_5);
                # self.after(8000, self.animate_6);
                #self.after(2000, self.looper);


        def showImg(self):                
                self.image = Image.open('fx.jpg');
                self.photo = ImageTk.PhotoImage(self.image);
                self.labelHome = tk.Label(self, image = self.photo, bg = '#33AA66');
                self.labelHome.image = self.photo;
                self.labelHome.grid(row = 0, column = 0, sticky = 'EW', pady = 2, padx = 2);
                self.label = tk.Label(self, text = 'Trading Journal', fg = 'white', bg = '#33AA66', font = ('helvatica',30));	 	
                self.label.grid(row = 0, column = 0, sticky = 'NEW');



        def animate(self):
                self.image = Image.open('fx.jpg').resize((300,300)).rotate(0);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,300), anchor = 'sw', image = self.photo);
                self.canvas.grid(row = 1, column = 0, sticky = "S");		
                self.label = tk.Label(self, text = 'Trading Journal', fg = 'white', bg = '#33AA66', font = ('helvatica',30));	 	
                self.label.grid(row = 0, column = 0, sticky = 'NEW');		
                #self.after(100, self.canvas.destroy);


        def animate_1(self):
                self.image = Image.open('fx.jpg').resize((150,150)).rotate(60);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,150), anchor = 'sw', image = self.photo);
                self.canvas.grid();
                self.after(300, self.canvas.destroy);

        def animate_2(self):
                self.image = Image.open('fx.jpg').resize((200,200)).rotate(90);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,200), anchor = 'sw', image = self.photo);
                self.canvas.grid();
                self.after(400, self.canvas.destroy);

        def animate_3(self):				
                self.image = Image.open('fx.jpg').resize((250,250)).rotate(120);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,250), anchor = 'sw', image = self.photo);
                self.canvas.grid();
                self.after(500, self.canvas.destroy);

        def animate_4(self):		
                self.image = Image.open('fx.jpg').resize((300,300)).rotate(150);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,300), anchor = 'sw', image = self.photo);
                self.canvas.grid();
                self.after(600, self.canvas.destroy);

        def animate_5(self):
                self.image = Image.open('fx.jpg').resize((330,330)).rotate(180);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,330), anchor = 'sw', image = self.photo);
                self.canvas.grid();
                self.after(700, self.canvas.destroy);

        def animate_6(self):		
                self.image = Image.open('fx.jpg').resize((360,360)).rotate(210);
                self.photo = ImageTk.PhotoImage(self.image);		
                self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                self.canvas.create_image((0,360), anchor = 'sw', image = self.photo);
                #self.after(800,self.canvas.destroy);
                self.canvas.grid();

        def looper(self):
                for i in range(0,361):
                        self.image = Image.open('fx.jpg').resize((i,i)).rotate(i);
                        self.photo = ImageTk.PhotoImage(self.image);		
                        self.canvas = tk.Canvas(self, bg = '#33AA66', width = self.image.size[0], height = self.image.size[1]);
                        self.canvas.create_image((0,i), anchor = 'sw', image = self.photo);
                        self.canvas.grid();
                        #self.after(10, self.canvas.destroy);


                        #self.after(200, self.canvas.destroy);

		
class App_Page(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg = '#00DD88');		

		self.grid_rowconfigure(0, weight = 1);           
		self.grid_columnconfigure(1, weight = 1);
		self.after(60000, self.update);
		
		global cont; global page_label;			

		page_label = tk.Label(self, text = 'Dash Board', bg = '#00DD88', fg = '#000000', font = ('courier', 20, 'italic'));
		page_label.pack(side = tk.TOP, fill ='x', expand = 0);

		cont = tk.Frame(self, bg = 'Orange');
		cont.pack(fill = tk.BOTH, expand = 0);
		cont.grid_rowconfigure(0, weight = 1);
		cont.grid_columnconfigure(1, weight = 1);		
		

		#self.after_idle(self.update_file);
		#self.bind('<Control-D>', self.new);
		#self.bind('<Control-d>', self.new);

		#TEXT VARS & global VARS
		global date_entryVar; global pair_entryVar;	global strategy_entryVar;
		global date_entry;	global pair_entry;	global strategy_entry;		
		global date_label;	global pair_label; global strategy_label; global notes_label;
		global date;
		global text;
		global overwrite_var;
		
		date_entryVar = tk.StringVar();
		pair_entryVar = tk.StringVar();
		strategy_entryVar = tk.StringVar();
		

		# #LABELS
		date_label = tk.Label(cont, text = 'Date-Time', bg = 'Orange', fg = 'black', font = ('courier', 14, 'italic'));
		date_label.grid(row = 0, column = 0,sticky = 'NW', padx = 2, pady = 4);

		pair_label = tk.Label(cont, text = 'Pair/Ticker', bg = 'Orange', fg = 'black', font = ('courier', 14, 'italic'));
		pair_label.grid(row = 1, column = 0, sticky = 'NW', padx = 2, pady = 4);

		strategy_label = tk.Label(cont, text = 'Strategy', bg = 'Orange', fg = 'black', font = ('courier', 14, 'italic'));
		strategy_label.grid(row = 2,  column = 0, sticky = 'NW', padx = 2, pady = 4);

		notes_label = tk.Label(cont, text = 'Notes', bg = 'Orange', fg = 'black', font = ('courier', 14, 'italic'));
		notes_label.grid(row = 3, column = 0, sticky = 'NW', padx = 2, pady = 4);
		

		

		date = dt.datetime.now().strftime("%Y-%m-%d %H:%M");

		date_entry = tk.Entry(cont, textvariable = date_entryVar, relief = 'groove', font = ('courier', 12), justify = tk.LEFT);
		date_entryVar.set(date);				
		date_entry.grid(row = 0, column = 1, sticky = 'nwe', pady = 4, padx = 2);			
 
		pair_entry = tk.Entry(cont, textvariable = pair_entryVar, relief = 'groove', font = ('courier', 12), justify = tk.LEFT);
		pair_entry.grid(row = 1, column = 1, sticky = 'nwe', pady = 4, padx = 2);
		pair_entry.focus_set();	

		strategy_entry = tk.Entry(cont, textvariable = strategy_entryVar, relief = 'groove', font = ('courier', 12), justify = tk.LEFT);
		strategy_entry.grid(row = 2, column = 1, sticky = 'nwe', pady = 4, padx = 2);

		#TEXTPAD		
		text = tk.Text(cont, wrap = tk.WORD, autoseparators = True, undo = True, bg = 'white', relief = 'groove', font =  ('courier', 12));
		text.grid(row = 3, column = 1, sticky = 'NWSE', padx = 2, pady = 4);
		self.vscroll = ttk.Scrollbar(cont);
		text.configure(yscrollcommand = self.vscroll.set);
		self.vscroll.config(command = text.yview);
		self.vscroll.grid(row = 3, column = 2, sticky = 'NS');


		self.button_Two = ttk.Button(cont, text = 'Prev', command = self.prev);
		self.button_Two.grid(row = 4, column = 1, sticky = 'sw', padx= 2, pady = 2);

		self.button_Three = ttk.Button(cont, text = 'Next', command = self.next);
		self.button_Three.grid(row = 4, column = 1, sticky = 'se', pady = 2, padx = 2);

		## Risk Calculator Implementation
			#Label widgets for Risk management

		#Lot
		self.lotVar = tk.StringVar();
		self.fx_lot_label = tk.Label(cont, text = 'Lot Size', fg = 'Black', font = ('helvatica', 12, 'bold'));
		self.fx_lot_label.grid(row = 5, sticky ='W', padx = 4, pady = 4);

		self.fx_lot = tk.Entry(cont, fg = 'black', font = ('helvatica', 12, 'bold'));
		self.fx_lot.grid(row = 5, column = 1, sticky = 'W', padx = 4, pady = 4);

		#Entry
		self.fx_entryVar = tk.StringVar();
		self.fx_entry_label = tk.Label(cont, text = 'Entry', fg = 'aqua', font = ('helvatica', 12, 'bold'));
		self.fx_entry_label.grid(row = 6, sticky ='W', padx = 4, pady = 4);

		self.fx_entry = tk.Entry(cont, fg = 'black', font = ('helvatica', 12, 'bold'));
		self.fx_entry.grid(row = 6, column = 1, sticky = 'W', padx = 4, pady = 4);

		#Exit
		self.fx_exitVar = tk.StringVar();
		self.fx_exit_label = tk.Label(cont, text = 'Exit', fg = '#66FF00', font = ('helvatica', 12, 'bold'));
		self.fx_exit_label.grid(row = 7, sticky ='W', padx = 4, pady = 4);

		self.fx_exit = tk.Entry(cont, fg = 'black', font = ('helvatica', 12, 'bold'));
		self.fx_exit.grid(row = 7, column = 1, sticky = 'W', padx = 4, pady = 4);

		#Stop Loss
		self.fx_SL_Var = tk.StringVar();
		self.fx_SL_label = tk.Label(cont, text = 'Stop Loss', fg = '#E03C31', font = ('helvatica', 12, 'bold'));
		self.fx_SL_label.grid(row = 8, sticky ='W', padx = 4, pady = 4);

		self.fx_SL = tk.Entry(cont, fg = 'black', font = ('helvatica', 12, 'bold'));
		self.fx_SL.grid(row = 8, column = 1, sticky = 'W', padx = 4, pady = 4);

		#PIP Show
		self.pipVar = tk.StringVar();
		self.fx_pip_label = tk.Label(cont, text = 'Pips', textvariable = self.pipVar, fg = 'blue', bg = 'white', font = ('helvatica', 12, 'bold'));
		self.fx_pip_label.grid(row = 9, column = 1, sticky = 'WE');


		text.unbind_all('<Control-y>');
		text.unbind_all('<Control-Y>');
		#text.bind('<Ctrl + S>', self.saveFile);
		text.unbind('Ctrl + Y');
		text.unbind('Ctrl + y');
		#text.bind('<Control-A>', select_all);
		#text.bind('<Control-a>', select_all);

		


		

		#self.text.bind('Button-3', self.pop);
		
				
		
		# self.button_One = tk.Button(self, text = 'Back', command = lambda: controller.next_page(Risk_Page));
		# self.button_One.grid(row = 8, column = 1, sticky = 's', padx = 2, pady = 2);		

		self.data_dict = {'Date':date_entryVar.get(), 'Pair':pair_entryVar.get(), 'Strategy':strategy_entryVar.get(), 'Notes':text.get(1.0, tk.END)};
		

		#self.update();

#Not working
	def update_file(self):
		global data_dict;

		if self.data_dict['Pair'] == pair_entryVar.get() or self.data_dict['Strategy'] == strategy_entryVar.get() or self.data_dict['Notes'] == text.get(1.0, tk.END):
			self.saveFile();
			#time.sleep(1)
		#return self.update();			

	
		
	
	def saveFile(self):
		'''Handles data Creation and Overwrite'''		
		global date_file;
		global note_file;
		global strategy_file;		
		global numStor;
		global overwrite_var;
		global num;

		num = [1];	
		
		
		data_dict = {'Date':date_entryVar.get(), 'Pair':pair_entryVar.get(), 'Strategy':strategy_entryVar.get(), 'Notes':text.get(1.0, tk.END)};
		
		#print(os.getcwd())
		if os.path.exists('Tjournal_data') == False:
			overwrite_var = False;
			os.makedirs('Tjournal_data');
			os.chdir('Tjournal_data');
			n = num[0];
			n = str(n);
			
			pickle_data = open('pickle_data'+n+'.pickle', 'wb');
			pickle.dump(data_dict, pickle_data);
			pickle_data.close(); n = int(n); n+=1;			
			num[0] = n;
			

			num_pickle = open('num.pickle', 'wb');
			pickle.dump(num, num_pickle);
			num_pickle.close();			
			os.chdir('..');
			
		else:
			#print(os.getcwd())
			if overwrite_var == True:
				overwrite_var = False;			
				os.chdir('Tjournal_data');
				
				
				num_out = open('num.pickle', 'rb');
				num_data = pickle.load(num_out);					
				n = num_data;
				n = n[0];					
				n = str(n);

				if os.path.exists('pickle_data'+n+'.pickle') == False:				
					pickle_data = open('pickle_data'+n+'.pickle', 'wb');
					pickle.dump(data_dict, pickle_data);
					pickle_data.close(); n = int(n); n+=1;
					
					num[0] = n;
										
					num_pickle = open('num.pickle', 'wb');
					pickle.dump(num, num_pickle);
					num_pickle.close();					
					os.chdir('..');					

			else:
				#print(os.getcwd())
				n = num[0];
				n = str(n);
				os.chdir('Tjournal_data');
				pickle_data = open('pickle_data'+n+'.pickle', 'wb');
				pickle.dump(data_dict, pickle_data);
				pickle_data.close();
				os.chdir('..');



	global bool_off;
	global n;
	global x;
	global List;
	global pchang_bool;
		
	pchang_bool = False
	List = [1];
	bool_off = True;

	def prev(self):
		global bool_off;
		global x;
		global n;
		global List;
		global pchang_bool;

		pchang_bool = True;

		try:
			#print(os.getcwd())				
			if os.path.exists('Tjournal_data') == True:			
				os.chdir('Tjournal_data');	
				#print(os.getcwd())				
				if bool_off == True:
					bool_off = False;

					if os.path.exists('num.pickle') == True:					
						num = open('num.pickle', 'rb');
						num = pickle.load(num);
						n = num[0];
						
				n = int(n);

				if n > 1:					
					n -= 1;
					n = str(n);
					#print(n)
				else:					
					n = str(n);					
				
				if os.path.exists('pickle_data'+n+'.pickle') == True:
					data_dict = open('pickle_data'+n+'.pickle', 'rb');
					data_dict = pickle.load(data_dict);				
					date_entryVar.set(data_dict['Date']);
					pair_entryVar.set(data_dict['Pair']);
					strategy_entryVar.set(data_dict['Strategy']);
					text.delete(1.0, tk.END);
					text.insert(1.0, data_dict['Notes']);
					List[0] = int(n)+1;
					#print('list num from prev:',List[0])
					#print('num from prev', n)
					os.chdir('..');	
					x = str(n);
					#print(x)						
				else:
					os.chdir('..');	
			else:
				pass;
			
		except:
			pass;	
		

	

	def next(self):
		global n;
		global x;
		global List;
		global pchang_bool;		
		x = List[0];
		#print(x);
		if pchang_bool == True:

			try:
				#print(os.getcwd())
				if os.path.exists('Tjournal_data') == True:			
					#print(os.getcwd())				
					os.chdir('Tjournal_data');

					if os.path.exists('num.pickle') == True:					
							num = open('num.pickle', 'rb');
							num = pickle.load(num);
							num = num[0];

					if int(x) == int(num):
						self.clear_all();			

					elif int(x) < int(num):
						#print(num)
						x = str(x);
																	
						#print('Looping num:',x)
						
						if os.path.exists('pickle_data'+x+'.pickle') == True:
							#print('Pickle num:',num)	
							data_dict = open('pickle_data'+x+'.pickle', 'rb');
							data_dict = pickle.load(data_dict);				
							date_entryVar.set(data_dict['Date']);
							pair_entryVar.set(data_dict['Pair']);
							strategy_entryVar.set(data_dict['Strategy']);
							text.delete(1.0, tk.END);
							text.insert(1.0, data_dict['Notes']);
							x = int(x); n = x;	x+=1;
							
							if x > num:
								pass;
							
							else:								
								List[0] = x
								#print('list num from next:',List[0])
								#print('num from next', num)
							
							os.chdir('..');															
							return n;

						else:							
							os.chdir('..');

					else:						
						os.chdir('..');
				
			except:
				pass;
		else:
			pass;
		

	

	def select_all(self):
		text.tag_add('sel', '1.0', 'end');	

	

		# self.popup = tk.Menu(text);

		# for i in ('copy', 'cut', 'paste', 'redo', 'undo'):
		# 	self.cmd = eval(i);
		# 	self.popup.add_command(label = i, compound = tk.LEFT, command = self.cmd);
		# 	self.popup.add_separator();

	def clear_all(self):		
		text.delete(1.0, tk.END);
		date_entry.delete(0, tk.END);
		pair_entry.delete(0, tk.END);
		strategy_entry.delete(0, tk.END);
		self.reset();
		os.chdir('..')
			
	def reset(self):
		date = dt.datetime.now().strftime("%Y-%m-%d %H:%M");
		date_entryVar.set(date);		


	def pop(self, event):
		self.popup.tk.tk_popup(event.x_self, event.y_self, 0);

	def undo(self):
		text.edit_undo();

	
	def redo(self):		
		try:
			text.edit_redo();
		except:
			pass;


	def onEnterPressed(self, event):
		self.entryValue = self.entryVar.get();
		self.boxSet();
	
	
	def onDoubleClicked(self, event):
		self.entry.selection_range(0, tk.END);
			
	
	def onRightClicked(self):
		pass;

# class  Risk_Page(tk.Toplevel):
# 	"""Window for risk management  """
# 	def __init__(self, parent, controller):
# 		tk.Toplevel.__init__(self, parent)
# 		self.label = tk.Label(self, text = 'Risk Page');
# 		self.label.pack();
		

		
if __name__ == '__main__':

	App = TradingPlan();
	#cut_photo = ImageTk.PhotoImage(Image.open('cut.ico'));
	#App.wm_iconbitmap('cut_photo');
	App.title('Trading Journal');
	App.geometry('450x900');	
	App.mainloop();

def main():
	pass;

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
from pylab import linspace, axis
import pylab


WINDOW_WIDTH=835
WINDOW_HEIGHT=560
WINDOW_SPACE_X=370
WINDOW_SPACE_Y=100

class Plotter(Frame):
    def __init__(self, master):
        """ Frame initialization. """
        super(Plotter, self).__init__(master)
        self.grid()
        self.themeColor='#2196F3'
        self.fontColor='#fef'
        self.inputBg='#e3f2fd'
        self.create_widgets()
        self.configure(bg='#fff')

    def quit(self):
        """ Closes the app. """
        self._root().destroy()

    def create_widgets(self):
        """ Creates widgets. """
        columnPad=40

        self.functionInput=Entry(self, font=("Helvetica", 14), relief='raised', bg=self.inputBg)
        self.functionInput.insert(0, 'sin(x)')
        self.functionInput.grid(row=0, column=0, columnspan=5,  ipady=2, ipadx=265, sticky='NW', padx=40, pady=5)


        #wykres
        self.fig=Figure(figsize=(4,3), dpi=100)
        self.ax=self.fig.add_subplot(111)
        self.canvas=FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, sticky='NW', pady=15)
        self.canvas._tkcanvas.grid(row=1, rowspan=10, columnspan=2)

        #zakresy
        padxLabels, padxInputs=columnPad, columnPad+80
        labelsStyle=dict(pady=2, font=("Helvetica", 12), bg='#fff')
        inputsStyle=dict(width=25, font=("Helvetica", 14), relief='raised', bg=self.inputBg)
        optionsGridStyle=dict(column=1, sticky='NW', pady=8)
        self.xLim=Label(self,text="Lim x:", **labelsStyle)
        self.xLim.grid(row=3,  padx=padxLabels, **optionsGridStyle)
        self.xInput=Entry(self, **inputsStyle)
        self.xInput.grid(row=3, padx=padxInputs, **optionsGridStyle)
        self.yLim=Label(self,text="Lim y:", **labelsStyle)
        self.yLim.grid(row=4, padx=padxLabels, **optionsGridStyle)
        self.yInput=Entry(self, **inputsStyle)
        self.yInput.grid(row=4, padx=padxInputs, **optionsGridStyle)

        #title
        self.title=Label(self,text="Title:", **labelsStyle)
        self.title.grid(row=5, padx=padxLabels, **optionsGridStyle)
        self.titleInput=Entry(self, **inputsStyle)
        self.titleInput.grid(row=5, padx=padxInputs, **optionsGridStyle)
        self.xTitle=Label(self,text="Label x:", **labelsStyle)
        self.xTitle.grid(row=6, padx=padxLabels, **optionsGridStyle)
        self.xTitleInput=Entry(self, **inputsStyle)
        self.xTitleInput.insert(INSERT,'x')
        self.xTitleInput.grid(row=6, padx=padxInputs, **optionsGridStyle)
        self.yTitle=Label(self,text="Label y:", **labelsStyle)
        self.yTitle.grid(row=7, padx=padxLabels, **optionsGridStyle)
        self.yTitleInput=Entry(self, **inputsStyle)
        self.yTitleInput.insert(INSERT, 'y')
        self.yTitleInput.grid(row=7, padx=padxInputs, **optionsGridStyle)

        self.drawLegend=IntVar()
        self.checkLegend=Checkbutton(self, text='Legend', font=("Helvetica", 12), variable=self.drawLegend, bg="#fff", activebackground='#fff')
        self.checkLegend.grid(row=8, column=1, columnspan=2, sticky ='nW', padx=columnPad)

        leftColumnPad = 45
        #przycisk informujący o błędach
        self.error=Label(self, width=40, height=1, font=("Helvetica", 12), bg="#fff", fg="#f44336", anchor='w')
        self.error.grid(row=8, column=0, sticky='NW', pady=20, padx=leftColumnPad, columnspan=5)

        buttonStyle=dict(font=("Helvetica", 14), bg=self.themeColor, fg=self.fontColor, relief='raised', padx=10)

        self.filename=Label(self,text="Filename:", font=("Helvetica", 12), bg='#fff')
        self.filename.grid(row=9, column=0, padx=leftColumnPad, sticky='NW', pady=20)
        self.filenameInput=Entry(self, width=20, font=("Helvetica", 14), relief='raised', bg=self.inputBg)
        self.filenameInput.grid(row=9, column=0, sticky='NW', pady=20, padx=leftColumnPad+80, columnspan=2)
        self.saveButton=Button(self, text="Save", command=self.save, width=25, **buttonStyle)
        self.saveButton.grid(row=10, column=0, sticky='NW', padx=leftColumnPad, pady=10)


        #przycisk kończący działanie programu
        self.quit=Button(self, text="Quit", command=self.quit, width=30, **buttonStyle)
        self.quit.grid(row=10, column=1,  pady=10, sticky='NW', padx=columnPad)

        #przycisk rysujący
        self.drawButton=Button(self, text="Draw",command=self.draw, width=30, **buttonStyle)
        self.drawButton.grid(row=9, column=1, pady=10, sticky='NW', padx=columnPad)

        #kalkulatorowe przyciski
        padx1, pwidth1, pwidth2=columnPad, 36, 52
        helpersStyle=dict(padx=4, pady=2, font=("Helvetica", 12, 'bold'), width=2, relief="raised", bg=self.themeColor, fg=self.fontColor)
        helpersStyle2=dict(padx=10, pady=2, font=("Helvetica", 12, 'bold'), width=2, relief="raised", bg=self.themeColor, fg=self.fontColor)
        helpersGridStyle1=dict(row=1, column=1, columnspan=5)
        helpersGridStyle2=dict(row=2, column=1, columnspan=5)

        self.leftPar=Button(self, text='(', command=lambda: self.handleBtnPress('('), **helpersStyle)
        self.leftPar.grid(sticky=W, padx=padx1, pady=15, **helpersGridStyle1)
        self.rightPar=Button(self, text=')', command=lambda: self.handleBtnPress(')'), **helpersStyle)
        self.rightPar.grid(sticky=W, padx=padx1+pwidth1, **helpersGridStyle1)
        self.power=Button(self, text='**', command=lambda: self.handleBtnPress('**'), **helpersStyle)
        self.power.grid(sticky=W, padx=padx1+2*pwidth1, **helpersGridStyle1)
        self.plus=Button(self, text='+', command=lambda: self.handleBtnPress('+'), **helpersStyle)
        self.plus.grid(sticky=W, padx=padx1+3*pwidth1, **helpersGridStyle1)
        self.minus=Button(self, text='-', command=lambda: self.handleBtnPress('-'), **helpersStyle)
        self.minus.grid(sticky=W, padx=padx1+4*pwidth1, **helpersGridStyle1)
        self.division=Button(self, text='/', command=lambda: self.handleBtnPress('/'), **helpersStyle)
        self.division.grid(sticky=W, padx=padx1+5*pwidth1, **helpersGridStyle1)
        self.multiplication=Button(self, text='*', command=lambda: self.handleBtnPress('*'), **helpersStyle)
        self.multiplication.grid(sticky=W, padx=padx1+6*pwidth1, **helpersGridStyle1)
        self.comma=Button(self, text='.', command=lambda: self.handleBtnPress('.'), **helpersStyle)
        self.comma.grid(sticky=W, padx=padx1+7*pwidth1, **helpersGridStyle1)
        self.fact=Button(self, text='!', command=lambda: self.handleBtnPress('factorial()'), **helpersStyle)
        self.fact.grid(sticky=W, padx=padx1+8*pwidth1, **helpersGridStyle1)
        self.semicolon=Button(self, text=';', command=lambda: self.handleBtnPress(';'), **helpersStyle)
        self.semicolon.grid(sticky=W, padx=padx1+9*pwidth1, **helpersGridStyle1)

        self.ex=Button(self, text='x', command=lambda: self.handleBtnPress('x'), **helpersStyle2)
        self.ex.grid(sticky='W', padx=padx1, **helpersGridStyle2)
        self.pi=Button(self, text='π', command=lambda: self.handleBtnPress('pi'), **helpersStyle2)
        self.pi.grid(sticky=W, padx=padx1+pwidth2, **helpersGridStyle2)
        self.euler=Button(self, text='e', command=lambda: self.handleBtnPress('e'), **helpersStyle2)
        self.euler.grid(sticky=W, padx=padx1+2*pwidth2, **helpersGridStyle2)
        self.sin=Button(self, text='sin', command=lambda: self.handleBtnPress('sin()'), **helpersStyle2)
        self.sin.grid(sticky=W, padx=padx1+3*pwidth2,  **helpersGridStyle2)
        self.log=Button(self, text='log', command=lambda: self.handleBtnPress('log()'), **helpersStyle2)
        self.log.grid(sticky=W, padx=padx1+4*pwidth2, **helpersGridStyle2)
        self.exp=Button(self, text='exp', command=lambda: self.handleBtnPress('exp()'), **helpersStyle2)
        self.exp.grid(sticky=W, padx=padx1+5*pwidth2, **helpersGridStyle2)
        self.squared=Button(self, text='sqrt', command=lambda: self.handleBtnPress('sqrt()'), **helpersStyle2)
        self.squared.grid(sticky=W, padx=padx1+6*pwidth2, **helpersGridStyle2)


    def errorMessage(self, msg):
        self.ax.cla()
        self.canvas.draw()
        self.error['text'] = msg


    def draw(self):
        """ Rysuje wykres. """
        self.error['text'] = ''
        self.ax.cla()

        transformations = (standard_transformations + (implicit_multiplication_application,))
        functionsList = self.functionInput.get().split(';')
        xLims=self.xInput.get().split(',')
        yLims=self.yInput.get().split(',')
        try:
            xLims=[ float(x) for x in xLims ]
        except:
            xLims=[1, 10]
        try:
            yLims=[ float(y) for y in yLims ]
        except:
            yLims=[-10, 10]

        data = []
        X = linspace(*xLims, 100) + 0.0000001


        for func in functionsList:
            try:
                equation = parse_expr(func, evaluate=False, transformations=transformations, local_dict={'pi': 3.14159265, 'e': 2.71828182846})
                Y = [ equation.evalf(subs={'x':x}) for x in X ]
                data = [ *data, X, Y ]
            except:
                print(func)
                self.errorMessage(f'Wrong parameters for function {str(func)}.')


        try:
            title = self.titleInput.get()
            self.ax.axis([ *xLims, *yLims])
            self.ax.title.set_text(title)
            self.ax.set_ylabel(self.yTitleInput.get())
            self.ax.set_xlabel(self.xTitleInput.get())

            if self.drawLegend.get():
                self.ax.plot(*data)
                self.ax.legend(functionsList)
            else:
                self.ax.plot(*data)

            self.fig.tight_layout()
            self.canvas.draw()
        except:
            self.errorMessage("An error ocurred while drawing functions.")

    def save(self):
        filename = 'saved' if len(self.filenameInput.get()) == 0 else self.filenameInput.get()
        self.fig.savefig(f'{filename}.png')

    def handleBtnPress(self, value):
        """ Umieszcza argument w polu tekstowym. """
        self.functionInput.insert(INSERT,value)

root=Tk()
root.title("Plotter 2000 Morska Bryza theme")
root.geometry("%dx%d+%d+%d" %
              (WINDOW_WIDTH, WINDOW_HEIGHT,
               WINDOW_SPACE_X, WINDOW_SPACE_Y))
root.configure(bg='#fff')
app=Plotter(root)

root.mainloop()

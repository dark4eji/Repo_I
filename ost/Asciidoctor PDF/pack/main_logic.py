from tkinter.filedialog import *
from tkinter import messagebox
import os
import subprocess
from pack import lblw as l


class Mlogic:

    def __init__(self, parent):

        self.temppath = None
        self.fontfolder = None

        self.var1 = IntVar()
        self.chbtn = Checkbutton(parent,
                                 text="Open file after publishing",
                                 variable=self.var1)
        self.btn1 = Button(parent,
                           text="...",
                           width=3,
                           height=1,
                           command=self.get_projpath)

        self.btn2 = Button(parent,
                           text="...",
                           width=3,
                           height=1,
                           command=self.get_template)

        self.btn3 = Button(parent,
                           text="...",
                           width=3,
                           height=1,
                           command=self.get_fontfolder)

        self.btn4 = Button(parent,
                           text="...",
                           width=3,
                           height=1,
                           command=self.get_outfolder)

        self.btn5 = Button(parent,
                           text="Publish",
                           width=20,
                           height=1,
                           command=self.pubcheck)

        self.entry1 = Entry(parent,
                            width=40,
                            bd=3)

        self.entry2 = Entry(parent,
                            width=40,
                            bd=3)

        self.entry3 = Entry(parent,
                            width=40,
                            bd=3)

        self.entry4 = Entry(parent,
                            width=40,
                            bd=3)

        self.label1 = Label(parent,
                            text="Path to the project file:")
        self.label2 = Label(parent,
                            text="Path to the template file:")
        self.label3 = Label(parent,
                            text="Path to the fonts folder:")
        self.label4 = Label(parent,
                            text="Output folder:")

        self.elements_placing()

    def get_projpath(self):

        self.entry1.delete(0, END)
        self.projpath = str(askopenfilename(filetype=[('Adoc file', '*.adoc'), ('Text file', '*.txt')]))
        self.entry1.insert(END, os.path.normpath(self.projpath))

    def get_template(self):
        self.entry2.delete(0, END)
        self.temppath = str(askopenfilename(filetype=[('Template file', '*.yml')]))
        self.entry2.insert(END, os.path.normpath(self.temppath))

    def get_fontfolder(self):
        self.entry3.delete(0, END)
        self.fontfolder = str(askdirectory())
        self.entry3.insert(END, os.path.normpath(self.fontfolder))

    def get_outfolder(self):
        self.entry4.delete(0, END)
        self.outfolder = str(askdirectory())
        self.entry4.insert(END, os.path.normpath(self.outfolder))

    def get_pub_vars(self):

        self.projectplace = None
        self.template = None
        self.fonts = None

        if self.temppath not in "":
            self.template = " -a pdf-style=" + "\"" + self.temppath + "\"" + " "
        else:
            self.template = ""

        if self.fontfolder not in "":
            self.fonts = " -a pdf-fontsdir=" + "\"" + self.fontfolder + "\"" + " "
        else:
            self.fonts = ""

        self.projectplace = " \"" + self.projpath + "\""
        self.outputplace = " -D " + "\"" + self.outfolder + "\""

    def postpub(self):

        self.logcheck = subprocess.check_output(self.outtext, stderr=subprocess.STDOUT, shell=True).decode('UTF-8')

        self.pubbed_file = (os.path.basename(self.projpath)).replace(".adoc", ".pdf")

        print(os.path.dirname(self.outfolder) + "/" + self.pubbed_file)
        print(self.pubbed_file)

        if self.logcheck in '':
            pass
        elif self.logcheck not in '':
            with open(os.path.abspath(self.outfolder) + '/Log.txt', 'w') as log:
                log.write(self.logcheck)

        self.result = messagebox.askyesno("Issues", "Issues occurred while publishing. Show log file?")

        if self.result:
            print("explorer.exe " + os.path.abspath(self.outfolder) + '\Log.txt')
            os.system("explorer.exe " + (os.path.abspath(self.outfolder) + '\Log.txt').replace("\\\\", "\\"))

    def pubcheck(self):

        if self.entry1.get() in '':
            messagebox.showwarning("No Project File", "Specify path to the project file")
            return

        if self.entry1.get() not in '':
            if self.entry4.get() in '':
                messagebox.showwarning("No output folder", "Specify output folder")
                return

        if self.temppath is None:
            self.temppath = ''

        if self.fontfolder is None:
            self.fontfolder = ''

        self.publishing()

    def publishing(self):

        self.get_pub_vars()
        
        self.outtext = "asciidoctor-pdf " + '{}{}{}{}'.format(self.outputplace, self.fonts, self.template, self.projectplace)

        os.system(self.outtext)

        self.postpub()


        # if self.var1 == 1:
        #     if
        #     while True:
        #         try:
        #             os.system("explorer.exe " + self.projpath.replace(".adoc", ".pdf"))
        #         except BaseException:
        #             print('CAnt')
        #
    # def interruption(self):
    #
    #     if os.path.exists(os.path.normpath(self.projpath)):
    #         pass
    #     else:
    #         messagebox.showwarning("No path", "Path does not exist. Try again")
    #         return
    #
    #     if os.path.exists(os.path.normpath(self.temppath)):
    #         pass
    #     else:
    #         messagebox.showwarning("No path", "Path does not exist. Try again")
    #         return
    #
    #     if os.path.exists(os.path.normpath(self.outfolder)):
    #         pass
    #     else:
    #         messagebox.showwarning("No path", "Path does not exist. Try again")
    #         return
    #
    #     if os.path.exists(os.path.normpath(self.fontfolder)):
    #         pass
    #     else:
    #         messagebox.showwarning("No path", "Path does not exist. Try again")
    #         return

    def elements_placing(self):

        self.btn1.grid(column=3, row=1, padx=10, sticky=W)
        self.btn2.grid(column=3, row=2, padx=10, sticky=W)
        self.btn3.grid(column=3, row=3, pady=10, padx=10, sticky=W)
        self.btn4.grid(column=3, row=4, padx=10, sticky=W)
        self.btn5.grid(column=2, row=6, padx=0, pady=10, sticky=W)

        self.entry1.grid(column=2, row=1, pady=20)
        self.entry2.grid(column=2, row=2)
        self.entry3.grid(column=2, row=3, pady=20, sticky=W)
        self.entry4.grid(column=2, row=4, sticky=W)

        self.chbtn.grid(column=1, row=5, padx=10, pady=10)

        self.label1.grid(column=1, row=1, pady=5, padx=10, sticky=W)
        self.label2.grid(column=1, row=2, pady=5, padx=10, sticky=W)
        self.label3.grid(column=1, row=3, pady=5, padx=10, sticky=W)
        self.label4.grid(column=1, row=4, pady=5, padx=10, sticky=W)

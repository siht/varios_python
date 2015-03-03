BINPATH = E:/portableapps/Dev-CppPortable/App/devcpp/bin/
INSTALLPATH = E:/portableapps/PortablePython_1.1_py2.6.1/App/DLLs/
INSTALLPATH2 = E:\\portableapps\\PortablePython_1.1_py2.6.1\\App\\DLLs\\
LIBPATH = E:/portableapps/PortablePython_1.1_py2.6.1/App/libs
INCLUDEPATH = E:/portableapps/PortablePython_1.1_py2.6.1/App/include
FILEIN = assemblermodule
FILEOUT = assembler

$(FILEOUT).pyd : $(FILEIN).o
	$(BINPATH)gcc -shared $(FILEIN).o -L$(LIBPATH) -lpython26 -o $(FILEOUT).pyd

$(FILEIN).o : $(FILEIN).c
	$(BINPATH)gcc -c $(FILEIN).c -I$(INCLUDEPATH)

clean:
	rm $(FILEOUT).pyd $(FILEIN).o
install:
	copy $(FILEOUT).pyd $(INSTALLPATH2)
uninstall:
	rm $(INSTALLPATH)$(FILEOUT).pyd

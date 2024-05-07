@ECHO OFF

cl.exe /nologo /Ox /MT /W0 /GS- /DNDEBUG /Tcnew1.cpp /link /OUT:aesencrypted.exe /SUBSYSTEM:CONSOLE /MACHINE:x64
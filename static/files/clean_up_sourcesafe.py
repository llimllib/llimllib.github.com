import os, re

PROJ_RE = re.compile(r"^\s+Scc")
SLN_RE = re.compile(r"GlobalSection\(SourceCodeControl\).*?EndGlobalSection",
                    re.DOTALL)
VDPROJ_RE = re.compile(r"^\"Scc")

for (dir, dirnames, filenames) in os.walk('.'):
    for fname in filenames:
        fullname = os.path.join(dir, fname)
        if fname.endswith('scc'):
            os.unlink(fullname)
        elif fname.endswith('vdproj'):
            #Installer project has a different format
            fin = file(fullname)
            text = fin.readlines()
            fin.close()

            fout = file(fullname, 'w')
            for line in text:
                if not VDPROJ_RE.match(line):
                    fout.write(line)
            fout.close()
        elif fname.endswith('csproj'):
            fin = file(fullname)
            text = fin.readlines()
            fin.close()

            fout = file(fullname, 'w')
            for line in text:
                if not PROJ_RE.match(line):
                    fout.write(line)
            fout.close()
        elif fname.endswith('sln'):
            fin = file(fullname)
            text = fin.read()
            fin.close()

            text = SLN_RE.sub("", text)

            fout = file(fullname, 'w')
            fout.write(text)

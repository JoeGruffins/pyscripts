import subprocess
import sys

all = []
depth = 0


def walk(dep):
    global depth
    proc = subprocess.Popen(["go", "list", "-f", '{{ join .Imports \"\\n\"}}',
                             dep], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    o = output.split("\n")
    add = [a for a in o if a not in all]
    all.extend(add)
    depth += 1
    spaces = ""
    for _ in range(depth):
        spaces += " "
    for a in add:
        if a == "":
            continue
        print(spaces + "|-" + a)
        if a == "C":
            continue
        walk(a)
    depth -= 1


print(sys.argv[1])
walk(sys.argv[1])

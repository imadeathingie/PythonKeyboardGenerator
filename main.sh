#! /bin/bash
mkdir -p ./output/keylists
mkdir -p ./output/scad
mkdir -p ./output/stl
name=$(python3 keylist.py $1)
python3 keyboard.py ${name}_keylist.json
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD --backend=manifold -o output/stl/${name}.stl output/scad/${name}.scad
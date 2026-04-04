#! /bin/bash
mkdir -p ./output/keylists
mkdir -p ./output/scad
mkdir -p ./output/stl
mkdir -p ./output/data
if [[ $# -eq 1 ]]; then
    START=$1
    END=$1
elif [[ $# -eq 2 ]]; then
    START=$1
    END=$2
else
    echo "Usage: $0 <index> or $0 <start> <end>"
    exit 1
fi

for i in $(seq $START $END)
do
    echo "Processing $i"
    name=$(python3 keylist.py $i)
    mkdir -p ./output/keyboards/${name}/stl
    mkdir -p ./output/keyboards/${name}/scad
    mkdir -p ./output/keyboards/${name}/config
    cp ./output/keylists/${name}_keylist.json ./output/keyboards/${name}/config/${name}_keylist.json
    cp ./output/data/${name}.json ./output/keyboards/${name}/config/${name}_conf.json
    python3 keyboard.py ${name}_keylist.json
    cp ./output/scad/${name}_full.scad ./output/keyboards/${name}/scad/${name}_full.scad
    cp ./output/scad/${name}_keys.scad ./output/keyboards/${name}/scad/${name}_keys.scad
    cp ./output/scad/${name}_base.scad ./output/keyboards/${name}/scad/${name}_base.scad
    /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD --backend=manifold -o output/stl/${name}.stl output/keyboards/${name}/scad/${name}_full.scad
    /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD --backend=manifold -o output/keyboards/${name}/stl/${name}_keys.stl output/keyboards/${name}/scad/${name}_keys.scad
    /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD --backend=manifold -o output/keyboards/${name}/stl/${name}_base.stl output/keyboards/${name}/scad/${name}_base.scad
    cp ./output/stl/${name}.stl ./output/keyboards/${name}/stl/${name}.stl
done

rm -rf ./output/scad
rm -rf ./output/keylists
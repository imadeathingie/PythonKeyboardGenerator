include <../CherryMX/cherrymx.scad>
include <../KeyV2/includes.scad>
/*
Profiles:
asa
cherry
dcs
dsa
dss
g20
grid
hex
hipro
mt3
oem
regular_polygon
sa
typewriter
*/

module keycap(profile="dsa", row=3, legend="Q", size=7){
    translate([0,0,7]) {
        if(profile == "asa"){
            asa_row(row) legend(legend, size=size) key();
        }
        else if(profile == "cherry"){
            cherry_row(row) legend(legend, size=size) key();
        }
        else if(profile == "dcs"){
            dcs_row(row) legend(legend, size=size) key();
        }
        else if(profile == "dsa"){
            dsa_row(row) legend(legend, size=size) key();
        }
        else if(profile == "dss"){
            dss_row(row) legend(legend, size=size) key();
        }
        else if(profile == "g20"){
            g20_row(row) legend(legend, size=size) key();
        }
        else if(profile == "grid"){
            grid_row(row) legend(legend, size=size) key();
        }
        else if(profile == "hex"){
            hex_row(row) legend(legend, size=size) key();
        }
        else if(profile == "hipro"){
            hipro_row(row) legend(legend, size=size) key();
        }
        else if(profile == "mt3"){
            mt3_row(row) legend(legend, size=size) key();
        }
        else if(profile == "oem"){
            oem_row(row) legend(legend, size=size) key();
        }
        else if(profile == "regular_polygon"){
            regular_polygon_row(row) legend(legend, size=size) key();
        }
        else if(profile == "sa"){
            sa_row(row) legend(legend, size=size) key();
        }
        else if(profile == "typewriter"){
            typewriter_row(row) legend(legend, size=size) key();
        }
        else {
            dsa_row(3) legend("Q", size=7) key();
        }
    }
}

module KeySwitch(profile="dsa") {
    CherryMX();
    keycap(profile=profile);
}
class Keyboard:
    import json
    import sys

    def __init__(self, fn=sys.argv[1] if len(sys.argv) > 1 else "default_keylist.json"):
        with open(f"output/keylists/{fn}", 'r') as fr:
            data = self.json.load(fr)
            self.eps = 0.001
            self.name = data["name"] if data.get("name") is not None else "default"
            self.hole_size = data["hole_size"]
            self.key_1u = data["key_1u"]
            self.thickness = data["thickness"]
            self.keylist = data["keylist"]
            str = self.matrix(self.keylist)
            with open(f"output/scad/{self.name}.scad", 'w') as fw:
                fw.write(f"mirror([0,0,0]){{\n{str}\n}}")

    def tl(self, k):
        u = k['u_width']
        h = k['u_height']
        return [(-self.hole_size/2,self.hole_size/2,0),
                (-self.hole_size/2,self.hole_size/2,-self.thickness),
                (-(u*self.key_1u)/2,(h*self.key_1u)/2,0),
                (-(u*self.key_1u-4)/2,(h*self.key_1u)/2,-self.thickness),
                (-(u*self.key_1u)/2,(h*self.key_1u)/2,-self.thickness),
                (-(u*self.key_1u-4)/2,(h*self.key_1u-4)/2,-self.thickness),
                (-(u*self.key_1u)/2,(h*self.key_1u-4)/2,-self.thickness)]
        
    def tr(self, k):
        u = k['u_width']
        h = k['u_height']
        return [(self.hole_size/2,self.hole_size/2,0),
                (self.hole_size/2,self.hole_size/2,-self.thickness),
                ((u*self.key_1u)/2,(h*self.key_1u)/2,0),
                ((u*self.key_1u-4)/2,(h*self.key_1u)/2,-self.thickness),
                ((u*self.key_1u)/2,(h*self.key_1u)/2,-self.thickness),
                ((u*self.key_1u-4)/2,(h*self.key_1u-4)/2,-self.thickness),
                ((u*self.key_1u)/2,(h*self.key_1u-4)/2,-self.thickness)]

    def br(self, k):
        u = k['u_width']
        h = k['u_height']
        return [(self.hole_size/2,-self.hole_size/2,0),
                (self.hole_size/2,-self.hole_size/2,-self.thickness),
                ((u*self.key_1u)/2,-(h*self.key_1u)/2,0),
                ((u*self.key_1u-4)/2,-(h*self.key_1u)/2,-self.thickness),
                ((u*self.key_1u)/2,-(h*self.key_1u)/2,-self.thickness),
                ((u*self.key_1u-4)/2,-(h*self.key_1u-4)/2,-self.thickness),
                ((u*self.key_1u)/2,-(h*self.key_1u-4)/2,-self.thickness)]

    def bl(self, k):
        u = k['u_width']
        h = k['u_height']
        return [(-self.hole_size/2,-self.hole_size/2,0),
                (-self.hole_size/2,-self.hole_size/2,-self.thickness),
                (-(u*self.key_1u)/2,-(h*self.key_1u)/2,0),
                (-(u*self.key_1u-4)/2,-(h*self.key_1u)/2,-self.thickness),
                (-(u*self.key_1u)/2,-(h*self.key_1u)/2,-self.thickness),
                (-(u*self.key_1u-4)/2,-(h*self.key_1u-4)/2,-self.thickness),
                (-(u*self.key_1u)/2,-(h*self.key_1u-4)/2,-self.thickness)]

    def hull(self, lst):
        str = "hull() {\n"
        for i in range(len(lst)):
            str += f" translate([{lst[i][0]}, {lst[i][1]}, {lst[i][2]}])cube({self.eps}, center=true);\n"
        str += "}\n"
        return str

    def translate(self, key, str, z= None):
        px = key['pos']['x']
        py = key['pos']['y']
        pz = key['pos']['z']
        rx = key['rotation']['x']
        ry = key['rotation']['y']
        rz = key['rotation']['z']
        if z is not None:
            pz = z
        return "translate([%s,%s,%s]) {\n  rotate([%s,%s,%s]) {\n%s  }\n}\n" % (px, py, pz, rx, ry, rz, str)
    
    def neighbours(self, key, keys):
        neighbours = {}
        for k in keys:
            if k['row'] == key['row'] and k['col'] == key['col'] + 1:
                neighbours['r'] = k
            elif k['row'] == key['row'] and k['col'] == key['col'] - 1:
                neighbours['l'] = k
            elif k['row'] == key['row'] + 1 and k['col'] == key['col']:
                neighbours['b'] = k
            elif k['row'] == key['row'] - 1 and k['col'] == key['col']:
                neighbours['t'] = k
        return neighbours

    def diagonals(self, key, keys):
        diagonals = {}
        for k in keys:
            if k['row'] == key['row'] + 1 and k['col'] == key['col'] + 1:
                diagonals['br'] = k
            elif k['row'] == key['row'] + 1 and k['col'] == key['col'] - 1:
                diagonals['bl'] = k
            elif k['row'] == key['row'] - 1 and k['col'] == key['col'] + 1:
                diagonals['tr'] = k
            elif k['row'] == key['row'] - 1 and k['col'] == key['col'] - 1:
                diagonals['tl'] = k
        return diagonals

    def walls(self, key, keys):
        neighs = self.neighbours(key, keys)
        diags = self.diagonals(key, keys)
        walls = []
        if 't' in neighs:
            if neighs['t']['pos']['x'] > key['pos']['x'] and 'tl' not in diags:
                str = "hull(){\n"+self.translate(key, self.hull(self.tl(key)[3:]))+"\n"+self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            if neighs['t']['pos']['x'] < key['pos']['x'] and 'tr' not in diags:
                str = "hull(){"+self.translate(key, self.hull(self.tr(key)[3:]))+"\n"+self.translate(neighs['t'], self.hull(self.br(neighs['t'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
        elif 't' not in neighs:
            str = self.translate(key, self.hull(self.tl(key)[3:] + self.tr(key)[3:]))
            walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            # if 'r' in neighs:
            #     str_r = self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_r+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_r+"}\n  }\n }\n")
            # if 'l' in neighs:
            #     str_l = self.translate(neighs['l'], self.hull(self.tr(neighs['l'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_l+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_l+"}\n  }\n }\n")
        if 'r' in neighs:
            if neighs['r']['pos']['y'] < key['pos']['y'] and 'tr' not in diags:
                str = "hull(){\n"+self.translate(key, self.hull(self.tr(key)[3:]))+"\n"+self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            if neighs['r']['pos']['y'] > key['pos']['y'] and 'br' not in diags:
                str = "hull(){"+self.translate(key, self.hull(self.br(key)[3:]))+"\n"+self.translate(neighs['r'], self.hull(self.bl(neighs['r'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
        if 'r' not in neighs:
            str =self.translate(key, self.hull(self.tr(key)[3:] + self.br(key)[3:]))
            walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            walls.append("//r")
            # if 't' in neighs:
            #     str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_t+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_t+"}\n  }\n }\n")
            # if 'b' in neighs:
            #     str_b =self.translate(neighs['b'], self.hull(self.tr(neighs['b'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_b+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_b+"}\n  }\n }\n")
        if 'b' in neighs:
                if neighs['b']['pos']['x'] > key['pos']['x'] and 'bl' not in diags:
                    str = "hull(){\n"+self.translate(key, self.hull(self.bl(key)[3:]))+"\n"+self.translate(neighs['b'], self.hull(self.tl(neighs['b'])[3:5]))+"\n}\n"
                    walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
                if neighs['b']['pos']['x'] < key['pos']['x'] and 'br' not in diags:
                    str = "hull(){"+self.translate(key, self.hull(self.br(key)[3:]))+"\n"+self.translate(neighs['b'], self.hull(self.tr(neighs['b'])[3:5]))+"\n}\n"
                    walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
        elif 'b' not in neighs:
            str =self.translate(key, self.hull(self.bl(key)[3:] + self.br(key)[3:]))
            walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            # if 'r' in neighs:
            #     str_r =self.translate(neighs['r'], self.hull(self.bl(neighs['r'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_r+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_r+"}\n  }\n }\n")
            # if 'l' in neighs:
            #     str_l =self.translate(neighs['l'], self.hull(self.br(neighs['l'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_l+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_l+"}\n  }\n }\n")
        if 'l' in neighs:
            if neighs['l']['pos']['y'] < key['pos']['y'] and 'tl' not in diags:
                str = "hull(){\n"+self.translate(key, self.hull(self.tl(key)[3:]))+"\n"+self.translate(neighs['l'], self.hull(self.tr(neighs['l'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            if neighs['l']['pos']['y'] > key['pos']['y'] and 'bl' not in diags:
                str = "hull(){"+self.translate(key, self.hull(self.bl(key)[3:]))+"\n"+self.translate(neighs['l'], self.hull(self.br(neighs['l'])[3:5]))+"\n}\n"
                walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
        elif 'l' not in neighs:
            str =self.translate(key, self.hull(self.bl(key)[3:] + self.tl(key)[3:]))
            walls.append("hull(){  "+str+"\n  linear_extrude(0.1)projection(){"+str+"}\n  }\n")
            # if 't' in neighs:
            #     str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_t+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_t+"}\n  }\n }\n")
            # if 'b' in neighs:
            #     str_b =self.translate(neighs['b'], self.hull(self.tl(neighs['b'])[3:]))
            #     walls.append("hull(){  "+str+"\n"+str_b+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_b+"}\n  }\n }\n")
        
        # if 'tr' not in diags:
        #     if 't' in neighs and 'r' in neighs:
        #         str =self.translate(key, self.hull(self.tr(key)[3:]))
        #         str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[3:]))
        #         str_r =self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[3:]))
        #         walls.append("hull(){  "+str+"\n"+str_t+"\n"+str_r+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_t+"\n"+str_r+"}\n  }\n }\n")
        # if 'br' not in diags:
        #     if 'b' in neighs and 'r' in neighs:
        #         str =self.translate(key, self.hull(self.br(key)[3:]))
        #         str_b =self.translate(neighs['b'], self.hull(self.tr(neighs['b'])[3:]))
        #         str_r =self.translate(neighs['r'], self.hull(self.bl(neighs['r'])[3:]))
        #         walls.append("hull(){  "+str+"\n"+str_b+"\n"+str_r+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_b+"\n"+str_r+"}\n  }\n }\n")
        # if 'bl' not in diags:
        #     if 'b' in neighs and 'l' in neighs:
        #         str =self.translate(key, self.hull(self.bl(key)[3:]))
        #         str_b =self.translate(neighs['b'], self.hull(self.tl(neighs['b'])[3:]))
        #         str_l =self.translate(neighs['l'], self.hull(self.br(neighs['l'])[3:]))
        #         walls.append("hull(){  "+str+"\n"+str_b+"\n"+str_l+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_b+"\n"+str_l+"}\n  }\n }\n")
        # if 'tl' not in diags:
        #     if 't' in neighs and 'l' in neighs:
        #         str =self.translate(key, self.hull(self.tl(key)[3:]))
        #         str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[3:]))
        #         str_l =self.translate(neighs['l'], self.hull(self.tr(neighs['l'])[3:]))
        #         walls.append("hull(){  "+str+"\n"+str_t+"\n"+str_l+"\n  linear_extrude(0.1)projection(){ hull(){"+str+"\n"+str_t+"\n"+str_l+"}\n  }\n }\n")
        return walls

    def intersections(self, key, keys):
        neighs = self.neighbours(key, keys)
        diags = self.diagonals(key, keys)
        intersections = []
        if 't' in neighs:
            str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4] + self.bl(neighs['t'])[2:4]))
            str =self.translate(key, self.hull(self.tr(key)[2:4] + self.tl(key)[2:4]))
            intersections.append(f"hull(){{\n  {str_t}\n  {str}\n  }}\n")
            if 'r' in neighs:
                str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tr(key)[2:4]))
                str_r =self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_r}\n  {str}\n  }}\n")
            if 'l' in neighs:
                str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tl(key)[2:4]))
                str_l =self.translate(neighs['l'], self.hull(self.tr(neighs['l'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_l}\n  {str}\n  }}\n")
            if 'tr' in diags:
                str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tr(key)[2:4]))
                str_tr =self.translate(diags['tr'], self.hull(self.bl(diags['tr'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_tr}\n  {str}\n  }}\n")
            if 'tl' in diags:
                str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tl(key)[2:4]))
                str_tl =self.translate(diags['tl'], self.hull(self.br(diags['tl'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_tl}\n  {str}\n  }}\n")
        
        if 'r' in neighs:
            str_r =self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[2:4] + self.bl(neighs['r'])[2:4]))
            str =self.translate(key, self.hull(self.tr(key)[2:4] + self.br(key)[2:4]))
            intersections.append(f"hull(){{\n  {str_r}\n  {str}\n  }}\n")
        return intersections


    def base(self, key, keys, base_thickness=3):
        neighs = self.neighbours(key, keys)
        diags = self.diagonals(key, keys)
        intersections = []

        intersections.append(
           self.translate(key, self.hull(self.tl(key) + self.tr(key) + self.br(key) + self.bl(key)))
        )
        if 't' in neighs:
            str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4] + self.bl(neighs['t'])[2:4]))
            str =self.translate(key, self.hull(self.tr(key)[2:4] + self.tl(key)[2:4]))
            intersections.append(f"hull(){{\n  {str_t}\n  {str}\n  }}\n")
            if 'r' in neighs:
                str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tr(key)[2:4]))
                str_r =self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_r}\n  {str}\n  }}\n")
            if 'l' in neighs:
                str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tl(key)[2:4]))
                str_l =self.translate(neighs['l'], self.hull(self.tr(neighs['l'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_l}\n  {str}\n  }}\n")
            if 'tr' in diags:
                str_t =self.translate(neighs['t'], self.hull(self.br(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tr(key)[2:4]))
                str_tr =self.translate(diags['tr'], self.hull(self.bl(diags['tr'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_tr}\n  {str}\n  }}\n")
            if 'tl' in diags:
                str_t =self.translate(neighs['t'], self.hull(self.bl(neighs['t'])[2:4]))
                str =self.translate(key, self.hull(self.tl(key)[2:4]))
                str_tl =self.translate(diags['tl'], self.hull(self.br(diags['tl'])[2:4]))
                intersections.append(f"hull(){{\n  {str_t}\n  {str_tl}\n  {str}\n  }}\n")
        
        if 'r' in neighs:
            str_r =self.translate(neighs['r'], self.hull(self.tl(neighs['r'])[2:4] + self.bl(neighs['r'])[2:4]))
            str =self.translate(key, self.hull(self.tr(key)[2:4] + self.br(key)[2:4]))
            intersections.append(f"hull(){{\n  {str_r}\n  {str}\n  }}\n")
        
        str = []
        for i in intersections:
            str.append(f"hull(){{translate([0,0,-5-{base_thickness}])linear_extrude({base_thickness})projection(){{\n  {i}\n  }}}}")
        return str
    
    def keyhole(self, key):
        str = []
        px = key['pos']['x']
        py = key['pos']['y']
        pz = key['pos']['z']
        rx = key['rotation']['x']
        ry = key['rotation']['y']
        rz = key['rotation']['z']
        str.append("translate([%s,%s,%s]) {\n  rotate([%s,%s,%s]) {\n" % (px, py, pz, rx, ry, rz))
        str.append(self.hull(self.tl(key)+self.tr(key)))
        str.append(self.hull(self.tr(key)+self.br(key)))
        str.append(self.hull(self.br(key)+self.bl(key)))
        str.append(self.hull(self.bl(key)+self.tl(key)))
        str.append("  }\n}\n")
        return "\n".join(str)

    def matrix(self, keys):
        str = []
        for key in keys:
            str.append(self.keyhole(key))
            for i in self.intersections(key, keys):
                str.append(i)
            for i in self.walls(key, keys):
                str.append(i)
            for i in self.base(key, keys, base_thickness=3):
                str.append(i)
        
        print("\n".join(str))
        return "\n".join(str)

Keyboard()
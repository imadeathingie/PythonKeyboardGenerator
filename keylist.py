import json
import ast
import defaults

import sys

def parse_algo(expr, x, y, z):
    """
    Safely evaluate simple arithmetic expressions using variables x,y,z and
    whitelisted functions (abs, min, max).
    """
    allowed_funcs = {'abs': abs, 'min': min, 'max': max}
    names = {'x': x, 'y': y, 'z': z}

    tree = ast.parse(expr, mode='eval')

    def _check(node):
        if isinstance(node, ast.Expression):
            return _check(node.body)
        if isinstance(node, ast.IfExp):
            # ternary conditional: <body> if <test> else <orelse>
            _check(node.test)
            _check(node.body)
            _check(node.orelse)
            return
        if isinstance(node, ast.BinOp):
            _check(node.left); _check(node.right)
            if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div,
                                        ast.FloorDiv, ast.Mod, ast.Pow)):
                raise ValueError("Disallowed operator")
            return
        if isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.UAdd, ast.USub, ast.Not)):
                raise ValueError("Disallowed unary operator")
            return _check(node.operand)
        if isinstance(node, ast.BoolOp):
            # and/or
            if not isinstance(node.op, (ast.And, ast.Or)):
                raise ValueError("Disallowed boolean operator")
            for v in node.values:
                _check(v)
            return
        if isinstance(node, ast.Compare):
            # comparisons like x > 5
            _check(node.left)
            for comp in node.comparators:
                _check(comp)
            for op in node.ops:
                if not isinstance(op, (ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE)):
                    raise ValueError("Disallowed comparison operator")
            return
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in allowed_funcs:
                raise ValueError("Disallowed function")
            for a in node.args:
                _check(a)
            return
        if isinstance(node, ast.Name):
            if node.id not in names:
                raise ValueError("Disallowed name")
            return
        if isinstance(node, ast.Constant):  # Python 3.6+
            if not isinstance(node.value, (int, float)):
                raise ValueError("Only numeric constants allowed")
            return
        if isinstance(node, ast.Num):  # older AST node
            return
        raise ValueError(f"Disallowed expression node: {type(node).__name__}")

    _check(tree)
    return eval(compile(tree, "<expr>", "eval"), {"__builtins__": {}}, {**allowed_funcs, **names})

class Keylist:                                         
    def __init__(self, data):
        self.gen_matrix(data)
        self.export_json(data)
        print(self.name)


    def gen_matrix(self, data):

        self.name = data.get('name', "default")
        self.ignored_keys = data.get('ignored_keys', [])
        self.hole_size = data.get('hole_size', 14.5)
        self.key_1u = data.get('key_1u', 19.05)
        self.thickness = data.get('thickness', 5)

        width = data.get('width', 6)
        height = data.get('height', 4)
        x_algo = data.get('x_algo', f"x*{self.key_1u}") # x*1905/100+(x*10)
        y_algo = data.get('y_algo', f"-y*{self.key_1u}") # -y*1905/100-(y*10)
        z_algo = data.get('z_algo', "10") # abs(y-2)*4+abs(x-2)*3 + 10
        x_rot_algo = data.get('x_rot_algo', "0") # (y-2)*-5
        y_rot_algo = data.get('y_rot_algo', "0") # (x - 2)*(-9)
        z_rot_algo = data.get('z_rot_algo', "0") # 0

        keys = [
            {
            "u_width": 1,
            "u_height": 1,
            "col": x,
            "row": y,
            "linked_keys": {},
            "pos": {
                "x": parse_algo(x_algo, x, y, 0),
                "y": parse_algo(y_algo, x, y, 0),
                "z": parse_algo(z_algo, x, y, 0)
            },
            "rotation": {
                "x": parse_algo(x_rot_algo, x, y, 0),
                "y": parse_algo(y_rot_algo, x, y, 0),
                "z": parse_algo(z_rot_algo, x, y, 0)
            },
            "insert": {},
            "legend":"",
            "switch_profile": "dsa",
            "switch_rotation": 0
        } for x in range(width) for y in range(height)
        ]

        self.keylist = [k for k in keys if not (k['col'], k['row']) in self.ignored_keys]
        for u in data.get('u_diff', []):
            for k in self.keylist:
                if (k['col'], k['row']) in u.get('keys', []):
                    k['u_width'] = u.get('u_width', 1)
                    if k['u_width'] != 1:
                        if k['u_width'] > 0:
                            k['pos']['x'] = parse_algo(x_algo, k['col'] + (k['u_width'] - 1)/2, k['row'], 0)
                        else:
                            k['u_width'] = abs(k['u_width'])
                            k['pos']['x'] = parse_algo(x_algo, k['col'] - (k['u_width'] - 1)/2, k['row'], 0)
                    k['u_height'] = u.get('u_height', 1)
                    if k['u_height'] != 1:
                        k['pos']['y'] = parse_algo(y_algo, k['col'], k['row'] + (k['u_height'] - 1)/2, 0)
        for group in data.get('linked_keys', {}):
            for k in self.keylist:
                linked = {}
                if (k['col'], k['row']) == group.get('l'):
                    k['linked_keys']['r'] = group.get('r')
                elif (k['col'], k['row']) == group.get('r'):
                    k['linked_keys']['l'] = group.get('l')
                elif (k['col'], k['row']) == group.get('t'):
                    k['linked_keys']['b'] = group.get('b')
                elif (k['col'], k['row']) == group.get('b'):
                    k['linked_keys']['t'] = group.get('t')
        for inserts in data.get('inserts', []):
            for k in self.keylist:
                if k['col'] == inserts.get('col') and k['row'] == inserts.get('row'):
                    k['insert']['x'] = inserts.get('x')
                    k['insert']['y'] = inserts.get('y')
                    k['insert']['rot'] = inserts.get('rot')
        for legends in data.get('legends', []):
            for k in self.keylist:
                if k['col'] == legends.get('col') and k['row'] == legends.get('row'):
                    k['legend'] = legends.get('legend')
        for switches in data.get('switches', []):
            for k in self.keylist:
                if k['col'] == switches.get('col') and k['row'] == switches.get('row'):
                    k['switch_profile'] = switches.get('profile', 'dsa')
                    k['switch_rotation'] = switches.get('rot', 0)
                    
        
    def export_json(self, data):
        fn = f"output/keylists/{self.name}_keylist.json"
        with open(fn, 'w') as f:
            json.dump(
                {
                    "name": self.name,
                    "hole_size": self.hole_size, 
                    "key_1u": self.key_1u, 
                    "thickness":self.thickness, 
                    "keylist":self.keylist
                }, f, indent=4)
        fn = f"output/data/{self.name}.json"
        with open(fn, 'w') as f:
            json.dump(data, f, indent=4)

    
arg = sys.argv[1] if len(sys.argv) > 1 else 0
if len(defaults.data) > int(arg):
    Keylist(defaults.data[int(arg)])
else:
    import datetime
    t = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    with open("output/error.log", 'a') as f:
        f.write(f"{t}: Invalid argument {arg}, defaulting to 0. ({len(defaults.data)} items available, zero-indexed)\n")
        Keylist(defaults.data[0])
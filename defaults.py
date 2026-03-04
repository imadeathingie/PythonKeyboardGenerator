data = [
    {
        'name': "5x5",
        "width": 5,
        "height": 5,
        # "hole_size": 14.5,
        # "key_1u": 19.05,
        # "thickness": 5,
        # "x_algo": "x*1905/100+(x*10)",
        # "y_algo": "-y*1905/100-(y*10)",
        # "z_algo": "abs(y-2)*4+abs(x-2)*3 + 10",
        # "x_rot_algo": "(y-2)*-5",
        # "y_rot_algo": "(x - 2)*(-9)",
        # "z_rot_algo": "0"
    },
    {
        'name': "5x5_2",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*1905/100+(x*10)",
        "y_algo": "-y*1905/100-(y*10)",
        "z_algo": "abs(y-2)*4+abs(x-2)*3 + 10",
        "x_rot_algo": "(y-2)*-5",
        "y_rot_algo": "(x - 2)*(-9)",
        "z_rot_algo": "0"
    },
    {
        'name': "5x5_3",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*1905/100",
        "y_algo": "-y*1905/100",
        "z_algo": "abs(y-2)*2+abs(x-2)*2 + 10",
        "x_rot_algo": "(y-2)*-3",
        "y_rot_algo": "(x - 2)*(-5)",
        "z_rot_algo": "0",
        "ignored_keys": [(0, 0), (0, 2), (0, 4), (2, 0), (2, 4), (4, 0), (4, 4)]
    },
    {
        "name": "staggered_11x4_6",
        "width": 12,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*19.05 + ((-abs(y-5)*0.25*19.05 if x>6 else abs(y-5)*0.25*19.05) if y<4 else 0)",
        "y_algo": "-y*19.05",
        "z_algo": "20 - abs(x-5.5)*3 + (abs(y-5)*4 if y<4 else 0)",
        "x_rot_algo": "0",
        "y_rot_algo": "((-10 + abs(x-5.5)*2 if x<5 else (0 if x<8 else 10 - abs(x-5.5)*2))) if y != 0 and x != 4 else 0",
        "z_rot_algo": "0",
        "ignored_keys": [(0, 4), (1,4), (2,4), (9,4), (10,4), (11,4), (5, 0), (6,0),(7,0),(5,1),(6,1),(5,2),(6,2),(6,3)],
        "linked_keys": [{
            'l':(4,0),
            'r':(8,0),
        }, 
        {
            'l':(4,1), 
            'r':(7,1)
        }, 
        {
            'l':(5,3), 
            'r':(7,3)
        }],
        "u_diff":[{
            "keys": [(4,0)],
            "u_width": 1.5,
            "u_height": 1
        }]
    },
    {
        "name": "staggered_y_5x5",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*19.05",
        "y_algo": "-y*19.05+(5 if x %2 == 0 else -5)",
        "z_algo": "10",
        "x_rot_algo": "0",
        "y_rot_algo": "0",
        "z_rot_algo": "0"
    },
    {
        "name": "staggered_x_5x5",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*19.05+(5 if y %2 == 0 else -5)",
        "y_algo": "-y*19.05",
        "z_algo": "10",
        "x_rot_algo": "0",
        "y_rot_algo": "0",
        "z_rot_algo": "0"
    }
]
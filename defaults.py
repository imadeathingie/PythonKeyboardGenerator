data = [
    {
        'name': "5x5",
        "width": 5,
        "height": 5
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
        "x_algo": "x*19.05 + ((-abs(y-5)*0.25*19.05 if x>6 else (abs(y-5)*0.25*19.05) if x<6 else 0) if y<4 else 0)",
        "y_algo": "-y*19.05",
        "z_algo": "25 - abs(x-5.5)*4 + (abs(y-5)*4 if y<4 else 0)",
        "x_rot_algo": "0",
        "y_rot_algo": "((-10 + abs(x-5.5)*-1 if x<5 else (0 if x<8 else 10 - abs(x-5.5)*-1))) if y != 0 and x != 4 else 0",
        "z_rot_algo": "0",
        "ignored_keys": [(0, 4), (1,4), (2,4), (9,4), (10,4), (11,4), (5, 0), (6,0),(7,0),(5,1),(6,1),(5,2),(6,2),(6,3)],
        "linked_keys": [{
            'l':(4,0),
            'r':(8,0),
        },
        {
            't':(4,0),
            'b':(7,1)
        },
        {
            't':(8,0),
            'b':(4,1)
        },
        {
            'l':(4,1), 
            'r':(7,1)
        }, 
        {
            'l':(5,3), 
            'r':(7,3)
        },
        {
            't':(5,3),
            'b':(6,4)
        },
        {
            't':(7,3),
            'b':(6,4)
        },
        {
            'l':(4,2),
            'r':(7,2)
        }
        ],
        "u_diff":[{
            "keys": [(4,0)],
            "u_width": 1.5,
            "u_height": 1
        },
        {
            "keys": [(4,2)],
            "u_width": 1.25,
            "u_height": 1
        },
        {
            "keys": [(7,2)],
            "u_width": -1.25,
            "u_height": 1
        }
        ]
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
    },
    {
        "name": "y_gappy_5x5",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*19.05",
        "y_algo": "-y*20.05",
        "z_algo": "10",
        "x_rot_algo": "-y*5",
        "y_rot_algo": "0",
        "z_rot_algo": "0"
    },
    {
        "name": "x_gappy_5x5",
        "width": 5,
        "height": 5,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*22.05",
        "y_algo": "-y*19.05",
        "z_algo": "10",
        "x_rot_algo": "0",
        "y_rot_algo": "(x-3)*-10",
        "z_rot_algo": "0",
        "inserts": [
            {
                "col": 0,
                "row": 0,
                "x": -5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 0,
                "x": 5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 4,
                "x": 5,
                "y": -6,
                "rot": 180
            },
            {
                "col": 0,
                "row": 4,
                "x": -5,
                "y": -6,
                "rot": 180
            }
        ]
    },
    {
        'name': "5x3",
        "width": 5,
        "height": 3,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*1905/100",
        "y_algo": "-y*1905/100",
        "z_algo": "abs(y-1)*4+10",
        "x_rot_algo": "(y-1)*-5",
        "y_rot_algo": "0",
        "z_rot_algo": "0",
        "inserts": [
            {
                "col": 0,
                "row": 0,
                "x": -5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 0,
                "x": 5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 2,
                "x": 5,
                "y": -6,
                "rot": 180
            },
            {
                "col": 0,
                "row": 2,
                "x": -5,
                "y": -6,
                "rot": 180
            }
        ]
    },
    {
        'name': "5x3_staggered_pinky",
        "width": 5,
        "height": 3,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*1905/100 + x",
        "y_algo": "-y*1905/100 - y + (5 if x == 4 else 0)",
        "z_algo": "y*(y+1)+13- x + (1 if x == 4 else 0)",
        "x_rot_algo": "y*-8",
        "y_rot_algo": "x*-5",
        "z_rot_algo": "0",
        "inserts": [
            {
                "col": 0,
                "row": 0,
                "x": -6,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 0,
                "x": 6,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 2,
                "x": 6,
                "y": -7,
                "rot": 180
            },
            {
                "col": 0,
                "row": 2,
                "x": -6,
                "y": -7,
                "rot": 180
            }
        ],
        "switch_rotation": 180,
        "switch_profile": "dsa",
        "legends": [
            {
                "col": 0,
                "row": 0,
                "legend": "A"
            },
            {
                "col": 1,
                "row": 0,
                "legend": "Bb"
            },
            {
                "col": 2,
                "row": 0,
                "legend": "B"
            },
            {
                "col": 3,
                "row": 0,
                "legend": "C"
            },
            {
                "col": 4,
                "row": 0,
                "legend": "C#"
            },
            {
                "col": 0,
                "row": 1,
                "legend": "D"
            },
            {
                "col": 1,
                "row": 1,
                "legend": "D#"
            },
            {
                "col": 2,
                "row": 1,
                "legend": "E"
            },
            {
                "col": 3,
                "row": 1,
                "legend": "F"
            },
            {
                "col": 4,
                "row": 1,
                "legend": "F#"
            },
            {
                "col": 0,
                "row": 2,
                "legend": "G"
            },
            {
                "col": 1,
                "row": 2,
                "legend": "G#"
            },
            {
                "col": 2,
                "row": 2,
                "legend": "A"
            },
            {
                "col": 3,
                "row": 2,
                "legend": "Bb"
            },
            {
                "col": 4,
                "row": 2,
                "legend": "B"
            }
        ]
    },
    {
        'name': "5x3_staggered",
        "width": 5,
        "height": 3,
        "hole_size": 14.5,
        "key_1u": 19.05,
        "thickness": 5,
        "x_algo": "x*1905/100 - x*10",
        "y_algo": "-y*1905/100 if x != 4 else -y*1905/100 + 5",
        "z_algo": "y*(y+1)+13+x*15",
        "x_rot_algo": "y*-5",
        "y_rot_algo": "(x-5)*-12",
        "z_rot_algo": "0",
        "inserts": [
            {
                "col": 0,
                "row": 0,
                "x": -5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 0,
                "row": 0,
                "x": -5,
                "y": 6,
                "rot": 90
            },
            {
                "col": 4,
                "row": 0,
                "x": 5,
                "y": 6,
                "rot": 0
            },
            {
                "col": 4,
                "row": 2,
                "x": 5,
                "y": -6,
                "rot": 180
            },
            {
                "col": 0,
                "row": 2,
                "x": -5,
                "y": -6,
                "rot": 180
            }
        ]
    }
]
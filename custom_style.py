
def eurogenius_css():
    return '''
    <style>
        body, .main {
            background-color: #0F2027;
            background-image: linear-gradient(to right, #2C5364, #203A43, #0F2027);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }

        h1, h2, h3 {
            color: #00BFFF; /* Blau */
        }

        .stButton button {
            background-color: #FFD700; /* Gold */
            color: #000;
            font-weight: bold;
            border-radius: 20px;
            padding: 0.5em 1.5em;
            transition: 0.3s;
        }

        .stButton button:hover {
            background-color: #FF4500; /* Rot */
            color: white;
        }

        .stSlider > div[data-baseweb="slider"] {
            background-color: #32CD32; /* Grün */
        }

        .st-expanderHeader {
            color: #00BFFF;
            font-weight: bold;
        }

        .stDataFrame {
            background-color: white;
            color: black;
        }

        .css-1v0mbdj {
            color: #00FFEF;
        }

        footer {
            visibility: hidden;
        }
    </style>
    '''

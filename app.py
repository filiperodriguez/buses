import cleandata

jsondata = """[4,"1.0",1408033180430]
[1,"Vicarage Rd / Wandle Park Tram Stop","410","Wallington",1408033244000]
[1,"Vicarage Rd / Wandle Park Tram Stop","455","Wallington Station",1408033604000]
[1,"Vicarage Rd / Wandle Park Tram Stop","407","Sutton Town Centre",1408033780000]
[1,"Vicarage Rd / Wandle Park Tram Stop","410","Wallington",1408033897000]
[1,"Vicarage Rd / Wandle Park Tram Stop","410","Wallington",1408034324000]
[1,"Vicarage Rd / Wandle Park Tram Stop","407","Sutton Town Centre",1408034731000]
[1,"Vicarage Rd / Wandle Park Tram Stop","410","Wallington",1408034821000]"""

tfl_data = cleandata.CleanData()

to_clean = tfl_data.clea_array(jsondata)

print tfl_data.set_json(to_clean)
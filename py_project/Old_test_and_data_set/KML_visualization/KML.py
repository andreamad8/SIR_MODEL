import simplekml
kml = simplekml.Kml()
pnt=kml.newpoint(name="London United Kingdom Heathrow", coords=[(-0.103,51.795)])
kml.newpoint(name="Moscow Russia Domododevo", coords=[(38.51,55.681)])   # lon, lat, optional height
kml.newpoint(name="Hong Kong", coords=[(114.524,22.514)]) 
pnt.style.iconstyle.scale = 0.5  # Icon thrice as big
pnt.style.iconstyle.icon.href = 'C:/Users/andrea/Desktop/flight/KML_visualization/red.png'

pol = kml.newpolygon()
print pol.outerboundaryis # Shows that the outer boundary of a polygon is a linear ring
pol.outerboundaryis.coords = [(-0.103,51.795), (38.51,55.681)]

kml.save("botanicalgarden.kml")
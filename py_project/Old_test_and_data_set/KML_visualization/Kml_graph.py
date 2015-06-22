
import simplekml
kml = simplekml.Kml()


for line in open("data_set.csv"):
    csv_row = line.split(',')
    lng_a=csv_row[1].replace('"','')
    lat_a=csv_row[0].replace('"','')
    lng_b=csv_row[3].replace('"','')
    lat_b=csv_row[2].replace('"','')
    pnt_a=kml.newpoint(name="a", coords=[(lng_a,lat_a)])
    pnt_a.style.iconstyle.scale = 1.5  # Icon thrice as big
    pnt_a.style.iconstyle.icon.href = 'C:/Users/andrea/Desktop/flight/KML_visualization/orange.png'
    pnt_b=kml.newpoint(name="b", coords=[(lng_b,lat_b)])
    pnt_b.style.iconstyle.scale = 1.5  # Icon thrice as big
    pnt_b.style.iconstyle.icon.href = 'C:/Users/andrea/Desktop/flight/KML_visualization/orange.png'
    ls=kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",coords=[(lng_a,lat_a),(lng_b,lat_b)])
    ls.tessellate=1


kml.save("edges.kml")


	
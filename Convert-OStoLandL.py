import osgb
from geopy.distance import geodesic as GD

home = (51.4229253,-0.1940419)

file_in = open("Coal Posts Input.csv", "r")
coal_posts = file_in.readlines()
file_out_w = open("Coal Posts Output Wordy.txt", "w")
file_out_b = open("Coal Posts Output Brief.txt", "w")

min_distance_geodis = 999
min_coal_post_number = 0

for coal_post in coal_posts:
    # Load the data from the file
    coal_post_data = coal_post.split(',')
    coal_post_number = coal_post_data[0]
    coal_post_type = coal_post_data[1]
    coal_post_grid_ref = coal_post_data[2].strip()

    # Convert to long and lat
    ll = osgb.grid_to_ll(osgb.parse_grid(coal_post_grid_ref))

    # Get geodis and haversine distances
    distance_geodis = GD(home, ll).km
    if distance_geodis < min_distance_geodis:
        min_coal_post_number = coal_post_number
        min_distance_geodis = distance_geodis

    # Spit out the results
    line_w = "Number: {}, Type: {}, Grid Ref: {}, Longitude: {}, Latitude: {}, Distance: {:.2f}".format(
        coal_post_number,
        coal_post_type,
        coal_post_grid_ref,
        ll[0],
        ll[1],
        distance_geodis)
    line_b = "{},{},{}".format(coal_post_number, ll[0], ll[1])
    print(line_w)
    file_out_w.write(line_w + "\n")
    file_out_b.write(line_b + "\n")

# Print the nearest and close file
file_out_w.close()
file_out_b.close()
print(min_coal_post_number)

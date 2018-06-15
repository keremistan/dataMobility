from folium import Map, Marker, Icon, CustomIcon
from csv import reader
from pathlib import Path
from time import sleep
from PIL import Image
from base64 import b64encode
from os import listdir
from os.path import isfile, join
from random import choice

def read_csv_data(path):
    data = []
    with open(path, 'r', newline='') as file:
        # reads the opened csv file
        csv_reader = reader(file)
        for line in csv_reader:
            if 'lat' not in line:
                data.append([float(line[0]), float(line[1])])
    return data

def create_map(start_coords: tuple):
    # creates map instance with the given coordinates
    location = Map(start_coords[:2])
    # scale of the starting map
    location.zoom_start = 12
    return location

def put_marker(coord: list, location: Map, color_icon: str):
    
    # create a marker with a specific coords
    marker = Marker(coord[:2], icon=Icon(color=color_icon))
    # add the marker to the passed the map
    marker.add_to(location)

if __name__ == '__main__':
    trajectory_path = './data/'
    trajectory_datas = []
    number_of_files_tbr = 3 # tbr = to be read
    colors_for_icons = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'beige', 'darkblue', 'gray']

    # Get all the files with extension '.csv' and put them into an array with the folder name
    data_paths = [join(trajectory_path, path) for path in listdir(trajectory_path) if isfile(join(trajectory_path, path)) and ('.csv' in path) ]

    # Extract the data from the trajectory files with the given number of files
    for x in range(number_of_files_tbr):
        trajectory_datas.append(read_csv_data(data_paths[x]))

    # Create the map with a sample coord
    area = create_map(trajectory_datas[1][1])

    for tr in trajectory_datas:
        color_of_icon = choice(colors_for_icons)
        for data_point in tr:
            put_marker(data_point, area, color_of_icon)

    area.save(str(Path.home()) + "/Desktop/map.html")
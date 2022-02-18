import numpy as np


def create_mercator_transformer(width):
    radius = width / (2 * np.pi)

    def from_mercator_projection(array_of_coords):
        new_coords = map(lambda coord: {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Point",
                "coordinates": [
                    np.degrees(coord[0] / radius),
                    np.degrees(2 * np.arctan(np.exp(coord[1] / radius)) - np.pi / 2)
                ],
            }
        }, array_of_coords)

        return list(new_coords)

    return from_mercator_projection

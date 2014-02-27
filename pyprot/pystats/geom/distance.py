def dist_3d(coord0, coord1):
    """ Returns the geometrical distance between 2 coordinates in a 3D space. 
    Args:
        coord0 (list): list of x,y,z coordinates, e.g., [1,2,3]
        coord1 (list): list of x,y,z coordinates, e.g., [4,5,6]

    """
    assert len(coord0) == 3 and len(coord1) == 3,\
         "List must have 3 coordinates each"
    return sum([(j-i)**2 for i,j in zip(coord0,coord1)])**0.5

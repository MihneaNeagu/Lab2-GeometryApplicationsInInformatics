# Lab2-GeometryApplicationsInInformatics

Write a program in Python that determines the image of a polygon in the plane by a reflection from a given line.

Consider both the given line by the general equation (the input data will be the coefficients of the equation).

The program must contain the following steps:

determine the point of intersection between the line ̧and one of the axes;

determination of the matrix of the translation that makes the line pass through the origin;

determination of the rotation matrix with respect to the origin that makes the line overlap one of the axes;

determining the matrix of the reflection from the chosen coordinate axis;

determination of the rotation matrix with respect to the origin that brings the line to the initial direction;

determination of the translation matrix which brings the line to the initial position;

determination of the transformation matrix, by multiplying the 5 previous matrices.
reading the vertices of the polygon;

determining the homogeneous matrix of the coordinates of the vertices of the transformed polygon.

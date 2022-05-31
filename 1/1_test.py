class Point:
    color = 'red'
    circle = 2


a = Point()
b = Point()

# add attr
setattr(Point, 'type_pt', 'new_attr')
# show attr
getattr(Point, 'color')
# Check attr
hasattr(Point, 'color')
# del attr
delattr(Point, 'type_pt')


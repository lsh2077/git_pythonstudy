import chapter_10
from chapter_10.my_area import PI, square_area

#import chapter10.my_area
print('pi=',PI)
print('square area =', square_area(5))
print(dir(chapter_10.my_area))
[print(content) for content in dir(chapter_10.my_area)]
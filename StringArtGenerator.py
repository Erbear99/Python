

from PIL import Image, ImageDraw
import numpy

nail_width = .05 # inches
string_width = .05 # inches
background_size = 5000 #inches
number_of_nails = 100

new_img = Image.new(mode="RGB", size=(5000,5000), color = (255,255,255))
draw = ImageDraw.Draw(new_img)
for i in range(number_of_nails):
    #from 0 to 2pi
    angle = i/number_of_nails*2*numpy.pi
    centroid = (int(numpy.sin(angle)*(background_size/2)+background_size/2),int(numpy.cos(angle)*(background_size/2)+background_size/2) )
    draw.ellipse((centroid[0]-2, centroid[1]-2, centroid[0]+2, centroid[1]+2) ,fill='blue')

    

new_img.show()
#each of the nail's locations are generated

greyscaleimg = numpy.asarray(Image.open("C:/Users/Erik/Desktop/Bear-test.png").convert('L'))
Image.open("C:/Users/Erik/Desktop/Bear-test.png").convert('L').show()

print(greyscaleimg[0][0])
print(greyscaleimg)
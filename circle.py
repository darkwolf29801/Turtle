from turtle import *
def circle(r):
    c=2*3.14*4*r
    for i in range(360):
      right(1)
      forward(c/360)

r=int(input('Enter the radius in mm\n'))
circle(r)
done()

import turtle
import matplotlib.pyplot as plt 
from random import randint
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Draw a fractal')
parser.add_argument('--fractal_type', default='tree', choices=['tree', 'snowflake', 'fern', 'mandelbrot'],
                    help='Choose a fractal type.')

args = parser.parse_args()

def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)
    build_tree(t, new_length, shorten_by, angle)
    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    t.backward(branch_length)

def koch_curve(t, iterations, length, shortening_factor, angle):
  if iterations == 0:
    t.forward(length)
  else:
    iterations = iterations - 1
    length = length / shortening_factor
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle * 2)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)

def mandelbrot(c, z):
   global iterations
   count = 0
   for a in range(iterations):
      z = z**2 + c
      count += 1        
      if(abs(z) > 4):
         break
   return count

def mandelbrot_set(x, y):
   m = np.zeros((len(x), len(y)))
   for i in range(len(x)):
      for j in range(len(y)):
         c = complex(x[i], y[j])
         z = complex(0, 0)
         count = mandelbrot(c, z)
         m[i, j] = count    
   return m

if __name__ == "__main__":
  
  if args.fractal_type == 'tree':
    MINIMUM_BRANCH_LENGTH = 5
    tree = turtle.Turtle()
    tree.hideturtle()
    tree.setheading(90)
    tree.color('green')
    build_tree(tree, 50, 5, 30)
    turtle.mainloop()

  elif args.fractal_type == 'snowflake':
    t = turtle.Turtle()
    t.hideturtle()
    for i in range(3):
      koch_curve(t, 4, 200, 3, 60)
      t.right(120)
    turtle.mainloop()

  elif args.fractal_type == 'fern':

    x = [0]
    y = [0]

    for i in range(0, 50000): 
    
      p = randint(1, 100) 
        
      if p == 1: 
          x.append(0) 
          y.append(0.16*(y[i])) 
           
      if p >= 2 and p <= 86: 
          x.append(0.85*(x[i]) + 0.04*(y[i])) 
          y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 
        
      if p >= 87 and p <= 93: 
          x.append(0.2*(x[i]) - 0.26*(y[i])) 
          y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
            
      if p >= 94 and p <= 100: 
          x.append(-0.15*(x[i]) + 0.28*(y[i])) 
          y.append(0.26*(x[i]) + 0.24*(y[i])+0.44)

    plt.scatter(x, y, s = 0.2, c ='#5dbb63') 
    plt.axis("off")
    plt.show()

  else:
  #elif args.fractal_type == 'mandelbrot':
    # initialize rows, columns and iterations
    rows = 1000
    cols = 1000
    iterations = 150
    # creating our x and y arrays
    x = np.linspace(-2, 1, rows)
    y = np.linspace(-1, 1, cols)
    # create our mandelbrot set
    m = mandelbrot_set(x, y) 
    # plot the set (best colors: binary, hot, bone, magma)
    plt.imshow(m.T, cmap = "magma")
    plt.axis("off")
    plt.show()
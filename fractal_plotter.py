import turtle
import matplotlib.pyplot as plt 
from random import randint
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Draw a fractal')
parser.add_argument('--fractal_type', default='tree', choices=['tree', 'snowflake', 'fern', 'mandelbrot'],
                    help='Choose a fractal type.')

args = parser.parse_args()

def draw_tree(t, branch_length, shorten_length, angle, min_branch_length):
  if branch_length > min_branch_length:
    t.forward(branch_length)
    new_length = branch_length - shorten_length
    t.left(angle)
    draw_tree(t, new_length, shorten_length, angle, min_branch_length)
    t.right(angle * 2)
    draw_tree(t, new_length, shorten_length, angle, min_branch_length)
    t.left(angle)
    t.backward(branch_length)

def draw_koch_curve(koch, iterations, length, shorten_factor, angle):
  if iterations == 0:
    koch.forward(length)
  else:
    iterations = iterations - 1
    length = length / shorten_factor
    draw_koch_curve(koch, iterations, length, shorten_factor, angle)
    koch.left(angle)
    draw_koch_curve(koch, iterations, length, shorten_factor, angle)
    koch.right(angle * 2)
    draw_koch_curve(koch, iterations, length, shorten_factor, angle)
    koch.left(angle)
    draw_koch_curve(koch, iterations, length, shorten_factor, angle)

def fern_set(iterations):

  x = [0]
  y = [0]

  for i in range(0, iterations): 
  
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

  return x, y

def mandelbrot(c, z, iterations):
   count = 0
   for a in range(iterations):
      z = z**2 + c
      count += 1        
      if(abs(z) > 4):
         break
   return count

def mandelbrot_set(x, y, iterations):
   m = np.zeros((len(x), len(y)))
   for i in range(len(x)):
      for j in range(len(y)):
         c = complex(x[i], y[j])
         z = complex(0, 0)
         count = mandelbrot(c, z, iterations)
         m[i, j] = count    
   return m

if __name__ == "__main__":
  
  if args.fractal_type == 'tree':
    tree = turtle.Turtle()
    tree.ht()
    tree.penup()
    tree.goto(0,-250)
    tree.pendown()
    tree.setheading(90)
    tree.color('green')
    tree.speed('fastest')
    draw_tree(tree, 100, 10, 20, 1)
    turtle.mainloop()

  elif args.fractal_type == 'snowflake':
    koch = turtle.Turtle()
    koch.ht()
    koch.penup()
    koch.goto(-200,100)
    koch.pendown()
    koch.speed('fastest')
    koch.color("#87CEFA")
    for i in range(3):
      draw_koch_curve(koch, 4, 400, 3, 60)
      koch.right(120)
    turtle.mainloop()

  elif args.fractal_type == 'fern':

    iterations = 50000
    # create fern set
    x, y = fern_set(iterations)
    # plot fern set
    plt.scatter(x, y, s=0.2, c='#228B22') 
    plt.axis("off")
    plt.show()

  else:
  #elif args.fractal_type == 'mandelbrot':
    # initialize rows, columns and iterations
    rows = 1000
    cols = 1000
    iterations = 150
    # creating x and y arrays
    x = np.linspace(-2, 1, rows)
    y = np.linspace(-1, 1, cols)
    # create our mandelbrot set
    m = mandelbrot_set(x, y, iterations) 
    # best colors: binary, hot, bone, magma
    plt.imshow(m.T, cmap = "magma")
    plt.axis("off")
    plt.show()
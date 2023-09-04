import imageio

filenames = ['Eren1.png', 'Eren2.png']
images = [ ]

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('eren_animation.gif', images, duration = 1.0, loop=0)
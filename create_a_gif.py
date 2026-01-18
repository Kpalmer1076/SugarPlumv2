import imageio.v3 as iio

filenames = ['nanna1.png', 'nanna2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))
    iio.imwrite('bannana.gif', images, duration = 500, loop = 0)
    
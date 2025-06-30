import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('filexlsx/rekap-nilai.png')
plt.imshow(img)
plt.axis('off')  # Hide the axes
plt.show()  # Display the image
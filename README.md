# Imgur_Downloader

Created by Ahmed Ashraf (ultimat3pro)

Easily download images from an imgur album 
by providing the album Id regardless of image format.

Imgur allows us to upload a lot of images and keep them
in organized albums. Though imgur provides a way for us
to download the entire album, it is incredibly slow and
often does not work. Many of us have resorted to downloading
each image rather than waiting for that process to finish.
I don't know about you, but I am not going though a 700+ image 
album, right-clicking and saving each one. So, I made this.

The user is only asked for the unique id assigned to each
album (typically the last part of the url pointing to the
album. For example, "QwP9J" is the id of the album available
through the link "http://imgur.com/gallery/QwP9J"). The program
ensures that the album actually exists. If
the album exists, a folder, named as the id, is created and all
the images from the album is downloaded inside that folder. The
images are named with numbers, starting from 0 and incremented 
for each image.

I do not claim this is the first to do this. In fact, considering
the amount of people who want to have this capability, I am rather
certain that something like this already exists that achieves similar
results in this manner or completely differently.

Hope this can be as useful to you as it is to me. No executable yet,
so some assembly required (basically run with a python IDE with the used
libraries installed).

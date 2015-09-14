def viewPicture():
  #Pick photo
  file1 = pickAFile()
  file2 = pickAFile()
  file3 = pickAFile()
  file4 = pickAFile()
  file5 = pickAFile()
  file6 = pickAFile()
  file7 = pickAFile()
  file8 = pickAFile()
  file9 = pickAFile()
  
  #Make photo a picture
  pic1 = makePicture(file1)
  pic2 = makePicture(file2)
  pic3 = makePicture(file3)
  pic4 = makePicture(file4)
  pic5 = makePicture(file5)
  pic6 = makePicture(file6)
  pic7 = makePicture(file7)
  pic8 = makePicture(file8)
  pic9 = makePicture(file9)
  
  #Get image width and height (amount of pixels)
  picWidth = getWidth(pic1)
  picHeight = getHeight(pic1)
  print "The picture width and height are", picWidth, picHeight
  
  #Get pixels and print value
  pixX = 0
  pixY = 0
  #pixel = getPixel(pic,pixX,PixY)
  #pixels = getPixels(pic)
  #print "The pixel values at 0,0 is",pixel
  
  
  #Change colors to white
  while(pixX != 494):
   pixel1 = getPixel(pic1,pixX,pixY)
   pixel2 = getPixel(pic2,pixX,pixY)
   pixel3 = getPixel(pic3,pixX,pixY)
   pixel4 = getPixel(pic4,pixX,pixY)
   pixel5 = getPixel(pic5,pixX,pixY)
   pixel6 = getPixel(pic6,pixX,pixY)
   pixel7 = getPixel(pic7,pixX,pixY)
   pixel8 = getPixel(pic8,pixX,pixY)
   pixel9 = getPixel(pic9,pixX,pixY)
   
   #Start comparing pixels
   if(pixY != 556):
    #Setting Red
    r = getRed(pixel1), getRed(pixel2), getRed(pixel3), getRed(pixel4), getRed(pixel5), getRed(pixel6), getRed(pixel7), getRed(pixel8), getRed(pixel9)
    #print sorted(r)
    #print sorted(r)[4]
    
    #Setting Green
    g = getGreen(pixel1), getGreen(pixel2), getGreen(pixel3), getGreen(pixel4), getGreen(pixel5), getGreen(pixel6), getGreen(pixel7), getGreen(pixel8), getGreen(pixel9)
    #print sorted(g)
    #print sorted(g)[4]
    
    #Setting Green
    b = getBlue(pixel1), getBlue(pixel2), getBlue(pixel3), getBlue(pixel4), getBlue(pixel5), getBlue(pixel6), getBlue(pixel7), getBlue(pixel8), getBlue(pixel9)
    #print sorted(b)
    #print sorted(b)[4]
    
    setRed(pixel1, sorted(r)[4])
    setGreen(pixel1, sorted(g)[4])
    setBlue(pixel1, sorted(b)[4])
    pixY += 1
   else:
    #Getting Red
    r = getRed(pixel1), getRed(pixel2), getRed(pixel3), getRed(pixel4), getRed(pixel5), getRed(pixel6), getRed(pixel7), getRed(pixel8), getRed(pixel9)
    
    #Getting Green
    g = getGreen(pixel1), getGreen(pixel2), getGreen(pixel3), getGreen(pixel4), getGreen(pixel5), getGreen(pixel6), getGreen(pixel7), getGreen(pixel8), getGreen(pixel9)
    
    #Getting Blue
    b = getBlue(pixel1), getBlue(pixel2), getBlue(pixel3), getBlue(pixel4), getBlue(pixel5), getBlue(pixel6), getBlue(pixel7), getBlue(pixel8), getBlue(pixel9)
    
    #Setting Colors
    setRed(pixel1, sorted(r)[4])
    setGreen(pixel1, sorted(g)[4])
    setBlue(pixel1, sorted(b)[4])
    
    #Increment X & Y
    pixY = 0
    pixX += 1
  repaint(pic1)

#Run Program
viewPicture()
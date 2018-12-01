import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path    
import numpy as np    
#we just imported a bunch of necessary libraries right here   

def moodify(original_image,flavor,mood): #define function that performs moodification
    
    '''
    This function returns bottle-cut of image pasted over colorfully generated pattern 
    whose color and pattern are determined by the arguments flavor and mood respectively.
    '''
    
    #resize original image to suit pattern, assign rows/columns to new
    #dimensions
    columns, rows = original_image.size
    new_image=original_image.resize((int(200*columns/rows),200))
    columns,rows=new_image.size
    
    #define flavors and moods (colors and pattern parameters)
    #flavors are represented by 3-tuples of 4-item lists with rgb values and alpha channel value
    flavors={"Classic Marley":([85,128,0,255],[255,198,26,255],[230,45,0,255]),
             "Citrus":([255,166,77,255],[153,204,0,255],[255,255,102,255]),
             "Black Tea":([153,39,0,255],[45,20,20,255],[77,20,0,255]),
             "Berry":([153,51,103,255],[153,0,51,255],[211,121,166,255]),
             "Green Tea":([153,204,0,255],[197,141,83,255],[102,102,51,255]),
             "Lemonade and Tea":([230,115,0,255],[134,179,0,255],[240,230,3,255]),
             "Passion Flower":([210,210,200,255],[153,230,80,255],[193,83,141,255]),
             "Raspberry":([0, 126, 128,255],[211, 121, 166,255],[134, 45, 134,255]),
             "Tropical Punch":([0,127,128,255],[179,255,240,255],[255,92,51,255]),
             "Winterberry":([0,102,153,255],[153,204,255,255],[236,217,198,255]),
             "Mocha":([255,243,229,255],[77,38,0,255],[217,140,140,255]),
             "Grape":([102,0,102,255],[179,0,89,255],[38,115,38,255]),
             "Cotton Candy":([179,179,179,255],[255,77,166,255],[0,230,184,255]),
             "Autumn Spice":([160,0,0,255],[234,145,89,255],[102,50,0,255]),
             "Banana Blast":([138,0,230,255],[230,172,0,255],[229,230,0,255])
             }
    #moods are represented by lists containing mod parameters
    #[mod,lower1,upper1,lower2,upper2,exponent,multiplication]
    moods={"Happy-Go-Lucky":[50,4,16,36,49,4,1],
           "Breezy":[100,1,36,64,81,1.12,1],
           "Laid-Back":[20,0,7,9,16,2,.5],
           "Serene":[50,36,49,16,27,2,1],
           "Devil-May-Care":[100,4,36,64,81,4,1],
           "Nonchalant":[25,4,9,13,19,2,1],
           "Chill":[15,0,5,7,12,3,1.0/3.0],
           "Indolent":[25,1,9,12,17,2,4],
           "Carefree":[75,16,27,36,64,2,3],
           "Mild":[26,13,19,3,7,2,2],
           "Insouciant":[100,4,49,64,94,2,4],
           "Hang-Loose":[34,17,27,3,8,2,4]
           }
            
    #Make a background from selected flavor and mood      
    pattern = PIL.Image.new('RGBA', (int(columns*1.2), int(rows*1.2)))#pattern in 20% larger in width/height than original
    array= np.array(pattern) #pattern converted to array to iterate through pixels
    for row in range(int(rows*1.2)):
        for column in range(int(columns*1.2)):#iterate through pixels by row and column of array
           #the row and column are multiplied, raised to a specified power, and the result is multiplied by specified factor
           #the value is then compared to preset ranges to determine the pixel's color
           #three possible colors are assigned depending on which range it falls or does not fall within
           if moods[mood][1]<((row*column)**moods[mood][5]*moods[mood][6])%moods[mood][0]<moods[mood][2]:
               array[row][column]= flavors[flavor][0]
           elif moods[mood][3]<((row*column)**moods[mood][5]*moods[mood][6])%moods[mood][0]<moods[mood][4]:
               array[row][column]= flavors[flavor][1]
           else:
               array[row][column]= flavors[flavor][2]

    #show array with pattern with correct dimensions for debug purpose
    #fig, ax = plt.subplots(1, 1) 
    #ax.imshow(array) 
    #fig.show()
    
    #convert array to image
    bg=PIL.Image.fromarray(array)
    
    #retrieve bottle-shaped mask
    bottle_mask = PIL.Image.open("bottle.png") #open bottle.png in local directory
    bottle_mask = bottle_mask.resize((columns,rows)) #resize to fit over edited image
    
    #print dimensions of resized image/mask for debug reasons
    print bottle_mask.size
    
    #Paste image onto background with that mask, return result
    result = bg #make result the bg pattern
    #paste the resized image on the bg with 10% offset in both dimensions and bottle-shaped mask
    result.paste(new_image, (int(columns*.1),int(rows*.1)), mask=bottle_mask)
    
    return result #function returns bottle-cut of image pasted over colorfully generated pattern
    
 
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregators
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:#iterate through directory contents
        absolute_filename = os.path.join(directory, entry)#get absolute filename
        try:
            image = PIL.Image.open(absolute_filename)#open the image
            file_list += [entry]#add filename to file_list
            image_list += [image]#add actual image to image_list
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list #2 lists containing all images and all coresponding filenames

def moodify_all(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'moodified', creating it if it does not exist.
    New image files are of type PNG and have been officially moodified.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'moodified'
    new_directory = os.path.join(directory, 'moodified')
    
    try:
        os.mkdir(new_directory)#try making new directory named 'moodified
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #Allow user to select flavor/mood
    #establish dictionaries associating a single letter to the full flavor/mood name
    #this makes user input quicker and easier
    flavor_selection={"a":"Classic Marley",
                      "b":"Citrus",
                      "c":"Black Tea",
                      "d":"Berry",
                      "e":"Green Tea",
                      "f":"Lemonade and Tea",
                      "g":"Passion Flower",
                      "h":"Raspberry",
                      "i":"Tropical Punch",
                      "j":"Winterberry",
                      "k":"Mocha",
                      "l":"Grape",
                      "m":"Cotton Candy",
                      "n":"Autumn Spice",
                      "o":"Banana Blast"
                      }
    mood_selection={"a":"Happy-Go-Lucky",
                    "b":"Breezy",
                    "c":"Laid-Back",
                    "d":"Serene",
                    "e":"Devil-May-Care",
                    "f":"Nonchalant",
                    "g":"Chill",
                    "h":"Indolent",
                    "i":"Carefree",
                    "j":"Mild",
                    "k":"Insouciant",
                    "l":"Hang-Loose"
                    }
    for key in flavor_selection: #iterate through flavors dictionary printing key with flavor
        print "%-5s%-20s" %(key, flavor_selection[key]) 
    #have user input letter key and assign flavor to the flavor_selection item at that key
    flavor=flavor_selection[raw_input("Pick a flavor (corresponding letter): ")]
    
    for key in mood_selection:#iterate through moods dictionary printing key with mood
        print "%-5s%-20s" %(key, mood_selection[key]) 
    #have user input letter key and assign mood to the mood_selection item at that key
    mood=mood_selection[raw_input("Pick a mood (corresponding letter): ")]
    
    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        
        # moodify w/ flavor and mood
        new_image = moodify(image_list[n],flavor, mood)
        
        #save the altered image, adding PNG extension to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

   
    
     
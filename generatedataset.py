import os
import numpy as np

# Used to generate random data of the same format as our previous Dataset_1
def convertdataset(filename_out):

    # Create the output file
    output = open(filename_out, 'w')

    dimension = 32
    low=0
    high = 1000
    numberOfLines = 68040

    # Write dimension to file
    output.write(str(dimension) + "\n")

    counter = 1
    for i in range(numberOfLines):
        newline = [str(element) for element in np.random.randint(low=low,high=high,size=dimension,dtype=int)]
        newline.append("({0})".format(counter))
        newline = ":".join(newline)
        output.write(newline + "\n")
        # Can use this to control the number of lines you
        # want to be written.
        # if counter == 1000:
        #    break
        counter += 1
        print("Lines written:", counter, end='\r')

    # Close stream
    output.close()

output_filename = "Dataset_1_Homemade.rcd"
if os.path.exists(output_filename):
    print("The file seems to already exist. \nDelete it or change the name of the output file.")
else:
    print("Generating...")
    convertdataset(output_filename)

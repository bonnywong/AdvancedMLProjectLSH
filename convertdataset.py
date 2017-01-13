import os


# Used to convert the Aerial data format to suit our own file format.
# Note the hardcoded names! Files are read and written to root of project.
def convertdataset(filename_out):
    # Read open original dataset file
    file = open("Aerial40_norm.txt", 'r')

    # To find the dimension we need to read the first line
    # and count the coordinates. We also process the line
    # since we read it.
    line = file.readline();
    line = line.strip().split()  # Split turns it into a list
    dimension = len(line)  # Count coordinates in the list
    counter = 1
    line.append("({0})".format(counter))  # Append the index within "()" to end of file
    line = ":".join(line)  # Join with ":" as separator

    # Create the output file
    output = open(filename_out, 'w')

    # Write dimension and processed first line to file
    output.write(str(dimension) + "\n")
    output.write(line + "\n")

    counter += 1

    for line in file:
        newline = line.strip().split()
        newline.append("({0})".format(counter))
        newline = ":".join(newline)
        output.write(newline + "\n")
        # Can use this to control the number of lines you
        # want to be written.
        # if counter == 1000:
        #    break
        counter += 1
        print("Lines written:", counter, end='\r')

    # Close streams
    file.close()
    output.close()

output_filename = "Dataset_2.rcd"
if os.path.exists(output_filename):
    print("The file seems to already exist. \nDelete it or change the name of the output file.")
else:
    print("Converting...")
    convertdataset(output_filename)

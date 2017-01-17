from datakeeper_dataset1 import *

print("Doing dimension 8")
for i in [1]:
    print("Dimension 8, i="+str(i))
    #main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_8.rcd",saveFilename="dataset_homemade_2/Dataset_2_Homemade_data_8_hashtables="+str(i)+".bin",numberOfHashtables=i)

print("Doing dimension 27")
for i in [35,40,45,50]:
    print("Dimension 27, i="+str(i))
    main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_27.rcd",saveFilename="dataset_homemade_2/Dataset_2_Homemade_data_27_hashtables="+str(i)+".bin",numberOfHashtables=i)

print("Doing dimension 64")
for i in [1]:
    print("Dimension 64, i="+str(i))
    #main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_64.rcd",saveFilename="dataset_homemade_2/Dataset_2_Homemade_data_64_hashtables="+str(i)+".bin",numberOfHashtables=i)

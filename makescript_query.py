from query import *

print("[makescript_query] Starting dimension 8")
dim8results=[]
# for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,15,20,24,25]:
#     print("[makescript_query] Dimension 8, i="+str(i))
#     dim8results.append(main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_8_hashtables="+str(i)+".bin",csvFilename="dataset_homemade_2/distanceVector_dim8.csv",dimensionForReshape=10,queryPointsFilename="dataset_homemade_2/Dataset_2_Homemade_query_8.rcd"))

print("[makescript_query] Starting dimension 27")
dim27results=[]
for i in [35,40,45,50]:
    print("[makescript_query] Dimension 27, i="+str(i))
    dim27results.append(main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_27_hashtables="+str(i)+".bin",csvFilename="dataset_homemade_2/distanceVector_dim27.csv",dimensionForReshape=10,queryPointsFilename="dataset_homemade_2/Dataset_2_Homemade_query_27.rcd"))

print("[makescript_query] Starting dimension 64")
dim64results=[]
# for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,15,20,25,27,30]:
#     print("[makescript_query] Dimension 64, i="+str(i))
#     dim64results.append(main(loadFilename="dataset_homemade_2/Dataset_2_Homemade_data_64_hashtables="+str(i)+".bin",csvFilename="dataset_homemade_2/distanceVector_dim64.csv",dimensionForReshape=10,queryPointsFilename="dataset_homemade_2/Dataset_2_Homemade_query_64.rcd"))

filename="dataset_homemade_2/query_results.txt"
output = open(filename, 'w')
output.write("dim8results: \n"+str(dim8results) + "\ndim27results: \n"+str(dim27results) + "\ndim64results: \n"+ str(dim64results))
output.close()
print("Saved results in "+filename)
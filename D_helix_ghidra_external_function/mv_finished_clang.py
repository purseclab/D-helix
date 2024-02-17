import os
import sys


directname_originalclang = "./test_muqi/originalclang"
directname_generated_whole_c = "./test_muqi/generated_whole_c"
directname_folder_for_project="./test_muqi/generated_function_c/project_folder"
directname_folder_finished_clang = "./test_muqi/finished_clang"

def main():
    os.system("mkdir "+ directname_folder_finished_clang)
    for filename_folder in os.listdir(directname_folder_for_project):
        filename = filename_folder[:-7]
        #print("mv "+directname_originalclang+"/"+filename+" "+directname_folder_finished_clang+"/")
        os.system("mv "+directname_originalclang+"/"+filename+" "+directname_folder_finished_clang+"/")

if __name__ == "__main__":
    main()


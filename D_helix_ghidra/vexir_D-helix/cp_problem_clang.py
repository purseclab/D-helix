import os
import sys


directname_originalclang_bakup = "/home/muqi/pthread_Angr_Promp../test_muqi/originalclang_bakup"
directname_originalclang_finished = "/home/muqi/pthread_Angr_Promp../test_muqi/originalclang_finished"
directname_originalclang = "../test_muqi/originalclang"
directname_generated_whole_c = "../test_muqi/generated_whole_c"
directname_generated_whole_html = "../test_muqi/generated_html"
directname_folder_for_project="/home/muqi/pthread_Angr_Prompt/regenerated_first_version__wrong_on../function_name_original"
directname_folder_finished_clang = "../test_muqi/finished_clang"

def main():
    '''
    #os.system("mkdir "+ directname_folder_finished_clang)
    for filename_folder in os.listdir(directname_folder_for_project):
        filename = filename_folder
        #print("mv "+directname_originalclang+"/"+filename+" "+directname_folder_finished_clang+"/")
        os.system("cp "+directname_originalclang_bakup+"/"+filename+" "+directname_originalclang+"/")
    
    os.system("mkdir "+ directname_originalclang_finished)
    for filename_c in os.listdir(directname_generated_whole_c):
        filename = filename_c.replace(".c","")
        os.system("mv "+directname_originalclang+"/"+filename+" "+directname_originalclang_finished+"/")
    '''
    
    for filename_html in os.listdir(directname_generated_whole_html):
        filename = filename_html.replace(".html","")
        os.system("mv "+directname_originalclang+"/"+filename+" "+directname_originalclang_finished+"/")
if __name__ == "__main__":
    main()


import os

def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    #Detect all forms of binod like BiNod    
    if "binod" in fileContent.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    #Listing the contents of this folder
    dir_contents = os.listdir()

    nBinod = 0 
    # For each text file, run isBinod for them
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item) 
            if(flag):
                print(f"******Binod found in {item}")
        else:
            print(f"Binod not found in {item}")

    print("*******Binod Detector Summary******")
    print(f"{nBinod} files found with Binod hidden into them")                                
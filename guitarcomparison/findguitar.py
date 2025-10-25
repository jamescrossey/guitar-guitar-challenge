import sys,urllib.request,json

def findGuitar(guitarName):
    print("function running")
    with urllib.request.urlopen("https://www.guitarguitar.co.uk/hackathon/products/") as url:
        guitars = json.loads(url.read().decode())
        
    idlist = []
    
    for guitar in guitars:
        if (guitarName.lower() in guitar["ItemName"].lower()):
            print(guitar["ItemName"])
            idlist.append(guitar["SKU_ID"])
    
    return idlist

if __name__ == "__main__":
      if len(sys.argv) != 2:
        print("this for finding guitars fool")
        sys.exit(1)
 
guitarName = (sys.argv[1])
 
findGuitar(guitarName)



import sys,urllib.request,json,os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','guitarcomparison.settings')

django.setup()

from guitarguitar.models import Guitars

def findGuitar(guitarName):
    print("function running")
    with urllib.request.urlopen("https://www.guitarguitar.co.uk/hackathon/products/") as url:
        guitars = json.loads(url.read().decode())
        
    idlist = []
    
    for guitar in guitars:
        if (guitarName.lower() in guitar["ItemName"].lower()):
            print(guitar["ItemName"])
            nguitar = Guitars.objects.create(sku=guitar["SKU_ID"], SalesPrice=guitar["SalesPrice"], colour=guitar["Colour"], pickup = guitar["Pickup"], BodyShape =guitar["BodyShape"], CreatedOn="2000-01-12", imageUrls=guitar["PictureMain"], rating=guitar["Rating"])
            idlist.append(guitar["SKU_ID"])

    if(not idlist):
        print("Ain't no guitar like that")
    
    return idlist

if __name__ == "__main__":
      if len(sys.argv) != 2:
        print("this for finding guitars fool")
        sys.exit(1)
 
guitarName = (sys.argv[1])
 
findGuitar(guitarName)



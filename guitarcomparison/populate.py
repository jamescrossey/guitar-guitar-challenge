import sys,urllib.request,json,os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','guitarcomparison.settings')

django.setup()

from guitarguitar.models import Guitars, matches

def populateGuitars():
    print("function running")
    
    genre_list =["pop", "rock", "metal", "jazz", "blues", "classical", "punk", "country", "folk", "indie", "funk", "reggae", "grunge", "alternative", "shoegaze"]
    genre_to_guitars = {
    "pop": ["acoustic", "telecaster"],
    "rock": ["stratocaster", "les paul", "sg"],
    "metal": ["les paul", "flying v", "explorer"],
    "jazz": ["classical", "casino", "semi-acoustic"],
    "blues": ["acoustic"],
    "classical": ["classical", "acoustic"],
    "punk": ["les paul", "stratocaster"],
    "folk": ["semi-acoustic", "acoustic", "stratocaster"],
    "grunge": ["les paul", "SG", "mustang", "jaguar"],
    "indie": ["telecaster", "mustang"],
    "funk": ["stratocaster"],
    "shoegaze": ["jazzmaster"],
    "reggae": ["acoustic","stratocaster"],
    "country": ["acoustic", "telecaster", "stratocaster"],
    "alternative": ["jaguar", "semi-acoustic", "telecaster"]
    }

    
    typelist = ["stratocaster","telecaster","les paul","SG","mustang","flying v","jaguar","jazzmaster","explorer","acoustic","classical","casino","semi-acoustic"]
    for g in genre_list:
        for t in genre_to_guitars[g]:
            matches.objects.create(type=t, genre=g)
    
    with urllib.request.urlopen("https://www.guitarguitar.co.uk/hackathon/products/") as url:
        guitars = json.loads(url.read().decode())
        
    idlist = []
    typelist = ["stratocaster","telecaster","les paul","SG","mustang","flying v","jaguar","jazzmaster","explorer","acoustic","classical","casino","semi-acoustic"]
    for guitarName in typelist:
        for guitar in guitars:
            if (guitarName.lower() in guitar["ItemName"].lower() and guitar["SKU_ID"] not in idlist):
                print(guitar["ItemName"])
                nguitar = Guitars.objects.create(sku=guitar["SKU_ID"], asn = guitar["ASN"], Category = guitar["Category"], online = str(guitar["Online"]), itemName = guitar["ItemName"], title = guitar["Title"], brandName = guitar["BrandName"], productDetail = guitar["ProductDetail"], SalesPrice=guitar["SalesPrice"], colour=guitar["Colour"], pickup = guitar["Pickup"], BodyShape =guitar["BodyShape"], CreatedOn="2000-01-12", pictureMain=guitar["PictureMain"], rating=guitar["Rating"],guitarType = guitarName)
                idlist.append(guitar["SKU_ID"])

    if(not idlist):
        print("Ain't no guitar like that")
    
    return idlist

if __name__ == "__main__":
      if len(sys.argv) != 1:
        print("this for populating guitars fool")
        sys.exit(1)
 
 
populateGuitars()



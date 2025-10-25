import sys,urllib.request,json,os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','guitarcomparison.settings')

django.setup()

from guitarguitar.models import Guitars

def populateGuitars():
    print("function running")
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



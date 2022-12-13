import random
import re
from text_unidecode import unidecode
from slugify import slugify

# 3.-kod  aleyatwa alfabetik san repetisyon
alfa1="abcdefghijklmnopqrstuvwxyz"

aleyatwa1 = lambda alfa,nomb : "".join(random.sample(alfa,nomb))


kod1=aleyatwa1(alfa1,10)
print(kod1)
print(len(kod1))


# 4.-kod aleyatwa alfanimerik san repetisyon

alfa2="abcdefghijklmnopqrstuvwxyz1234567890"

aleyatwa2=lambda alfa,nomb: "".join(random.sample(alfa,nomb))


kod2=aleyatwa2(alfa2,36)
print(kod2)
print(len(kod2))

# 5.-jenere yon SLUG 

alfa3="yon --c'henn pou fé\\slug"

slug= lambda alfa: slugify(alfa)

print(slug(alfa3))

# 6.- separe chak let pa yon vigil
mesaj1="metevigigilyoaprelet"

met_vigil=lambda mesaj: ",".join([elt for elt in mesaj])

print(met_vigil(mesaj1))

# 7.- kripte yon mo ak vale index li nan alfabe a

mesaj2= "ALO"

crypt=lambda mesaj: "-".join([str(ord(elt)-97) for elt in mesaj.lower()])

print(crypt(mesaj2))

# 8.- dekripte yon kod avek valel nan alfabe a

mesaj3="0-11-14"

decrypt=lambda mesaj: "".join(chr(int(elt)+97) for elt in re.findall(r'\d+',mesaj))

print(decrypt(mesaj3))

# 9.- pemite de(2)varyab

pemite1="Bonjou"
pemite2="Klas"

def permute(var1,var2):
    var1,var2=var2,var1
    tup = (var1,var2)
    return tup
    # print(f"Pemite1 = {var1}\nPemite2 = {var2}")

print(permute(pemite1,pemite2))


# 10.-FOnksyon pou inisyal

nom="JEAN-BAPTISTE JEAN"

inisyal=lambda nom: "".join([n[0] for n in nom.replace("-"," ").split()])

print(inisyal(nom)) 
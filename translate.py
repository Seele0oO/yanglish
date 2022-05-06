from pygtrans import Translate
# import translators as ts
client = Translate()
text = client.translate("hello",target="es",source='en',fmt='text')
print(text)
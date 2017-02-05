# -*- coding: utf-8 -*-
"""

@author: Nicolas Rivet
"""

import requests
from lxml import etree as ET

api_url='http://ws.seloger.com'

def search_buy(cp, nb_pieces=0, nb_chambres=0, pxmin=0, pxmax=0, surfacemin=0):
    """
    r=search_buy(75001, '4,+5', '3,4', 500000, 800000,70)
    xml=r.content
    """
    api_endpoint=api_url + '/search.xml?idtt=2&cp=' + str(cp)
    if nb_pieces!=0:
        api_endpoint=api_endpoint + '&np_pieces=' + str(nb_pieces)
    if nb_chambres!=0:
        api_endpoint=api_endpoint + '&nb_chambres=' + str(nb_chambres)
    if pxmin!=0:
        api_endpoint=api_endpoint + '&pxmin=' + str(pxmin)
    if pxmax!=0:
        api_endpoint=api_endpoint + '&pxmax=' + str(pxmax)
    if surfacemin!=0:
        api_endpoint=api_endpoint + '&surfacemin!=' + str(surfacemin)
        
    print(api_endpoint)
     
    response = requests.get(api_endpoint)
    return response

    
    
def look_search(xml):
    
    tree = ET.fromstring(xml)
    idAnnonces=tree.xpath('//recherche//annonces//annonce//idAnnonce')
    annonces=[]
    for annonce in idAnnonces:
        annonces.append(annonce.text)
    return annonces
    
"""
POST https://outlook.office.com/api/v2.0/me/sendmail

{
  "Message": {
    "Subject": "Meet for lunch?",
    "Body": {
      "ContentType": "Text",
      "Content": "The new cafeteria is open."
    },
    "ToRecipients": [
      {
        "EmailAddress": {
          "Address": "garthf@a830edad9050849NDA1.onmicrosoft.com"
        }
      }
    ],
    "Attachments": [
      {
        "@odata.type": "#Microsoft.OutlookServices.FileAttachment",
        "Name": "menu.txt",
        "ContentBytes": "bWFjIGFuZCBjaGVlc2UgdG9kYXk="
      }
    ]
  },
  "SaveToSentItems": "false"
}
"""

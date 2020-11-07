import pandas as pd
from pandas import ExcelWriter
import os.path

def export(names,comments,images,url):
    url=str(url).replace("https://www.instagram.com/p/","")
    url = url.replace("/","")
    name_file = f"{url}.xlsx"
    fname =name_file
    temp = {}
    temp_names = []
    temp_comments=[]
    temp_image=[]
    if os.path.isfile(fname):
        saved = pd.read_excel(fname)
        temp_names.extend(saved['name'])
        temp_comments.extend(saved['comment'])
        temp_image.extend(saved['image'])
    temp_names.extend(names)
    temp_comments.extend(comments)
    temp_image.extend(images)
    # temp.update({'name': temp_names, 'comment': temp_comments,'Label':temp_label})
    temp.update({'name': temp_names,'comment':temp_comments,'image':temp_image})
    df = pd.DataFrame(temp)
    writer = ExcelWriter(fname,options={'strings_to_urls': False})
    df.to_excel(writer, 'Arif Kurniawan', index=False)
    writer.save()
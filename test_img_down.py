
from google_images_download import google_images_download  
import pandas as pd
from pandas import DataFrame


import chardet
with open('D://AIM//translated_final.csv', 'rb') as f:
    result = chardet.detect(f.read()) 


# pd.read_csv('filename.csv', encoding=result['encoding'])


df=pd.read_csv('D://AIM//translated_final.csv',header=None, encoding=result['encoding'])

df.columns=['index','prodName']


row_list =[] 
 
# Iterate over each row 
for index, rows in df.iterrows(): 
   # Create list for the current row 
   my_list =rows.prodName
   
   # append the list to the final list 
   row_list.append(my_list) 
 
# Print the list 
print(row_list)

# creating object 
response = google_images_download.googleimagesdownload()  


def downloadimages(search_queries): 
  # keywords is the search query 
  # format is the image file format 
  # limit is the number of images to be downloaded 
  # print urs is to print the image file url 
  # size is the image size which can 
  # be specified manually ("large, medium, icon") 
  # aspect ratio denotes the height width ratio 
  # of images to download. ("tall, square, wide, panoramic") # Add copyright attribute
  arguments = {"keywords": query, 
               "format": "jpg", 
               "limit":4, 
               "print_urls":True, 
               "size": "medium",
                "usage_rights" : "labeled-for-reuse"
               }      
  try: 
      response.download(arguments) 
    
  # Handling File NotFound Error     
  except FileNotFoundError:  
      arguments = {"keywords": query, 
                   "format": "jpg", 
                   "limit":4, 
                   "print_urls":True,  
                   "size": "medium"} 
                     
      # Providing arguments for the searched query 
      try: 
          # Downloading the photos based 
          # on the given arguments 
          response.download(arguments)  
      except: 
          pass

# Driver Code 
for query in row_list[0:3]: 
  downloadimages(query)  
  print()  


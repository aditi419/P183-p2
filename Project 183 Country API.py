from tkinter import *
import requests 
import json 

root=Tk()


root.geometry("350x350")
root.configure(background="light slate blue")
#Setting labels
city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="light slate blue", fg="white")
city_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.24,rely=0.25,anchor=CENTER)

country_name = Label(root,text="Country:", bg="light slate blue",fg="White", font=("Helvetica",10,"bold"))
country_name.place(relx=0.06,rely=0.45,anchor=W) 

region = Label(root,text="Region:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold")) 
region.place(relx=0.06,rely=0.55,anchor=W) 

language = Label(root,text="Language:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold")) 
language.place(relx=0.06,rely=0.65,anchor=W) 

population= Label(root,text="Population:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold")) 
population.place(relx=0.06,rely=0.75,anchor=W) 

area = Label(root,text="Area:",bg="light slate blue", fg="white", font=("Helvetica",10,"bold")) 
area.place(relx=0.06,rely=0.85,anchor=W) 
    
#main function
def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    country = api_output_json[0]['name']
    reg = api_output_json[0]['region']
    lang = api_output_json[0]['languages']
    popn = api_output_json[0]['population']
    country_area = api_output_json[0]['area']
    
    country_name['text'] = 'Country:' + country
    region['text'] = 'Region:' + reg
    language['text'] = 'Language:' + str(lang)
    population['text'] = 'Population:' + popn
    area['text'] = 'Area:' + country_area
    
    
search_btn=Button(root, text="City Details", command=city_details , relief=FLAT,bg="Yellow")  
search_btn.place(relx=0.16,rely=0.35,anchor=CENTER)
root.mainloop()

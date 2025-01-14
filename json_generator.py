import json

dict = {
  1:{
    "name" : "Iron Man",
    "year" : 2008,
    "cast" : ["Robert Donwney Jr.", "Gwyneth Paltrow", "Terrence Howard"],
    "genre" : "Action",
    "director" : "Jon Favreau"
  },
  2:{
    "name" : "Iron Man 2",
    "year" : 2010,
    "cast" : ["Robert Donwney Jr.", "Mickey Rourke", "Gwyneth Paltrow"],
    "genre" : "Action",
    "director" : "Jon Favreau"
  },
  3:{
    "name" : "Iron Man 3",
    "year" : 2013,
    "cast" : ["Robert Donwney Jr.", "Guy Pearce", "Gwyneth Paltrow"],
    "genre" : "Action",
    "director" : "Shane Black"
  },
  4:{
    "name" : "Thor",
    "year" : 2011,
    "cast" : ["Chris Hemsworth", "Anthony Hopkins", "Natalie Portman"],
    "genre" : "Action",
    "director" : "Kenneth Branagh"
  },
  5:{
    "name" : "Thor: The Dark World",
    "year" : 2013,
    "cast" : ["Chris Hemsworth", "Tom Hiddleston", "Natalie Portman"],
    "genre" : "Action",
    "director" : "Alan Taylor"
  }
}

json_object = json.dumps(dict, indent=4)

with open("data.json", "w") as outfile:
    outfile.write(json_object)




DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
 

def run():

 #python proficient worker filter whith list comprehesion
     all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
     print("\nPython proficient worker filter \n")
     for worker in all_python_devs:
         print(worker)

 # filter with list comprehension of the platzi workers
     all_platzi_worker = [worker ['name'] for worker in DATA if worker['organization'] == 'Platzi']
     print("\nPlatzi workers filter  \n")
     for worker in all_platzi_worker:
         print(worker)

# #filter with heigh order function and lambda of adult
   
     print("\nAdults workers\n")
     adults = list(filter(lambda worker: worker['age'] > 17,DATA))
     adults= list(map(lambda worker: worker ['name'],adults ))
     adults = "\n".join(adults)
     print(adults)

 #add new key in dictionary
     print("\nNew key in dictionary\n")

     old_people= list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA  ))
     for worker in old_people:
         print(worker)

if __name__ == '__main__':
   run()
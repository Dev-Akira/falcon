import os
print(os.listdir())
for dire in os.listdir()[1:]:
    try:  
        os.system('cd '+dire)
        os.system('git init')
        os.system('git remote remove')
        os.system('git remote add origin https://github.com/Hunter-janis/'+dire+'.git')
        os.system('git add .')
        os.system('git commit -a -m "first"')
        os.system('git push -u origin master')
        os.system('cd ..')
    except Exception as E:
        print(E)
"""os.remove('.git')
os.system('git init')
os.system('git remote add origin https://github.com/Hunter-janis/unofficial-duolingo-stories.git')
os.system('git add .')
os.system('git commit -a -m "first"')
os.system('git push -u origin master')"""

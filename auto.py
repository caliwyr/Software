import os , random

for i in range(3000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 300)
    with open('Software.txt','a') as file:
        file.write(d+'\n')
    os.system('git add Software.txt')
    os.system('git commit --amend --date=" 2022-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')
os.system('python auto.py')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master

import requests
def menu():
    print('1. Server registreren')
    print('2. Vagrant box beheer')
    print('3. Remote execution van commandos / scripts op servers')
    print('4. Monitoring van de remote hosts ')
    print('5. Enkele predefined architecturen opzetten in vagrant')
    print('6. Script verlaten')

    optie=int(input('Kies wat je wilt doen'))
    if optie == 1:
        getServer()
    elif optie == 2:
        getVagrant()
    elif optie == 3:
        getRemote()
    elif optie == 4:
        getMonitoring()
    elif optie == 5:
        getPredefVagrant()
    elif optie == 6: sys.exit()
    else:
        print('Geef het juiste nr\n')
def getServer():
    print('1. IP en naam toekennen ')
    optie = string(input('Kies "a" om door te gaan of tik m om terug naar het hoofdmenu te keren'))
    if optie == "a":
        serverRegistreren()
    elif optie =="m":
        menu()
    else:
        print('Geef het juiste nr\n')
        getServer()
def getVagrant():
    print('a. Vagrant files interactief maken')
    print('b. Beheren van vagrant boxen')
    optie =int(input('Kies "a" of "b" om door te gaan of tik m om terug naar het hoofdmenu te keren'))
    if optie == 'a':
        vagrantfileMaken()
    elif optie == 'b':
        vagrantBeheren()
    elif optie =='m':
        menu()
    else:
        print('Geef het juiste nr\n')
        getVagrant()
def getRemote():
    print('a. Open een connectie naar bestaande server en geeft commandos door via bv Netmiko')
    print('b. Script naar keuze uitvoeren op remote server -pad opgeven-')
    optie =int(input('Kies "a" of "b" om door te gaan of tik m om terug naar het hoofdmenu te keren'))
    if optie == 'a':
        connectieServer()
    elif optie == 'b':
        eigenScript()
    elif optie =='m':
        menu()
    else:
        print('Geef het juiste nr\n')
        getRemote()
def getMonitoring():
    print('a. Disk usage van remote host')
    print('b. CPU usage van remote host')
    print('c. RAM usage van remote host')
    print('d. Actieve processen van remote host')
    optie =int(input('Kies "a" , "b" , "C" of "d" om door te gaan of tik m om terug naar het hoofdmenu te keren'))
    if optie == 'a':
        diskUsage()
    elif optie == 'b':
        cpuUsage()
    elif optie == 'c':
        ramUsage()
    elif optie == 'd':
        activeProces()
    elif optie =='m':
        menu()
    else:
        print('Geef het juiste nr\n')
        getMonitoring()
def getPredefVagrant():
    print('a. Predefined LAMP installatie LINUX')
    print('b. Predefined Windows met installatie van Chrome en git')
    optie =int(input('Kies "a" of "b" om door te gaan of tik m om terug naar het hoofdmenu te keren'))
    if optie == 'a':
        LAMP()
    elif optie == 'b':
        Windows()
    elif optie =='m':
        menu()
    else:
        print('Geef het juiste nr\n')
        getPredefVagrant()
#functies
menu()


def cls(): print '\n'*45
def linedesign(): print '@'*50
def menu():
        linedesign()
        print """Deployment options
        1. Show deployed Apps
        2. Install App
        3. Uninstall App
        4. Exit
        """
        linedesign()
        ch=input("Please enter your choice: ")
        return ch
 
def main():
        """ Main program logic starts here """
        while 1:
                ch=menu()
                if ch == 1:
                        cls(); linedesign()
                        print "The list of application deployed on the Cell"
                        print AdminApp.list()
                        linedesign()
                elif ch == 2:
                        print "You selected to deploy application"
                        appPath=raw_input("Enter application path: ")
                        appName=raw_input("Enter application name: ")
                        AdminApp.install( appPath,  ['-appname',appName , '-MapWebModToVH', [['.*', '.*', 'default_host']]])
                        AdminConfig.save()
                elif ch == 3:
                        linedesign()
                        print "Uninstall which application?"; appName=raw_input("Application name: ")
                        AdminApp.uninstall(appName)
                        AdminConfig.save()
                        print "Uninstallation completed...."
                else:
                        print "Exiting from the script...."
                        #sys.exit(0)
                        break
 
main()
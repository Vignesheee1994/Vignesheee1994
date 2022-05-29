a1=input("Enter 1 for app uninstall ---- 2 for app install:  ");
print("Installed applications:")
print(AdminApp.list().splitlines())


if a1==1: 
    nameapp=input("Enter the Application name with single quotes: ");   
    print(nameapp);
    AdminApp.uninstall(nameapp)
    if(nameapp not in AdminApp.list().splitlines()):
        AdminConfig.save()
        print("Application Unistalled successfully")
    else:
        print("App is not uninstalled try in mannual method")
elif a1==2:
    nameapp=input("Enter the Application name: ");
    deploy_app="/opt/IBM/WebSphere/AppServer/installableApps/"+nameapp;
    AdminApp.install(deploy_app, '[-cluster cluster1 -server webtest1]')
    AdminConfig.save()
    print(nameapp, "installed successfully")
else:
    print("Enter the correct value")


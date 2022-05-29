def serverState(serverName):
 serverObj = AdminControl.completeObjectName('WebSphere:type=Server,name=' + serverName + ',*')
 if len(serverObj) > 0:
  serverStatus = AdminControl.getAttribute(serverObj, 'state')
 else:
  serverStatus = 'STOPPED'
 print "%15s %s" %(serverName, serverStatus)
serverState('server1')
serverState('webserver1')
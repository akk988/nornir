# 1 - Initialise a Nornir Object.
r = InitNornir(config_file='config.yaml')
  nr = InitNornir(config_file='config.yaml', core={'num_workers': 1})		# Useful for testing as it works in serial, doesn't paralellise connections.

# 2 - Filtering Objects - Can be cumulative.
  routers = nr.filter(dev_type='Router').inventory.hosts.keys()
  switches = nr.filter(dev_type='Switch').inventory.hosts.keys()
	r1 = nr.filter(hostname='r1')
	r2 = nr.filter(hostname='r1')	
	
	device = nr.filter(dev_type='Router').filter(hostname='r2')		# Cumulative example

#3 - Run tasks against inventory devices (Previously filtered or not).
  confs = device.r1(task=render_configs)			# Against the filtered var called r1.
  confs = device.run(task=render_configs)			# Against the filtered var called device.
  confs = nr.run(task=render_configs)				# All the devices in the nr.object

#4 - Printing results.
  from nornir.plugins.functions.text import print_title, print_result

  print_result(confs)

#5 - Accessing variables
  nr.inventory.hosts['r2'].username 
  nr.inventory.hosts['r2'].password
  nr.inventory.hosts['r2'].port

  task.host.hostname
  task.host.username
  task.host.password
  task.host.port
  task.host.connection_options

# inventory variables
  inv_hosts = nr.inventory.hosts
  inv_hosts_items = nr.inventory.hosts.items()
  inv_hosts_values = nr.inventory.hosts.values()

  # Inventory groups
inv_groups = nr.inventory.groups
  inv_groups_itmes = nr.inventory.groups.items()
  inv_groups_values = nr.inventory.groups.values()
  nr.inventory.defaults.data.keys()   
  dict_keys(['domain:', 'username:', 'password:', 'port:', 'platform:', 'extras:', 'init_conf', 'local_acc', 'lin_con', 'lin_vty'])



#6 - Inspecting the inventory

  nr.inventory.get_inventory_dict()
  nr.inventory.get_hosts_dict()
  nr.inventory.get_groups_dict()
  nr.inventory.get_defaults_dict()

#7 - Inspecting the AggregatedResult object.

ipdb> confs 
AggregatedResult (render_configs): {'dsw-1': MultiResult: [Result: "render_configs", Result: "Base Template Configuration"], 'dsw-2': MultiResult: [Result: "render_configs", Result: "Base Template Configuration"], 'asw-1': MultiResult: [Result: "render_configs", Result: "Base Template Configuration"], 'asw-2': MultiResult: [Result: "render_configs", Result: "Base Template Configuration"]}


ipdb> confs.items()                                                                                                                      
dict_items([('dsw-1', MultiResult: [Result: "render_configs", Result: "Base Template Configuration"]), ('dsw-2', MultiResult: [Result: "render_configs", Result: "Base Template Configuration"]), ('asw-1', MultiResult: [Result: "render_configs", Result: "Base Template Configuration"]), ('asw-2', MultiResult: [Result: "render_configs", Result: "Base Template Configuration"])])


ipdb> asw1 = confs['asw-1']                                                                                                              
ipdb> asw1                                                                                                                               
MultiResult: [Result: "render_configs", Result: "Base Template Configuration"]


ipdb> asw1[0]                                                                                                                            
Result: "render_configs"
ipdb> asw1[1]                                                                                                                            
Result: "Base Template Configuration"
False


ipdb> asw1_result = asw1[1] 


ipdb> asw1_result.diff                                                                                                                   
''

ipdb> asw1_result.exception                                                                                                              
ipdb> asw1_result.failed                                                                                                                 
False

ipdb> asw1_result.host                                                                                                                   
Host: asw-1

ipdb> asw1_result.name                                                                                                                   
'Base Template Configuration'

ipdb> asw1_result.severity_level                                                                                                         
20

ipdb> asw1_result.stderr                                                                                                                 
ipdb> asw1_result.stdout                                                                                                                 


ipdb> print(f'Hostname:{asw1_result.host} || Changed: {asw1_result.changed}')                                                            
Hostname:asw-1 || Changed: False

ipdb> asw1_result.result                                                                                                                 
'! ######################## Initial-config.j2 ###########################\nhostname asw-1\nenable secret ccnplab\nno ip domain-lookup\nservice password-encryption\n\n! ######################## AAA CONF ####################################\naaa new-model\naaa authentication login default local\naaa authorization exe ....

#

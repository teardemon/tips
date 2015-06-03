#icehouse
Delete compute node
Remove from neutron
1 - list compute nodes to be removed
$ neutron agent-list |grep -e <hv1> -e <hv2> -e <hv3> -e <hv4> -e <hv5>
11ae2faf-cc8d-4a29-99d6-af59fa7427fc | Open vSwitch agent | <hv5> | xxx | True | neutron-openvswitch-agent |
44aa0b9e-01d7-45e8-8374-f4baeb0638a6 | Open vSwitch agent | <hv3> | xxx | True | neutron-openvswitch-agent |
8a307cab-08bd-4f90-bfed-442cfcec14ec | Open vSwitch agent | <hv2> | xxx | True | neutron-openvswitch-agent |
95a6cbb5-b402-4b99-b8e7-bb3d9f37fcb1 | Open vSwitch agent | <hv4> | xxx | True | neutron-openvswitch-agent |
a7d61ba3-22d3-4fe6-9e9e-65e9c9e91773 | Open vSwitch agent | <hv1> | xxx | True | neutron-openvswitch-agent |

2 - remove from neutron
$ neutron agent-delete 11ae2faf-cc8d-4a29-99d6-af59fa7427fc
Deleted agent: 11ae2faf-cc8d-4a29-99d6-af59fa7427fc

$ neutron agent-delete 44aa0b9e-01d7-45e8-8374-f4baeb0638a6
Deleted agent: 44aa0b9e-01d7-45e8-8374-f4baeb0638a6

$ neutron agent-delete 8a307cab-08bd-4f90-bfed-442cfcec14ec
Deleted agent: 8a307cab-08bd-4f90-bfed-442cfcec14ec

$ neutron agent-delete 95a6cbb5-b402-4b99-b8e7-bb3d9f37fcb1
Deleted agent: 95a6cbb5-b402-4b99-b8e7-bb3d9f37fcb1

$ neutron agent-delete a7d61ba3-22d3-4fe6-9e9e-65e9c9e91773
Deleted agent: a7d61ba3-22d3-4fe6-9e9e-65e9c9e91773
Remove from nova
1 - list aggregates for each compute

$ for aggr in `nova aggregate-list |grep '[0-9]' |awk '{print $2}'`
do
        nova aggregate-details $aggr |grep <hv> |awk '{print "id: "$2 " name: " $4}'
done
2 - remove hv from aggregates

$  nova aggregate-remove-host <aggregate id> <hv>
Host <hv> has been successfully removed from aggregate <aggregate id>
repeat for each hv and aggregate

3 - get a token

$ TOKEN=`keystone token-get |grep '   id' |awk '{print $4}'`
$ export TOKEN
4 - pretend to remove service, check output

$ for srv in `nova service-list | grep -e <hv1> -e <hv2> -e <hv3> |awk '{print $2}'` ;
do echo curl -i -H "Content-Type: application/json" -X DELETE http://58.215.181.7:8774/v2/4869754a3f75444dbdac5e5b7bb48bb0/os-services/$srv -H "User-Agent: python-keystoneclient" -H "X- Auth-Token: $TOKEN" ;
done
5 - now for real, remove the service/<hv>

$ for srv in `nova service-list | grep -e  <hv1> -e <hv2> -e <hv3>  |awk '{print $2}'` ;
do
curl -i -H "Content-Type: application/json" -X DELETE http://58.215.181.7:8774/v2/4869754a3f75444dbdac5e5b7bb48bb0/os-services/$srv -H "User-Agent: python-keystoneclient -H "X- Auth-Token: $TOKEN" ;
done
NOTES:
url and tenant id show here are for regionOne deploy, change if need.
always remove the hv from the aggregate before service, otherwise you won’t be able to remove the hv from the aggregate later.

1st, get the token from keystone:

(Use a tenant for which you have admin privileges.)

curl -d '{"auth":{"passwordCredentials":{"username": "admin","password": "42"},"tenantName": "myTenant"}}'  -H "Content-Type: application/json" http://openstack:5000/v2.0/tokens
2nd, identify the id of the compute service you want to remove

(do this one way, or the other. Here's what worked for us -- using novaclient python module)

import novaclient.v1_1.client as nvclient
nova = nvclient.Client(**creds)
services = nova.services.list()
for service in services:
   if service.host == "node-to-remove": print service.id
3rd, get the tenant-id (you will need it later)

keystone tenant-list | grep myTenant
4th, use token, tenant-id, and the service-id to gracefully remove service from nova

curl -i -H "Content-Type: application/json" -X DELETE http://openstack:8774/v2/{tenant-id}/os-services/{service-id} -H "User-Agent: python-keystoneclient" -H "X-Auth-Token: {token}"
You're done.

If everything worked fine, you should no longer see your nova-compute service in the output of the

nova service-list
nor in the hypervisor list in the dashboard.

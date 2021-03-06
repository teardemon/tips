#!/bin/bash
IPTABLES="/sbin/iptables"

$IPTABLES -P INPUT ACCEPT
$IPTABLES -P FORWARD ACCEPT
$IPTABLES -P OUTPUT ACCEPT

$IPTABLES -t nat -P PREROUTING ACCEPT
$IPTABLES -t nat -P POSTROUTING ACCEPT
$IPTABLES -t nat -P OUTPUT ACCEPT

$IPTABLES -t mangle -P PREROUTING ACCEPT
$IPTABLES -t mangle -P OUTPUT ACCEPT


# flush all the rules in the filter and nat tables.
$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -t mangle -F

# erase all chains that's not default in filter and nat table.
$IPTABLES -X
$IPTABLES -t nat -X
$IPTABLES -t mangle -X

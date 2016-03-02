#!/bin/bash
BACKUP_BASE="/backup/"
CURRENT_DATE=$(date +%F)
BACKUP_NAME="zabbix"_${CURRENT_DATE}."sql.gz"
USER=USER
PASSWD=PASSWD
mysqldump --single-transaction -u{USER} -p${PASSWD} zabbix acknowledges actions alerts application_template applications auditlog auditlog_details autoreg_host conditions config dbversion dchecks dhosts drules dservices escalations events expressions functions globalmacro globalvars graph_discovery graph_theme graphs graphs_items group_discovery group_prototype groups host_discovery host_inventory hostmacro hosts hosts_groups hosts_templates housekeeper httpstep httpstepitem httptest httptestitem icon_map icon_mapping ids images interface interface_discovery item_condition item_discovery items items_applications maintenances maintenances_groups maintenances_hosts maintenances_windows mappings media media_type opcommand opcommand_grp opcommand_hst opconditions operations opgroup opmessage opmessage_grp opmessage_usr optemplate profiles proxy_autoreg_host proxy_dhistory proxy_history regexps rights screens screens_items scripts service_alarms services services_links services_times sessions slides slideshows sysmap_element_url sysmap_url sysmaps sysmaps_elements sysmaps_link_triggers sysmaps_links timeperiods trigger_depends trigger_discovery triggers user_history users users_groups usrgrp valuemaps |gzip >${BACKUP_BASE}${BACKUP_NAME}

if [ $?==0 ]
then
    echo ${CURRENT_DATE}' new_zabbix backup success'|logger -t BACKUP_ZABBIX
else
    echo ${CURRENT_DATE}' new_zabbix bakup failed'|logger -t BACKUP_ZABBIX
fi

find ${BACKUP_BASE} -name "zabbix_*.sql.gz" -type f -mtime +10 -exec rm {} \; > /dev/null 2>&1

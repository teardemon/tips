#Bind 9 配置
##配置cache-only DNS server(forward)
```bash
options {
        listen-on port 53 { any; };
        listen-on-v6 port 53 { any; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        recursion yes;
        forward only;
        allow-query        { any; };
        forwarders {
                8.8.8.8;
                //114.114.114.114;
        };
};
```


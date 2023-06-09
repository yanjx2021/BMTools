# Database Tool

Contributor: [Xuanhe Zhou](https://github.com/zhouxh19)

### API Functions

- *get_database_schema*: obtain the information of target tables 
- *select_database_data*: fetch the query results from a database instance
- *rewrite_sql*: transform a sql query into an semantic-equivalent but execution-efficient sql

### Dataset

- *./data/tpch10x/text2res_multi_table.json*: relativley complex database queries (2-6 tables)
- *./data/tpch10x/text2res_single_table.json*: basic database queries

### Setup

1. Follow the steps in [main readme](https://github.com/OpenBMB/BMTools/blob/main/README.md)

2. Rename config.ini.template into my_config.ini

3. Modify database settings in my_config.ini, e.g.,

```bash
    [{db_system}]
    host = 127.0.0.1
    port = 5432
    user = postgres
    password = postgres
    dbname = postgres
```

Note. {db_system} must match with that in ./api.py

4. Modify and run the test.py script to test the tool
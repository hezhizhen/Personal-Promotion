# Utilities

## 1. Backup and Restore

### 1.1 What is it

a **backup** is simply a full copy of your **database schema and data**, with restore being the ability to use that backed up data and load it into your DB or another DB

**backup & restore** is done on an entire `DB` or entire `table`, not meant for extracts of `data`

### 1.2 Backup

`pg_dump` is the utility for backing up your DB

some key knobs for dumping DB

* Plaintext format & binary format & tarball
    * plaintext: reabable, large
    * binary: unreadable, small
    * tarball: ideal for restore
* all of the DB or specific schemas/tables

1. list the databases

```bash
psql -l
```

2. carry out the dump with (create the plaintext dump of the DB)

```bash
pg_dump database_name > database.sql # plaintext
```

3. if you want to create a different form

```bash
pg_dump -Fc database_name > database.bak # compressed binary format
pg_dump -Ft database_name > database.tar # tarball
```

### 1.3 Restore 

some options to consider when restoring

* if the DB exists
* the format of the backup

1. if DB exists

```bash
pg_restore -Fc database.bak # compressed binary format
pg_restore -Ft database.tar # tarball
```

2. if create the DB new from the restore

```bash
pg_restore -Fc -C database.bak # compressed binary format
pg_restore -Ft -C database.tar # tarball
```

## 2. Copy

### 2.1 What is copy

some utilities for moving data around

* pg_dump: DB backups
* pg_restore: DB resotres
* copy: copy data into and out of tables in the DB; support some modes
    * binary
    * tab delimited 
    * csv delimited 

### 2.2 Copy in Action

1. extract all employees to a tab delimited file

```bash
\copy (SELECT * FROM employees) TO '~/employees.tsv';
```

2. extract all employees to a csv delimited file

```bash
\copy (SELECT * FROM employees) TO '~/employees.csv' WITH (FORMAT CSV);
```

3. extract all employees to a binary file

```bash
\copy (SELECT * FROM employees) TO '~/employees.dat' WITH (FORMAT "Binary");
```

4. load data into a table

```bash
\copy employees FROM '~/employees.tsv';
\copy employees FROM '~/employees.csv' WITH CSV;
\copy employees FROM '~/employees.dat' WITH BINARY;
```

## 3. Psql

### 3.1 What is psql

the interactive terminal for working with Postgres

thre are many flags available, some of the most important ones:

* `-h`: the host to connect to
* `-U`: the user to connect with 
* `-p`: the port to connect to (default: 5432)

```bash
psql -h localhost -U username databasename
psql "dbname=dbhere host=hosthere user=userhere password=pwhere port=5432 sslmode=require" # another option, use a full string and let psql parses it
```

once you have connected, you can begin querying immediately

in addition to **basic queries**, you can use **certain commands**

`\?`: give a list all available commands

### 3.2 Commonly used commands

* `\timing`: turn query timing on; show query timing in milliseconds (default: the timing of query results is not available)
* `\d`: list tables in DB
* `\d table_name`: describe a table whose table name is table_name
* `\d+`: list all tables in DB along with some additional information
* `\d+ table_name`: describe a table with additional information
* `\l`: list all DBs
* `\l+`: list all DBs with additional information
* `\dn`: list all schemas
* `\dn+`: list all schemas with additional information
* `\df`: list all functions
* `\df+`: list all functions with additional informaiton
* `\c dbname`: connect to another DB
* `\q`: quit from postgres shell
* `\e`: text editor inside psql
* the commands can be given a `regex` (e.g.: `\df *to_array*` list all functions that contain `to_array` in its name)

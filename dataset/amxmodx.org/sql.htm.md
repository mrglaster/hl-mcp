. Configuration: SQL
AMX Mod X features a universal set of natives to be used across all SQL connectors. This means you should only enable one SQL module, but it should work with all 0.20+ plugins.  
  
To begin, enable one of the SQL modules - mysql_amxx, pgsql_amxx, or mssql_amxx. See the [modules section](http://127.0.0.1:8000/modules/index.htm) for enabling modules.  
  
Next you need to edit your SQL configuration. Open addons\amxmodx\configs\sql.cfg with your favorite text editor. You will need to change the settings for the CVARs. See below is a table showing their definitions and purposes.   
  
Once you have configured this, enable the admin_sql plugin and disable the admin plugin (see [Plugins section](http://127.0.0.1:8000/plugins/index.htm) for enabling/disabling plugins).   
  
Next time your server changes map or restarts, the table will be created for you automatically.   
  
To add administrators via SQL, follow the same directions as in the "Adding Administrators" section, except the four fields are not written to users.ini, they are added to the four corresponding fields in the amx.admins table.   
  
CVAR | Default Setting | Purpose  
---|---|---  
amx_sql_host | "127.0.0.1" | IP address of SQL server.  
amx_sql_user | "root" | Username to connect to the SQL server.  
amx_sql_pass | "" | Password to connect to the SQL server.  
amx_sql_db | "amx" | Database to use on the SQL server.  
amx_sql_table | "admins" | The table to use for the admin_sql plugin.

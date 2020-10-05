----------------------------------------------------------------------------------------------
The scripts and everything else in this folder and any of its subfolders is created by 
Marwin Acker (marwin.ack@googlemail.com), HiWi of Gerald Jagusch.
If you have guestions about my script or need some help with your own script, contact me.
----------------------------------------------------------------------------------------------

These scripts are made so you can upload your files to items, add metadata to items and create 
items in the archive TUdatalib of the TU Darmstadt. Follow the instructions in the README.txt's
in the folders if existing and also in the config files.
Also you can use these to make your own scripts since basically everything in here can be used 
as example.

----------------------------------------------------------------------------------------------
The following scripts can be executed:
create_item.py
upload_files.py
upload_metadata.py

In general it is necessary to fill in the config files in the "configs" folder before executin
the scripts. 
for the script "create_item.py" fill in "config_IC.py"*
for the script "upload_files.py" fill in "config_FILES.py"
for the script "upload_metadata.py" fill in "config_META.py"
You can edit these with a regular text editor like vim or standart your notepad.

It will be checked if you filled in the information in the configs.
If you dont know how to get informations like the collection id (which is not easily accessible
if you are not an admin) you can go to the "helpers" folder. The scripts there can get you some
of the information needed.

(* you do not neccessarily have to fill in any metadata here, the script will ask for the name)
----------------------------------------------------------------------------------------------
IMPORTANT:
For execution use python3!
I still do not guarante that it will work, but it will with python3 rather than with python2!

Also do NOT delete any files even if they are empty! This will cause the scripts to not work
properly!
----------------------------------------------------------------------------------------------

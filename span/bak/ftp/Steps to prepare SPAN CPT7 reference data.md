Steps to prepare SPAN CPT7 reference data

Take the SPAN data in "Z:\RTK\data\2020\100\span" as an example

1. Look for folders contain *novatel_<local time>.bin*

2. for each *novatel_<local time>.bin* file in each folder, **download** the corresponding **hourly** WX02 base data in RTCM format from azure server (ask xuehai), 

   - ​	novatel_CPT7-2020_04_09_15_24_28.bin, starting from 15:00 hour and ending in 16:12 (get it from the file property)

   - get the WX02 RTCM data in hours 15:00 - 17:00， i.e. wx02100n.rtcm, wx02100o.rtcm, wx02100p.rtcm, 

   - use ./convbin.exe to convert *.rtcm files to *.obs files

     ```
     	./convbin.exe wx02100n.rtcm -r rtcm3
     ```

3. **download** GNSS RINEX ephemeris file from

   ```
   ftp://cddis.gsfc.nasa.gov/gnss/data/daily/2020/100/20p/BRDC00IGS_R_*_MN.rnx.gz
   ```

      and unzip




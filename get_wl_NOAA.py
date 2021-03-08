import noaa_coops as nc

#NOAA station: Chesapeake Channel, VA (CBBT, ID: 8638901)
#lon=-76.83,lat=37.03
ches = nc.Station(8638901)
df_water_levels=ches.get_data( begin_date="20210301",
    end_date="20210305", product="water_level",
    datum="MLLW", units="metric", time_zone="gmt")

print(df_water_levels.head())

This long-term repository contains three files:

1) Simplified GRWL Vector Product: GRWL_summaryStats_V01.01.zip

2) GRWL Mask (raster): GRWL_mask_V01.01.zip 

3) GRWL Vector Product: GRWL_vector_V01.01.zip

Other data:

\- Location map of the individual GRWL tiles: [Shapefile download](https://drive.google.com/file/d/1K6x1E0mmLc0k7er4NCIeaZsTfHi2wxxI/view?usp=sharing) 

\- River and stream surface area totals by drainage basin (Fig. 4 in Allen & Pavelsky, 2018): [Shapefile download](https://drive.google.com/open?id=11hzVVg6OEs1c7zIKjuy0u4WeE0UG6BsH)

 ## Simplified Vector Product 

**1) Documentation for the Global River Width from Landsat (GRWL) Simplified Vector Product V01.01**

This zip file contains a single ESRI shapefile polyline of river centerlines. 
Projection: Geographic WGS84 

This file is a simplified version of the raw GRWL vector product (see #3 below). This product is a smaller and more wieldy compared to the raw GRWL vector dataset and **most users of GRWL will prefer to use this simplified version**. This simplified vector product reduces the number of feature vertices and attributes by simplifying the polyline geometry and by calculating summary statistics along each polyline segment. Polyline segments are roughly the line segments between each tributary junction. 

For each polyline segment, the shapefile contains the following attributes:
\1.   width_min: the minimum of river width measurements along the segment at mean discharge (meters)

\2.   width_med: the median of river width measurements along the segment at mean discharge (meters)

\3.   width_mean: the mean of river width measurements along the segment at mean discharge (meters)

\4.   width_max: the maximum of river width measurements along the segment at mean discharge (meters)

\5.   `width_sd`: the **standard deviation** of river width measurements along the segment at mean discharge (meters)

\6.   lakeflag: integer specifying if segment is located on a river (lakeflag=0), lake/reservoir (lakeflag=1), tidal river (lakeflag=2), or canal (lakeflag=3). This information is of much higher quality in the Global River Width from Landsat (GRWL) Vector Product V01.01 (product #3 below). 

\8.   nSegPx: number of pixels within the segment (N pixels)

\9.   Shape_Leng: length of the segment (kilometers)

 ## Mask

**2) Documentation for the Global River Width from Landsat (GRWL) Mask V01.01**

This zip file contains 830 GeoTIFF tiles of water masks **at mean discharge**. The assembly of this database is described in Allen and Pavelsky (2018) “Global Extent of Rivers and Streams” published in Science. **The GRWL mask is an intermediate product in the production the GRWL vector product and thus is not explicitly validated. **

Tile coverage: 4 degrees latitude by 6 degrees longitude

File format: GeoTIFF (unsigned byte)

Projection: Geographic WGS84 

Resolution: 30 m

**Pixel classifications**: 
DN = 256 : No Data

DN = 255 : River

DN = 180 : Lake/reservoir 

DN = 126 : Tidal rivers/delta 

DN = 86 : Canal

DN = 0 : Land/water not connected to the GRWL river network

 ## Vector Product

**3) Documentation for the Global River Width from Landsat (GRWL) Vector Product V01.01**

This zip file contains 829 ESRI shapefile polylines of river centerlines. 
Tile coverage: 4 degrees latitude by 6 degrees longitude. 
Projection: Geographic WGS84
Resolution: 30 m

At each GRWL measurement location, the shapefile contains the following attributes:
\1.   utm_east: UTM Easting (UTM Zone is given in tile file name; meters)

\2.   utm_north: UTM Northing (UTM Zone is given in tile file name; meters)

\3.   width_m: wetted width of river (meters)
note: width_m == 1 indicates NA (no width data along the centerline) 

\4.   nchannels: braiding index (-)

\5.   segmentID: unique ID of river segment in each tile

\6.   segmentInd: Index of each observation in each segment. Not sorted by upstream or downstream

\7.   lakeflag: integer specifying if observation is located on a river (lakeflag=0), lake/reservoir (lakeflag=1), tidal river (lakeflag=2), or canal (lakeflag=3). 

\8.   lon: Longitude (decimal degrees)

\9.   lat: Latitude (decimal degrees)

\10.   elev: Elevation (meters) – sampled from the Hydro1k DEM
## [getwidth]

> 1、获取河道宽

| 参数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| thresh     | Searching window threshold in same units as input data set   |
| output     | Shapefile output file path                                   |
| recf       | Rec file path                                                |
| netf       | Target mask file path                                        |
| proj       | Output projection in **Proj4** format                        |
| fwidth     | Source width file path **GDAL** format                       |
| method     | [const_thresh或var_thresh]                                   |
| fbankfullq | Source *bankfullq* shapefile (Optional, to determine variable threshold) |

## [getbankelevs]

> 2、从高分辨DEM中获取河岸高程

| 参数     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| output   | Shapefile output file path                                   |
| recf     | Read rec file                                                |
| netf     | Target mask file path                                        |
| proj     | Output projection in Proj4 format                            |
| outlier  | Outlier detection yes/no                                     |
| method   | Reductions available **near**, **mean**, **min**, **meanmin** |
| hrnodata | NODATA value for high resolution DEM                         |
| thresh   | Saerching threshold in degrees                               |
| hrdemf   | High resolution DEM file                                     |

## [fixelevs]

> 3、修正河岸高程（两种方法可选，用于平滑）

| 参数   | 描述                                                     |
| ------ | -------------------------------------------------------- |
| output | Shapefile output file path                               |
| recf   | Rec file path                                            |
| netf   | Target mask file path                                    |
| proj   | Output projection in Proj4 format                        |
| method | `yamazaki`, `lowless`                                    |
| source | Shapefile input file to fix (e.g  from lfp-getbankelevs) |

## [rasterresample]

> 4、对洪泛区高程进行重采样。
>
> Resample a DEM by upscaling.

| 参数     | 描述                                |
| -------- | ----------------------------------- |
| nproc    | Number of cores to use              |
| outlier  | Outlier detection yes/no            |
| method   | Reduction method mean, min, meanmin |
| hrnodata | High resolution NODATA value        |
| thresh   | Searching windows threshold         |
| demf     | High resolution DEM                 |
| netf     | Target mask file path               |
| output   | Output file, GeoTIFF output         |

## [getdepth]

>  5、获取河深

| 参数   | 描述                                               |
| ------ | -------------------------------------------------- |
| recf   | Rec file path                                      |
| proj   | Output projection in Proj4 format                  |
| netf   | Target mask file path                              |
| method | `depth_raster`，`depth_geometry`，`depth_mannings` |
| output | Shapefile output file path                         |

### depth_raster

> Get depths from a raster of depths

**fdepth** = Depth raster source file **GDAL** format **projection EPSG:4326**

**thresh** = Serching threshold in degrees

### depth_geometry

> Get depths by using hydraulic geometry equation
>
> depth = r * width ^ p

**wdtf**  = Shapefile width **from lfp-getwidths**

**r** = Constant number

**p** = Constant number

### depth_mannings

> Get depths by using simplified mannings equation
>
>   ((bankfull_flow\*manning_coef)/(slope\*\*0.5\*width))\**(3/5)

**n**   = Manning's coefficient 

**wdtf**  = Shapefile width **from lfp-getwidths**

**slpf**  = Shapefile slope **from lfp-getslopes**

**qbnkf** = Shapefile q bank full

## [getbedelevs]

> 6、获取河床高程（用河岸减去水深）

| 参数   | 描述                               |
| ------ | ---------------------------------- |
| output | Shapefile output file path         |
| netf   | Target mask file path              |
| proj   | Output projection in Proj4 format  |
| bnkf   | Shapefile input bank (bank file)   |
| dptf   | Shapefile input depth (depth file) |

## buildmodel

> 7、生成运行LISFLOOD-FP模拟所需的文件


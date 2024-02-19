# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
out_ = LegacyVTKReader(registrationName='out_*', FileNames=['/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_0.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_1.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_2.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_3.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_4.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_5.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_6.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_7.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_8.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_9.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_10.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_11.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_12.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_13.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_14.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_15.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_16.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_17.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_18.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_19.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_20.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_21.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_22.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_23.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_24.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_25.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_26.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_27.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_28.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_29.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_30.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_31.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_32.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_33.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_34.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_35.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_36.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_37.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_38.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_39.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_40.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_41.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_42.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_43.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_44.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_45.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_46.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_47.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_48.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_49.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_50.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_51.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_52.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_53.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_54.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_55.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_56.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_57.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_58.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_59.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_60.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_61.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_62.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_63.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_64.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_65.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_66.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_67.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_68.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_69.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_70.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_71.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_72.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_73.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_74.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_75.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_76.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_77.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_78.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_79.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_80.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_81.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_82.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_83.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_84.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_85.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_86.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_87.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_88.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_89.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_90.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_91.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_92.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_93.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_94.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_95.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_96.vtk',
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_97.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_98.vtk', 
'/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/out_99.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

UpdatePipeline(time=0.0, proxy=out_)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=out_)
cellDatatoPointData1.ProcessAllArrays = 1
cellDatatoPointData1.CellDataArraytoprocess = ['Label', 'cvar', 'mu', 'phivar', 'pressure', 'rho', 'str', 'velocity']
cellDatatoPointData1.PassCellData = 0
cellDatatoPointData1.PieceInvariant = 0

UpdatePipeline(time=0.0, proxy=cellDatatoPointData1)

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'Label']
contour1.ComputeNormals = 1
contour1.ComputeGradients = 0
contour1.ComputeScalars = 1
contour1.OutputPointsPrecision = 'Same as input'
contour1.GenerateTriangles = 1
contour1.Isosurfaces = [1.0]
contour1.PointMergeMethod = 'Uniform Binning'

# init the 'Uniform Binning' selected for 'PointMergeMethod'
contour1.PointMergeMethod.Divisions = [50, 50, 50]
contour1.PointMergeMethod.Numberofpointsperbucket = 8

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'cvar']

UpdatePipeline(time=0.0, proxy=contour1)

# Properties modified on contour1
contour1.Isosurfaces = [0.0]

animationScene1.Play()

# create a new 'Generate Ids'
generateIds1 = GenerateIds(registrationName='GenerateIds1', Input=contour1)
generateIds1.GeneratePointIds = 1
generateIds1.PointIdsArrayName = 'PointIds'
generateIds1.GenerateCellIds = 1
generateIds1.CellIdsArrayName = 'CellIds'

UpdatePipeline(time=6.0, proxy=generateIds1)

# save data
SaveData('/home/tf/FreeFEM-NS-CH/drop_Pe30_Cn0.04/data/Pe30_Cn0.04.tsv', proxy=generateIds1, WriteTimeSteps=1,
    Filenamesuffix='_%d',
    ChooseArraysToWrite=1,
    PointDataArrays=['PointIds'],
    CellDataArrays=[],
    FieldDataArrays=[],
    VertexDataArrays=[],
    EdgeDataArrays=[],
    RowDataArrays=[],
    Precision=5,
    UseScientificNotation=0,
    FieldAssociation='Point Data',
    AddMetaData=1,
    AddTime=0)

# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
out_ = LegacyVTKReader(registrationName='out_*', FileNames=['/home/tf/FreeFEM-NS-CH/toy_sheardrop/Pe100_Cn0.01/out_305.vtk'])

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
SaveData('/home/tf/FreeFEM-NS-CH/toy_sheardrop/facets_Pe100_Cn0.01_305.tsv', proxy=generateIds1, WriteTimeSteps=1,
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

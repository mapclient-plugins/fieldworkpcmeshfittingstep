Fieldwork PC Mesh Fitting Step
==============================
MAP Client plugin for non-rigid registration of a Fieldwork mesh to a pointcloud using a shape model.

The mesh is translated, rotated, and deformed according to the principal components of the shape model to minimise the least-squares distance between target points and points sampled on the mesh.

Requires
--------
- GIAS2 : https://bitbucket.org/jangle/gias2

Inputs
------
- **pointcloud** [nx3 NumPy Array] : The target point cloud.
- **fieldworkmodel** [GIAS2 GeometricField instance] : The source Fieldwork mesh to be registered.
- **principalcomponents** [GIAS2 PrincipalComponents instance] : An instance of the GIAS2 PrincipalComponents class. The object contains the population mean, principal components, and eigenvalues. It is the shape model used to deform the Fieldwork mesh.
- **geometrictransform** [GIAS2 Transformation Instance][Optional] : An optional initial rigid-body transform to apply to the Fieldwork mesh before registration.
- **array1d** [1-D NumPy Array] : An array of weights for each target point.
- **landmarks** [dict][Optional] : An optional dictionary of landmark names mapping to coordinates. These landmarks can be used as targets in the registration with the target pointcloud.

Outputs
-------
- **fieldworkmodel** [GIAS2 GeometricField instance] : The registered Fieldwork mesh.
- **geometrictransform** [GIAS2 Transformation Instance] : The final registering transformation from the source mesh to the target pointcloud. The object contains the rigid-body translation and rotations, plus the principal components scores used.
- **float** [float] : The registration error in terms of the root-mean-squared Euclidean distance between the target points and the registered mesh.
- **array1d** [1-D NumPy Array] : An array of the Euclidean distance between each target point and its closest point on the registered mesh.

Configuration
-------------
- **identifier** : Unique name for the step.
- **Distance Mode** : How distance is calculated in the registration objective function.
	- DPEP : Distance between each target point and its closest point on the mesh. Points on the mesh are sampled according to the Surface Discretisation.
	- EPDP : Distance between each point on the mesh and its closest target point. Points on the mesh are sampled according to the Surface Discretisation.
- **PCs to Fit** : Number of principal components to use when deforming the Fieldwork mesh.
- **Surface Discretisation** : How densely the Fieldwork mesh is to be sampled when calculating distance to or from the target points. A value n means each element in the mesh will be sampled at n points in each element coordinate direction. E.g. a value of 5 means each 2-D quadralateral element will be discretised into 25 points. High values give a more accurate discretisation and a more accurate fit.
- **Mahalanobis Weight** : Weighting on the Mahalanobis distance penalty term during registration. Higher weights penalise more against shape far from the mean. Value should be between 0.1 and 1.0.
- **Max Func Eval** : Maximum number of objective function evaluations before termination.
- **xtol** : Minimum relative error between successive objective function evaluations before termination.
- **Fit Size** : If isotropic scaling should be introduced as a degree of freedom.
- **N Closest Points** : Number of closest points to find when calculating distances between mesh and target points.
- **Landmarks** : Mappings between optional input target landmark names and corresponding model landmark names (see Model Landmarks section). Expected format: input_landmark_1:model_landmark_1, input_landmark_2:model_landmark2, .... Example: R.ASIS:pelvis-RASIS, L.ASIS:pelvis-LASIS 
- **Landmark Weights** : Weights associated with input landmark to be used in the registration. Should be a series of comma-separated numbers, e.g. 100, 200.
- **GUI** : If the step GUI should be lauched on execution. Disable if running workflow in batch mode.

Step GUI
--------
- **3D Scene** : Interactive viewer for the target point cloud, the unregistered Fieldwork model, and the registered model.
- **Visibles box** : Show or hide objects in the 3D scene.
- **Fitting Parameters** : Parameters for the registation optimisation. See the Configuration section for an explanation of the parameters.
- **Fit** : Run the registration using the given parameters.
- **Reset** : Removes the registered Fieldwork model and transformations.
- **Abort** : Abort the workflow.
- **Accept**: Finish the step and outputs the current registered model and transformation.
- **Fitting Errors** : Displays registration errors.
	- **RMS** : The root-mean-squared distance between target and mesh points.
	- **Mean** : The mean distance between target and mesh points.
	- **S.D.** : The standard deviation of distances between target and mesh points.
- **Screeshot** : Save a screenshot of the current 3-D scene to file.
	- **Pixels X** : Width in pixels of the output image.
	- **Pixels Y** : Height in pixels of the output image.
	- **Filename** : Path of the output image file. File format is defined by the suffix of the given filename.
	- **Save Screenshot** : Take screenshot and write to file.
	
Usage
-----
This step provides coarse non-rigid registration of a Fieldwork mesh to a target pointcloud (e.g. surface vertices from a segmented STL file). This step is typically used in between rigid-body registration and a more local mesh fitting step. Deformations applied to the mesh are constrained to the shape variations seen in the training-set of the input PCA shape model. The shape model must match the input fieldwork model. See GIAS PC Source Step as a way to import a PCA shape model. 

The shape model deforms the mesh globally which means that the mesh can be registered to partial data - the shape model estimates the mesh shape where there are no corresponding target points. In this use case, the DPEP distance mode should be used.

Model Landmarks
---------------
- pelvis-LASIS : pelvis left anterior superior iliac spine
- pelvis-LPSIS : pelvis left posterior superior iliac spine
- pelvis-LHJC : pelvis left hip joint centre
- pelvis-LIS : pelvis left ischial spine 
- pelvis-LIT : pelvis left ischial tuberosity
- pelvis-LPS : pelvis left pubis symphysis
- pelvis-RASIS : pelvis right anterior superior iliac spine
- pelvis-RPSIS : pelvis right posterior superior iliac spine
- pelvis-RHJC : pelvis right hip joint centre
- pelvis-RIS : pelvis right ischial spine 
- pelvis-RIT : pelvis right ischial tuberosity
- pelvis-RPS : pelvis right pubis symphysis
- pelvis-Sacral : pelvis sacral
- femur-GT-l : femur left greater trochanter
- femur-HC-l : femur left head centre
- femur-LEC-l : femur left lateral epicondyle
- femur-MEC-l : femur left medial epicondyle
- femur-kneecentre-l : femur left knee centre
- femur-GT-r : femur right greater trochanter
- femur-HC-r : femur right head centre
- femur-LEC-r : femur right lateral epicondyle
- femur-MEC-r : femur right medial epicondyle
- femur-kneecentre-r : femur right knee centre
- tibiafibula-LC-l : tibia-fibula left tibia plateau most lateral point
- tibiafibula-MC-l : tibia-fibula left tibia plateau most medial point
- tibiafibula-LM-l : tibia-fibula left lateral malleolus
- tibiafibula-MM-l : tibia-fibula left medial malleolus
- tibiafibula-TT-l : tibia-fibula left tibial tuberosity
- tibiafibula-LC-r : tibia-fibula right tibia plateau most lateral point
- tibiafibula-LM-r : tibia-fibula right tibia plateau most medial point
- tibiafibula-MC-r : tibia-fibula right lateral malleolus
- tibiafibula-MM-r : tibia-fibula right medial malleolus
- tibiafibula-TT-r : tibia-fibula right tibial tuberosity

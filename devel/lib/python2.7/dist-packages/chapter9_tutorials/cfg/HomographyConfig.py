## *********************************************************
##
## File autogenerated for the chapter9_tutorials package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Feature detector.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'detector', 'edit_method': "{'enum_description': 'Feature detectors.', 'enum': [{'srcline': 11, 'description': 'FAST', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'FAST', 'ctype': 'std::string', 'type': 'str', 'name': 'FAST'}, {'srcline': 12, 'description': 'Good Features To Track', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'GFTT', 'ctype': 'std::string', 'type': 'str', 'name': 'GFTT'}, {'srcline': 13, 'description': 'Maximal Stable Extremal Regions', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'MSER', 'ctype': 'std::string', 'type': 'str', 'name': 'MSER'}, {'srcline': 14, 'description': 'ORiented BRIEF', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'ORB', 'ctype': 'std::string', 'type': 'str', 'name': 'ORB'}, {'srcline': 15, 'description': 'SIFT', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'SIFT', 'ctype': 'std::string', 'type': 'str', 'name': 'SIFT'}, {'srcline': 16, 'description': 'STAR', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'STAR', 'ctype': 'std::string', 'type': 'str', 'name': 'STAR'}, {'srcline': 17, 'description': 'SURF', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'SURF', 'ctype': 'std::string', 'type': 'str', 'name': 'SURF'}]}", 'default': 'ORB', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Descriptor extractor.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'descriptor', 'edit_method': "{'enum_description': 'Descriptor extractors.', 'enum': [{'srcline': 15, 'description': 'SIFT', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'SIFT', 'ctype': 'std::string', 'type': 'str', 'name': 'SIFT'}, {'srcline': 17, 'description': 'SURF', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'SURF', 'ctype': 'std::string', 'type': 'str', 'name': 'SURF'}]}", 'default': 'SURF', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Descriptor matcher.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'matcher', 'edit_method': "{'enum_description': 'Descriptor matchers.', 'enum': [{'srcline': 28, 'description': 'BruteForce', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'BruteForce', 'ctype': 'std::string', 'type': 'str', 'name': 'BruteForce'}, {'srcline': 29, 'description': 'FlannBased', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'FlannBased', 'ctype': 'std::string', 'type': 'str', 'name': 'FlannBased'}]}", 'default': 'FlannBased', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'Matcher filter.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'filter', 'edit_method': "{'enum_description': 'Matcher filters.', 'enum': [{'srcline': 35, 'description': 'NoneFilter', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'NoneFilter', 'ctype': 'std::string', 'type': 'str', 'name': 'NoneFilter'}, {'srcline': 36, 'description': 'CrossCheckFilter', 'srcfile': '/home/kimsanggil/study_ws/src/chapter9_tutorials/cfg/Homography.cfg', 'cconsttype': 'const char * const', 'value': 'CrossCheckFilter', 'ctype': 'std::string', 'type': 'str', 'name': 'CrossCheckFilter'}]}", 'default': 'CrossCheckFilter', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'RANSAC reprojection threshold.', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'threshold', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Homography_FAST = 'FAST'
Homography_GFTT = 'GFTT'
Homography_MSER = 'MSER'
Homography_ORB = 'ORB'
Homography_SIFT = 'SIFT'
Homography_STAR = 'STAR'
Homography_SURF = 'SURF'
Homography_BruteForce = 'BruteForce'
Homography_FlannBased = 'FlannBased'
Homography_NoneFilter = 'NoneFilter'
Homography_CrossCheckFilter = 'CrossCheckFilter'
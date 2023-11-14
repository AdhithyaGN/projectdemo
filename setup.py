from setuptools import setup,find_packages

 

def get_requirement_list(req_file='requirements.txt',)-> list:
    try:
        with open(req_file) as f:
            
            requirement_list=[require.replace("\n","") for require in f]
            requirement_list.remove("-e .")
        return requirement_list
    except Exception as e:
        raise e 
    






setup(
  name='mlprojectdemo',
  version='0.0.0',
  license='MIT',
  description='project completed',
  author='adhi',
  packages=find_packages(),
  install_requires=get_requirement_list()
)
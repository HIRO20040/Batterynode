from setuptools import setup


package_name = 'batterynode'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiro',
    maintainer_email='hizzino0817@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery = batterynode.battery:main',
        ],
    },
)

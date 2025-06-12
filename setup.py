from setuptools import setup, find_packages

setup(
    name='bearing_alert',
    version='0.1.0',
    description='Bridge bearing force anomaly alert module',
    author='肖图刚',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.2.3',
        'numpy>=1.26.4',
        'matplotlib>=3.9.4',
        'tabulate>=0.9.0'
    ],
    python_requires='>=3.9'
)

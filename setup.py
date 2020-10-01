import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(name="hello_package",
                 version="0.1.2",
                 # scripts=["initial_setting.bat"],
                 author="Pham Duc",
                 description="First package created by Phamduc",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=['package'],
                 py_modules=['hello_package'],
                 entry_points={'console_scripts': ['duc_script = hello_package:hello', 'duc_parser= hello_package:parser']},
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 )

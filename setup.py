import setuptools
from pkg_resources import resource_stream, resource_string, resource_filename

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SIMULADOR_CARGAS", 
    version="0.0.1",
    author="Jean Pierre Cifuentes Salazar & Juan Diego Zuñiga",
    author_email="bcifuentes@unal.edu.co",
    description="Un agradable simulador de campo electrico",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ceratoide/CARGAS",
    packages=['SIMULADOR_CARGAS'],
    package_data={"SIMULADOR_CARGAS":["sprites/*","pantallas/*","fuentes/*","creaciones/*"]},

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['SIMULADOR.py'],
    python_requires='>=3.6',
)
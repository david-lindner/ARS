import setuptools

setuptools.setup(
    name="ars",
    version="0.1dev",
    description="",
    install_requires=["numpy", "gym", "ray==0.7.0"],
    packages=setuptools.find_packages(),
    zip_safe=True,
    entry_points={},
)

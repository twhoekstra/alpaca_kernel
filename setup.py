import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='alpaca_kernel',
    version='0.1.7',
    author='Thijn Hoekstra',
    author_email='t.w.hoekstra@student.tudelft.nl',
    description='Fork of jupyter_micropython_kernel  by goatchurchprime',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/twhoekstra/alpaca_kernel',
    project_urls = {
        "Bug Tracker": "https://github.com/twhoekstra/alpaca_kernel"
    },
    license='MIT',
    packages=['alpaca_kernel'],
    install_requires=[],
)
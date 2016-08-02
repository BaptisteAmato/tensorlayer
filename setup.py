from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'tensorflow',
    'matplotlib',
]

setup(
    name = "tlayer",
    version = "1.1",
    include_package_data=True,
    author='TLayer Contributors',
    author_email='hao.dong11@imperial.ac.uk',
    url = "https://github.com/zsdonghao/tlayer" ,
    license = "apache" ,
    packages = find_packages(),
    install_requires=install_requires,
    # scripts=['tutorial_mnist.py'],
    description = "Deep learning and Reinforcement learning library for Researcher and Engineer",
    keywords = "deep learning, reinforcement learning, tensorflow",
    platform=['any'],
)
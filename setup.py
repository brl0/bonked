import os
import re
import shlex
from setuptools import setup, find_packages, Command

base_package = "bonked"

EXTRAS_REQUIRE = {
    "tests": ["pytest", "mock", "scripttest==1.3", "ipython", "bpython"],
    "lint": [
        "mypy==0.710",
        "flake8==3.7.7",
        "flake8-bugbear==19.3.0",
        "pre-commit==1.17.0",
    ],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["ptpython", "tox"]
)
PYTHON_REQUIRES = ">=3.6"


class Shell(Command):
    user_options = [
        ("name=", "n", "Named config to use."),
        ("shell=", "s", "Shell to use."),
        ("file=", "f", "File path of konch config file to execute."),
    ]

    def initialize_options(self):
        self.name = None
        self.shell = None
        self.file = None

    def finalize_options(self):
        pass

    def run(self):
        import konch

        argv = []
        for each in ("name", "shell", "file"):
            opt = getattr(self, each)
            if opt:
                argv.append(f"--{each}={opt}")
        konch.main(argv)


def read(fname):
    try:
        with open(fname) as fp:
            content = fp.read()
        return content
    except:
        return ""


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    """
    # Get the version (borrowed from SQLAlchemy)
    version = ""
    module_content = read(fname)
    reg = re.compile(r".*__version__ = \'(.*?)\'", re.S)
    m = reg.match(module_content)
    if m:
        version = m.group(1)
    return version


def find_license(fname):
    """Attempts to find the license in the file names fname.
    """
    LICENSE = ""
    module_content = read(fname)
    reg = re.compile(r".*__license__ = \'(.*?)\'", re.S)
    m = reg.match(module_content)
    if m:
        LICENSE = m.group(1)
    return LICENSE


base_path = os.path.dirname(__file__)
fname = os.path.join(base_path, "bonked", "__init__.py")
VERSION = find_version(fname)
LICENSE = find_license(fname)

readme = read("README.rst")
changes = read("CHANGELOG.rst")
requirements = [
    line for line in read("requirements.txt").split("\n") if len(line.strip())
]

packages = [
    base_package + "." + x for x in find_packages(os.path.join(base_path, base_package))
]
if base_package not in packages:
    packages.append(base_package)

if __name__ == "__main__":
    setup(
        name="bonked",
        description="Konch shell wrapper",
        long_description="\n\n".join([readme, changes]),
        license=LICENSE,
        url="https://github.com/brl0/bonked",
        version=VERSION,
        author="Brian Larsen",
        author_email="bmelarsen+bonked@gmail.com",
        maintainer="Brian Larsen",
        maintainer_email="bmelarsen+bonked@gmail.com",
        py_modules=["bonked"],
        entry_points={"console_scripts": ["bonked = bonked.cli:main"]},
        install_requires=requirements,
        cmdclass={"shell": Shell},
        extras_require=EXTRAS_REQUIRE,
        python_requires=PYTHON_REQUIRES,
        keywords=["bonked"],
        packages=packages,
        zip_safe=False,
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: System :: Shells",
        ],
        project_urls={
            "Changelog": "https://konch.readthedocs.io/en/latest/changelog.html",
            "Issues": "https://github.com/sloria/konch/issues",
            "Source": "https://github.com/sloria/konch/",
        },
    )

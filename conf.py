# -*- coding: utf-8 -*-
#
import os
import sys
import datetime
import sphinx

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinxext.rediraffe",
    'sphinx.ext.mathjax',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bede Documentation'
# Extract the year from the current time.
year = datetime.datetime.now().year
copyright = f'{year}, N8 CIR'
author = u'N8 CIR'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
version = u''
release = u''

# Specify the default language of english, which improves accessibility
language="en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst', "common/*.rst", '**.inc.rst', 'venv*', '.venv*']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

## Added by CA to get MathJax rendering loaded
mathjax_path='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_book_theme'
html_title = 'Bede Documentation'
html_static_path = ['_static']

# add custom css files
html_css_files = [
    'css/custom.css',
]

# Add custom js files
html_js_files = [
    'https://use.fontawesome.com/c79ff27dd1.js',
    'js/custom.js',
]

html_logo = '_static/images/logo-cmyk.png'

html_theme_options = {
    "repository_url": "https://github.com/N8-CIR-Bede/documentation",
    "use_edit_page_button": False,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": False,
    "use_fullscreen_button": False,
    "home_page_in_toc": False,
    "show_navbar_depth": 1,  # Sets the depth for expanded content
    # Control the right hand in-page toc
    "toc_title": "Contents",
    "show_toc_level": 2,
    "show_prev_next": False,
    # Code highlighting theme for light mode
    "pygment_light_style": "github-light-high-contrast",
    # Code highlighting theme for dark mode
    "pygment_dark_style": "github-dark-high-contrast",
    # Add an announcement bar, visible at the top of each page.
    # "announcement": "",
    # Add the traditional footer theme and sphinx acknowledgements
    "extra_footer": f"<p>&nbsp;Built with <a href=\"http://sphinx-doc.org/\">Sphinx</a> {sphinx.__version__} using a theme by the <a href=\"https://ebp.jupyterbook.org/\">Executable Book Project</a>.</p>"
}

# Select the default theme automatically. options light/dark/auto
html_context = {
    "default_mode": "auto",
}

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "a11y-search-field.html",
        "sbt-sidebar-nav.html",
        "ethical-ads.html"
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'bede-documentation'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'bede-documentation.tex', u'Bede Documentation',
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'bede-documentation', u'Bede Documentation',
     author, 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'bede-documentation', u'Bede Documentation',
     author, 'Bede', 'Documentation for usage of N8 CIR Bede Tier 2 HPC',
     'Miscellaneous'),
]

def setup(app):
    # If not building on Read the docs or Github, manually include the RTD JS to enable local testing of RTD specific content (i.e. the version switcher and ethical ads).
    # Only do this if the environment variable "MOCK_RTD" is defined.
    if os.environ.get("MOCK_RTD") and not os.environ.get("READTHEDOCS") and not os.environ.get("GITHUB_ACTIONS"):
        # Based on the same functionality in https://github.com/executablebooks/sphinx-book-theme/blob/master/docs/conf.py
        app.add_css_file("https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css")
        app.add_css_file("https://assets.readthedocs.org/static/css/badge_only.css")
        app.add_js_file("rtd-data.js")
        app.add_js_file("https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js", priority=501)

# Control use of the sphinx-rediraffe plugin to generate redirect files for moved documentation.
# This is only viable for whole-pages, not for any bookmarks within a page unfortunately.
rediraffe_redirects = {
    "bug/index.rst": "user-group/index.rst",
    "profiling/index.rst": "guides/nvidia-profiling-tools.rst",
    "software/resnet50/bede-README-sbatch.rst": "software/applications/wmlce.rst",
    "software/wanderings/wanderings-in-CUDALand.rst": "guides/wanderings/wanderings-in-CUDALand.rst",
    "software/wanderings/Estimating-pi-in-CUDALand.rst": "guides/wanderings/Estimating-pi-in-CUDALand.rst",
    "software/applications/amber.rst": "software/ppc64le/applications/amber.rst",
    "software/applications/conda.rst": "software/ppc64le/applications/conda.rst",
    "software/applications/eman2.rst": "software/ppc64le/applications/eman2.rst",
    "software/applications/grace.rst": "software/ppc64le/applications/grace.rst",
    "software/applications/gromacs.rst": "software/ppc64le/applications/gromacs.rst",
    "software/applications/index.rst": "software/ppc64le/applications/index.rst",
    "software/applications/namd.rst": "software/ppc64le/applications/namd.rst",
    "software/applications/open-ce.rst": "software/ppc64le/applications/open-ce.rst",
    "software/applications/openmm.rst": "software/ppc64le/applications/openmm.rst",
    "software/applications/python.rst": "software/ppc64le/applications/python.rst",
    "software/applications/pytorch.rst": "software/ppc64le/applications/pytorch.rst",
    "software/applications/r.rst": "software/ppc64le/applications/r.rst",
    "software/applications/rust.rst": "software/ppc64le/applications/rust.rst",
    "software/applications/tensorflow.rst": "software/ppc64le/applications/tensorflow.rst",
    "software/applications/wmlce.rst": "software/ppc64le/applications/wmlce.rst",
    # "software/applications/wmlce/sbatch_resnet50base.sh": "software/ppc64le/applications/wmlce/sbatch_resnet50base.sh",
    "software/compilers/gcc.rst": "software/ppc64le/compilers/gcc.rst",
    "software/compilers/ibmxl.rst": "software/ppc64le/compilers/ibmxl.rst",
    "software/compilers/index.rst": "software/ppc64le/compilers/index.rst",
    "software/compilers/llvm.rst": "software/ppc64le/compilers/llvm.rst",
    "software/compilers/nvcc.rst": "software/ppc64le/compilers/nvcc.rst",
    "software/compilers/nvhpc.rst": "software/ppc64le/compilers/nvhpc.rst",
    # "software/environments/Cryo-EM_Bede.pdf": "software/ppc64le/environments/Cryo-EM_Bede.pdf",
    "software/environments/cryo-em.rst": "software/ppc64le/environments/cryo-em.rst",
    "software/environments/easybuild.rst": "software/ppc64le/environments/easybuild.rst",
    "software/environments/index.rst": "software/ppc64le/environments/index.rst",
    "software/environments/spack.rst": "software/ppc64le/environments/spack.rst",
    "software/libraries/blas-lapack.rst": "software/ppc64le/libraries/blas-lapack.rst",
    "software/libraries/boost.rst": "software/ppc64le/libraries/boost.rst",
    "software/libraries/fftw.rst": "software/ppc64le/libraries/fftw.rst",
    "software/libraries/hdf5.rst": "software/ppc64le/libraries/hdf5.rst",
    "software/libraries/index.rst": "software/ppc64le/libraries/index.rst",
    "software/libraries/mpi.rst": "software/ppc64le/libraries/mpi.rst",
    "software/libraries/netcdf.rst": "software/ppc64le/libraries/netcdf.rst",
    "software/libraries/nvtoolsext.rst": "software/ppc64le/libraries/nvtoolsext.rst",
    "software/libraries/plumed.rst": "software/ppc64le/libraries/plumed.rst",
    "software/libraries/vtk.rst": "software/ppc64le/libraries/vtk.rst",
    "software/projects/hecbiosim.rst": "software/ppc64le/projects/hecbiosim.rst",
    "software/projects/ibm-collaboration.rst": "software/ppc64le/projects/ibm-collaboration.rst",
    "software/projects/index.rst": "software/ppc64le/projects/index.rst",
    "software/tools/cmake.rst": "software/ppc64le/tools/cmake.rst",
    "software/tools/index.rst": "software/ppc64le/tools/index.rst",
    "software/tools/make.rst": "software/ppc64le/tools/make.rst",
    "software/tools/nsight-compute.rst": "software/ppc64le/tools/nsight-compute.rst",
    "software/tools/nsight-systems.rst": "software/ppc64le/tools/nsight-systems.rst",
    "software/tools/nvidia-smi.rst": "software/ppc64le/tools/nvidia-smi.rst",
    "software/tools/singularity.rst": "software/ppc64le/tools/singularity.rst",
}

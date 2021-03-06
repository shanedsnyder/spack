# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RHmisc(RPackage):
    """Contains many functions useful for data analysis, high-level
    graphics, utility operations, functions for computing sample size
    and power, importing and annotating datasets, imputing missing
    values, advanced table making, variable clustering, character
    string manipulation, conversion of R objects to LaTeX and html
    code, and recoding variables."""

    homepage = "http://biostat.mc.vanderbilt.edu/Hmisc"
    url      = "https://cran.rstudio.com/src/contrib/Hmisc_4.1-1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/Hmisc"

    version('4.1-1', 'd255611f2b108d3cc0212b8a98fef6e3')
    version('4.0-3', '7091924db1e473419d8116c3335f82da')

    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-survival', type=('build', 'run'))
    depends_on('r-formula', type=('build', 'run'))
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-latticeextra', type=('build', 'run'))
    depends_on('r-acepack', type=('build', 'run'))
    depends_on('r-gridextra', type=('build', 'run'))
    depends_on('r-data-table', type=('build', 'run'))
    depends_on('r-htmltools', type=('build', 'run'))
    depends_on('r-base64enc', type=('build', 'run'))
    depends_on('r-htmltable', type=('build', 'run'))
    depends_on('r-viridis', type=('build', 'run'))

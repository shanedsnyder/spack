# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyOntFast5Api(PythonPackage):
    """This project provides classes and utility functions for working with
    read fast5 files. It provides an abstraction layer between the underlying
    h5py library and the various concepts central to read fast5 files, such as
    "reads", "analyses", "analysis summaries", and "analysis datasets".
    Ideally all interaction with a read fast5 file should be possible via this
    API, without having to directly invoke the h5py library."""

    homepage = "https://github.com/nanoporetech/ont_fast5_api"
    url      = "https://pypi.io/packages/source/o/ont-fast5-api/ont-fast5-api-0.3.2.tar.gz"

    version('0.3.2', '2ccfdbcd55239ffae712bb6e70ebfe8c')

    depends_on('py-setuptools', type='build')
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-numpy@1.8.1:', type=('build', 'run'))
